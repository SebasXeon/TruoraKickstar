"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from TruoraKickstar.pages.index import index
from TruoraKickstar.pages.new_doc import new_doc
from TruoraKickstar.pages.login import login

app = rx.App(
    theme=rx.theme(
        accent_color="purple",
        radius="large"
    )
)
app.add_page(index)
app.add_page(login, route="/login")
app.add_page(new_doc, route="/create-doc")
