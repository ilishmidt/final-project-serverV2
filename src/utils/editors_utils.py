import src.database

from src.models.uml_editor import UMLEditor
from src.models.nfr_editor import NFREditor
from src.models.sql_editor import SQLEditor


class EditorsUtils:
    def __init__(self):
        pass

    @staticmethod
    def save_editors(data, type):
        new_editor = None
        if type == 'UML':
            new_editor = UMLEditor(undeciphered_json=data)
        elif type == 'NFR':
            new_editor = NFREditor(undeciphered_json=data)
        elif type == 'SQL':
            new_editor = SQLEditor(undeciphered_json=data)
        src.database.mongo.db['Editors'].insert_one(new_editor)

    @staticmethod
    def load_editor(id):
        query = {'EditorID': id}
        return src.database.mongo.db.Editors.find_one(query)
