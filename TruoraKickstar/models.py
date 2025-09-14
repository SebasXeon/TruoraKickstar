from typing import Optional
import reflex as rx


class DocRequest(rx.Model, table=True):
    client: str
    product: str
    lang: str
    framework: Optional[str] = None
    notes: Optional[str] = None

class Documentacion(rx.Model, table=False):
    """Modelo para documentaciones generadas."""
    titulo: str
    descripcion: str
    contenido: str
    fecha_creacion: Optional[str] = None
    # quizá autor, etc.

    # Si quieres: metadata, tags, etc.