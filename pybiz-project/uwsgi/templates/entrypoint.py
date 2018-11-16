from os.path import dirname, realpath, join

from {{ project.context.project.name|snake }}.api import web
from {{ project.context.project.name|snake }}.env import {{ project.context.project.name|camel }}Environment

env = {{ project.context.project.name|camel }}Environment()

uwsgi_callable = web.start

web.bootstrap(env.manifest_filepath)
