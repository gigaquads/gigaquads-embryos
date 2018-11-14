from appyratus.time import utc_now
from appyratus.schema import fields
from embryo import Embryo


class LicenseEmbryo(Embryo):
    """
    # License Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective License schema
        """
        author = fields.String()
        year = fields.String(
            nullable=True, default=lambda: utc_now().strftime('%Y')
        )
