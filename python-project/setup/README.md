Setup your program for the world

All the things setuptools maybe didn't do for ya, or did for ya but it was just
so dense that you went mad in the process.

# Resource
- Packaging https://packaging.python.org/tutorials/packaging-projects/
- Licensing https://opensource.org/licenses/category
- Versioning https://www.python.org/dev/peps/pep-0440/
- Registering https://test.pypi.org/account/register/
- Testing https://test.pypi.org/
- Classifying https://pypi.org/classifiers/
- Key projects https://packaging.python.org/key_projects/

# Using PyPi
The following is a loose guide to pushing your project up to PyPi once the setup has been constructed

## Requirements
```sh
python3 -m pip install --user --upgrade setuptools wheel twine
```

## Build
```sh
python3 setup.py sdist bdist_wheel
```

## Test
```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ example_pkg
```

## Production
```
twine upload dist/*
```
