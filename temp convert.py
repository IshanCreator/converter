from tkinter import *
import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.geometry("500x500")
root.title("Ishan APK")


def mtoh():
    f2=Frame(bg="deep sky blue")
    f2.place(x=0, width=500, height=500)
    l1 = Label(f2, text="Minute's Into Hour's", font=("Comic Sans MS", 21), bg="deep sky blue", fg="white")
    l1.place(x=110, y=20)

    Button(text="Back", fg="white", bg="red", font=("Comic Sans MS", 20), cursor="hand2", command=back).place(x=0,y=450)

    # -------------------------- Minute _____________________________

    def entry_focus_in(event):
        if min.get() == "Enter Minute's":
            min.delete(0, "end")
            min.config(bg="white")

    def entry_focus_out(event):
        if min.get() == "":
            min.insert(0, "Enter Minute's")
            min.config(bg="white")

    min = Entry(f2, width=20, fg="black", font=("Comic Sans MS", 20))
    min.place(x=100, y=110)

    min.insert(0, "Enter Minute's")
    min.bind("<FocusIn>", entry_focus_in)
    min.bind("<FocusOut>", entry_focus_out)



    # ________________________ Hours _______________________

    def entry_focus_in(event):
        if hours.get() == "Enter Hour's":
            hours.delete(0, "end")
            hours.config(bg="white")

    def entry_focus_out(event):
        if hours.get() == "":
            hours.insert(0, "Enter Hour's")
            hours.config(bg="white")

    hours = Entry(f2, width=20, fg="black", font=("Comic Sans MS", 20))
    hours.place(x=100, y=230)

    hours.insert(0, "Enter Hour's")
    hours.bind("<FocusIn>", entry_focus_in)
    hours.bind("<FocusOut>", entry_focus_out)

    # ------------------------ change button def ------------------------------------------

    def mtoh_change():
        minute=min.get()
        hour=hours.get()


        if int(minute)>=60:
            datachage=int(minute)/60
            hours.delete(0,"end")
            hours.insert(0,f"{str(datachage)} Hour's")
        else:
            messagebox.showinfo("Ooop","Please Enter 60 + Minute's")



    # ----------------------------------------- change button _____________________-

    b1 = Button(f2, text="Change", fg="white", bg="green", font=("Comic Sans MS", 30), cursor="hand2",command=mtoh_change)
    b1.place(x=150, y=350)

    #  --------------------------------------- Switch ---------------------------------
    def switch2():
        sf2=Frame(bg="deep sky blue")
        sf2.place(x=0, width=500, height=500)

        l1 = Label(sf2, text="Hour's Into Minute's", font=("Comic Sans MS", 21), bg="deep sky blue", fg="white")
        l1.place(x=110, y=20)

        # ________________________ Hours _______________________

        def entry_focus_in(event):
            if hours.get() == "Enter Hours":
                hours.delete(0, "end")
                hours.config(bg="white")

        def entry_focus_out(event):
            if hours.get() == "":
                hours.insert(0, "Enter Hours")
                hours.config(bg="white")

        hours = Entry(sf2, width=20, fg="black", font=("Comic Sans MS", 20))
        hours.place(x=100, y=110)

        hours.insert(0, "Enter Hour's")
        hours.bind("<FocusIn>", entry_focus_in)
        hours.bind("<FocusOut>", entry_focus_out)

        # -------------------------- Minute _____________________________

        def entry_focus_in(event):
            if min.get() == "Enter Minute's":
                min.delete(0, "end")
                min.config(bg="white")

        def entry_focus_out(event):
            if min.get() == "":
                min.insert(0, "Enter Minute's")
                min.config(bg="white")

        min = Entry(sf2, width=20, fg="black", font=("Comic Sans MS", 20))
        min.place(x=100, y=230)

        min.insert(0, "Enter Minute's")
        min.bind("<FocusIn>", entry_focus_in)
        min.bind("<FocusOut>", entry_focus_out)

        # ------------------------ change button def ------------------------------------------

        def mtoh_change():
            minute = min.get()
            hour = hours.get()

            if int(hour) >= 1:
                datachage = int(hour) * 60
                min.delete(0, "end")
                min.insert(0, f"{str(datachage)} Minute's")
            else:
                messagebox.showinfo("Ooop", " Zero Number Not Valid")

        # ----------------------------------------- change button _____________________-

        b1 = Button(f2, text="Change", fg="white", bg="green", font=("Comic Sans MS", 30), cursor="hand2",
                    command=mtoh_change)
        b1.place(x=150, y=350)

    # ---------------------------- switch butto -----------------------------
        Button(sf2, text="Back", fg="white", bg="red", font=("Comic Sans MS", 20), cursor="hand2", command=back).place(
            x=0, y=450)

    # --------------------------- switch back ------------------
        change2 = Button(sf2, text="<->", bg="deep sky blue", fg="Black", font=("Comic Sans MS", 18), cursor="hand2",
                         command=backswitch2)
        change2.place(x=220, y=162)

        #   ------------------------------------- sChange button ------------
        b1 = Button(sf2, text="Change", fg="white", bg="green", font=("Comic Sans MS", 30), cursor="hand2",
                    command=mtoh_change)
        b1.place(x=150, y=350)

    change2 = Button(f2, text="<->", bg="deep sky blue", fg="Black", font=("Comic Sans MS", 18),cursor="hand2",command=switch2)
    change2.place(x=220, y=162)

