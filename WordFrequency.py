# src/hello.py
import re
text = "Data, data! AI transforms data—clean data wins."
tokens = re.findall(r"[a-zA-Z]+", text.lower())
freq = {}
for t in tokens:
    freq[t] = freq.get(t, 0) + 1
print("Tokens:", tokens)
print("Freq:", dict(sorted(freq.items(), key=lambda x:(-x[1], x[0]))))
# Expected most frequent: 'data': 3
