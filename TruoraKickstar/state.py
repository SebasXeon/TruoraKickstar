# generador_doc_ai/state.py

import reflex as rx

from TruoraKickstar.models import DocRequest
#from .models import Documentacion
from TruoraKickstar.services.doc_generator import gen_docs

class State(rx.State):
    # Vars del formulario
    client: str = ""
    product: str = ""
    lang: str = ""
    framework: str = ""
    notes: str = ""
    generated_docs: str = ""
    procesando: bool = False

    # Vars para listado y búsqueda
    #lista_docs: list[Documentacion] = []
    #termino_busqueda: str = ""

    # Event handler: cuando el usuario envía el formulario
    @rx.event
    def generate_documentation(self):
        """Lanza la generación IA de la documentación."""
        print(self.client, self.product, self.lang, self.framework, self.notes)
        self.procesando = True
        doc_request = DocRequest(client=self.client, product=self.product, lang=self.lang, framework=self.framework, notes=self.notes)
        yield 
        generated_docs = gen_docs(doc_request)
        print(generated_docs)
        self.generated_docs = generated_docs
        self.procesando = False

    @rx.event
    def set_client(self, nuevo: str):
        self.client = nuevo

    @rx.event
    def set_product(self, nuevo: str):
        self.product = nuevo

    @rx.event
    def set_lang(self, nuevo: str):
        self.lang = nuevo

    @rx.event
    def set_framework(self, nuevo: str):
        self.framework = nuevo

    @rx.event
    def set_notes(self, nuevo: str):
        self.notes = nuevo

    @rx.event
    def cargar_docs(self):
        """Cargar documentos existentes desde la base de datos."""
        # implementar...
        pass
