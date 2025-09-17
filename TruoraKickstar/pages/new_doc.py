import reflex as rx
from TruoraKickstar.states.form_state import FormState
from TruoraKickstar.auth.auth_guard import protected_page
from TruoraKickstar.components.layout.sidebar import SideBar
from TruoraKickstar.components.layout.page_title import PageTitle
from TruoraKickstar.components.form_doc import FormDoc
from TruoraKickstar.components.doc_viewer import DocViewer

def new_doc() -> rx.Component:
    return protected_page(
        rx.flex(
            SideBar(),
            rx.flex(
                PageTitle("Crear documentación", "Completa el formulario para generar una nueva documentación con ayuda del agente Truora Kickstart."),
                rx.grid(
                    FormDoc(),
                    rx.flex(
                        rx.cond(
                            FormState.generated_docs == "",
                            rx.cond(
                                FormState.procesando,
                                rx.center(
                                    rx.spinner(size="3"),
                                    rx.text("Generando documentación"),
                                    width="100%",
                                    gap="1rem",
                                    flex_direction="column",
                                ),
                                rx.center(
                                    rx.icon("scroll", size=64),
                                    rx.text("Aún no se ha generado una documentación."),
                                    width="100%",
                                    gap="1rem",
                                    flex_direction="column",
                                )
                            ),
                            DocViewer(FormState.generated_docs)
                        ),
                        bg=rx.color("gray", 6),
                        padding="1rem 1rem",
                        border_radius=".8rem",
                        max_height="100%",
                        overflow="auto"
                    ),
                    grid_template_columns="1fr 2fr",
                    gap="1rem",
                    overflow="auto"
                ),
                gap="1rem",
                flex_direction="column",
                width="100%"
            ),
            padding="2em",
            height="100dvh",
            gap="1rem"
        )
    )
