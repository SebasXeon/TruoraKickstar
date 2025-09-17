import reflex as rx
from TruoraKickstar.supabase_client import supabase

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
        try:
            session = supabase.auth.sign_in_with_password(
                {"email": self.email, "password": self.password}
            )
            if session.user:
                self.logged_in = True
                supabase.auth.set_session(session.session.access_token, session.session.refresh_token)
                supabase.postgrest.auth(session.session.access_token)
                self.message = f"Bienvenido {session.user.email}"
            else:
                print(session)
                self.message = "Login fallido."
        except Exception as e:
            print(e)
            self.message = f"Error: {str(e)}"
        self.processing = False

    @rx.event
    def set_email(self, nuevo: str):
        self.email = nuevo

    @rx.event
    def set_password(self, nuevo: str):
        self.password = nuevo
