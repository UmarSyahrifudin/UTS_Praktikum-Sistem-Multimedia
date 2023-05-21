from pydub import AudioSegment
import pydub.effects as effects
import pydub.silence as silence
from pydub.playback import play

# Load the audio file
audio = AudioSegment.from_file("pop.wav")

# Apply audio processing effects
processed_audio = audio.fade_in(1000)  # Fade in selama 1 detik
processed_audio = processed_audio.fade_out(1000)  # Fade out selama 1 detik
processed_audio = effects.normalize(processed_audio)  # Normalisasi audio
processed_audio = effects.pan(processed_audio, 0.8)  # Pindahkan audio ke kanan (channel kanan)
processed_audio = effects.speedup(processed_audio, playback_speed=1.5)  # Mempercepat pemutaran audio


# Apply audio compression
compressed_audio = processed_audio.compress_dynamic_range(threshold=-20.0, attack=5.0, release=50.0, ratio=4.0)
compressed_audio = compressed_audio.low_pass_filter(1000)  # Apply a low-pass filter to the audio

# Trim silence from the audio
chunks = silence.split_on_silence(compressed_audio, min_silence_len=500, silence_thresh=-30)
trimmed_audio = sum(chunks)

# Export the processed and compressed audio
trimmed_audio.export("output.wav", format="wav")
