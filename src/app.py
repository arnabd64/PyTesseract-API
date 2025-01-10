import io

import uuid
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from PIL import Image
from pytesseract import Output, pytesseract

app = FastAPI(title="Tesseract API", version=str(pytesseract.get_tesseract_version()))

app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=9)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def parse_image(encoded_image: UploadFile) -> Image.Image:
    return Image.open(io.BytesIO(encoded_image.file.read()))


def ocr(decoded_image: Image.Image) -> str:
    return pytesseract.image_to_string(decoded_image, output_type=Output.STRING)


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Tesseract Server is Running</h1>"


@app.post("/ocr", response_class=PlainTextResponse)
def text_to_string(image: UploadFile):
    return ocr(parse_image(image))


@app.middleware("http")
async def response_id(request, call_next):
    response = await call_next(request)
    response.headers["x-response-id"] = str(uuid.uuid4())
    return response
