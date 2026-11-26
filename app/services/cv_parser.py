from PyPDF2 import PdfReader
import tempfile

async def extract_text(file):

    temp = tempfile.NamedTemporaryFile(delete=False)

    contents = await file.read()

    temp.write(contents)

    temp.close()

    reader = PdfReader(temp.name)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text