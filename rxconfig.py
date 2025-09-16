import os
import reflex as rx
from dotenv import load_dotenv

load_dotenv()

config = rx.Config(
    app_name="TruoraKickstar",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    db_url=f"postgresql://postgres:{os.getenv('SUPABASE_PASS')}@db.xecdliostxcgdjyolvqz.supabase.co:5432/postgres",
)