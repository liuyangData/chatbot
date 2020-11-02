from chatbot import Chatbot
import json

if __name__ == "__main__":
    robby = Chatbot("Robby")
    robby.loadEchoRepeat()
    robby.loadConvAI()

    # userResponse = robby.hearMic()
    userResponse = input()
    while 'goodbye' not in userResponse:
        
        reply = robby.reply(userResponse)
        if reply == None:
            reply = robby.convAI(userResponse)
            if reply == None:
                reply = robby.echoRepeat(userResponse)
        robby.speak(reply)
        # userResponse = robby.hearMic()
        print(reply)
        userResponse = input()
    print(robby.name + " has learnt the following from EchoRepeat:", robby.echoRepeatMemory)
    
    print("Save? [y/n]") 
    save = input()
    if save == "y":
        with open('echoRepeat.json', 'w') as fp:
            json.dump(robby.echoRepeatMemory, fp)



### Information Retrieval System

from chatbot import IR_Bot
ir = IR_Bot('ir')

ir_dictionary = {'hi': "Hello.",
                 'hello': 'Hey there.', 
                 'parcel': 'To check you parcel status, go to My Purchase on the top right corner on your screen. For more information, please download this user manual.',
                 'promotion': 'Limited sales will be held on the first Sunday of every month. To receive the latest updates, please subcribe to our mailer list',
                 'vouchers': 'To check you current voucher, go the My Vouchers on the top right corner on your screen. To find out more ways to earn vouchers, check out this webpage: www.earnvouchers.com',
                 'refund': "To request for a refund, please follow the following steps. 1) Go to My Purchase... 2) Submit the reasons for the refund with supporting picture/screenshots. 3) We will respond in 3-5 working days",
                 'help': "To assist you better, please type one quesiton at a time, or use any of keywords here: 1) promotion 2) vouchers 3) refund 4) parcel"} 

ir.loadDictionary(ir_dictionary)

userResponse = input()
while 'quit' not in userResponse:

    print(ir.reply(userResponse))
    userResponse = input()


# Machine Learning Bot
from chatbot import ML_Bot

ml = ML_Bot("ML")

ml.trainJSON('convAI.json')

ml.reply("HI")

userResponse = input()
while 'quit' not in userResponse:

    print(ml.reply(userResponse))
    userResponse = input()

