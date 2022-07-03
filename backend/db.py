import sqlite3


class DatabaseError(Exception):
    pass

def add_headers_sqlite(d, cursor):
    headers = [description[0] for description in cursor.description]
    _data = {headers[index]: value for index, value in enumerate(d)}
    return _data


def get_documents():
    documents = []
    with sqlite3.connect("document.db") as conn:
        try:
            cursor = conn.execute('SELECT * FROM document')
            data = cursor.fetchall()
        except sqlite3.Error as err:
            raise DatabaseError(err.args[0])

        for d in data:
            documents.append(add_headers_sqlite(d, cursor))

    return documents

def get_document_by_id(id):
    document = []
    with sqlite3.connect("document.db") as conn:
        try:
            cursor = conn.execute('SELECT * FROM document WHERE id = {}'.format(id))
            data = cursor.fetchall()
        except sqlite3.Error as err:
            raise DatabaseError(err.args[0])

        for d in data:
            document.append(add_headers_sqlite(d, cursor))

    return document


def get_tags_from_document(id):
    tags = []
    with sqlite3.connect("document.db") as conn:
        try:
            cursor = conn.execute('''SELECT t.name as tags
                                     FROM document_tag as dt, tag as t, document as d 
                                     WHERE dt.document_id = {}
                                     AND dt.tag_id = t.id
                                     AND d.id = dt.document_id
                                     '''.format(id))
            data = cursor.fetchall()
        except sqlite3.Error as err:
            raise DatabaseError(err.args[0])

        for d in data:
            tags.append(add_headers_sqlite(d, cursor))

    return tags

def get_tags_from_documents(id):
    tags = []
    with sqlite3.connect("document.db") as conn:
        try:
            cursor = conn.execute('''SELECT t.name as tags
                                     FROM document_tag as dt, tag as t, document as d 
                                     WHERE dt.document_id = {}
                                     AND dt.tag_id = t.id
                                     AND d.id = dt.document_id
                                     '''.format(id))
            data = cursor.fetchall()
        except sqlite3.Error as err:
            raise DatabaseError(err.args[0])

        for d in data:
            tags.append(add_headers_sqlite(d, cursor))

    return tags