import reflex as rx


def PageTitle(text: str, desc: str) -> rx.Component:

    return rx.flex(
        rx.heading("Crear documentación", as_="h1", size="9"),
        rx.text(desc),
        flex_direction="column",
        width="100%",
        bg=rx.color("gray", 2),
        padding="1rem 1rem",
        border_radius=".8rem"
    )