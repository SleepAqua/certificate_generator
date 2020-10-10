import os
from docx import Document

from .consts import LOGGER, TEMPLATE_PATH, OUT_DOC_DIR, OUT_PDF_DIR
from .pdf_dealer import d2p


class CertGenerator:
    def __init__(self, name, name_row, num, num_row):
        self.read_path = TEMPLATE_PATH
        self.docx_obj = Document(self.read_path)

        self.doc_path = OUT_DOC_DIR / f"{name}.docx"
        self.pdf_path = OUT_PDF_DIR / f"{name}.pdf"

        self.name = name
        self.name_row = name_row
        self.num = num
        self.num_row = num_row

    def modify(self):
        paragraphs = self.docx_obj.paragraphs
        print(len(paragraphs))
        paragraphs[self.name_row].text = self.name
        paragraphs[self.num_row].text = self.num

    def view(self):
        for child in self.docx_obj.element.body.iter():
            if child.tag.endswith("textbox"):
                for c in child.iter():
                    c_tag = c.tag
                    if c_tag.endswith("main}r"):
                        print(c.text)

    def dump_docx(self):
        if os.path.isfile(self.doc_path):
            LOGGER.info("{}的doc证书文件已存在，跳过".format(self.name))
        else:
            self.docx_obj.save(self.doc_path)
            LOGGER.info("{}的doc证书文件已保存".format(self.name))

    def main(self):
        self.modify()
        self.dump_docx()
        d2p(self.doc_path, self.pdf_path)
