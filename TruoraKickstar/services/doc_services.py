from TruoraKickstar.models.request_model import DocRequest
import httpx
import os
import markdown
from fpdf import FPDF

from dotenv import load_dotenv
load_dotenv()
N8N_WEBHOOK = os.getenv("N8N_WEBHOOK")

async def gen_docs(doc_request: DocRequest):
    data = {
        "request_id": doc_request.id
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            N8N_WEBHOOK,
            json=data,
            timeout=60
        )
    return resp.json()


def render_doc(doc_md: str, output_path: str):
    html_string = markdown.markdown(
        doc_md,
        extensions=["extra", "nl2br", "sane_lists"]
    )

    # Crear PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    pdf.write_html(html_string)

    # Path de salida
    filepath = os.path.join("temp", output_path)

    # Guardar PDF
    pdf.output(filepath)

    return filepath