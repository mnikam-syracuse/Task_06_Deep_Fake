# Task_06_Deep_Fake

This repository contains my deliverables for **Research Task 6: Deep Fake**. It includes:
- AI-generated (or AI-assisted) interview **script**, **prompts**, **workflow documentation**, and **audio assets**.
- A reproducible **workflow** to generate voices with free/student tools and to assemble the final interview.
- Ethical considerations, risk notes, and time-tracking checklist.

> Instructor brief referenced: see course handout and email submission details. (Submission email: `jrstrome@syr.edu`).

## Repository Map
```
Task_06_Deep_Fake/
├─ README.md
├─ assets/
│  ├─ interview_script.md
│  ├─ interview_questions.md
│  └─ consent_and_ethics.md
├─ prompts/
│  ├─ system_prompt.txt
│  ├─ interviewer_prompt.txt
│  └─ guest_prompt.txt
├─ scripts/
│  ├─ assemble_interview.py
│  ├─ split_script.py
│  └─ coqui_tts_instructions.md
├─ workflow/
│  ├─ PROCESS.md
│  └─ TIME_REPORT_CHECKLIST.md
├─ results/
│  ├─ audio/
│  │  ├─ interview_host.wav
│  │  ├─ interview_guest.wav
│  │  └─ interview_mix.wav
│  └─ figures/
│     └─ waveform_preview.png  (optional placeholder)
└─ logs/
   └─ run_log_2025-08-31.json
```

## How to Reproduce (Free/Student-Friendly)
1. **Generate Voices (Option A: Fully Free Offline)**
   - Use **Coqui TTS** (open-source) with pretrained voices to synthesize both the *Interviewer* and the *Guest* lines:
     - Install: `pip install TTS` (if not installed)
     - Example cmd (English model): `tts --text "Hello..." --model_name tts_models/en/ljspeech/tacotron2-DDC --out_path results/audio/interview_host.wav`
     - Repeat for *Guest* with different speaker/voice.
   - Alternative: **Bark** (Sunō) or **VITS** models; see `scripts/coqui_tts_instructions.md`.

2. **Generate Voices (Option B: Student-Tier Cloud)**
   - Use a free-tier TTS (e.g., **ElevenLabs**, **PlayHT**, **Cobalt**, etc.).
   - Export WAV files as `interview_host.wav` and `interview_guest.wav` into `results/audio/`.

3. **Assemble Dialogue**
   - Run `python scripts/assemble_interview.py` to stitch host/guest lines (reads from `assets/interview_script.md`) into a mixed WAV (`interview_mix.wav`).  
   - If you generated two single-speaker full takes instead, you can skip this and provide the two mono tracks separately.

4. **Document the Process**
   - Fill in `workflow/PROCESS.md` with the tools you used, steps taken, any issues, and lessons learned.
   - Complete `workflow/TIME_REPORT_CHECKLIST.md` (dates, hours) and submit the **Qualtrics** form (due Sept 1).

5. **Submit**
   - Make the repo **public** as `Task_06_Deep_Fake`.
   - Email the link to **jrstrome@syr.edu** (per the course instruction).
   - Ensure your OPT time reporting is complete (Qualtrics).

## Notes
- The audio files currently included (`interview_host.wav`, `interview_guest.wav`, `interview_mix.wav`) are **placeholders** created programmatically so that the repo is complete and ready. Replace them with your own generated speech following the workflow.
- This project intentionally focuses on **process quality**: choices, constraints, and clear documentation.

## License
MIT
