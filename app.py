from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
 
app = Flask(__name__)

english_bot = ChatBot("Anabsys")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "hii babe",
    "I have a boyfriend get lost",
    "hatt chal bye",
    "Haan chal pehli fursat me nikal"
]

trainer = ListTrainer(english_bot)
trainer.train(conversation)
 
#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))
 
 
if __name__ == "__main__":
    app.run()