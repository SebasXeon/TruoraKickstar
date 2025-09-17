import uuid
from TruoraKickstar.supabase_client import supabase
from TruoraKickstar.models.request_model import DocRequest

def add_requests(doc_request: DocRequest) -> DocRequest:
    doc_request.id = str(uuid.uuid4())
    response = supabase.table("requests").insert(doc_request.dict()).execute()
    return DocRequest(**response.data[0])