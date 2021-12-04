from src.models import Editor
from src.parsers import UMLParser


class UMLEditor(Editor):
    def __init__(self, undeciphered_json, project_id, converted_data=None, editor_id=None):
        super().__init__(undeciphered_json, project_id, converted_data, editor_id)
        self.parseJson()
        self.type = 'UML'

    def parse_json(self):
        editor_project = load_project(self.project_id)
        self.converted_data = UMLParser.parse(self.undeciphered_json)

    def update_editor(self, undecipheredJson):
        self.undeciphered_json = undecipheredJson
        self.parse_json()
