import re

def text_cleaner(txt):
    # from text remove HTML tags
    txt = re.sub(r'<[^>]*?>', '', txt)

    # from text remove special characters
    txt = re.sub(r'[^a-zA-Z0-9 ]', '', txt)

    # from text remove URLs
    txt = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', txt)

    # from text replace multiple spaces with a single space
    txt = re.sub(r'\s{2,}', ' ', txt)

    # trim leading and trailing whitespace
    txt = txt.strip()

    # from text remove extra whitespace
    txt = ' '.join(txt.split())
    
    return txt