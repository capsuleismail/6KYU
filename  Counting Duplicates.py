def duplicate_count(text):
    text = text.lower()
    res = {t: text.count(t) for t in text}
    return len([v for v in list(res.values()) if v > 1])
