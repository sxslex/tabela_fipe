from TabelaFipe import __description__
from TabelaFipe import __keywords__
from TabelaFipe import __version__
from TabelaFipe import __author__
from TabelaFipe import __author_email__
from setuptools import setup
from setuptools import find_packages

setup(
    name='TableFipe',
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    description=__description__,
    keywords=__keywords__,
    long_description=open('README.rst').read(),
    packages=find_packages(),
    package_data={'': ['tabela_fipe.db']},
    include_package_data=True,
)
