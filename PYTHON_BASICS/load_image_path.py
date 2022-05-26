from mmap import PROT_READ
from pathlib import Path

cwd = Path(__file__).resolve().parent
print()
print()
print(cwd)
print()
final_path = str(cwd) + '/linux_penguin.jpeg'
print(final_path)
print()