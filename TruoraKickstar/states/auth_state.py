import reflex as rx
from TruoraKickstar.services.auth_services import auth_user


class AuthState(rx.State):
    email: str = ""
    password: str = ""
    message: str = ""
    processing: bool = False
    logged_in: bool = False

    @rx.event
    def login(self):
        self.processing = True
        yield
        logged_in = auth_user(self.email, self.password)
        self.logged_in = logged_in
        if self.logged_in:
            from TruoraKickstar.states.index_state import IndexState
            yield IndexState.list_requests()
        self.processing = False

    @rx.event
    def set_email(self, nuevo: str):
        self.email = nuevo

    @rx.event
    def set_password(self, nuevo: str):
        self.password = nuevo
