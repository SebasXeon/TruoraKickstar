import reflex as rx
from TruoraKickstar.states.auth_state import AuthState


def login():
    return rx.center(
        rx.vstack(
            rx.input(
                placeholder="Correo",
                on_change=AuthState.set_email,
                value=AuthState.email,
                width="100%",
            ),
            rx.input(
                placeholder="Contraseña",
                type="password",
                on_change=AuthState.set_password,
                value=AuthState.password,
                width="100%",
            ),
            rx.flex(
                rx.button("Iniciar sesión", on_click=AuthState.login),
                align_self="end",
            ),
            rx.text(AuthState.message, color="red"),
            rx.cond(
                AuthState.logged_in,
                rx.script("window.location.href = '/';"),
            ),
            bg=rx.color("gray", 6),
            width="20rem",
            padding="1rem 1rem",
            border_radius=".8rem",
        ),
        height="100vh",
    )

