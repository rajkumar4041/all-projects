from plyer import notification 
import time 

if __name__=='__main__':
    while True:
        notification.notify(
            title="____  Take Rest ____",
            message="Rest is Vital for  better mental health improve mood is a better metabollism"
            # app_icon="path copied here", we can set icon as per convinient 
        timeout=5
        )
        time.sleep(10)#must be greater 

#background run pythonw file name.py