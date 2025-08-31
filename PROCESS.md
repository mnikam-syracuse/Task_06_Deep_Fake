# Workflow & Process

This document explains **how** I approached the task, the tools I tested, and my final workflow.

## Objectives
- Create an AI-generated interview based on prior analytics narratives.
- Use **free/student** tools.
- Prioritize documentation of **process** over polish.

## Tools Explored
- **Coqui TTS** (offline): Pros—free, reproducible. Cons—voice quality varies.
- **Bark (Sunō)**: Pros—expressive. Cons—setup time.
- **ElevenLabs / PlayHT** (student/free tiers): Pros—higher fidelity. Cons—cloud dependency and quotas.
- **Audacity**: Quick editing and mixing.
- **Python `wave`**: Programmatic assembly & silence insertion.

## Final Workflow (Replicable)
1. Drafted **script** from prior analytics narrative and coach scenario.
2. Split script per speaker (`scripts/split_script.py`) → `host_lines.txt`, `guest_lines.txt`.
3. Synthesized audio:
   - Option A (offline): Coqui TTS (see `scripts/coqui_tts_instructions.md`).
   - Option B (cloud): ElevenLabs free tier.
4. Assembled the dialogue timeline with `scripts/assemble_interview.py` (adds short pauses, crossfades optional).
5. Exported final WAV to `results/audio/interview_mix.wav` and confirmed clarity.
6. Labeled repo and added an **ethics disclosure**.
7. Reported time in Qualtrics and submitted repo link by email.

## Lessons & Risks
- Edge cases: pronunciation of player names; adjust SSML or re-generate.
- Balance authenticity vs. disclosure—clearly label as AI-generated.
- Keep all scripts and prompts for auditing and grading.

*Last updated:* 2025-08-31
