import os

file_path = 'templates/user_profile_edit.html'
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix gender comparisons
    content = content.replace('user.gender=="Male"', 'user.gender == "Male"')
    content = content.replace('user.gender=="Female"', 'user.gender == "Female"')
    content = content.replace('user.gender=="Other"', 'user.gender == "Other"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fix applied successfully.")
else:
    print(f"File not found: {file_path}")
