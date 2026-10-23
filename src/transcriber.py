#this file loads the model and reuses it  and also saves the transcription as .ext file in transcript folder 

from pathlib import Path
from faster_whisper import WhisperModel
from config import COMPUTE_TYPE, DEVICE, LANGUAGE, MODEL_SIZE, TRANSCRIPT_DIR

class Transcriber:
    def __init__(self):
        print(f"Loading Whisper model '{MODEL_SIZE}' (first run downloads it)...")
        self.model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

    def transcribe(self, audio_path: Path) -> tuple[str, str]:
        """Returns (text, detected_language)."""
        segments, info = self.model.transcribe(
            str(audio_path),
            language=LANGUAGE,
            beam_size=5,
            vad_filter=True,  # skips silence
        )
        # `segments` is a generator, so consuming it runs the actual transcription
        text = " ".join(segment.text.strip() for segment in segments)
        return text, info.language

    def save(self, text: str, audio_path: Path) -> Path:
        """Save transcript with the same name as the audio file."""
        out_path = TRANSCRIPT_DIR / f"{audio_path.stem}.txt"
        out_path.write_text(text, encoding="utf-8")
        return out_path