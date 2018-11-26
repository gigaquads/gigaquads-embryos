from appyratus.schema import fields
from embryo import Embryo


class ProjectEmbryo(Embryo):
    """
    # Project Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Project schema
        """
        project = fields.Nested({
            'name': fields.String(nullable=False),
        })
