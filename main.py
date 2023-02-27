import random
from tkinter import *
from tkinter import messagebox
import time
list_for_1_100 = []
for x in range(1,101):
    list_for_1_100.append(x)


def easy():
    """this is the function for assigning game life for easy play """
    global display
    display = lve
    return int(10)
def hard():
    """this is the function for assigning game life for easy play """
    global display
    display = lvh
    return int(5)
def wrong_guess(life):
    """this is the function for reduction the life when you have a wrong guess"""
    return life-1
#
#
def levels(uqx):
    if uqx == "False":
        return easy()
    elif uqx == "True":
        return hard()

blank = []
def word2():
    global wd, blankword,blank, ck
    blank = []
    wd = random.choice(list_for_1_100)

    blank.append("--")
    blankword = "".join(blank)
    return wd, blankword
###########################################################################################################################

def play_game():
    def check(user_guess, guess, life):
        global name, blankword, num
        if life > 1:
            if user_guess == guess:
                canvers.itemconfigure(ghh, text=f"you guess right {user_guess}")
                blankword = guess
            elif user_guess > guess:
                canvers.itemconfigure(ghh, text=f"{user_guess} Too high")
                blankword = "".join(blank)

                life = wrong_guess(life)
            elif user_guess < guess:
                canvers.itemconfig(ghh, text=f"{user_guess} Too low")
                blankword = "".join(blank)
                life = wrong_guess(life)

            # if user_input == word:  #     for x in range(0,len(word)):  #         if user_input == word:  #             blank[x] = user_input[x]  #  # else:  #     life = life - 1
        else:
            life = life - 1
            canvers.itemconfig(ghh, text=f"Answer is {guess}")
            canvers.itemconfig(hangtree, image=tree2)
            canvers.delete(manpic, womanpic)

        return blankword, life
    def bt():
        global life, blankword, num
        blankword, life = check(int(input_lt.get()), number, life)
        input_lt.delete(0, "end")
        canvers.itemconfig(bk, text=f"{blankword}", font=("Arial Rounded MT Bold", 30, "bold"), fill="white")
        canvers.itemconfig(health, image=display[life])
        if number == blankword:
            messagebox.showinfo("Game results", f"you win level {num}")
            num += 1
            life= levels(kok)
            play_game()

    def enter1(e):
        canvers.itemconfig(butten_exit, image=exit_b2)
        time.sleep(2)
        canver.delete("all")
        home.destroy()

    global hangtree, canvers, manpic, womanpic,ghh
    canvers = Canvas(width=826, height=620)
    mainpage = canvers.create_image(413, 310, image=background)
    hangtree = canvers.create_image(650, 270, image=tree)
    level2 = canvers.create_image(400, 110, image=level)
    stage = canvers.create_text(400, 133, text=f"{num}", font=("Arial Rounded MT Bold", 30, "bold"), fill="white")
    bd = canvers.create_image(400, 500, image=bread)
    manpic = canvers.create_image(100, 390, image=man)
    womanpic = canvers.create_image(200, 400, image=woman)
    butten_exit = canvers.create_image(100, 120, image=exit_b)
    health = canvers.create_image(680, 70, image=display[-1])

    number, blankwd = word2()
    canvers.tag_bind(butten_exit, "<Button>", enter1)
    input_lt = Entry(canvers, width=4, justify=CENTER, font=("Arial Rounded MT Bold", 25, "bold"), fg="white", border=1,
        bg="#ed2424")
    input_lt.place(x=350, y=539)
    bf = Button(canvers, text="check", command=bt, fg="white", border=1, bg="#ed2424")
    bf.place(x=460, y=545)
    bk = canvers.create_text(395, 500, text=f"{blankwd}", font=("Arial Rounded MT Bold", 30, "bold"), fill="white")
    ghh = canvers.create_text(400, 450, text=f"", font=("Arial Rounded MT Bold", 15, "bold"), fill="white")
    bh = canvers.create_text(400, 400, text=f"Guess a number", font=("Arial Rounded MT Bold", 15, "bold"), fill="white")
    canvers.place(x=-1, y=0)

def start_game(e):
    global life, kok
    kok = str(messagebox.askyesno("Game level", "Do you want the hard level"))
    life = levels(kok)
    canver.itemconfig(butten_play, image=play_on)
    time.sleep(2)
    canver.delete("all")
    play_game()



num =1

home = Tk()
home.title("NUMBER GUESSING GAME")
home.geometry("826x620")
background = PhotoImage(file="image/seamless-colorful-trees-forest-against-backdrop-mountains_284645-1314.png")
play = PhotoImage(file="image/play.png")
start_tree = PhotoImage(file="image/Layer 1.png")
play_on = PhotoImage(file="image/play 2.png")
exit_b = PhotoImage(file="image/exit.png")
exit_b2 = PhotoImage(file="image/exit 2.png")
level = PhotoImage(file="image/level.png")
bread = PhotoImage(file="image/word borad.png")
man = PhotoImage(file="image/man.png")
woman = PhotoImage(file="image/woman.png")
tree = PhotoImage(file="image/tree.png")
tree2 = PhotoImage(file="image/Layer 2.png")
l0 = PhotoImage(file="image/0h life.png")
l1 = PhotoImage(file="image/1h life.png")
l2 = PhotoImage(file="image/2h life.png")
l3 = PhotoImage(file="image/3h life.png")
l4 = PhotoImage(file="image/4h life.png")
l5 = PhotoImage(file="image/5h life.png")

lvh =[l0,l1,l2,l3,l4,l5]

l0e = PhotoImage(file="image/0e life.png")
l1e = PhotoImage(file="image/1e life.png")
l2e = PhotoImage(file="image/2e life.png")
l3e = PhotoImage(file="image/3e life.png")
l4e = PhotoImage(file="image/4e life.png")
l5e = PhotoImage(file="image/5e life.png")
l6e = PhotoImage(file="image/6e life.png")
l7e = PhotoImage(file="image/7e life.png")
l8e = PhotoImage(file="image/8e life.png")
l9e = PhotoImage(file="image/9e life.png")
l10e = PhotoImage(file="image/10e life.png")
lve =[l0e,l1e,l2e,l3e,l4e,l5e, l6e,l7e,l8e,l9e,l10e]

canver = Canvas(width=826,height=620)
canver.configure(highlightthickness=0)
mainpage = canver.create_image(413,310, image=background)
butten_play = canver.create_image(250,250, image=play)
butten_exit = canver.create_image(250, 350, image=exit_b)
tree_black = canver.create_image(650, 270, image=tree)

welcome = canver.create_text(520,30, text="WELCOME TO GUESSING GAME", font=("Arial Rounded MT Bold", 25, "bold"), fill="white")
canver.tag_bind(butten_play, "<Button>", start_game)
canver.tag_bind(butten_exit, "<Button>", exit)
canver.place(x=-1, y=0)

home.mainloop()

