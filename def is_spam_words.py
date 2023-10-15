import re

def is_spam_words(text, spam_words, space_around=False):
    # Переводимо весь текст до нижнього регістру для регістру-незалежного пошуку
    lower_text = text.lower()

    for spam_word in spam_words:
        lower_spam_word = spam_word.lower()

        # Створюємо регулярний вираз для пошуку забороненого слова з обмеженнями
        if space_around:
            pattern = r"(^|\s|\.)" + re.escape(lower_spam_word) + r"(\s|\.|$)"
        else:
            pattern = re.escape(lower_spam_word)

        if re.search(pattern, lower_text):
            return True

    return False


    
print(is_spam_words('Молох ти ужасний',['лох'],space_around=True))