from appyratus.schema import fields
from embryo import Embryo, Relationship


class PythonProjectFullEmbryo(Embryo):
    """
    # Full Embryo
    """

    base = Relationship(name='python-project/base', index=0, is_nested=True)
    setup = Relationship(name='python-project/setup', index=0, is_nested=True)
    # license

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Full schema
        """
        project = fields.Dict()
