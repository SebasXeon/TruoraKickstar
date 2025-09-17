import reflex as rx
from TruoraKickstar.supabase_client import supabase

class AuthState(rx.State):
    email: str = ""
    password: str = ""
    message: str = ""
    logged_in: bool = False

    @rx.event
    def login(self):
        try:
            result = supabase.auth.sign_in_with_password(
                {"email": self.email, "password": self.password}
            )
            if result.user:
                self.logged_in = True
                self.message = f"Bienvenido {result.user.email}"
            else:
                self.message = "Login fallido."
        except Exception as e:
            self.message = f"Error: {str(e)}"

    @rx.event
    def set_email(self, nuevo: str):
        self.email = nuevo

    @rx.event
    def set_password(self, nuevo: str):
        self.password = nuevo