def backswitch2():
    mtoh()

def back():
    home()

def temp():
    f1=Frame(bg="slate blue")
    f1.place(x=0,width=500,height=500)

    Button(f1, text="Back", fg="white", bg="red", font=("Comic Sans MS", 20), cursor="hand2",command=back).place(x=0, y=450)

    l1=Label(f1,text="Temperature Converter",font=("Comic Sans MS",21),bg="slate blue",fg="orange")
    l1.place(x=110,y=20)
    change = Button(f1, text="<->", fg="Black", bg="orange", cursor="hand2",command=switch1)
    change.place(x=250, y=170)

    # -------------- Celsius -------------------------------------------------

    l2=Label(text="Celsius",font=("comic sans ms",18),bg="slate blue",fg="white")
    l2.place(x=100,y=70)
    def entry_focus_in(event):
        if celsius.get()=="Celsius":
            celsius.delete(0,"end")
            celsius.config(bg="white")

    def entry_focus_out(event):
        if celsius.get() == "":
            celsius.insert(0,"Celsius")
            celsius.config(bg="white")

    celsius=Entry(f1,width=20,fg="black",font=("Comic Sans MS",20))
    celsius.place(x=100,y=110)
    celsius.insert(0,"Celsius")
    celsius.bind("<FocusIn>",entry_focus_in)
    celsius.bind("<FocusOut>",entry_focus_out)


    #----------------------------  Fahrenheit ----------------------

    l3=Label(text="Fahrenheit",font=("comic sans ms",18),bg="slate blue",fg="white")
    l3.place(x=100,y=280)

    def entry_focus_in(event):
        if fahrenheit.get()=="Fahrenheit":
            fahrenheit.delete(0,"end")
            fahrenheit.config(bg="white")

    def entry_focus_out(event):
        if fahrenheit.get() == "":
            fahrenheit.insert(0,"Fahrenheit")
            fahrenheit.config(bg="white")

    fahrenheit=Entry(f1,width=20,fg="black",font=("Comic Sans MS",20))
    fahrenheit.place(x=100,y=230)
    fahrenheit.insert(0,"Fahrenheit")
    fahrenheit.bind("<FocusIn>",entry_focus_in)
    fahrenheit.bind("<FocusOut>",entry_focus_out)

    # ____________________ change button ----------------------------

    def changeTemp():
        cdata = celsius.get()
        fdata = fahrenheit.get()

        # if int(fdata)>=0:
        #     data2=(int(fdata)-32)*5/9
        #     celsius.delete(0,"end")
        #     celsius.insert(0,str(data2))

        try:
            if int(cdata)>=0:
                data=(int(cdata)*9/5)+32
                fahrenheit.delete(0, "end")
                fahrenheit.insert(0,str(data))

        except:
            messagebox.showerror("Ooop Ishan","Ishan Sir , Temperature always in Digit")

    # ------------------ save Button ---------------

    b1=Button(f1,text="Change",fg="white",bg="green",font=("Comic Sans MS",30),cursor="hand2",command=changeTemp)
    b1.place(x=150,y=350)



