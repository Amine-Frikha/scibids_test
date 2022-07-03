from flask import Flask
from flask_restful import Resource, Api
# this is to avoid CORS errors where browsers block requests from this address 
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
    
# get a list of documents by id
class Document(Resource):
    @cross_origin()
    def get(self, id):
        try:
            document = db.get_document_by_id(id)
        except db.DatabaseError as e:
            return {'status': 500, 'errors': str(e)}, 500

        return {'status': 200, 'data': document}, 200

# get a list of a doucments' tags by id 
class TagsFromDocument(Resource):
    @cross_origin()
    def get(self, id):
        try:
            tags_from_doc = db.get_tags_from_document(id)
        except db.DatabaseError as e:
            return {'status': 500, 'errors': str(e)}, 500

        return {'status': 200, 'data': tags_from_doc}, 200

# Get a list of all documents with their tags
class FullDocuments(Resource):
    @cross_origin()
    def get(self):
        try:
            documents = db.get_documents()
            for doc in documents:
                tags = db.get_tags_from_document(doc["id"])
                tags_list = []
                for tag in tags:
                    tags_list.append(tag['tags'])
                doc.update({"tags":tags_list})
        except db.DatabaseError as e:
            return {'status': 500, 'errors': str(e)}, 500

        return {'status': 200, 'data': documents}, 200


api.add_resource(Documents, '/documents/')
api.add_resource(Document, '/document/<id>')
api.add_resource(TagsFromDocument, '/tagsfromdoc/<id>')
api.add_resource(FullDocuments, '/fulldocs')

if __name__ == '__main__':
    app.run(debug=True, port=7003)