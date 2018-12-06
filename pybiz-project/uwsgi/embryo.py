from appyratus.schema import fields
from embryo import Embryo, Relationship


class UwsgiEmbryo(Embryo):
    """
    # Uwsgi Embryo
    """
    project = Relationship(name='python-project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Uwsgi schema
        """
        pass
