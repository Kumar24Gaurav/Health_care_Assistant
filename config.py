import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Check Streamlit Cloud Secrets first, then fall back to local .env
API_KEY = st.secrets.get("MISTRAL_API_KEY") or os.getenv("MISTRAL_API_KEY") or os.getenv("API_KEY")

if not API_KEY:
    raise ValueError(
        "MISTRAL_API_KEY is missing! Please add MISTRAL_API_KEY under Settings -> Secrets in Streamlit Cloud."
    )