from tkinter import *
import speedtest

def speed_check():
    st=speedtest.speedtest()
    st.get_servers()
    down=str(round(st.download()/(10**6),3))+' Mbps'
    up=str(round(st.upload()/(10**6),3))+' Mbps'
    lab_down.config(text=down)
    lab_up.config(text=up)
    
    
st=Tk()
st.title=("Speedo Meter")
st.geometry("500x500")
st.config(bg="grey")

lab=Label(st,text="internet speed test ",font=("Time New Roman",30,"bold"),bg="grey",fg="blue")
lab.place(x=60,y=40,height=50,width=380)

lab_down=Label(st,text=" Downloading Speed  ",font=("Time New Roman",25,"bold"),fg="black")
lab_down.place(x=60,y=130,height=50,width=380)

lab=Label(st,text="00",font=("Time New Roman",25,"bold"),fg="black")
lab.place(x=60,y=200,height=50,width=380)

lab_up=Label(st,text="uploading Speed ",font=("Time New Roman",25,"bold"),fg="black")
lab_up.place(x=60,y=290,height=50,width=380)

lab=Label(st,text="00",font=("Time New Roman",25,"bold"),fg="black")
lab.place(x=60,y=360,height=50,width=380)

speed_button=Button(st,text="Check Speed",font=("Time New Roman,",25,"bold"),bg="black",fg="white",relief=RAISED,command=speed_check)
speed_button.place(x=60,y=460,height=50,width=380)

st.mainloop()
