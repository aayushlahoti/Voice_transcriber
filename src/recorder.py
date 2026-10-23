import wave
from datetime import datetime
from pathlib import Path

import numpy as np
import sounddevice as sd

from config import AUDIO_DIR, CHANNELS, SAMPLE_RATE


class Recorder:
    def __init__(self):
        self._frames = []
        self._stream = None

    def _callback(self, indata, frames, time, status):
        if status:
            print(f"[audio status] {status}")
        self._frames.append(indata.copy())

    def start(self):
        self._frames = []
        self._stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",
            callback=self._callback,
        )
        self._stream.start()

    def stop(self) -> Path | None:
        """Stop recording and save to a .wav file. Returns the file path."""
        if self._stream is None:
            return None

        self._stream.stop()
        self._stream.close()
        self._stream = None

        if not self._frames:
            return None

        audio = np.concatenate(self._frames, axis=0)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = AUDIO_DIR / f"recording_{timestamp}.wav"

        with wave.open(str(path), "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  # int16 = 2 bytes
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio.tobytes())

        return path

#Records from the mic until you tell it to stop, then saves a .wav file. It uses the standard-library wave module, so no extra dependency is needed.