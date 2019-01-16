from appyratus.schema import fields
from embryo import Embryo, Relationship


class SvcEmbryo(Embryo):
    """
    # Svc Embryo

    ## Relationships
    * `project`: TODO
    """
    project = Relationship(name='project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Svc schema
        """
        pass
