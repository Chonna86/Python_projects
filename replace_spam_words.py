import re
def replace_spam_words(text, *spam_words):
    for spam_word in spam_words:
        found = re.sub(spam_word, text, 0, re.IGNORECASE)
        for found_spam_word in found:
            text = re.sub(found_spam_word,'*'*len(spam_word), text)
    return text
    