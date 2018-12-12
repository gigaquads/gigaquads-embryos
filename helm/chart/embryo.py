from appyratus.schema import fields
from embryo import Embryo


class HelmChartEmbryo(Embryo):
    """
    # Helm Chart Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Helm Chart schema
        """
        pass
