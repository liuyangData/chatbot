import string
import json
import random 

class Chatbot:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a chatbot"
    
    # Main Actions
    def speak(self, words):
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(words)
        engine.runAndWait()

    def hearMic(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        flag = True    
        while flag:
            with sr.Microphone() as source:
                print("Say something!")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                inp = r.recognize_google(audio)
                flag = False
            except sr.UnknownValueError:
                print("Robby could not understand audio")
            except sr.RequestError as e:
                print("Request error; {0}".format(e))
        return inp

    def show(self):
        import pyglet
        animation = pyglet.resource.animation("robby.gif")
        sprite = pyglet.sprite.Sprite(animation)
        win = pyglet.window.Window(width=sprite.width, height=sprite.height, caption = self.name)
        green = 0, 1, 0, 1
        pyglet.gl.glClearColor(*green)
        @win.event
        def on_draw():
            win.clear()
            sprite.draw()
        pyglet.app.run()

class IR_Bot(Chatbot):

    dictionary = {}

    def loadDictJson(self, dictionary):
        with open(dictionary, 'r') as f:
            self.dictionary.update(json.load(f))
    def loadDictionary(self, dictionary):
        self.dictionary= dictionary

    def reply(self, text):
        keys = self.dictionary.keys() 
        text = text.translate(str.maketrans("","",string.punctuation)).lower().split()
        
        for key in keys:
            for word in text:
                if word == key:
                    response = word

        try:
            reply = self.dictionary[response]
        except:
            reply = 'Sorry I could not understand, could you rephrase your sentence? To assist you better, please type one quesiton at a time, or use any of keywords here: 1) promotion 2) vouchers 3) refund 4) parcel'
        return reply

    def saveDictionary(self):
        with open('irDictionary.json', 'w') as f:
            json.dump(self.dictionary, f)
 
    
class ML_Bot(Chatbot):
    import pandas as pd
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer

    bot = ChatBot(name='ML_Bot',  
            logic_adapters=['chatterbot.logic.BestMatch'])

    trainer = ListTrainer(bot)
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train('chatterbot.corpus.english')

    def trainJSON(self, file):
        with open(file, 'r') as f:
            self.trainer.train(json.load(f))
    
    def reply(self, text):
        return self.bot.get_response(text)


class Robby(Chatbot):

    import pandas as pd

    # Linguistic Ability
    with open('language.json', 'r') as f:
        language = json.load(f)

    # Special memory
    memory = ["Hello"]
    echoRepeatMemory = ["Hello"]
    convAIMemory = ["Hello"]

    ## Self Awareness
    with open('profile.json', 'r') as fp:
        profile = json.load(fp)

    
    # Machine Learning

    from sklearn import linear_model
    import pandas as pd

    model = linear_model.LinearRegression()
    dataset = pd.DataFrame()
    vectorDictionary = {}

    def loadDataset(self, data):
        self.dataset = pd.read_csv(data)
    
    def trainModel(self, X, y):
        self.model.fit(X, y)

    def textToVectors(self, text):
        vectors = pd.DataFrame()
        ### transform text to vectors
        return vectors

    def vectorToText(self, vector):
        text = ''

        return text
    
    def reply(self, text):
        X = self.textToVectors(text)
        y = self.model.predict(X)
        return self.vectorsToText(y)



    # Three Stage Process

    corpus = pd.DataFrame() 
    
    def textToTokens(self, text):
        tokens = []

        return tokens

    def loadCorpus(self, data):
        self.corpus = data

    def neuralNetwork(self, tokens):
        output = []

        return output

    def createTransitionalMatrix(self, data):
        matrix = np.matrix()

        return matrix


    def generateSentence(self, tokens):
        sentence = ''

        return sentence
    

        # language related methods
    def mutter(self):
        return f"{self.name} mutters {random.choice(self.language['vocabulary'])}"

    def read(self, vocab):
        self.language['vocabulary'].append(vocab)
    
    def askRandom(self):
        return random.choice(self.language['questions'])


    # Information Retrieval
    def reply(self, statement):

        # Structured Replies
        if self.containsAny(self.adjectives, statement.lower()):
            word = self.identify(self.adjectives, statement.lower())
            return f"What is so {word} about it?"

        # Dictionary Reply

        if self.containsAll(["you", "who"], statement.lower()):
            return self.language['sentenceStructure'][0].replace("_OBJ_", self.profile['identity'])

        if self.containsAll(["your", "purpose"], statement.lower()):
            return self.language['sentenceStructure'][1].replace("_OBJ_", "purpose").replace("_ATTR_", self.profile['purpose'])

        if self.containsAll(['what', 'your'], statement.lower()):
            topic = self.identify(self.profile, statement.lower())
            subtopic = self.identify(self.profile[topic], statement.lower())
            return f"My favourite {subtopic} is {self.profile[topic][subtopic]}"

    # Echo Repeat System
    def loadEchoRepeat(self):
        with open('echoRepeat.json', 'r') as fp:
            self.echoRepeatMemory = json.load(fp)

    def echoRepeat(self, statement):
        if (statement in self.echoRepeatMemory):
            allIndices = [i for i, x in enumerate(self.echoRepeatMemory) if x == statement]
            reply = self.echoRepeatMemory[random.choice(allIndices)+1]
            self.echoRepeatMemory.append(statement)
            self.echoRepeatMemory.append(reply)
        else:
            reply = statement
            self.echoRepeatMemory.append(statement)
        return reply

    # ConvAI
    def loadConvAI(self):
        with open('convAI.json', 'r') as fp:
            self.convAIMemory = json.load(fp)

    def convAI(self, statement):
        reply = None
        if (statement in self.convAIMemory):
            allIndices = [i for i, x in enumerate(self.convAIMemory) if x == statement]
            reply = self.convAIMemory[random.choice(allIndices)+1]
        return reply

    # Learning 

    def loadMemory(self, topic):
        with open(topic+'.json', 'r') as fp:
            self.memory = json.load(fp)


    # Instance Methods
    def containsAll(self, words, statement):
        flag = True
        for word in words:
            if word not in statement:
                flag = False 
        return flag

    def containsAny(self, words, statement):
        flag = False
        for word in words:
            if word in statement:
                flag = True 
        return flag
    def identify(self, ls1, lst2):
        word = ''
        for w in ls1:
            if w in lst2:
                word = w
        return word
 
        

