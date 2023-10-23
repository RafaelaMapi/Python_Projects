from nltk.stem import PorterStemmer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import syllables
import nltk
import re
from datetime import datetime



class Helper:
    ## A Classe não terá variáveis próprias para que todas as funções possam ser chamadas e utilizadas separadamente.    
    def __init__(self) -> None:
        pass
    
    ## "@staticmethod" é colocado nas funções que não precisam de nenhuma informação específica da classe.
    ## A função count_word conta a quantidade de palavras que existem dentro de um texto. Retorna a quantidade de palavras.
    @staticmethod
    def count_word(content):
        words = content.split()
        return len(words)

    ## A função replace_punct remove os sinais de pontuação e converte o conteúdo para minúsculo. Retorna o texto sem pontuação e convertido para minúsculo
    @staticmethod
    def replace_punct(content):
        punct_list = [',', '.', ';', '?', '!', '\xa0', '\n', '\t', '\\t', '\\n', "'", "(", ")", "“", "”", '\\n', '\\t', '☐', '☒', '\xa0', '●', '“', '”', "/span>"]
        content = ''.join(c for c in content if c not in punct_list)
        return content.lower()

    ## A função dict_content lê um texto, separa suas palavras e retorna um dicionário contendo a quantidade de ocorrencias de cada palavra.         
    @staticmethod        
    def dict_content(content):
        word_occurrences = {}
        word_list = content.lower().split()
        for word in word_list:
            if word in word_occurrences:
                word_occurrences[word] +=1
            else:
                word_occurrences[word]=1
        return word_occurrences
    

    ## A função count_tone_words conta a quantidade de ocorrencias de palavras dentro de uma lista de palavras (para as linstas de palavras positivas e negativas). 
    ## Retorna a quantidade de palavras que existem dentro da lista.
    @staticmethod
    def count_tone_words(word_occurrences, base_list):
        word_tone_count = 0
        for word in base_list:
            if word in word_occurrences.keys():
                word_tone_count += word_occurrences[word]
        return word_tone_count
    
    ## A função stemmed_base_list cria uma lista de palavras stemmed. Para aplicarmos nas listas de palavras positivas e negativas
    @staticmethod
    def stemmed_base_list(base_list):
        stemmer = PorterStemmer()
        base_list_stemmer = {stemmer.stem(w) for w in base_list}
        return base_list_stemmer
    
    ## A função aplica o stemm em um conteúdo. Retorna o texto com as palavras stemmadas.
    @staticmethod
    def stem_content(content):
        stemmer = PorterStemmer()
        content_stemmed = [stemmer.stem(word) for word in content.split()]
        return ' '.join(content_stemmed)
    
    ## A função count_word_with_tokenize conta a quantidade de palavras com o word_tokenize que existem dentro de um texto.
    @staticmethod
    def count_word_with_tokenize(content):
        token_counter=0
        tokens = word_tokenize(content)
        for token in tokens:
            if token not in string.punctuation:
                token_counter +=1
        return(token_counter)    
    
    ## A função count_sentences conta a quantidade de sentenças que existem dentro de um texto. Retorna a quantidade de sentenças. 
    @staticmethod
    def count_sentences(content):
        sentences = sent_tokenize(content)
        return(len(sentences))
    
    ## A função complex_words conta a quantidade de palavras complexas que existem dentro de um texto.
    @staticmethod
    def complex_words(content):
        complex_valido=0
        tokens = word_tokenize(content)
        for token in tokens:
            if token not in string.punctuation and syllables.estimate(token) >2:
                complex_valido +=1
        return(complex_valido)
    
    ## A função calc_fog_index calcula o Fog Index, sua fórumula é: fogIndex = 0.4 * (avgSentenceLength + rateComplexWords)
    @staticmethod
    def calc_fog_index(average_sentence_length, rate_complex_words):
        # Calculate the Fog Index by adding the average sentence length and the rate of complex words
        fog_index = 0.4 * (average_sentence_length + rate_complex_words)
        return fog_index
    
    ## Function to extract text between tags, with content, start tag and end tag
    @staticmethod
    def extract_text_between_tags(text, start_tag, end_tag):
    ## Regex expression that receives the initial tag, checks the content that comes after it, until the end tag 
    ## f"xxx{var}" means that we are passing a string, and a varible together.
    ## re.escape means that we are passing a string that contains special characters
        pattern = f"{re.escape(start_tag)}(.*?){re.escape(end_tag)}"
    ## matches finds the pattern, with the "re.DOTALL" and re.IGNORECASE option.
        matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
        return matches
    ## Function to get da date from a string like this: "Jan DD, YYYY"
    @staticmethod
    def get_date(string_date):
        try:
            ## This is the format of the date to convert %b means the mouth abbreviation, %d means the day of the month and %Y the year with 4 digits
            date_format = '%b %d, %Y'
            # Parse the string into a datetime object using the specified format
            date_object = datetime.strptime(string_date, date_format)
            # Convert the datetime object to a date object
            date = date_object.date()
        except :
            date = string_date
        return date