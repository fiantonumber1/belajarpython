import speech_recognition as sr
from pydub import AudioSegment
import os

# Lokasi file audio dan direktori sementara
audio_file = "E:\\voicedetector\\nata.wav"
output_file = "C:\\Users\\fiansyah\\Downloads\\transkripsi.txt"
temp_dir = "E:\\voicedetector\\temp\\"

# Pastikan direktori sementara ada
os.makedirs(temp_dir, exist_ok=True)

# Potong file audio menjadi segmen-segmen kecil
def split_audio(file_path, segment_length_ms):
    audio = AudioSegment.from_wav(file_path)
    segments = []
    for i, start_time in enumerate(range(0, len(audio), segment_length_ms)):
        end_time = min(start_time + segment_length_ms, len(audio))
        segment = audio[start_time:end_time]
        segment_file = os.path.join(temp_dir, f"segment_{i}.wav")
        segment.export(segment_file, format="wav")
        segments.append(segment_file)
    return segments

# Transkripsi audio
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data, language="id-ID")
        except sr.UnknownValueError:
            return "[Audio tidak dapat dipahami]"
        except sr.RequestError as e:
            return f"[Terjadi kesalahan: {e}]"

# Main process
def main():
    segment_length_ms = 60000  # Durasi potongan audio dalam milidetik (misalnya 60 detik)
    segments = split_audio(audio_file, segment_length_ms)

    with open(output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            transcription = transcribe_audio(segment)
            f.write(transcription + "\n")

    # Hapus file sementara
    for segment in segments:
        os.remove(segment)

    print(f"Hasil transkripsi disimpan di {output_file}")

if __name__ == "__main__":
    main()
