from sphinx.builders import Builder
from ._writer import DocbookWriter

import os.path
import os


class DocbookXMLBuilder(Builder):
    """
    Builds standalone HTML docs.
    """
    name = 'docbook'
    format = 'xml'
    supported_image_types = [
        'image/svg+xml', 'image/png', 'image/gif', 'image/jpeg'
    ]

    def get_outdated_docs(self):
        return []

    def prepare_writing(self, docnames):
        self.docwriter = DocbookWriter(self)
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        self._docnames = docnames

    def write_doc(self, docname, doctree):
        with open(
                os.path.join(
                    self.outdir,  # "docbook",
                    docname + ".xml"),
                "w") as f:
            self.docwriter.write(doctree, f)
        self.finish()  # hac

    def get_target_uri(self, *args, **kwds):
        return "index.xml"

    def finish(self):
        with open(os.path.join(self.outdir, "index.xml"), "w") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>')
            f.write(
                '<!DOCTYPE book PUBLIC'
                ' "-//OASIS//DTD DocBook XML V4.5//EN"'
                ' "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">')
            f.write('<book>\n')
            XI = "http://www.w3.org/2001/XInclude"
            for doc in self._docnames:
                if doc != "index":
                    f.write('<xi:include xmlns:xi="{XI}" href="{doc}.xml"/>\n'.
                            format(XI=XI, doc=doc))
            f.write('</book>')
