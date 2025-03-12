from flask_restful import Resource, abort
from flask_security import auth_required
from app.models import db, Video
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader



class VideoSummary(Resource):
    @auth_required('session')
    def post(self, video_id):
        video = db.get_or_404(Video, video_id, description="Video not found")
        try:
            loader = YoutubeLoader.from_youtube_url(video.url)
            docs = loader.load()
            transcript = '\n'.join([doc.page_content for doc in docs])
        except Exception as e:
            print(e)
            abort(400, message="Failed to load video transcript")

        prompt = PromptTemplate(
            template="Summarise the following lecture: \n\n{transcript}", 
            input_variables=['transcript']
        )
        llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
        chain = prompt | llm
        response = chain.invoke({'transcript': transcript})

        return {'video_url': video.url, 'summary': response.text()}
    

class GenerateQuiz(Resource):
    @auth_required('session')
    def post(self, video_id):
        video = db.get_or_404(Video, video_id, description="Video not found")
        try:
            loader = YoutubeLoader.from_youtube_url(video.url)
            docs = loader.load()
            transcript = ' '.join([doc.page_content for doc in docs])
        except Exception as e:
            print(e)
            abort(400, message="Failed to load video transcript")

        prompt = PromptTemplate(
            template="""Generate a quiz of 5 mcqs from the following lecture.
                Your response should only contain the questions with 4 options. \n\n{transcript}""",
            input_variables=['transcript']
        )
        llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001', temperature=0)
        chain = prompt | llm
        response = chain.invoke({'transcript': transcript})

        return {'video_url': video.url, 'quiz': response.text()}
            
