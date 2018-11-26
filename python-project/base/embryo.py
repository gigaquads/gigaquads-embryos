from appyratus.schema import fields
from embryo import Embryo


class PythonProjectBaseEmbryo(Embryo):
    """
    An embryo for Base
    """

    class context_schema(Embryo.Schema):
        """
        The respective Base schema
        - `name`, the name of the python project
        - `description`, a description
        - `version`, a version identifying this project
        - `tagline` a powerful tag line
        """
        project = fields.Nested({
            'name': fields.String(nullable=False),
        })
        description = fields.String(nullable=True, default='')
        version = fields.String(nullable=True, default='0b0')
        tagline = fields.String(nullable=True)
