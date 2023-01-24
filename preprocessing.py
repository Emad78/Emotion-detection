import hazm
import re
import emoji
PUNCTUATIONS = ['.', '؟', '!', '،', ':', '؛', '(', ')', '*', '/']


class Preprocessing:
    def __init__(self):
        
        self.stop_words = []
        fin=open('resources/stopword.txt',encoding='utf8')
        for word in fin.readlines():
            self.stop_words.append(word.replace('\n', '').lower().replace('\ufeff', '').lower().replace('\ufeff', '').upper().replace('ك' , 'ک').replace(" " ,""))

    def normalize(self, text):
        normalizer = hazm.Normalizer()
        return normalizer.normalize(text)

    def remove_emojis(self, text):
        return emoji.replace_emoji(text)
    
    def convert_emoji_to_text(self, text):
        return emoji.demojize(text)
    
    def remove_english_words(self, text):
        return re.sub(r'[A-Za-z]+', '' , text)

    def remove_hashtags(self, text):
        text = re.sub(r"#[A-Za-z0-9_]+","", text)
        text = re.sub(r"#[\u06F0-\u06F9\u0660-\u0669\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC\u200c_]+","", text)
        return text
    
    def remove_specific_character(self, text, char):
        return text.replace(char, '')

    def remove_mentions(self, text):
        return re.sub(r"@[A-Za-z0-9_]+","", text)

    def sentence_tokenize(self, text):
        pattern = re.compile(r'[.!؟؛?\n][ ]*')
        return pattern.split(text)

    def word_tokenize(self, sentence):
        return re.findall(r"[\w']+", sentence)

    def remove_stop_words(self, words):
        return list(filter(lambda x: x not in self.stop_words and len(x) > 1, words))
    
    def remove_stop_words_from_sentences(self, sentences):
        sentences = list(map(self.remove_stop_words, sentences))
        sentences = list(filter(lambda x: len(x)>0, sentences))
        return sentences

    def remove_punctuations_from_sentences(self, sentences):
        sentences = list(map(self.remove_punctuations, sentences))
        sentences = list(filter(lambda x: len(x)>0, sentences))
        return sentences

                
    def remove_character_duplications(self, word:str):
        if word.isnumeric():
            return word
        return re.sub(r'(.)\1\1+', r'\1', word)
    
    def remove_character_duplications_from_sentences(self, sentences):
        new_sentences = []
        for sentence in sentences:
            new_sentences.append(list(map(self.remove_character_duplications, sentence)))
        
        new_sentences = list(filter(lambda x: len(x)>0, new_sentences))
        return new_sentences

    
    def remove_url(self, text):
        text =  re.sub(r'http\S+', '', text)
        text = re.sub(r'www\S+', '', text)
        return text
    
    def remove_punctuations(self, words):
        punctuations = PUNCTUATIONS
        return list(filter(lambda x: x not in punctuations, words))
    
    def remove_number(self, text):
        return re.sub("\d+", " ", text)
    
    def find_sentences_words(self, text):
        sentences = self.sentence_tokenize(text)
        sentences_words = list(map(self.word_tokenize, sentences)) 
        sentences_words = list(filter(lambda x: len(x)>0, sentences_words))       
        return sentences_words

    def lemmatizer(self, word):
        lemmatizer = hazm.Lemmatizer()
        return lemmatizer.lemmatize(word)

    def lemmatization_sentences(self, sentences):
        new_sentences = []
        for sentence in sentences:
            new_sentences.append(list(map(self.lemmatizer, sentence)))
        
        new_sentences = list(filter(lambda x: len(x)>0, new_sentences))
        return new_sentences




