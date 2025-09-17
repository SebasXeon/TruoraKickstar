import reflex as rx
from TruoraKickstar.auth.auth_guard import protected_page
from TruoraKickstar.components.layout.sidebar import SideBar


def index() -> rx.Component:
    return protected_page(rx.flex(
        SideBar(),
        rx.heading("Truora KickStart"),
        padding="2em",
        align_items="stretch",
        height="100vh",
        gap="2rem"
    ))
