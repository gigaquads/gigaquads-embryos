from appyratus.schema import fields
from embryo import Embryo, Relationship


class EnvEmbryo(Embryo):
    """
    # Env Embryo
    """
    project = Relationship(name='pybiz-project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Env schema
        """
        project = fields.Dict()
