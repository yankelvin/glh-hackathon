from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def gerar_keys():
    ask_keys = []
    msg = ["Eu não sei exatamente o que devo fazer.", "Sim. Me sinto",
           "Meu marido é alcoólatra e ontem ele me agrediu, chamei a polícia e disseram que não era motivo de prestar B.O, o que eu faço?"]

    for txt in msg:
        palavras = word_tokenize(txt.lower())
        stopw = set(stopwords.words('portuguese') + list(punctuation))
        palavras_sem_stopwords = [
            palavra for palavra in palavras if palavra not in stopw]
        ask_keys.append(palavras_sem_stopwords)
    return ask_keys
