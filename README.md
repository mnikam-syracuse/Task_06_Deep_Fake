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


---

## 🔧 Tools & Methods  

### Tools Explored  
- 🗣️ **ElevenLabs** – natural voices, used for final host/guest audio.  
- 🖥️ **Coqui TTS** – open-source offline tool, tested for reproducibility.  
- 🎛️ **Audacity / Online Audio Joiners** – used for merging files when needed.  
- 🐍 **Python Scripts** – automation for splitting and combining text/audio.  

### Workflow Summary  
1. Drafted **script** in `assets/interview_script.md`.  
2. Split into **host_lines.txt** and **guest_lines.txt`**.  
3. Generated audio separately in ElevenLabs (two different voices).  
4. Exported files → `interview_host.wav` + `interview_guest.wav`.  
5. Combined them into **one file** → `interview_mix.wav`.  
6. Documented process, ethics, and time reporting.  

---

## 🔄 Process & Reflection  

### 1. Initial Planning  
- Converted narrative into Q&A dialogue with Host + Guest.  
- Wrote **role-based prompts** for clarity (system, host, guest).  

### 2. Tool Exploration  
- Tried **Coqui TTS** (free but robotic).  
- Settled on **ElevenLabs** (natural, but free tier has limits).  
- Used **Audacity / Python scripts** for audio assembly.  

### 3. Execution  
- Generated Host and Guest audio separately.  
- Merged into one interview file.  
- Added ethics statement & documentation.  

### 4. Challenges  
- ElevenLabs doesn’t support true multi-speaker → solved by generating separately.  
- Some mispronunciations required rewriting lines.  
- Balancing realism with ethics (ensured clear AI-labeling).  

### 5. Lessons Learned  
- **Process > Product** → documenting choices/trade-offs is key.  
- Free tools are enough if combined smartly.  
- Reproducibility matters (scripts + repo structure).  

### 6. Reflection  
This task showed how to move from **static text** to **dynamic audio** while balancing technical, ethical, and workflow challenges. The final interview file is important, but the real value lies in the **structured process and clear documentation**.  

---

## 🔊 Results  
- Final AI-generated interview:  


