from copy import deepcopy

from appyratus.validation import fields
from appyratus.io import Ini
from embryo import Embryo

from . import constants    # import PROJECT_CLASSIFIERS


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
        author = fields.Str(allow_none=True)
        author_email = fields.Str(allow_none=True)
        url = fields.Str(allow_none=True)
        classifiers = fields.List(fields.Str(), default=[])

    def on_create(self, context):
        setup_config = self.fs['/setup.cfg']
        # clone the existing config
        setup_context = deepcopy(context)
        del setup_context['embryo']
        import ipdb
        ipdb.set_trace()
        print('=' * 100)
        # XXX merge context
