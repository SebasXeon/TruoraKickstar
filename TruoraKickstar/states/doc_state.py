import reflex as rx
import json

from TruoraKickstar.models.request_model import DocRequest
from TruoraKickstar.services.request_services import get_request


class DocState(rx.State):
    request: DocRequest = None
    request_guide: str = ""

    @rx.event
    async def load_request(self):
        yield
        request = get_request(self.request_id)
        if request:
            self.request = request
            self.request_guide = json.loads(request.generated_doc)['guide']