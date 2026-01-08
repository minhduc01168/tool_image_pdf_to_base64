# Image/PDF to Base64 Converter

A simple Streamlit web tool to convert Images and PDF files to Base64 strings.

## Features
- Upload Images (JPG, PNG, BMP, TIFF, WEBP) and PDFs.
- Automatic conversion to Base64.
- Copy to clipboard or download as `.txt`.
- No server-side file storage (processing is done in-memory).

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deploying to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Log in to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Connect your GitHub account and select this repository.
4. Click "Deploy".
