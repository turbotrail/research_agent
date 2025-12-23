def clean_text(text, max_chars=2500):
    lines = [l.strip() for l in text.splitlines()]
    cleaned = "\n".join(l for l in lines if len(l) > 40)
    return cleaned[:max_chars]