from src.models import Editor
from src.parsers import NFRParser


class NFREditor(Editor):
    def __init__(self, undeciphered_json, project_id, converted_data=None, editor_id=None):
        super().__init__(undeciphered_json, project_id, converted_data, editor_id)
        self.parse_json()
        self.type = 'NFR'

    def parse_json(self):
        editor_project = load_project(self.projectID)
        self.converted_data = NFRParser.parse(self.undeciphered_json, editor_project.get_project_uml(),
                                              editor_project.get_project_sql())

    def update_editor(self, undeciphered_json):
        self.undeciphered_json = undeciphered_json
        self.parse_json()
