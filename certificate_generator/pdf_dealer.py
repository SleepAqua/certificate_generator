import os
import comtypes.client

from .consts import LOGGER


def d2p(in_file, out_file):
    """
    docx to pdf
    """
    in_file = str(in_file)
    out_file = str(out_file)
    if os.path.isfile(out_file):
        LOGGER.info(f"{out_file} exists, pass")
        return False
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=17)
    doc.Close()
    word.Quit()
    LOGGER.info(f"{out_file} saved")
    return True
