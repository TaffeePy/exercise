from tkinter import *
window = Tk()

window.title("Text Editor")
window.geometry("750x850")

#*frame 1 & Label 1
frame1 = Frame(window, bg="deep sky blue", borderwidth=3,relief=GROOVE)
frame1.pack(side=TOP, fill=X)
#Label 1
head_label=Label(frame1,text='File     Edit      View    Search    Documents    Help\n',fg='black',bg="deep sky blue")
head_label.pack(anchor='nw',side= LEFT,fill=X,)

#2frame2 & Label2
frame2=Frame(window,borderwidth=3,bg="sky blue",relief=GROOVE)
frame2.pack(side=TOP,fill=X)
#Label 2
Second_label=Label(frame2,text='Open    Save    Undo    Cut     Copy',fg='black',bg='sky blue')
Second_label.pack(anchor='w',side= LEFT,fill=X)

#3.Frame 3 & Label 3
frame_below=Frame(window,bg='sky blue', borderwidth=3,relief=GROOVE).pack(side=BOTTOM,fill=X,anchor='s')
#Label 3
bellow_label=Label(frame_below,text="text type:Python3 ^            line:1 col:1         INS",bg='sky blue',fg='black')
bellow_label.pack(side=BOTTOM,anchor='e',fill=X)
#4.frame 4 & Label 4 
frame_left_y=Frame(bg='LightCyan2', borderwidth=6,relief=GROOVE).pack(side=LEFT,anchor='n',fill=Y)
#label 4
label_left_y=Label(frame_left_y,text="Unsaved Document1",bg='LightCyan2',fg='black')
label_left_y.pack(fill=Y,side=LEFT,anchor='n')
window.mainloop()