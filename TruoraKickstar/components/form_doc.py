import reflex as rx

from TruoraKickstar.states.form_state import FormState

def FormDoc() -> rx.Component:
    return rx.flex(
        rx.heading("Especificaciones", as_="h2"),

        rx.form(
            rx.vstack(
                rx.form.field(
                    rx.form.label("Cliente"),
                    rx.input(
                        name="client",  
                        placeholder="Nombre del cliente",
                        value=FormState.client,
                        on_change=FormState.set_client,
                        required=True,
                        # opcional: value/on_change si quieres enlazar con State
                    ),
                    width="100%"
                ),
                
                rx.form.field(
                    rx.form.label("Producto"),
                    rx.select(
                        ["Verificación de antecedentes", "Validación de identidad digital", "Firma electrónica"],
                        value=FormState.product,
                        on_change=FormState.set_product,
                    ),
                    width="100%"
                ),

                rx.form.field(
                    rx.form.label("Lenguaje implementación"),
                    rx.select(
                        ["JavaScript", "Python", "Java", "PHP", "Ruby", "Dart", "GoLang"],
                        value=FormState.lang,
                        on_change=FormState.set_lang,
                    ),
                    width="100%"
                ),

                rx.form.field(
                    rx.form.label("Framework"),
                    rx.input(
                        name="framework",  
                        placeholder="Framework usado por el cliente",
                        required=False,
                        value=FormState.framework,
                        on_change=FormState.set_framework,
                    ),
                    width="100%"
                ),

                rx.form.field(
                    rx.form.label("Notas y/o especificaciones"),
                    rx.text_area(
                        name="notes",
                        placeholder="Notas y/o especicifaciones para la generación de docs.",
                        min_height="120px",
                        value=FormState.notes,
                        on_change=FormState.set_notes,
                    ),
                    width="100%"
                ),

                # Submit
                rx.flex(
                    rx.button(
                        "Generar",
                        type_="submit",
                        loading=FormState.processing,
                    ),
                    width="100%",
                    justify="end"
                )
            ),
            on_submit=FormState.generate_documentation,
            reset_on_submit=False,
            width="100%",
            spacing="1rem",
        ),

        flex_direction="column",
        gap="1rem",
        width="100%",
        bg=rx.color("gray", 4),
        padding="1rem 1rem",
        border_radius=".8rem"
    )