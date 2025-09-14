import reflex as rx

config = rx.Config(
    app_name="TruoraKickstar",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    db_url="sqlite:///reflex.db",
)