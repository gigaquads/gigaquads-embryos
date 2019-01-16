from appyratus.schema import fields
from embryo import Embryo, Relationship


class PybizProjectBaseEmbryo(Embryo):
    """
    # Pybiz Project Base Embryo
    """

    project = Relationship(name='project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Base schema

        ## Fields
        * `project`: TODO
            * `name`: TODO
        """
        project = fields.Nested({
            'name': fields.String(),
        })
