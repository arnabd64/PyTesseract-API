#!/bin/bash
# Install Tesseract
sudo apt update && \
sudo apt install --yes tesseract-ocr-all

# install python libs
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install --no-cache-dir -r requirements.txt