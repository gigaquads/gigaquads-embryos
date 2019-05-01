from appyratus.schema import fields
from embryo import Embryo, Relationship


class SessionEmbryo(Embryo):
    """
    # Session Embryo
    """

    resource_rel = Relationship(
        name='pybiz-project/resource', index=0, is_nested=True
    )

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Session schema
        """

        session = fields.Nested({'name': fields.String(default='session')})
        user = fields.Nested({'name': fields.String(default='user')})
        resource = fields.Nested(
            {
                'session': fields.Dict(),
                'user': fields.Dict(),
            },
        )

    def pre_create(self, context, *args, **kwargs):
        if self.context['resource'] is None:
            self.context['resource'] = {}
        if not context['session']:
            self.context['resource']['session'] = {'resource': {'name':  'session', 'component': 'Session'}}
        if not context['user']:
            self.context['resource']['user'] = {'resource': {'name': 'user', 'component': 'User'}}
