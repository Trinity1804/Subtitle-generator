# Python AI Transcriptor

This tool automatically generates subtitles for an MP4 video by:

- Extracting audio using MoviePy.
- Transcribing the audio using OpenAI's Whisper API.
- Generating an SRT subtitles file.

## Requirements

- Python 3.12+
- [whisper](https://github.com/openai/whisper)
- [moviepy](https://zulko.github.io/moviepy/)

Install dependencies:

```bash
pip install moviepy openai-whisper
```

## Usage

Run the script with the path to your video:

```bash
python generate_subtitles.py path/to/video.mp4
```

The subtitles file (`subtitles.srt`) will be created in the current directory.

The temporary audio file is automatically removed after transcription.
