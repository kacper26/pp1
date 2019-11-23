import re

tekst = "To be, or not to be, that is the question"
re_path = r"[aeiouy]"

print(len(re.findall(re_path, tekst)))