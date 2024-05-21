from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()
    return


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().split()
    return



setup(
    name='src',
    version='{{ cookiecutter.project_version }}',
    author='{{ cookiecutter.author_name.replace("\'", "\\\'") }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.description }}',
    python_requires='>=3',
    license="{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}",
    url='https://github.com/dghorai',
    packages=find_packages(),
    long_description=readme(),
    install_requires=get_requirements()
)