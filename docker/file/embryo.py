from appyratus.schema import fields
from embryo import Embryo


class DockerFileEmbryo(Embryo):
    """
    # File Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective File schema
        """
        pass
