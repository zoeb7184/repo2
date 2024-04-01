from tkinter import*
# from chat import get_response, bot_name


# Creating main window
root = Tk()
root.title("HappifyMe")
root.geometry('1080x720')
root.resizable(width=False, height=False)

#  Creating Menu Bar
menu_bar = Menu(root)
menu_bar.add_command(label='Exit')
root.config(menu=menu_bar)


#  Creating Chat Area
chat_area = Text(root, bd=3, bg='#eb94ae', width=400, height=600)
chat_area.place(x=350, y=10, width=400, height=600)
# chat_area.tag_configure("tag_name", justify='center')


root.mainloop()
