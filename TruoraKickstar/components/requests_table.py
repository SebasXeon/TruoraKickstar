import reflex as rx

from TruoraKickstar.models.request_model import DocRequest
from TruoraKickstar.states.index_state import IndexState



def show_request(doc_request: DocRequest):
    return rx.table.row(
        rx.table.cell(doc_request.id),
        rx.table.cell(doc_request.client_name),
        rx.table.cell(doc_request.product),
        rx.table.cell(doc_request.lang),
        rx.table.cell(doc_request.framework),
        rx.table.cell(doc_request.notes),
        rx.table.cell(rx.link("Ver documentación", href=f"/doc/{doc_request.id}")),
    )


def RequestTable() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Cliente"),
                rx.table.column_header_cell("Producto"),
                rx.table.column_header_cell("Lenguaje"),
                rx.table.column_header_cell("Framework"),
                rx.table.column_header_cell("Notas"),
                rx.table.column_header_cell(""),
            ),
        ),
        rx.table.body(
            rx.foreach(
                IndexState.requests, show_request
            )
        ),
        width="100%",
    )