from ._builder import DocbookXMLBuilder

from setuptools_scm import get_version
__version__ = get_version(root='..', relative_to=__file__)


def setup(app):
    app.add_builder(DocbookXMLBuilder)


__all__ = []
