from pathlib import Path 

# Paths (resolved relative to the project root)
BASE_DIR = Path(r"C:\Users\Aayush\OneDrive\Desktop\projects\voice_transcriber\src\config.py").resolve().parent.parent
AUDIO_DIR = Path(r"C:\Users\Aayush\OneDrive\Desktop\projects\voice_transcriber\audio").resolve()
TRANSCRIPT_DIR = Path(r"C:\Users\Aayush\OneDrive\Desktop\projects\voice_transcriber\transcripts").resolve()

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)


# Audio settings (Whisper expects 16 kHz mono)
SAMPLE_RATE = 16000
CHANNELS = 1


# Whisper settings
MODEL_SIZE = "base"        # tiny, base, small, medium, large-v3
DEVICE = "cpu"             # "cuda" if you have an NVIDIA GPU
COMPUTE_TYPE = "int8"      # "float16" for GPU
LANGUAGE = None            # None = auto-detect, or "en", "hi", etc.