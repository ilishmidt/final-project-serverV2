from abc import ABC, abstractmethod
editors_id = 1


class Editor(ABC):
    def __init__(self, undeciphered_json, project_id, converted_data=None, editor_id=editors_id):
        self.undeciphered_json = undeciphered_json
        self.project_id = project_id
        self.converted_data = converted_data

        global editors_id
        if editor_id == editors_id:
            editors_id += 1
        self.UserID = editor_id

    @abstractmethod
    def parse_json(self):
        pass

    @abstractmethod
    def update_editor(self):
        pass
