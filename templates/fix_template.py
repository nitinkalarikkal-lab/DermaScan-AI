
import os
import re
import time

file_path = "doctor_paid_patients.html"
print(f"Current working directory: {os.getcwd()}")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    # Try absolute path just in case
    file_path = r"c:\Users\NITIN\OneDrive\Desktop\derma\Dermascan AI\project\templates\doctor_paid_patients.html"
    if not os.path.exists(file_path):
        print("Still not found.")
        exit(1)

print(f"Targeting file: {file_path}")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Regex to match the split pattern
pattern = r'\{\{ booking\.shedule_id\.start_time\|time:"g:i A" \}\} - \{\{\s+booking\.shedule_id\.end_time\|time:"g:i A" \}\}'
replacement = '{{ booking.shedule_id.start_time|time:"g:i A" }} - {{ booking.shedule_id.end_time|time:"g:i A" }}'

new_content = re.sub(pattern, replacement, content)

if content == new_content:
    print("No matches found for the regex pattern. Dumping snippet around line 570:")
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "booking.shedule_id.end_time" in line:
            print(f"Line {i+1}: {line}")
            print(f"Prev Line {i}: {lines[i-1]}")
else:
    print("Pattern matched. Deleting file...")
    try:
        os.remove(file_path)
        print("File deleted.")
        time.sleep(1) # Wait for file system
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Re-wrote file with corrected content.")
    except Exception as e:
        print(f"Error during delete/write: {e}")
