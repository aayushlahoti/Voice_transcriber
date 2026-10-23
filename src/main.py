#this encompasses the main entry file that ties everything together and runs the program. It uses the Recorder and Transcriber classes to record audio, transcribe it, and save the transcript. 

from recorder import Recorder
from transcriber import Transcriber


def main():
    transcriber = Transcriber()
    recorder = Recorder()

    print("\n=== Voice Transcriber ===")
    print("Press Enter to start recording, Enter again to stop.")
    print("Type 'q' then Enter to quit.\n")

    while True:
        cmd = input("Ready > ").strip().lower()
        if cmd == "q":
            print("Bye!")
            break

        recorder.start()
        input("Recording... press Enter to stop.")
        audio_path = recorder.stop()

        if audio_path is None:
            print("No audio captured.\n")
            continue

        print("Transcribing...")
        text, lang = transcriber.transcribe(audio_path)

        if not text:
            print("No speech detected.\n")
            continue

        transcript_path = transcriber.save(text, audio_path)
        print(f"\n[{lang}] {text}\n")
        print(f"Saved: {transcript_path}\n")


if __name__ == "__main__":
    main()