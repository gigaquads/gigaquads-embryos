from appyratus.schema import fields
from embryo import Embryo, Relationship


class DroneEmbryo(Embryo):
    """
    # Drone Embryo
    """

    project = Relationship(name='project', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Drone schema
        """

        project = fields.Dict()       
