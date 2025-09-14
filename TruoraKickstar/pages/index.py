import reflex as rx
from TruoraKickstar import state
from TruoraKickstar.components.layout.sidebar import SideBar
#from TruoraKickstar.components.doc_list_item import DocListItem

def index() -> rx.Component:
    """Página principal: listado de documentaciones + buscador."""
    # placeholder: listado vacío o cargado
    """ list_items = rx.foreach(
        State.lista_docs,
        lambda doc: DocListItem(doc=doc),
    ) """
    return rx.flex(
        SideBar(),
        rx.heading("Truora KickStart"),
        padding="2em",
        align_items="stretch",
        height="100vh",
        gap="2rem"
    )
