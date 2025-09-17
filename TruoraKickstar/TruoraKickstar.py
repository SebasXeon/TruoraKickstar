"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from TruoraKickstar.pages.index import index
from TruoraKickstar.pages.login import login
from TruoraKickstar.pages.new_doc import new_doc
from TruoraKickstar.pages.view_doc import view_dow


from TruoraKickstar.states.index_state import IndexState
from TruoraKickstar.states.doc_state import DocState


app = rx.App(
    theme=rx.theme(
        accent_color="purple",
        radius="large"
    )
)
app.add_page(
    index,
    route="/",
    title="Truora Kickstart",
    on_load=IndexState.list_requests
)
app.add_page(
    login,
    route="/login",
    title="Truora Kickstart - Login"
)
app.add_page(
    new_doc,
    route="/new_doc",
    title="Truora Kickstart - Nueva documentación"
)

app.add_page(
    view_dow,
    route="/doc/[request_id]",
    title="Truora Kickstart - Ver documentación",
    on_load=DocState.load_request,
)
