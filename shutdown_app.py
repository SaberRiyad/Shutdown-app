from tkinter import*
import os#operating system
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")
st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")
r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="Plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)
rt_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",comman=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)
lg_button=Button(st,text="LOg Out",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="Plus",command=log_out)
lg_button.place(x=150,y=270,height=50,width=200)
st_button=Button(st,text="Shut Down",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="Plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)
st.mainloop()#to create graphic