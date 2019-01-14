from appyratus.schema import fields
from embryo import Embryo


class ProjectBaseEmbryo(Embryo):
    """
    # Project Base Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Project Baseschema
        """
        project = fields.Nested({
            'name': fields.String(nullable=False),
        })
