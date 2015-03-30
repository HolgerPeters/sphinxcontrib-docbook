import pytest

from lxml import etree



def test_validity(dtd):
    "verify that minimal docbook xml tree is matched"
    root = etree.XML("""<book><title>Test</title></book>""")
    assert dtd.validate(root)


def test_schema_fail(dtd):
    """A test verifying that schemas are not matched"""
    root = etree.XML("<bk/>")
    assert not dtd.validate(root)
