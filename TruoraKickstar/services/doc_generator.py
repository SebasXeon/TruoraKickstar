import reflex as rx
from TruoraKickstar.models import DocRequest
import httpx

async def gen_docs(doc_request: DocRequest):
    data = {
        "client": doc_request.client,
        "product": doc_request.product,
        "language": doc_request.lang,
        "framework": doc_request.framework,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://sebasxeon.app.n8n.cloud/webhook-test/dfd2c398-9217-4f67-99e8-f9ebebf95d3e",
            json=data,
            timeout=60
        )
    return resp.json()
