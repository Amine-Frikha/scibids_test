from flask import Flask
from flask_restful import Resource, Api
from flask_cors import cross_origin
import db

app = Flask(__name__)
api = Api(app)


class Documents(Resource):
    @cross_origin()
    def get(self):
        try:
            documents = db.get_documents()
        except db.DatabaseError as e:
            return {'status': 500, 'errors': str(e)}, 500

        return {'status': 200, 'data': documents}, 200
    

class Document(Resource):
    @cross_origin()
    def get(self, id):
        try:
            documents = db.get_document_by_id(id)
        except db.DatabaseError as e:
            return {'status': 500, 'errors': str(e)}, 500

        return {'status': 200, 'data': documents}, 200

class TagsFromDocument(Resource):
    @cross_origin()
    def get(self, id):
        try:
            tags_from_docs = db.get_tags_from_document(id)
        except db.DatabaseError as e:
            return {'status': 500, 'errors': str(e)}, 500

        return {'status': 200, 'data': tags_from_docs}, 200

api.add_resource(Documents, '/documents/')
api.add_resource(Document, '/document/<id>')
api.add_resource(TagsFromDocument, '/tagsfromdoc/<id>')

if __name__ == '__main__':
    app.run(debug=True, port=7003)