
import os
import re

file_path = "doctor_paid_patients.html"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match the line we THINK is there (the fixed one)
pattern_fixed = r'\{\{ booking\.shedule_id\.start_time\|time:"g:i A" \}\} - \{\{ booking\.shedule_id\.end_time\|time:"g:i A" \}\}'

# Also match the broken one just in case
pattern_broken = r'\{\{ booking\.shedule_id\.start_time\|time:"g:i A" \}\} - \{\{\s+booking\.shedule_id\.end_time\|time:"g:i A" \}\}'

# Simplified replacement
replacement = '{{ booking.shedule_id.start_time }} - {{ booking.shedule_id.end_time }}'

new_content = re.sub(pattern_fixed, replacement, content)
if new_content == content:
    # Try replacing the broken pattern
    new_content = re.sub(pattern_broken, replacement, content)

if content == new_content:
    print("Could not find the target line (fixed or broken). Dumping file section:")
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "booking.shedule_id.end_time" in line:
            print(f"Line {i+1}: {repr(line)}")
else:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Simplified the time slot display (removed filters).")
