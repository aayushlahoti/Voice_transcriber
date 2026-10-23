this file is for the understanding of the project (how does the project works and what is the workflow of the project) 
what is the function of each file?????


- main.py : this is the entry point of the, the command is used to run this file which starts the whole project

- recorder.py : this file is used for the microphone input 
                It handles things like:

microphone selection
sample rate
recording duration
audio chunks
starting/stopping recording


- transcriber.py : this file is the point where your whisper flow is loaded which transforms the voice fiel to text 

- config.py : it contains settings of the project 



audio/ :
this folders saves the voice recordings in your device's memory 


transcripts/ :
this folder saves the text files that are transcribed 


WORKFLOW OF THE PROJECT :

                    VOICE TRANSCRIBER
                           │
                           ▼
                     🎤 Microphone
                           │
                           ▼
                    recorder.py
                           │
                           ▼
                      Audio Data
                           │
                           ▼
                   transcriber.py
                           │
                           ▼
                  faster-whisper
                           │
                           ▼
                    Transcribed Text
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
             Terminal            .txt file


this project as of now only takes the voice record as an input, processes it and then transcribes the voice into text, changes and mods will be done later on and will be documented.