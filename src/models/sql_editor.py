from src.models import Editor
from src.parsers import SQLParser


class SQLEditor(Editor):
    def __init__(self, undeciphered_json, project_id, converted_data=None, editor_id=None):
        super().__init__(undeciphered_json, project_id, converted_data, editor_id)
        self.parse_json()
        self.type = 'SQL'

    def parse_json(self):
        editor_project = load_project(self.project_id)
        self.converted_data = SQLParser.parse(self.undeciphered_json, editor_project.get_project_uml())  # Need to check if should extract the json or the class

    def update_editor(self, undeciphered_json):
        self.undeciphered_json = undeciphered_json
        self.parse_json()
