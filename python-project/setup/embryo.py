from appyratus.validation import fields
from appyratus.io import Ini
from embryo import Embryo


class SetupEmbryo(Embryo):
    """
    # Setup Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Setup schema
        """
        name = fields.Str()
        description = fields.Str(allow_none=True, default='')
        version = fields.Anything(allow_none=True, default='0b0')
        tagline = fields.Str(allow_none=True)

    def on_create(self, context):
        config_data = self.fs['/setup.cfg']
        import ipdb; ipdb.set_trace(); print('=' * 100)
        # XXX merge context
