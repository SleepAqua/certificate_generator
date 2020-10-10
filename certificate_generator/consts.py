import sys
from pathlib import Path

from .txx_tools.txx_log import single_lvl_logger
from .txx_tools.txx_io import read_json
from .txx_tools.txx_os import make_parent_dir


PROG_PATH = Path(sys.path[0])

LOGGER = single_lvl_logger()
MAIL_INFO = read_json(PROG_PATH / "original_info" / "mail_info.json")
TEMPLATE_PATH = PROG_PATH / "original_info" / "template.docx"
RECEIVER_PATH = PROG_PATH / "original_info" / "receivers.xlsx"

OUT_DOC_DIR = PROG_PATH / "generated_info" / "docs"; make_parent_dir(OUT_DOC_DIR)
OUT_PDF_DIR = PROG_PATH / "generated_info" / "pdfs"; make_parent_dir(OUT_PDF_DIR)
