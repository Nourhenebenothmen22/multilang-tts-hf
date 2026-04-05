import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "tts-hf")
    APP_ENV = os.getenv("APP_ENV", "development")
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(os.getenv("APP_PORT", "8000"))

    HF_MODEL = os.getenv("HF_MODEL", "facebook/mms-tts-fra")
    HF_TOKEN = os.getenv("HF_TOKEN", "")
    HF_CACHE_DIR = os.getenv("HF_CACHE_DIR", "/app/.cache/huggingface")

    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/app/data/output")
    DEFAULT_TEXT = os.getenv(
        "DEFAULT_TEXT",
        "Bonjour, ceci est un test de synthese vocale avec Hugging Face."
    )
    DEFAULT_OUTPUT_FILE = os.getenv("DEFAULT_OUTPUT_FILE", "sample_output.wav")

    DEVICE = os.getenv("DEVICE", "cpu").lower()
    PRELOAD_MODEL = os.getenv("PRELOAD_MODEL", "true").lower() == "true"
    MAX_TEXT_LENGTH = int(os.getenv("MAX_TEXT_LENGTH", "500"))

settings = Settings()