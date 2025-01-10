FROM python:3.12-slim-bookworm

COPY requirements.txt .
RUN apt update && \
    apt install --yes tesseract-ocr-all && \
    pip install -r requirements.txt && \
    pip cache purge && \
    useradd -m py
USER py

WORKDIR /app
COPY --chown=py . .

EXPOSE 8000

CMD ["python3", "main.py"]