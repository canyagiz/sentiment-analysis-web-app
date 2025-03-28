import re

def clean_text(text):
    text = re.sub(r"http\S+|www.\S+","", text)

    text = re.sub(r"@\w+|#\w+", "", text)

    text = re.sub(r"[^\w\s]", "", text)
    
    text = text.lower()
    text = text.strip()

    return text