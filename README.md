# EchoSoul — Voice Assistant

EchoSoul is a simple Python-based voice assistant that listens to spoken English, converts speech into text, and responds aloud.

## Current Features

- Microphone input using PyAudio
- Speech recognition using OpenAI Whisper
- Voice responses using pyttsx3
- Basic conversational commands
- Clean exit command

## Supported Commands

| Voice command | Response |
|---|---|
| Hello / Hi / Hey | Greets the user |
| Who are you? | Introduces EchoSoul |
| How are you? | Gives a conversational response |
| Exit / Quit / Stop / Goodbye | Ends the assistant |

## Requirements

- Python 3.12
- A working microphone
- Speakers or headphones
- Internet access for the initial Whisper model download

## Installation

Clone the repository and open its directory in PowerShell.

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run EchoSoul

```powershell
python echosoul.py
```

Speak clearly after the assistant says it is listening. Each command currently records approximately five seconds of audio.

## Project Status

**Prototype — basic voice interaction working.**

Wake-word activation, broader command support, and other advanced features are planned for future development.

## Privacy

Audio is recorded temporarily for speech recognition. Review the code before using the assistant in sensitive environments.

## License

No license has been selected yet.
