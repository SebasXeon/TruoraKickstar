import reflex as rx

from TruoraKickstar.services.doc_services import render_doc
from pathlib import Path


class DocState(rx.State):
    @rx.event
    def download_pdf(self, doc_md: str):
        output_path = Path("output.pdf")
        render_doc(doc_md, output_path)
        return rx.download(output_path)


def DocViewer(documentation: str) -> rx.Component:
    return rx.box(
        rx.markdown(
            documentation,
            flex_direction="column",
            max_width="100%",
        ),
        rx.button(
            "Descargar",
            on_click=lambda: DocState.download_pdf(documentation),  # 👈 usa el md recibido
            style={
                "position": "fixed",
                "bottom": "4rem",
                "right": "4rem",
                "z_index": 1000,
            },
        ),
        max_height="100%",
        max_width="100%",
        overflow="scroll",
    )