from appyratus.schema import fields
from embryo import Embryo, Relationship


class ApiEmbryo(Embryo):
    """
    # Api Embryo

    ## Relationships
    * `project`: TODO
    """
    project = Relationship(name='python-project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Api schema

        ## Fields
        * `api`:
            * `name`: TODO
        """
        api = fields.Nested({'name': fields.String()})
