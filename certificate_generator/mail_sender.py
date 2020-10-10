import os
import pandas as pd
import yagmail

from .consts import LOGGER, MAIL_INFO, RECEIVER_PATH, OUT_PDF_DIR


def get_receivers(receiver_path=RECEIVER_PATH):
    receiver_df = pd.read_excel(receiver_path, usecols=[0,1,2], names=["id", "name", "addr"])
    return receiver_df

def send_all(mail_info=MAIL_INFO):
    receiver_df = get_receivers()
    LOGGER.info("Loaded the receivers info.")

    yag = yagmail.SMTP({mail_info["username"]: mail_info["from_"]}, mail_info["password"], mail_info["host"], encoding="gbk")
    LOGGER.info("Connected to the SMTP server.")

    for i, r in receiver_df.iterrows():
        del i
        name_ = r["name"]
        addr_ = r["addr"]
        
        pdf_name = f"{name_}.pdf"
        cert = str(OUT_PDF_DIR / pdf_name)

        if not os.path.isfile(cert):
            LOGGER.error(f"[NOT FOUND]: {cert}")
            continue
        
        subject = mail_info["title"]
        txt = mail_info["text"].format(name_)
        yag.send(to=addr_,
                 subject=subject,
                 contents=txt, 
                 attachments=cert
                )
        
        LOGGER.info(f"[SENT]: {name_} ==> {addr_}")
