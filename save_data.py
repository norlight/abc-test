import json
from datasets import load_dataset

# Save dataset to output.jsonl
raw_data = load_dataset("sander-wood/irishman")["train"]
with open('output.jsonl', 'w') as file:
    cnt = 0
    for item in raw_data:
        file.write(json.dumps(item) + '\n')
        cnt += 1
        if cnt > 10:
            break