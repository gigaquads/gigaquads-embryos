from copy import deepcopy
import os

from appyratus.validation import fields
from appyratus.io import Ini
from embryo import Embryo

PROJECT_CLASSIFIERS = {
    'python3': 'Programming Language :: Python :: 3',
    'mit-license': 'License :: OSI Approved :: MIT License',
    'os-independent': 'Operating System :: OS Independent'
}
"""
Project classifier mappings
"""


def as_list(value):
    if not value:
        return []
    if not isinstance(value, list):
        value = [value]
    return value


class SetupEmbryo(Embryo):
    """
    # Setup Embryo
    """

    class context_schema(Embryo.Schema):
        """
        # Context Schema
        The respective Setup schema
        """
        name = fields.Str(allow_none=True)
        description = fields.Str(allow_none=True)
        long_description = fields.Str(allow_none=True)
        version = fields.Anything(allow_none=True)
        tagline = fields.Str(allow_none=True)
        author = fields.Str(allow_none=True)
        author_email = fields.Str(allow_none=True)
        url = fields.Str(allow_none=True)
        license = fields.Str(allow_none=True)
        keywords = fields.List(fields.Str(), allow_none=True)
        classifiers = fields.List(fields.Str(), allow_none=True)
        scripts = fields.List(fields.Str(), allow_none=True)
        dependency_links = fields.List(fields.Str(), allow_none=True)
        packages = fields.Str(allow_none=True)
        install_requires = fields.Str(allow_none=True)

    def pre_create(self, context):
        if 'classifiers' in context:
            if not isinstance(context['classifiers'], list):
                context['classifiers'] = [context['classifiers']]

    def on_create(self, context):
        #https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files
        # look for readme for long description
        if 'long_description' not in context:
            description_files = ['README.md']
            context['long_description'
                    ] = 'file: {}'.format(','.join(description_files))
        self.load_classifiers(context)
        # scripts
        if 'scripts' not in context:
            scripts = self.load_scripts(context)
        # packages
        if 'packages' not in context:
            # this is the equivalent of running `find_packages()`
            context['packages'] = 'find:'
        self.load_requirements(context)
        # setup schema that defines the expected format of the setup config file
        setup_schema = {
            'metadata': [
                'name', 'description', 'long_description', 'version', 'author',
                'author_email', 'license', 'classifiers'
            ],
            'options':
            ['scripts', 'dependency_links', 'packages', 'install_requires']
        }
        # where the constructed setup data will go. to ensure that existing
        # data does not get overridden by setup values not provided, copy the
        # existing data first before apply the changes
        setup_config = deepcopy(self.fs['setup.cfg']) or {}

        # as far as it is known the underlying configparser does not accurately
        # represents lists (either comma-separated or dangling list), so here
        # we will adjust the list data so that it is represented in any of the
        # expected formats.
        list_format = 'dangling'
        def clean_value(value):
            if isinstance(value, list):
                if list_format == 'dangling':
                    value = "\n{}".format('\n'.join(value))
                elif list_format == 'csv':
                    value = ','.join(value)
            return value

        # prepare config data - everything is fetched from the main context,
        # and if it does not exist then it will not be included.  otherwise
        # every value must be a string
        for skey, skeys in setup_schema.items():
            sdata = {
                k: clean_value(context.get(k))
                for k in skeys if context.get(k)
            }
            if sdata:
                if skey not in setup_config:
                    setup_config[skey] = sdata
                else:
                    setup_config[skey].update(sdata)
        # apply config data to setup config
        self.fs['setup.cfg'].update(setup_config)

    def load_requirements(self, context):
        # requirements.txt is formatted for pip install, not setup tools.
        # As a result, we have to manually detect dependencies on github
        # and translate these into data setuptools knows how to handle.
        requirements_text = self.fs['requirements.txt']
        if not requirements_text:
            return
        requirements = []
        dependency_links = []
        for line in requirements_text:
            if line.startswith('-e'):
                # we're looking at a github repo dependency, so
                # install from a github tarball.
                match = re.search(
                    r'(https://github.+?)#egg=(.+)$', line.strip()
                )
                url, egg = match.groups()
                if url.endswith('.git'):
                    url = url[:-4]
                tarball_url = url.rstrip('/') + '/tarball/master#egg=' + egg
                requirements.append(egg)
                dependency_links.append(tarball_url)
            else:
                requirements.append(line.strip().replace('-', '_'))
        if requirements:
            self.context['requirements'] = requirements
        if dependency_links:
            self.context['dependency_links'] = dependency_links

    def load_scripts(self, context):
        """
        Load scripts found in the `bin`, also known as bin scripts
        """
        scripts = []
        bin_path = 'bin'
        for (dirpath, _, filenames) in os.walk(bin_path):
            for filename in filenames:
                # scanning a directory with open swaps files will lead to
                # failures in the setup script if they make it in
                if filename.endswith('.swp'):
                    continue
                scripts.append(os.path.join(bin_path, filename))
        if scripts:
            context['scripts'] = scripts

    def load_classifiers(self, context):
        """
        Load classifiers providing a list of keys that exist in PROJECT_CLASSIFIERS
        """
        if 'classifiers' not in context:
            return
        classifiers = []
        for k in context['classifiers']:
            classifier = PROJECT_CLASSIFIERS.get(k)
            if classifier:
                classifiers.append(classifier)
        if classifiers:
            context['classifiers'] = classifiers
