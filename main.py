import argparse
from certificate_generator.word_dealer import CertGenerator
from certificate_generator.pdf_dealer import d2p
from certificate_generator.mail_sender import get_receivers, send_all


def generate_and_send(name_row_, num_row_):
    receiver_df = get_receivers()
    for i, r in receiver_df.iterrows():
        del i
        id_ = r["id"]
        name_ = r["name"]

        CG = CertGenerator(name=name_, name_row=name_row_, num=id_, num_row=num_row_)
        CG.main()
    send_all()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("name", type=str, help="name on certificate")
    parser.add_argument("name_row", type=int, help="the row of name on certificate")
    # parser.add_argument("num", type=str, help="num on certificate")
    parser.add_argument("num_row", type=int, help="the row of num on certificate")
    args = parser.parse_args()

    generate_and_send(args.name_row, args.num_row)
