import hazm
import re

class Preprocessing:
    def __init__(self):
        pass

    def normalize(self, text):
        normalizer = hazm.Normalizer()
        return normalizer.normalize(text)

    def remove_emojis(self, text):
        pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           "]+", flags = re.UNICODE)
        
        return pattern.sub('', text)
    
    def remove_english_words(self, text):
        pass

    def remove_hashtags(self, text):
        pass

    def remove_special_character(self, text, char):
        pass

    def remove_mentions(self, text):
        pass

    def sentence_tokenize(self, text):
        tokenizer = hazm.SentenceTokenizer()
        return tokenizer.tokenize(text)

    def word_tokenize(self, sentence):
        tokenizer = hazm.WordTokenizer()
        return tokenizer.tokenize(sentence)

    def remove_stop_words(self, words):
        pass

    def remove_char_duplicates(self, word):
        pass