# Coqui TTS Quickstart (Offline, Free)

```bash
pip install TTS

# Host line example
tts --text "Welcome back! Today we're unpacking last season..."     --model_name tts_models/en/ljspeech/tacotron2-DDC     --out_path results/audio/interview_host.wav

# Guest line example (different voice or speed)
tts --text "Three standouts: transition defense tightened..."     --model_name tts_models/en/ljspeech/glow-tts     --out_path results/audio/interview_guest.wav
```

Tips:
- Use different models or speed (`--speed 0.9`) to separate voices.
- If using multi-speaker models, pick different `--speaker_idx`.
