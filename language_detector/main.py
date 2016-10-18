def detect_language(text, languages):
    """Returns the detected language of given text."""
    counts = { lang['name']:0 for lang in languages }
    words = text.split()
    for w in words:
        for lang in languages:
            if w in lang['common_words']:
                counts[lang['name']]+=1
    return max((count, name) for name, count in counts.items())[1]