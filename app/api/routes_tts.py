from fastapi import APIRouter, HTTPException
from app.schemas import TTSRequest, TTSResponse
from app.services.tts_service import synthesize_to_file, synthesize_default

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/tts", response_model=TTSResponse)
def generate_tts(payload: TTSRequest):
    try:
        output_path = synthesize_to_file(
            text=payload.text,
            output_file=payload.output_file
        )
        return TTSResponse(
            message="Audio generated successfully",
            output_path=output_path
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/tts/default", response_model=TTSResponse)
def generate_default_tts():
    try:
        output_path = synthesize_default()
        return TTSResponse(
            message="Default audio generated successfully",
            output_path=output_path
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))