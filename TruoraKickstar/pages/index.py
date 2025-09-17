import reflex as rx
from TruoraKickstar.auth.auth_guard import protected_page
from TruoraKickstar.components.requests_table import RequestTable
from TruoraKickstar.components.layout.sidebar import SideBar
from TruoraKickstar.components.layout.page_title import PageTitle


def index() -> rx.Component:
    return protected_page(rx.flex(
        SideBar(),
        rx.flex(
            PageTitle("Truora Kickstart", "Agente de implementación de Truora."),
            rx.flex(
                RequestTable(),
                bg=rx.color("gray", 4),
                padding="1rem 1rem",
                border_radius=".8rem",
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
