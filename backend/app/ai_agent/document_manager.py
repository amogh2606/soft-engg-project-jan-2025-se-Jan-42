import os
from flask import request, jsonify
from flask_restful import Resource, abort
from flask_security import roles_accepted, current_user
from werkzeug.utils import secure_filename
from app.ai_agent.embeddings import process_document, remove_vectors



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'documents')

class KnowledgeStack(Resource):
    # fetch all documents for a specific course
    @roles_accepted('instructor', 'admin')
    def get(self, course_id=None):
        if course_id and not self.check_access(course_id):
            abort(403, message="Access denied")

        collection_name = f'course_{course_id}' if course_id else 'general'
        collection_folder = os.path.join(UPLOAD_FOLDER, collection_name)
        if not os.path.exists(collection_folder):
            abort(404, message="Collection not found")
        
        files = os.listdir(collection_folder)
        return jsonify(collection=collection_name, documents=files)
    

    # upload a document for a specific course
    @roles_accepted('instructor', 'admin')
    def post(self, course_id=None):
        if course_id and not self.check_access(course_id):
            abort(403, message="Access denied")

        if 'file' not in request.files:
            abort(400)

        file = request.files['file']
        filename = secure_filename(file.filename)
        
        collection_name = f'course_{course_id}' if course_id else 'general'
        collection_folder = os.path.join(UPLOAD_FOLDER, collection_name)
        os.makedirs(collection_folder, exist_ok=True)

        file_path = os.path.join(collection_folder, filename)
        if os.path.exists(file_path):
            abort(400, message="File already exists")

        file.save(file_path)
        # store embeddings in vector db
        if not process_document(file_path, course_id):
            os.remove(file_path)
            abort(400, message="Could not process document")

        return {"message": "File uploaded and processed successfully"}, 201


    # delete a document for a specific course
    @roles_accepted('instructor', 'admin')
    def delete(self, course_id=None):
        # get filename from query params
        filename = request.args.get('filename')
        if not filename:
            abort(400, message="Filename is required")
        
        if not self.check_access(course_id):
            abort(403, message="Access denied")

        collection_name = f'course_{course_id}' if course_id else 'general'
        collection_folder = os.path.join(UPLOAD_FOLDER, collection_name)
        file_path = os.path.join(collection_folder, filename)
        if not os.path.exists(file_path):
            abort(404, message="File not found")
        
        # Remove document embeddings
        if not remove_vectors(filename, course_id):
            abort(500, message="Collection not found")

        os.remove(file_path)
        return {'message': "Deleted successfully"}
    

    # check if instructor has access to course
    def check_access(self, course_id):
        if current_user.has_role('admin'):
            return True
        course_ids = [course.id for course in current_user.courses]
        return course_id in course_ids
        