def switch1():
    sf1=Frame(bg="slate blue")
    sf1.place(x=0,width=500,height=500)


    Button(sf1, text="Back", fg="white", bg="red", font=("Comic Sans MS", 20), cursor="hand2",command=back).place(x=0, y=450)
    Label(sf1,text="Temperature Converter",font=("Comic Sans MS",21),bg="slate blue",fg="orange").place(x=110,y=20)
    Label(sf1,text="Celsius", font=("comic sans ms", 18), bg="slate blue", fg="white").place(x=100,y=280)
    Label(sf1,text="Fahrenheit", font=("comic sans ms", 18), bg="slate blue", fg="white").place(x=100,y=70)

    change = Button(sf1, text="<->", fg="Black", bg="orange", cursor="hand2", command=temp)
    change.place(x=250, y=170)

    # ----------------------------  Fahrenheit ----------------------

    def entry_focus_in(event):
        if fahrenheit.get() == "Fahrenheit":
            fahrenheit.delete(0, "end")
            fahrenheit.config(bg="white")

    def entry_focus_out(event):
        if fahrenheit.get() == "":
            fahrenheit.insert(0, "Fahrenheit")
            fahrenheit.config(bg="white")

    fahrenheit = Entry(sf1, width=20, fg="black", font=("Comic Sans MS", 20))
    fahrenheit.place(x=100, y=110)
    fahrenheit.insert(0, "Fahrenheit")
    fahrenheit.bind("<FocusIn>", entry_focus_in)
    fahrenheit.bind("<FocusOut>", entry_focus_out)

    # -------------- Celsius -------------------------------------------------


    def entry_focus_in(event):
        if celsius.get() == "Celsius":
            celsius.delete(0, "end")
            celsius.config(bg="white")

    def entry_focus_out(event):
        if celsius.get() == "":
            celsius.insert(0, "Celsius")
            celsius.config(bg="white")

    celsius = Entry(sf1, width=20, fg="black", font=("Comic Sans MS", 20))
    celsius.place(x=100, y=230)
    celsius.insert(0, "Celsius")
    celsius.bind("<FocusIn>", entry_focus_in)
    celsius.bind("<FocusOut>", entry_focus_out)

    # ____________________ change button ----------------------------

    def changeTemp2():
        cdata = celsius.get()
        fdata = fahrenheit.get()

        # if int(fdata)>=0:
        #     data2=(int(fdata)-32)*5/9
        #     celsius.delete(0,"end")
        #     celsius.insert(0,str(data2))

        try:
            if int(fdata) >= 0:
                data2=(int(fdata)-32)*5/9
                celsius.delete(0,"end")
                celsius.insert(0,str(data2))

        except:
            messagebox.showerror("Ooop Ishan", "Ishan Sir , Temperature always in Digit")

    b1 = Button(sf1, text="Change", fg="white", bg="green", font=("Comic Sans MS", 30), cursor="hand2",
                command=changeTemp2)
    b1.place(x=150, y=350)


def home():
    f1 = Frame(bg="orange")
    f1.place(x=0, width=500, height=500)
    Label(f1,text="The Converters",font=("Comic Sans MS",21),bg="Orange",fg="white").place(x=110,y=20)

    Button(f1, text="Temperature converter", fg="white", bg="green", font=("Comic Sans MS", 18), cursor="hand2",command=temp).place(x=100, y=100)
    Button(f1, text="Minute Into Hours", fg="white", bg="green", font=("Comic Sans MS", 18), cursor="hand2",command=mtoh).place(x=100, y=160)
    # Button(f1, text="Hours Into Days ", fg="white", bg="green", font=("Comic Sans MS", 18), cursor="hand2",command=htod).place(x=100, y=280)
    # Button(f1, text="Days Into Hours ", fg="white", bg="green", font=("Comic Sans MS", 18), cursor="hand2",command=dtoh).place(x=100, y=340)
    #

home()
root.mainloop()