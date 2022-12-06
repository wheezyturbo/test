#to install      pip install chatterbot==1.0.4

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>CRCE BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Greetings Ask me about some interesting stuff!",
            'maximum_similarity_threshold': 0.90
        },'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chatbot)


trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"help",
"Hello from the college bot<br>you might wanna try one of these:<br><button class = 'btnip'>syllabus</button><br><button class='btnip'>prev year questions</button><br><button class = 'btnip'>fee structure</button>",
"3",
"Please Enter your batch",
"cs",
"4000",
"astrophysics",
"2000",
"lol",
"idk",
"syllabus",
"<a href='https://www.google.com' target='_blank'>click here for syllabus</a>",
"who is adhnan",
"adhnan is gay",
]

trainer.train(conversation)
