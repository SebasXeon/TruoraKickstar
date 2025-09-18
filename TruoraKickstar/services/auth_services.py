from TruoraKickstar.supabase_client import supabase

def auth_user(email: str, password: str) -> bool:
    logged_in = False
    try:
        session = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )
        if session.user:
            logged_in = True
            supabase.auth.set_session(session.session.access_token, session.session.refresh_token)
            supabase.postgrest.auth(session.session.access_token)
    except Exception as e:
        print(f"Error: {str(e)}")
    return logged_in