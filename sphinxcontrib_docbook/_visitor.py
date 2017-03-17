from docutils.nodes import NodeVisitor

from xml.sax.saxutils import XMLGenerator
from six import StringIO


class DocbookVisitor(NodeVisitor):
    def __init__(self, document):
        NodeVisitor.__init__(self, document)

        self._output = StringIO()
        self.generator = XMLGenerator(self._output, "utf-8")
        self.generator.outf = self._output

        self.within_index = False

    def astext(self):
        return self._output.getvalue()

    def visit_paragraph(self, node):
        self.generator.startElement('para', {})

    def depart_paragraph(self, node):
        self.generator.endElement('para')

    def visit_document(self, node):
        self.generator.startDocument()

        self.generator.outf.write(
            '<!DOCTYPE chapter PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN"'
            ' "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">')
        self.sec_level = 0

    def depart_document(self, node):
        self.generator.endDocument()

    def visit_section(self, node):
        assert not self.within_index
        self.generator.startElement('chapter'
                                    if self.sec_level == 0 else 'section', {})
        self.sec_level += 1

    def depart_section(self, node):
        self.sec_level -= 1
        self.generator.endElement('chapter'
                                  if self.sec_level == 0 else 'section')

    def visit_title(self, node):
        self.generator.startElement('title', {})

    def depart_title(self, node):
        self.generator.endElement('title')

    def visit_Text(self, node):
        self.generator.characters(node.astext())

    def depart_Text(self, node):
        pass

    def visit_index(self, node):
        # self.generator.startElement('index', {})
        self.within_index = True
        pass

    def depart_index(self, node):
        # self.generator.endElement('index')
        self.within_index = False
        pass

    def visit_target(self, node):
        # self.generator.startElement('section', {})
        pass

    def depart_target(self, node):
        pass

    def visit_emphasis(self, node):
        self.generator.startElement("emphasis", {})

    def depart_emphasis(self, node):
        self.generator.endElement("emphasis")

    def visit_math(self, node):
        pass

    def depart_math(self, node):
        pass

    def visit_doctest_block(self, node):
        self.generator.startElement("programlisting", {"language": "python"})

    def depart_doctest_block(self, node):
        self.generator.endElement("programlisting")

    def visit_strong(self, node):
        self.generator.startElement("emphasis", {"role": "bold"})

    def depart_strong(self, node):
        self.generator.endElement("emphasis")

    def visit_title_reference(self, node):
        pass

    def depart_title_reference(self, node):
        pass

    def visit_displaymath(self, node):
        pass

    def depart_displaymath(self, node):
        pass

    def visit_note(self, node):
        self.generator.startElement('note', {})

    def depart_note(self, node):
        self.generator.endElement('note')

    def visit_tip(self, node):
        self.generator.startElement('tip', {})

    def depart_tip(self, node):
        self.generator.endElement('tip')

    def visit_warning(self, node):
        self.generator.startElement('warning', {})

    def depart_warning(self, node):
        self.generator.endElement('warning')

    def visit_unknown_visit(self, node):
        pass

    def depart_unknown_visit(self, node):
        pass

    def visit_literal_block(self, node):
        if "highlight_args" in node.attributes.keys():
            if "language" in node.attributes:
                args = dict(language=node.attributes["language"])
            else:
                args = {}
            self.generator.startElement("programlisting", args)
            self._lit_block_tag = "programlisting"
        else:
            self.generator.startElement("literal", {})
            self._lit_block_tag = "literal"

    def depart_literal_block(self, node):
        self.generator.endElement(self._lit_block_tag)
        del self._lit_block_tag

    def visit_literal(self, node):
        self.generator.startElement("literal", {})

    def depart_literal(self, node):
        self.generator.endElement("literal")

    def visit_comment(self, node):
        pass

    def depart_comment(self, node):
        pass

    def visit_compound(self, node):
        pass

    def depart_compound(self, node):
        pass

    def visit_compact_paragraph(self, node):
        pass

    def depart_compact_paragraph(self, node):
        pass

    def visit_figure(self, node):
        pass

    def depart_figure(self, node):
        pass

    def visit_image(self, node):
        pass

    def depart_image(self, node):
        pass

    def visit_reference(self, node):
        pass

    def depart_reference(self, node):
        pass

    def visit_caption(self, node):
        pass

    def depart_caption(self, node):
        pass

    def visit_bullet_list(self, node):
        self.generator.startElement("itemizedlist", {})

    def depart_bullet_list(self, node):
        self.generator.endElement("itemizedlist")

    def visit_enumerated_list(self, node):
        self.generator.startElement("orderedlist", {})

    def depart_enumerated_list(self, node):
        self.generator.endElement("orderedlist")

    def visit_list_item(self, node):
        self.generator.startElement("listitem", {})

    def depart_list_item(self, node):
        self.generator.endElement("listitem")

    def visit_field_list(self, node):
        self.generator.startElement("variablelist", {})

    def depart_field_list(self, node):
        self.generator.endElement("variablelist")

    def visit_field(self, node):
        self.generator.startElement("varlistentry", {})

    def depart_field(self, node):
        self.generator.endElement("varlistentry")

    def visit_field_name(self, node):
        self.generator.startElement("term", {})

    def depart_field_name(self, node):
        self.generator.endElement("term")

    def visit_field_body(self, node):
        self.generator.startElement("listitem", {})

    def depart_field_body(self, node):
        self.generator.endElement("listitem")

    def visit_definition_list(self, node):
        self.generator.startElement("variablelist", {})

    def depart_definition_list(self, node):
        self.generator.endElement("variablelist")

    def visit_definition_list_item(self, node):
        self.generator.startElement("varlistentry", {})

    def depart_definition_list_item(self, node):
        self.generator.endElement("varlistentry")

    def visit_term(self, node):
        self.generator.startElement("term", {})

    def depart_term(self, node):
        self.generator.endElement("term")

    def visit_definition(self, node):
        self.generator.startElement("listitem", {})

    def depart_definition(self, node):
        self.generator.endElement("listitem")

    def visit_block_quote(self, node):
        self.generator.startElement("blockquote", {})

    def depart_block_quote(self, node):
        self.generator.endElement("blockquote")

    def visit_inline(self, node):
        self.generator.startElement("inline", {})

    def depart_inline(self, node):
        self.generator.endElement("inline")

    def visit_programlisting(self, node):
        self.generator.startElement("programlisting", {})

    def depart_programlisting(self, node):
        self.generator.endElement("programlisting")
