from src.utils import EditorsUtils

projects_id = 1


class Project:
    def __init__(self, project_id=projects_id, description='', uml_editor_id=None, sql_editor_id=None,
                 nfr_editor_id=None, ahp_editor_id=None, owner=None, members=[]):
        # Manage users id
        global projects_id
        if project_id == projects_id:
            projects_id += 1
        self.project_id = project_id
        self.description = description
        self.uml_editor_id = uml_editor_id
        self.sql_editor_id = sql_editor_id
        self.nfr_editor_id = nfr_editor_id
        self.ahp_editor_id = ahp_editor_id
        self.owner = owner
        self.members = members

    def get_project_uml(self):
        return EditorsUtils.load_editor(self.uml_editor_id)

    def get_project_sql(self):
        return EditorsUtils.load_editor(self.sql_editor_id)

    def get_project_nfr(self):
        return EditorsUtils.load_editor(self.nfr_editor_id)

    def calc(self):
        pass
