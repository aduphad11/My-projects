import random
import tkinter
from logging import root

stats=[]

def get_winner(call):
    if random.random() <= (1/3):
        throw = "stone"
    elif(1/3) <random.random() <= (2/3):
        throw="scissors"
    else:
        throw="paper"

    if(throw =="stone" and call=="paper") or (throw =="paper" and call=="scissors") or (throw=="scissors" and call=="stone"):
        stats.append('w')
        result="you win!"
    elif throw==call:
        stats.append('D')
        result="its a draw"
    else:
        stats.append('L')
        result="you lost!"

    global output
    output.config(text="computer did: "+ throw + "\n" +result)

    def pass_s():
        get_winner("scissors")

    def pass_r():
        get_winner("stone")

    def pass_p():
        get_winner("paper")

    window = tkinter.Tk()

    scissors=tkinter.button(window, text="scissors", bg="#ff9999",
                            padx=10,pady=5,command=pass_s,width=20)
    stone = tkinter.button(window, text="stone", bg="#80ff80",
                              padx=10, pady=5, command=pass_r, width=20)
    paper = tkinter.button(window, text="paper", bg="#3399ff",
                              padx=10, pady=5, command=pass_p, width=20)
    output=tkinter.Label(window, width=20, fg="red", text="what's your call?")

    scissors.pack(side="left")
    stone.pack(side="left")
    paper.pack(side="left")
    output.pack(side="right")
    window.mainloop()

    for i in stats:
        print(i, end=" ")
    if stats.count('L')>stats.count('W'):
        result="\nyou lost the series."
    elif stats.count('L')>stats.count('W'):
        result="\n series ended with a draw."
    else:
        result="\n you won the series."

    print(result)
    #root.mainloop()
