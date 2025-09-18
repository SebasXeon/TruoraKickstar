from TruoraKickstar.models.request_model import DocRequest
import httpx
import os
import markdown
from fpdf import FPDF

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