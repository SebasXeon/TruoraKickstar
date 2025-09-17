from typing import Optional
import reflex as rx

class DocRequest(rx.Model):
    id: Optional[str] = None
    client_name: str
    product: str
    lang: str
    framework: Optional[str] = None
    notes: Optional[str] = None
    state: Optional[str] = None
    generated_doc: Optional[str] = None