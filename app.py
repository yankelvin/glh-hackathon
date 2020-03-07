import logging
from string import punctuation
from time import sleep
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from keys import gerar_keys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

ask_keys = gerar_keys()


def start():
    message = "Olá, meu nome é Abu. Aqui é um ambiente seguro, sinta-se à vontade para conversar. Em que posso ajudar?\n"
    return f"Bot: {message}"


def echo(msg):
    palavras = word_tokenize(msg.lower())
    stopw = set(stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [
        palavra for palavra in palavras if palavra not in stopw]

    cont_atual = cont_ant = index = 0

    ask_keys = gerar_keys()

    for ch, value in enumerate(ask_keys):
        cont_atual = 0
        for key in palavras_sem_stopwords:
            if key in ask_keys[ch]:
                cont_atual += 1
            if cont_atual > cont_ant:
                index = ch
        if cont_atual > cont_ant:
            cont_ant = cont_atual

    if cont_ant <= 1:
        index = -1

    message = ""

    if index == 0:
        message = "Você se sente à vontade para me contar o que aconteceu?"
    elif index == 1:
        message = "Não se preocupe, lembre-se: você está segura aqui."
    elif index == 2:
        message = "Primeiramente, mantenha a calma. Nossos advogados irão receber o seu relato e te orientar da melhor forma possível. "
        message += "O tempo estimado para atendimento é de 2h e 34min. Você pode ativar as notificações se quiser."
    elif index == -1:
        message = "Desculpe, não entendi!"

    return f"Bot: {message}"


print(start())

while True:
    msg = input("You: ")

    if msg == 'stop':
        break

    print("\n" + echo(msg) + "\n")
