import os
os.chdir('C:\\Users\\cheta\\rajasthan-helper')
if not os.path.exists('.github'):
    os.makedirs('.github')
import shutil
shutil.move('copilot-instructions.md', '.github\\copilot-instructions.md')
with open('.github\\move_completed.txt', 'w') as f:
    f.write('File move completed successfully\n')
    f.write(f'File exists: {os.path.exists(".github/copilot-instructions.md")}\n')
