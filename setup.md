## Setup
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

## Run
```bash
python src/main.py
```

Audio is saved to `audio/`, transcripts to `transcripts/`.
Edit `src/config.py` to change the model size, language, or device.