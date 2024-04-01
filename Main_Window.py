from tkinter import*
from tkinter.font import BOLD

# Creating main window
win = Tk()
win.title("HappifyMe")
win.geometry('75 0x750')


#  Creating Menu Bar
menu = Menu(win)
menu.add_command(label='Exit')
win.config(menu=menu, bg='#eb94ae')


#  Creating Chat Button
chat_button = Button(win, text="Chat", bd=3,
                     bg='#591425', width=400, height=600)
chat_button.place(x=50, y=20, width=300, height=225)
chat_button.config(font=('Arial Rounded MT Bold', 50))


#  Creating Journaling Button
journal_button = Button(win, text="Journal", bd=3,
                        bg='#591425', width=400, height=600)
journal_button.place(x=380, y=20,  width=300, height=225)
journal_button.config(font=('Arial Rounded MT Bold', 50))


#  Creating Diet Button
diet_button = Button(win, text="Diet", bd=3,
                     bg='#591425', width=400, height=600)
diet_button.place(x=50, y=265, width=300, height=225)
diet_button.config(font=('Arial Rounded MT Bold', 50))


#  Creating Medicine Button
med_button = Button(win, text="Medicine", bd=3,
                    bg='#591425', width=400, height=600)
med_button.place(x=380, y=265,  width=300, height=225)
med_button.config(font=('Arial Rounded MT Bold', 50))


#  Creating Physical Fitness Button
fitness_button = Button(win, text="Physical Fitness", bd=3,
                        bg='#591425', width=400, height=600)
fitness_button.place(x=50, y=510, width=630, height=100)
fitness_button.config(font=('Arial Rounded MT Bold', 30))


#  Creating Help Button
help_button = Button(win, text="Seek Professional Aid", bd=3,
                     bg='#591425', width=400, height=600)
help_button.place(x=50, y=620, width=630, height=100)
help_button.config(font=('Arial Rounded MT Bold', 30))


win.mainloop()
