import soundfile as sf
from transformers import pipeline

from app.config import settings
from app.utils.file_utils import build_output_path

_tts_pipeline = None

def get_tts_pipeline():
    global _tts_pipeline

    if _tts_pipeline is None:
        pipeline_kwargs = {
            "task": "text-to-speech",
            "model": settings.HF_MODEL,
            "model_kwargs": {
                "cache_dir": settings.HF_CACHE_DIR
            }
        }

        if settings.HF_TOKEN:
            pipeline_kwargs["token"] = settings.HF_TOKEN

        _tts_pipeline = pipeline(**pipeline_kwargs)

    return _tts_pipeline

def warmup_model():
    pipe = get_tts_pipeline()
    pipe("Bonjour")

def synthesize_to_file(text: str, output_file: str) -> str:
    if len(text) > settings.MAX_TEXT_LENGTH:
        raise ValueError(f"Text too long. Max allowed length is {settings.MAX_TEXT_LENGTH} characters.")

    pipe = get_tts_pipeline()
    result = pipe(text)

    audio = result["audio"]
    sampling_rate = result["sampling_rate"]

    output_path = build_output_path(settings.OUTPUT_DIR, output_file)
    sf.write(output_path, audio, sampling_rate)

    return output_path

def synthesize_default() -> str:
    return synthesize_to_file(settings.DEFAULT_TEXT, settings.DEFAULT_OUTPUT_FILE)