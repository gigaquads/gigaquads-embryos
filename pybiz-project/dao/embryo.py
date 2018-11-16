from appyratus.schema import fields
from embryo import Embryo, Relationship


class DaoEmbryo(Embryo):
    """
    # Dao Embryo

    ## Relationships
    * `project`: TODO
    """
    project = Relationship(name='pybiz-project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Dao schema

        ## Fields
        * `dao`:
            * `name`: TODO
            * `type`: TODO
            * `fields`: TODO
        """
        dao = fields.Nested(
            {
                'name': fields.String(),
                'type': fields.String(nullable=True),
                'fields': fields.List(fields.Dict())
            }
        )
