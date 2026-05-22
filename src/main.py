import re
import json

with open("input/raw-text.txt", "r") as file:
    text = file.read()

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@(alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)',
    text
)

urls = re.findall(r'https?://[^\s]+', text)

phones = re.findall(
    r'\+\d{3}\s\d{3}\s\d{3}\s\d{3}|\(\d{3}\)\s\d{3}-\d{4}',
    text
)

cards = re.findall(
    r'(?:\d{4}[- ]?){3}\d{4}',
    text
)

hidden_cards = []

for card in cards:
    clean = re.sub(r'[- ]', '', card)
    hidden_cards.append("************" + clean[-4:])

results = {
    "emails": emails,
    "urls": urls,
    "phones": phones,
    "credit_cards": hidden_cards
}

with open("output/sample-output.json", "w") as out:
    json.dump(results, out, indent=4)

print(results)