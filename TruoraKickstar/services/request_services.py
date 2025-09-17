import uuid
from TruoraKickstar.states.auth_state import AuthState
from TruoraKickstar.supabase_client import supabase
from TruoraKickstar.models.request_model import DocRequest

# Add request
def add_requests(doc_request: DocRequest) -> DocRequest:
    doc_request.id = str(uuid.uuid4())
    response = supabase.table("requests").insert(doc_request.dict()).execute()
    return DocRequest(**response.data[0])

# Get single request by id
def get_request(request_id: str) -> DocRequest | None:
    response = supabase.table("requests").select("*").eq("id", request_id).execute()
    if not response.data:
        return None
    return DocRequest(**response.data[0])


# Get all requests
def get_requests() -> list[DocRequest]:
    response = supabase.table("requests").select("*").execute()
    return [DocRequest(**request) for request in response.data]