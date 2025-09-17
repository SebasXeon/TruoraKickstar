import reflex as rx

from TruoraKickstar.models.request_model import DocRequest
from TruoraKickstar.services.request_services import add_requests
from TruoraKickstar.services.doc_services import gen_docs

class FormState(rx.State):
    client: str = ""
    product: str = ""
    lang: str = ""
    framework: str = ""
    notes: str = ""
    generated_docs: str = ""
    processing: bool = False

    @rx.event
    async def generate_documentation(self):
        print(self.client, self.product, self.lang, self.framework, self.notes)
        self.processing = True
        
        doc_request = DocRequest(
            client_name=self.client,
            product=self.product,
            lang=self.lang,
            framework=self.framework,
            notes=self.notes,
            state="Pending"
        )
        yield

        add_requests(doc_request)
        
        generated_docs = await gen_docs(doc_request)
        
        self.generated_docs = generated_docs.get("guide", "Erorr al procesar.")
        self.processing = False


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