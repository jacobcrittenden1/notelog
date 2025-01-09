import os
import subprocess
from datetime import datetime

def combine_text_files(folder_path, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in sorted(os.listdir(folder_path), reverse=True):
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    title = f"Title: {file_name}"
                    timestamp = f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    divider = '-' * 40

                    outfile.write(f"{title}\n{timestamp}\n{divider}\n{content}\n\n")

folder_path = 'C:\\Users\\jacob\\OneDrive\\Desktop\\MyNotes'
output_file = 'combined_log.txt'
combine_text_files(folder_path, output_file)

subprocess.Popen(["notepad.exe", "combined_log.txt"])
