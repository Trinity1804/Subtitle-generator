import sys
import os
import whisper
import moviepy.editor as mp

def seconds_to_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

def generate_srt(segments, srt_path):
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            start = seconds_to_timestamp(seg["start"])
            end = seconds_to_timestamp(seg["end"])
            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{seg['text'].strip()}\n\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_subtitles.py path/to/video.mp4")
        sys.exit(1)

    video_path = sys.argv[1]
    if not os.path.isfile(video_path):
        print("Provided video file does not exist.")
        sys.exit(1)

    audio_temp = "temp_audio.wav"

    print("Extracting audio from video...")
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_temp, fps=16000)

    print("Loading whisper model...")
    model = whisper.load_model("base")
    print("Transcribing audio...")
    result = model.transcribe(audio_temp)

    srt_path = "subtitles.srt"
    print("Generating SRT file...")
    generate_srt(result["segments"], srt_path)
    print(f"SRT subtitles file generated at {srt_path}")

    os.remove(audio_temp)

if __name__ == "__main__":
    main()
