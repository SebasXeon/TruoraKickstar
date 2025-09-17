import reflex as rx
from TruoraKickstar.pages.login import login
from TruoraKickstar.states.auth_state import AuthState

def require_login(page_func):
    def wrapper(*args, **kwargs):
        return rx.cond(
            AuthState.logged_in,
            page_func(*args, **kwargs),
            rx.redirect("/login")
        )
    return wrapper

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