import os, uuid
from datetime import datetime, timezone

import chromadb
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings



# Initialize ChromaDB
client = chromadb.PersistentClient()
embedding_function = GoogleGenerativeAIEmbeddings(model='models/text-embedding-005')


# processes document before storing in vector database
def process_document(file_path, course_id=None):
    if not valid_file(file_path):
            return False
    
    file_extension = file_path.split('.')[-1]
    if file_extension == 'pdf':
        loader = PyPDFLoader(file_path)
    elif file_extension in ['txt', 'md']:
        loader = TextLoader(file_path)
    elif file_extension == 'csv':
        loader = CSVLoader(file_path)
    else:
        return False
    
    # check if document already processed
    if is_processed(file_path, course_id):
        return False

    document = loader.load()
    # Splitting the document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(document)

    # Adding metadata
    for doc in split_docs:
        doc.metadata = {
            'filename': os.path.basename(file_path),
            'created': datetime.now(timezone.utc).isoformat()
        }
    store_vectors(split_docs, course_id)


def store_vectors(documents, course_id=None):
    # Stores document embeddings in ChromaDB
    collection_name = f'course_{course_id}' if course_id else 'general'
    vector_store = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )
    ids = [str(uuid.uuid4()) for _ in range(len(documents))]
    vector_store.add(ids=ids, documents=documents)


def remove_vectors(filename, course_id=None):
    # Removes document embeddings from ChromaDB
    collection_name = f'course_{course_id}' if course_id else 'general'
    try:
        collection = client.get_collection(collection_name, embedding_function)
    except ValueError:
        return False
    
    collection.delete(where={'filename': filename})
    return True


# util functions
def valid_file(file_path):
    allowed_extensions = {'pdf', 'txt', 'md', 'csv'}
    if '.' not in file_path:
        return False
    
    extension = file_path.rsplit('.', 1)[1].lower()
    return extension in allowed_extensions


def is_processed(file_path, course_id=None):
    collection_name = f'course_{course_id}' if course_id else 'general'
    try:
        collection = client.get_collection(collection_name, embedding_function)
    except ValueError:
        return False
    
    filename = os.path.basename(file_path)
    res = collection.get(where={'filename': filename}, limit=1, include=[])

    return True if res['ids'] else False
    
