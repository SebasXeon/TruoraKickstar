import reflex as rx

from TruoraKickstar.models.request_model import DocRequest
from TruoraKickstar.services.request_services import get_requests

class IndexState(rx.State):
    requests: list[DocRequest] = []

    @rx.event
    async def list_requests(self):
        yield
        self.requests = get_requests()