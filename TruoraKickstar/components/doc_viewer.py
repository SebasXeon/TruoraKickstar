import reflex as rx

from TruoraKickstar.state import State

def DocViewer(documentation) -> rx.Component:
    return rx.flex(
        rx.markdown(
            documentation,
            flex_direction="column",
            max_width="100%",
        ),
        max_height="100%",
        max_width="100%",
        overflow="scroll"
    )