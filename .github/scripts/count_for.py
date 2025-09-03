import subprocess
import re

def get_diff():
    # Get the diff for the last commit (for push events, this is the pushed commit)
    result = subprocess.run(['git', 'diff', 'HEAD~1', 'HEAD'], stdout=subprocess.PIPE, text=True)
    return result.stdout

def count_for_in_diff(diff):
    count = 0
    for line in diff.splitlines():
        if line.startswith('+') and not line.startswith('+++'):
            # Count 'for' as a word (not part of another word)
            count += len(re.findall(r'\\bfor\\b', line))
    return count

def main():
    diff = get_diff()
    count = count_for_in_diff(diff)
    print(f"Number of times 'for' is used in added lines: {count}")

if __name__ == "__main__":
    main()
