from appyratus.schema import fields
from embryo import Embryo, Relationship


class BizEmbryo(Embryo):
    """
    # Biz Embryo

    ## Relationships
    - `project`: TODO
    """
    project = Relationship(name='python-project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Biz schema

        ## Fields
        - `biz`: TODO
          - `fields`: TODO
          - `name`: TODO
          - `type`: TODO
        """
        biz = fields.Nested(
            {
                'name': fields.String(),
                'fields': fields.List(fields.Dict())
            }
        )
        project = fields.Dict()
