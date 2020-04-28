from tkinter import *
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# -------------------------------------chatbot-----------------------------------------
bot = ChatBot('butty bot')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

# -------------------------------------------interface-------------------------------------
main = Tk()

main.title("chatty bot")
main.geometry("720x720")
main.iconbitmap("icone.ico")

img = PhotoImage(file="funny.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


# --------------------------------------def section----------------------------------
def action():
    query = textF.get()
    response = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "Butty bot : " + str(response))
    textF.delete(0, END)


# ------------------------------------------------------------------------------------

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=70, height=20)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# -------------------Button--------------------
send_button = Button(main, text="Send", font=("Courrier", 18), bg='#FFFFFF', command=action,)
send_button.pack()
# --------------------------------------------------------------------------------------


# -------------------text field----------------------------------------------------
textF = Entry(main, font=("Verdana", 20), width=5)
textF.pack(fill=X, pady=10)
# ---------------------------------------------------------------------------
main.mainloop()
