from TruoraKickstar.models.request_model import DocRequest
import httpx

async def gen_docs(doc_request: DocRequest):
    data = {
        "request_id": doc_request.id
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://sebasxeon.app.n8n.cloud/webhook-test/dfd2c398-9217-4f67-99e8-f9ebebf95d3e",
            json=data,
            timeout=60
        )
    return resp.json()
