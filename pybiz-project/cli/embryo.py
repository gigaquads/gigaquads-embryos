import os
import stat

from appyratus.validation import fields
from appyratus.util import TextTransform
from embryo import Embryo, Relationship


class PybizProjectCliEmbryo(Embryo):
    """
    An embryo for Cli
    """

    project = Relationship(name='pybiz-project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        The respective Cli schema
        """
        project = fields.Dict()

    def post_create(self, context):
        """
        Make the cli bin script executable
        """
        cli_path = os.path.join(
            self.fs._root, 'bin',
            TextTransform.
            dash(self.related['project'].context['project']['name'])
        )
        st = os.stat(cli_path)
        os.chmod(cli_path, st.st_mode | stat.S_IEXEC)
