from tkinter import *
#akna seaded
aken = Tk()
aken.title('Joonistamine')
aken.iconbitmap('favicon.ico')

#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine
louend.create_rectangle(150, 150, 0, 0, fill='#ff0000')
louend.create_rectangle(200,150,500,0, fill="#ff0000")
louend.create_rectangle(150, 350, 0, 200, fill='#ff0000')
louend.create_rectangle(200,200,500,350, fill="#ff0000")

aken.mainloop()