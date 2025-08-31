"""
Split the `assets/interview_script.md` into two text files for Host (H) and Guest (G).
"""

from pathlib import Path
import re

script_path = Path(__file__).resolve().parents[1] / "assets" / "interview_script.md"
host_out = Path(__file__).resolve().parents[1] / "results" / "audio" / "host_lines.txt"
guest_out = Path(__file__).resolve().parents[1] / "results" / "audio" / "guest_lines.txt"

host_lines, guest_lines = [], []

for line in script_path.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\*\*(H|G)\*\*:\s*(.*)", line.strip())
    if m:
        who, text = m.groups()
        if who == "H":
            host_lines.append(text)
        else:
            guest_lines.append(text)

host_out.write_text("\n".join(host_lines), encoding="utf-8")
guest_out.write_text("\n".join(guest_lines), encoding="utf-8")
print(f"Wrote {len(host_lines)} host lines → {host_out}")
print(f"Wrote {len(guest_lines)} guest lines → {guest_out}")
