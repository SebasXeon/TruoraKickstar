import reflex as rx
from TruoraKickstar.pages.login import login
from TruoraKickstar.states.auth_state import AuthState

def redirect_to_login():
    return rx.html("""
        <script>
            window.location.href = '/login';
        </script>
    """)

def protected_page(content: rx.Component) -> rx.Component:
    return rx.cond(
        AuthState.logged_in,
        content,
        login()
    )