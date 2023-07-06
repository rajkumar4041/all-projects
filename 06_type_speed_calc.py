from time import *
import random as r

def mistakes(paraText,userText):
    error=0
    for i in range (len(paraText)):
        try:
            if paraText[i]==userText[i]:
                continue
            else:
                error=error+1
            
        except:
            error=error+1 
    print("error : ",error)

def speed_time(time_s,time_e,UserInput):
    res=time_e-time_s
    round_of=round(res,2)
    speed=len(UserInput)/round_of
    print("speed :",round(speed),"words per sec")
#string to print from user 
# def startapp():
    
text=["A Checking the network cables, modem,"," and router Reconnecting to Wi-Fi","Remembers what user said earlier"," in the conversation Allows ","user to provide follow-up corrections Trained to decline inappropriate"," requestsLimitationsMay occasionally ","generate incorrect informationMay ","occasionally produce harmful","instructions or biased contentLimited ","knowledge of world and events after 2021"]
text1=r.choice(text)

print("* "*10,"  |  "," typing Speed","  |  "," *"*10)
print(text1,"",end="\n")
time_1=time()
textinput=input("Enter .... \n\n")
time_2=time()


    #calling error helpiing function 
mistakes(text1,textinput)
speed=speed_time(time_1,time_2,textinput)
# print("error : ",error)
# print("speed : ",speed)

