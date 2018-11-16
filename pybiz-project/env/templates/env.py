from appyratus.io import Environment
from appyratus.schema import fields

class {{ project.context.project.name|camel }}Environment(Environment):
    {{ project.context.project.name|snake|upper }}_MANIFEST_FILEPATH = fields.FilePath(required=True)

    @property
    def manifest_filepath(self):
        return self.{{ project.context.project.name|snake|upper }}_MANIFEST_FILEPATH
