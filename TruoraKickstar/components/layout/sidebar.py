"""Sidebar component for the app."""

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.

    """
    return rx.button(
        rx.icon("search", size=18),
        width="100%",
        height="3.5rem",
        border_radius="1rem"

    )

def sidebar_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=18)

def sidebar_item(text: str, url: str, icon: str) -> rx.Component:
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/index") & text == "Inicio"
    )

    return rx.link(
        rx.vstack(
            rx.center(
                sidebar_item_icon(icon),
                padding=".4rem 0rem",
                border_radius="1rem",
                class_name="icon-box",  # <- clase en el hijo
                style={
                    "background_color": rx.cond(
                        active,
                        rx.color("purple", 6),
                        rx.color("gray", 2),
                    )
                }
            ),
            rx.text(
                text,
                size="1",
                class_name="sidebar-text",  # <- clase si quieres cambiar texto en hover
                padding_top=".4rem",
                weight="bold",
            ),
            color=rx.cond(
                active,
                rx.color("gray", 12),
                rx.color("gray", 11),
            ),
            align="center",
            spacing="2",
            style={
                # <- usar & .selector dentro de _hover
                "_hover": {
                    "& .icon-box": {
                        "background_color": rx.cond(
                            active,
                            rx.color("purple", 8),
                            rx.color("gray", 3),
                        )
                    },
                    "color": rx.color("gray", 12),
                    "cursor": "pointer",
                },
                "text_align": "center",
                "display": "block",
            },
            width="56px",
        ),
        href=url,
        underline="none"
    )




def SideBar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """

    return rx.flex(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                sidebar_item(
                    text="Inicio",
                    url="/",
                    icon="home",
                ),
                sidebar_item(
                    text="Crear docs",
                    url="/create-doc",
                    icon="clipboard-plus",
                ),
            )
        ),
        bg=rx.color("gray", 2),
        padding="1rem 1rem",
        border_radius=".8rem"
    )