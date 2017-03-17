from docutils.writers import Writer
from ._visitor import DocbookVisitor


class DocbookWriter(Writer):
    def __init__(self, builder):
        Writer.__init__(self)
        self.builder = builder

    def translate(self):
        self.visitor = visitor = DocbookVisitor(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()
