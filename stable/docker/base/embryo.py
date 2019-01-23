from appyratus.schema import fields
from embryo import Embryo, Relationship


class DockerBaseEmbryo(Embryo):
    """
    # Docker Project Embryo
    """

    project = Relationship(name='project/base', index=0)

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Docker Project schema
        """
        is_service = fields.Bool(default=False)
        project = fields.Dict()
        build = fields.Nested(
            {
                'repo': fields.Nested(
                    {
                        'server': fields.String(nullable=False),
                        'org': fields.String(nullable=False),
                        'name': fields.String(nullable=True),
                        'branch': fields.
                        String(nullable=True, default=lambda: 'master'),
                        'gitlab_host': fields.String(nullable=True)
                    }
                ),
                'dest': fields.
                FormatString(nullable=True, default=lambda: "./{repo[name]}"),
            },
            nullable=True
        )
        entrypoint = fields.String(nullable=True)
        expose = fields.String(nullable=True)
        env = fields.Dict()

    def pre_create(self, data):
        project = self.related['project']
        data.setdefault('build', {}).setdefault('repo', {}).setdefault(
            'name', project.context['project']['name']
        )

    def on_create(self, data):
        env_file = self.fs['env.yml']
        import ipdb; ipdb.set_trace(); print('=' * 100)
        if env_file:
            env_data = env_file[0]
            data['env'] = env_data
