from appyratus.schema import fields
from embryo import Embryo


class DockerBaseEmbryo(Embryo):
    """
    # Docker Project Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Docker Project schema
        """
        is_service = fields.Bool(default=False)
