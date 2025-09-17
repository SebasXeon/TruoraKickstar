import reflex as rx

from TruoraKickstar.states.doc_state import DocState
from TruoraKickstar.components.doc_viewer import DocViewer
from TruoraKickstar.auth.auth_guard import protected_page
from TruoraKickstar.components.requests_table import RequestTable
from TruoraKickstar.components.layout.sidebar import SideBar
from TruoraKickstar.components.layout.page_title import PageTitle


def view_dow():
    # Displays the dynamic part of the URL, the post ID
    #
    return protected_page(rx.flex(
            SideBar(),
            rx.flex(
                PageTitle(f"Documentación para {DocState.request.client_name}", f"Documentación generada con {DocState.request.product} - {DocState.request.lang}"),
                rx.flex(
                    DocViewer(DocState.request_guide),
                    bg=rx.color("gray", 4),
                    padding="1rem 1rem",
                    border_radius=".8rem",
                    max_height="100%",
                    overflow="auto"
                ),
                gap="1rem",
                flex_direction="column",
                width="100%"
            ),
            padding="2em",
            align_items="stretch",
            height="100vh",
            gap="1rem"
    ))