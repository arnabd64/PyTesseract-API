import pytesseract
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=8000,
        workers=1,
        loop="uvloop",
        http="httptools",
        log_config="log-config.yaml",
        headers=[("X-PyTesseract-Ver", pytesseract.__version__)],
    )
