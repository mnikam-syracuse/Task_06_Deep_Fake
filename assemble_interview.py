"""
Assemble a dialogue WAV by alternating segments from two input WAVs (host and guest)
or by concatenating per-line TTS outputs in `results/audio/host_lines.txt` / `guest_lines.txt`.
This fallback version simply concatenates host.wav + silence + guest.wav for demo purposes.
"""

import wave, struct, math, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIO = ROOT / "results" / "audio"

host_wav = AUDIO / "interview_host.wav"
guest_wav = AUDIO / "interview_guest.wav"
out_wav  = AUDIO / "interview_mix.wav"

def read_pcm16(wav_path):
    with wave.open(str(wav_path), "rb") as w:
        params = w.getparams()
        nframes = w.getnframes()
        frames = w.readframes(nframes)
    return params, frames

def write_pcm16(wav_path, params, frames):
    with wave.open(str(wav_path), "wb") as w:
        w.setparams(params)
        w.writeframes(frames)

def make_silence(duration_s, framerate=22050):
    n = int(duration_s * framerate)
    return b"\x00\x00" * n  # 16-bit mono

if not host_wav.exists() or not guest_wav.exists():
    raise SystemExit("Missing host/guest wav files. Generate TTS first.")

h_params, h_frames = read_pcm16(host_wav)
g_params, g_frames = read_pcm16(guest_wav)

# Basic compatibility check
if h_params[:3] != g_params[:3]:  # nchannels, sampwidth, framerate
    raise SystemExit("Host/Guest WAV format mismatch. Re-export with same sample rate/mono/16-bit.")

sil = make_silence(0.8, h_params.framerate)
combined = h_frames + sil + g_frames

write_pcm16(out_wav, h_params, combined)
print(f"Wrote {out_wav}")
