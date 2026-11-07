with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in style.css: {len(lines)}")

import re
media_blocks = []
for i, line in enumerate(lines):
    if '@media' in line:
        media_blocks.append((i+1, line.strip()))

for num, line in media_blocks:
    print(f"Line {num}: {line}")

