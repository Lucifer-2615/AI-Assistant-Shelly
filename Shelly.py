from Brain.AIBrain import ReplyBrain
# from Brain.QnA import QuestionsAnswer
from Body.Listen import Listen
print(">> Starting The Shelly : Wait for some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
import datetime
print(">> Starting The Shelly : Wait for some Seconds More.")
    

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak('Good Morning Lucifer')
    elif hour>=12 and hour<=18:
        Speak('Good Afternoon Lucifer')
    else:
        Speak('Good Evening Lucifer')

def MainExecution():
    wishme()
    Speak("I am Shelly, Ready to Assist you.")
    while True:
        
                
        Data = Listen() 
        Data = str(Data)
        if len(Data)<3:
            pass 
        
        # elif " What is " in Data or "Where is" in Data or "question" in Data or "answer" in Data:
        #     Reply = QuestionsAnswer(Data)
        elif "you need a break" in Data:
            break
        else: 
            Reply = ReplyBrain(Data)
            Speak(Reply)
        
def ClapDetect():
    query = Tester()
    if "True-mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
    else:
        pass

ClapDetect()
MainExecution()