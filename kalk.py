from tkinter import *

#akna seaded
aken = Tk()
aken.title("kalukaltor")
aken.iconbitmap('favicon.ico')
aken.geometry("200x200")
tekst = Label(aken,
              text="siia tuleb vastus",
              font="Tahoma 12",
               padx=2,
               pady=2)
tekst.grid(row=0, column=0, columnspan=4)

#nupud
nupp1 = Button(aken, text="7", width=4,font="Tahoma 12")
nupp1.grid(row=1, column=1, padx=2,pady=2)
nupp2 = Button(aken, text="8", width=4,font="Tahoma 12")
nupp2.grid(row=1, column=2, padx=2,pady=2)
nupp3 = Button(aken, text="9", width=4,font="Tahoma 12")
nupp3.grid(row=1, column=3,padx=2,pady=2)
nupp4 = Button(aken, text="/", width=4,font="Tahoma 12")
nupp4.grid(row=1, column=4,padx=2,pady=2)

nupp5 = Button(aken, text="4", width=4,font="Tahoma 12")
nupp5.grid(row=2, column=1, padx=2,pady=2)
nupp6 = Button(aken, text="5", width=4,font="Tahoma 12")
nupp6.grid(row=2, column=2, padx=2,pady=2)
nupp7 = Button(aken, text="6", width=4,font="Tahoma 12")
nupp7.grid(row=2, column=3,padx=2,pady=2)
nupp8 = Button(aken, text="*", width=4,font="Tahoma 12")
nupp8.grid(row=2, column=4,padx=2,pady=2)

nupp9 = Button(aken, text="1", width=4,font="Tahoma 12")
nupp9.grid(row=3, column=1, padx=2,pady=2)
nupp10 = Button(aken, text="2", width=4,font="Tahoma 12")
nupp10.grid(row=3, column=2, padx=2,pady=2)
nupp11 = Button(aken, text="3", width=4,font="Tahoma 12")
nupp11.grid(row=3, column=3,padx=2,pady=2)
nupp12 = Button(aken, text="-", width=4,font="Tahoma 12")
nupp12.grid(row=3, column=4,padx=2,pady=2)

nupp13 = Button(aken, text="0", width=4,font="Tahoma 12")
nupp13.grid(row=4, column=1, padx=2,pady=2)
nupp14 = Button(aken, text=",", width=4,font="Tahoma 12")
nupp14.grid(row=4, column=2, padx=2,pady=2)
nupp15 = Button(aken, text="=", width=4,font="Tahoma 12")
nupp15.grid(row=4, column=3,padx=2,pady=2)
nupp16 = Button(aken, text="+", width=4,font="Tahoma 12")
nupp16.grid(row=4, column=4,padx=2,pady=2)




aken.mainloop()