import reflex as rx
from TruoraKickstar.models import DocRequest


def gen_docs(doc_request = DocRequest):
    with rx.session() as session:
        session.add(
            doc_request
        )
        session.commit()
    return "Ok"