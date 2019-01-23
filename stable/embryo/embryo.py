import os

from appyratus.schema import fields
from appyratus.files import File
from embryo import Embryo


class EmbryoEmbryo(Embryo):
    """
    # An embryo for generating embryos
    """

    class context_schema(Embryo.Schema):
        """
        # Embryo Schema

        ## Fields
        - `name` The name of the embryo you want to create
        - `schema_fields` Schema fields to be applied to an embryo


        """
        name = fields.String(nullable=False)
        schema_fields = fields.List(nested=fields.Dict(), default=[])
        origin_path = fields.FilePath(default=lambda: '')

    def pre_create(self, context: dict):
        """
        Allow schema fields to be passed in as a string, that constructs a
        dictionary with the value as the field name and `Anything` as the type.
        And a dictionary, a presumed schema field structure, will be
        transformed to a list with itself being a member.
        """
        self._new_tree = None
        self._new_files = None
        schema_fields = context.get('schema_fields')
        if isinstance(schema_fields, str):
            schema_fields = dict(name=schema_fields, type='Anything')
        if isinstance(schema_fields, dict):
            schema_fields = [schema_fields]
        context['schema_fields'] = schema_fields
        if 'origin_path' in context:
            tree, files = self.build_tree(context['origin_path'])
            self._new_tree = tree
            self._new_files = files

    def on_create(self, context: dict):
        if 'origin_path' in context:
            self.fs['tree.yml'][0] = self._new_tree
            #for f in files:
            #    self.fs._read_file(f)
        #self.fs.read(self)

    def _render_tree(self):
        tree = super()._render_tree()
        for t in tree:
            if isinstance(t, dict) and 'templates/' in t.keys():
                import ipdb; ipdb.set_trace(); print('=' * 100)
                t['templates/'] = [
                    'base.html'
                ]    #[k for k in self._new_files.keys()]
        return tree

    def build_tree(self, origin_path: str) -> tuple:
        """
        # Build Tree
        Scan the provided origin path and return relevant file and directory
        tree and contents to be injected in the embryo's tree.yml and templates
        directory.
        """
        basename = os.path.basename(origin_path)
        templates = {}
        tree = []
        files_data = {}
        for root, dirs, files in os.walk(origin_path):
            relroot = os.path.relpath(root, origin_path)
            relroot = '' if relroot is '.' else relroot
            for d in dirs:
                rootdir = os.path.join(basename, relroot, "{}/".format(d))
                tree.append(rootdir)
            for f in files:
                relfile = os.path.join(basename, relroot, f)
                absfile = os.path.join(root, f)
                files_data[relfile] = absfile
                tree.append(relfile)
        return (tree, files_data)
