
import os
import re

def count_for_in_file(filepath):
    count = 0
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            count += len(re.findall(r'\bfor\b', line))
    return count

def main():
    total_count = 0
    # Scan all .py files in the repo
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                total_count += count_for_in_file(filepath)
    print(f"Total number of times 'for' is used in all .py files: {total_count}")

if __name__ == "__main__":
    main()
