from appyratus.env import Environment
from appyratus.schema import fields

class {{ project.context.project.name|camel }}Environment(Environment):
    {{ project.context.project.name|snake|upper }}_DATA_PATH = fields.FilePath(required=True)
    {{ project.context.project.name|snake|upper }}_MANIFEST_FILEPATH = fields.FilePath(required=True)

    @property
    def data_path(self):
        return self.{{ project.context.project.name|snake|upper }}_DATA_PATH

    @property
    def manifest_filepath(self):
        return self.{{ project.context.project.name|snake|upper }}_MANIFEST_FILEPATH

