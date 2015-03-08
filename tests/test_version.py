import sphinxcontrib_docbook


def test_version():
    "see if __version__ is defined"

    assert hasattr(sphinxcontrib_docbook, "__version__")
    assert sphinxcontrib_docbook.__version__ is not None
