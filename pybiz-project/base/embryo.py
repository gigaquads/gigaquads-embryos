from appyratus.validation import fields
from embryo import Embryo


class PybizProjectBaseEmbryo(Embryo):
    """
    # Pybiz Project Base Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Base schema

        ## Fields
        * `project`: TODO
            * `name`: TODO
        """
        project = fields.Object({
            'name': fields.Str(allow_none=False),
        })
