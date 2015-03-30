import pytest
from lxml import etree
from six.moves.urllib.request import urlretrieve
import os.path
import tempfile


@pytest.fixture(scope='module')
def dtd():
    tmp_dir = tempfile.mkdtemp()
    dtd_file = os.path.abspath(os.path.join(tmp_dir, "docbook.dtd"))
    urlretrieve("http://docbook.org/xml/5.0/dtd/docbook.dtd", dtd_file)
    return etree.DTD(file=dtd_file, external_id="-//OASIS//DTD DocBook XML V5.0//EN")
