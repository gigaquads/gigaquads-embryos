from appyratus.schema import fields
from appyratus.utils import StringUtils
from embryo import Embryo, Relationship

DAO_TYPES = {
    'filesystem': 'pybiz.dao.FilesystemDao',
}


class ResourceEmbryo(Embryo):
    """
    # Resource Embryo

    # Relationships
    - `biz`: TODO
    - `dao`: TODO
    """

    biz_rel = Relationship(name='pybiz-project/biz', index=0, is_nested=True)
    dao_rel = Relationship(name='pybiz-project/dao', index=0, is_nested=True)
    api_rel = Relationship(name='pybiz-project/api', index=0, is_nested=True)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Resource schema
        """
        resource = fields.Nested({'name': fields.String()})
        biz = fields.Nested({'name': fields.String()})
        dao = fields.Nested(
            {
                'name': fields.String(),
                'type': fields.String(default=lambda: DAO_TYPES['filesystem']),
                'params': fields.Dict()
            }
        )
        api = fields.Nested({'name': fields.String()})

    def pre_create(self, context, *args, **kwargs):
        # the resource name is optional, however if
        # provided it will be injected to the biz, dao,
        # and api- unless a name for them was also
        # specified, then the provided name takes precedent
        resource_name = context['resource'].get('name')
        if resource_name:
            for group in ('biz', 'dao', 'api'):
                group_context = {'name': resource_name}
                if not self.context.get(group):
                    self.context[group] = {}
                self.context[group].update(group_context)

    def on_create(self, context, *args, **kwargs):
        manifest = self.fs['/manifest.yml'][0]
        bindings = manifest.setdefault('bindings', [])
        biz_name = StringUtils.camel(context['biz']['name'])
        #dao_name = StringUtils.camel('{}Dao'.format(context['dao']['name']))
        dao_name = context['dao']['type']
        dao_params = context['dao'].get('params')
        found_bindings = [b for b in bindings if b['biz'] == biz_name]
        binding = found_bindings[0] if found_bindings else None
        new_binding = self.build_binding(biz_name, dao_name, dao_params)
        if not binding:
            bindings.append(new_binding)
        else:
            binding.update(new_binding)

    @classmethod
    def build_binding(cls, biz, dao, params=None):
        bnd = {'biz': biz, 'dao': dao}
        if params is not None:
            bnd['params'] = params
        return bnd
