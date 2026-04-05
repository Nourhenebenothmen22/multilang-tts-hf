from pydantic import BaseModel, Field

class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)
    output_file: str = Field(default="generated.wav")

class TTSResponse(BaseModel):
    message: str
    output_path: str