from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

app = Tk()
app.geometry("500x500")
app.configure(bg='#C0E1D2')

window = Tk()
window.geometry("500x500")
window.withdraw()

score_data = open('highscore.txt', 'r+')
x = 0

def game():
    global x
    if x == 0:
        app.withdraw()
        x = x+1
    window.deiconify()
    def check_result():
        j = error = 0
        answer = entry.get("1.0", "end-1c")
        end = timer()
        time_taken = end-start
        if len(words[word])>=len(answer):
            error = len(words[word])-len(answer)
            for i in answer:
                if i == words[word][j]:
                    pass
                else:
                    error+=1
                j+=1
        elif len(words[word])<=len(answer):
            error = len(answer)-len(words[word])
            for i in words[word]:
                if i == answer[j]:
                    pass
                else:
                    error+=1
                j+=1
        wpm = len(answer)/5
        wpm = wpm - error
        wpm = int(wpm/(time_taken/60))
        score_data.seek(0)
        line = int(score_data.readline())
        if wpm>line:
            score_data.seek(0)
            score_data.write(str(wpm))
            result = "Excellent! Your New High Score is: "+str(wpm)+" WPM"
            messagebox.showinfo("Score", result)
        else:
            result = "Your score is: "+str(wpm)+" WPM\nBetter luck next time!"
            messagebox.showinfo("Score", result)
    def finish():
        score_data.close()
        window.destroy()
        app.destroy()

    words = ["tom is a small boy", "i love to eat icecream", "kids playing in the park"]
    # words = ["Hunt and peck two fingered typing is a common form of typing in which the typist presses each key individually. Instead of relying on the memorized position of keys, the typist must find each key by sight. The use of this method may also prevent the typist from being able to see what has been typed without glancing away from the keys. Although good accuracy may be achieved, any typing errors that are made may not be noticed immediately due to the user not looking at the screen. There is also the disadvantage that because fewer fingers are used, those that are used are forced to move a much greater distance"]
    word = random.randint(0, (len(words)-1))

    title2 = Label(window, text=words[word], bg="black", fg="white", height=6, width=29, font="Arial 20")
    title2.place(x=15, y=10)

    sub_btn = Button(window, text="Submit!", font="Arial 20", bg="#fc2828", command=check_result)
    sub_btn.place(x=190, y=360)

    entry = Text(window)
    entry.place(x=80, y=210, height=150, width=350)

    done_btn = Button(window, text="Done", font="Arial 13", bg="#ffc003", width=12, command=finish)
    done_btn.place(x=130, y=420)

    btn2 = Button(window, text="Another one?", font="Arial 13", bg="#ffc003", width=12, command=game)
    btn2.place(x=265, y=420)

    start = timer()

    window.mainloop()

title = Label(app, text="Test Your Typing Speed!", bg="#C0E1D2", fg="black", font="Arial")
title.place(x=160, y=50)

btn = Button(app, text="Go!", width=12, bg="#ffe6bd", font="Arial 20", command=game)
btn.place(x=150, y=120)

hs_text = Label(app, text="High Score", width=12, fg="black", bg="#c5afe0", font="Arial 35")
hs_text.place(x=90, y=240)

hs = int(score_data.readline())
hs_val = Label(app, text=str(hs)+" WPM", fg="black", bg="#ff9c9c", font="Arial 30")
hs_val.place(x=180, y=350)


app.mainloop()