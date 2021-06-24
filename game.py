from tkinter import *
from tkinter.ttk import *
from random import randint
from leaderboard import *
import time

score = 0
level = 1
limit = 50

start_button = None
start_text = None
quit_button = None
quit_text = None
save_load_button = None
save_load_text = None
leaderboard_button = None
leaderboard_text = None
GameOvertext = None

again = None
again_text = None
exit_to_main = None
exit_text = None

gameOn = False
GameOver = False
has_hit = False
menu_page = True
cheat_1 = False
cheat_2 = False
pause_is_on = False


def leftKey(event):
    global pause_is_on
    if not GameOver and not pause_is_on and canvas.coords(ship)[0] - 10 >= 0:
        canvas.move(ship, -10, 0)


def rightKey(event):
    global pause_is_on
    if not GameOver and not pause_is_on:
        if (canvas.coords(ship)[0] + 10 <= screenwidth):
            canvas.move(ship, 10, 0)


def upKey(event):
    global pause_is_on
    if not GameOver and not pause_is_on and canvas.coords(ship)[1] - 10 >= 0:
        canvas.move(ship, 0, -10)


def downKey(event):
    global pause_is_on
    if not GameOver and not pause_is_on:
        if (canvas.coords(ship)[1] + 200 <= screenheight):
            canvas.move(ship, 0, 10)


save_menu = None
save_text = None
pause_text = None


def pauseGame(event):
    global save_menu
    global save_text
    global exit_to_main
    global exit_text
    global pause_is_on
    global pause_text
    if (pause_is_on):
        pause_is_on = False
        canvas.delete(save_menu)
        canvas.delete(save_text)
        canvas.delete(exit_to_main)
        canvas.delete(exit_text)
        canvas.delete(pause_text)
        canvas.pack()
        window.after(100, Game_start)
    else:
        pause_is_on = True
        pause_text = canvas.create_text(screenwidth/2, screenheight/2,
                                        fill="white", font="Arial 20",
                                        text="Paused")

        save_x1 = (screenwidth/2) - 150
        save_y1 = (screenheight/2) + 80
        save_x2 = save_x1 + 300
        save_y2 = save_y1 + 50

        save_menu = canvas.create_rectangle(save_x1, save_y1, save_x2, save_y2,
                                            fill="purple")
        save_text = canvas.create_text((save_x1 + save_x2)/2,
                                       (save_y1 + save_y2)/2, fill="white",
                                       font="Times 20", text="Save Game")

        exit_x1 = save_x1
        exit_y1 = save_y2 + 20
        exit_x2 = save_x2
        exit_y2 = exit_y1 + 50

        exit_to_main = canvas.create_rectangle(exit_x1, exit_y1, exit_x2,
                                               exit_y2, fill="purple")
        exit_text = canvas.create_text((exit_x1 + exit_x2)/2,
                                       (exit_y1 + exit_y2)/2, fill="white",
                                       font="Times 20",
                                       text="Exit to main menu")
        canvas.pack()

screenshot = None
screenshotOn = False


def bossKey(event):
    global pause_is_on
    global pause_text
    global GameOver
    global screenshotOn
    global screenshot

    if (not GameOver and not pause_is_on and not menu_page):
        pause_is_on = True
        pause_text = canvas.create_text(screenwidth/2, screenheight/2,
                                        fill="white", font="Arial 50",
                                        text="Pause")

    if (not screenshotOn):
        screenshotOn = True
        screenshot = canvas.create_image(0, 0, anchor=NW, image=screenshotImg)
    else:
        screenshotOn = False
        canvas.delete(screenshot)
        canvas.pack()


def click(event):
    global gameOn
    global start_button
    global start_text
    global quit_button
    global quit_text
    global leaderboard_button
    global leaderboard_text
    global save_load_button
    global save_load_text
    global GameOvertext
    global menu_page

    global score
    global level

    global GameOver
    global again
    global again_text
    global exit_to_main
    global exit_text

    global save_menu
    global save_text
    global exit_to_main
    global exit_text
    global pause_is_on
    global pause_text

    global pause_
    if (not gameOn and not GameOver and menu_page):
        x = event.x
        y = event.y

        start_x1 = screenwidth / 2 - 200
        start_y1 = screenheight / 3 - 150
        start_x2 = start_x1 + 400
        start_y2 = start_y1 + 100

        quit_x1 = start_x1
        quit_y1 = start_y2 + 30
        quit_x2 = start_x2
        quit_y2 = quit_y1 + 100

        save_load_x1 = start_x1
        save_load_y1 = quit_y1 + 130
        save_load_x2 = start_x2
        save_load_y2 = save_load_y1 + 100

        leaderboard_x1 = start_x1
        leaderboard_y1 = save_load_y1 + 130
        leaderboard_x2 = start_x2
        leaderboard_y2 = save_load_y1 + 230

        if (x >= start_x1 and x <= start_x2):
            if (y >= start_y1 and y <= start_y2):
                gameOn = True
                menu_page = False
                pause_is_on = False
                canvas.delete(start_button)
                canvas.delete(start_text)
                canvas.delete(quit_button)
                canvas.delete(quit_text)
                canvas.delete(leaderboard_button)
                canvas.delete(leaderboard_text)
                canvas.delete(save_load_button)
                canvas.delete(save_load_text)
                score = 0
                level = 1
                init()

        if (x >= quit_x1 and x <= quit_x2):
            if (y >= quit_y1 and y <= quit_y2):
                quitGame()

        if (x >= save_load_x1 and x <= save_load_x2):
            if (y >= save_load_y1 and y <= save_load_y2):
                gameOn = True
                menu_page = False
                pause_is_on = False
                canvas.delete(start_button)
                canvas.delete(start_text)
                canvas.delete(quit_button)
                canvas.delete(quit_text)
                canvas.delete(leaderboard_button)
                canvas.delete(leaderboard_text)
                canvas.delete(save_load_button)
                canvas.delete(save_load_text)
                # alien_list.clear()
                # meteor_list.clear()
                # bullets.clear()
                loadgame()

        if (x >= leaderboard_x1 and x <= leaderboard_x2):
            if (y >= leaderboard_y1 and y <= leaderboard_y2):
                show_leaderboard()

    if (not gameOn and not menu_page and GameOver):
        x = event.x
        y = event.y

        again_x1 = (screenwidth/2) - 150
        again_y1 = (screenheight/2) + 80
        again_x2 = again_x1 + 300
        again_y2 = again_y1 + 50

        exit_x1 = again_x1
        exit_y1 = again_y2 + 20
        exit_x2 = again_x2
        exit_y2 = exit_y1 + 50

        if (x >= again_x1 and x <= again_x2):
            if (y >= again_y1 and y <= again_y2):
                canvas.delete(again)
                canvas.delete(again_text)
                canvas.delete(exit_to_main)
                canvas.delete(exit_text)
                canvas.delete(GameOvertext)
                canvas.pack()
                GameOver = False
                gameOn = True
                score = 0
                level = 1
                print("Again pressed")
                init()

        if (x >= exit_x1 and x <= exit_x2):
            if (y >= exit_y1 and y <= exit_y2):
                canvas.delete(again)
                canvas.delete(again_text)
                canvas.delete(exit_to_main)
                canvas.delete(exit_text)
                canvas.delete(GameOvertext)
                canvas.pack()
                GameOver = False
                gameOn = False
                menu_page = True
                print("Exit pressed")
                GameMenu()

    if (pause_is_on and not GameOver):
        x = event.x
        y = event.y

        save_x1 = (screenwidth/2) - 150
        save_y1 = (screenheight/2) + 80
        save_x2 = save_x1 + 300
        save_y2 = save_y1 + 50

        exit_x1 = save_x1
        exit_y1 = save_y2 + 20
        exit_x2 = save_x2
        exit_y2 = exit_y1 + 50

        if (x >= save_x1 and x <= save_x2):
            if (y >= save_y1 and y <= save_y2):
                save_game()

        if (x >= exit_x1 and x <= exit_x2):
            if (y >= exit_y1 and y <= exit_y2):
                canvas.delete(save_menu)
                canvas.delete(save_text)
                canvas.delete(exit_to_main)
                canvas.delete(exit_text)
                canvas.delete(pause_text)
                canvas.pack()
                GameOver = False
                gameOn = False
                menu_page = True
                print("Exit pressed")
                GameMenu()

username = None


def save_game():
    global level
    global score
    global limit
    global username

    gamefile = open("lastSavedGame.txt", "+w")
    gamefile.write(str(level))
    gamefile.write("\n" + str(score))
    gamefile.write("\n" + str(limit))
    gamefile.write("\n" + username)
    return


def quitGame():
    window.quit()


def loadgame():
    global level
    global score
    global username
    global limit

    saved_game = open("lastSavedGame.txt")
    previous_level = saved_game.readline()
    previous_score = saved_game.readline()
    previous_limit = saved_game.readline()
    username = saved_game.readline()

    print(previous_level)
    print(previous_score)
    print(previous_limit)
    print(username)

    level = int(previous_level)
    score = int(previous_score)
    limit = int(previous_limit)
    saved_game.close()

    init()


def cleararray():
    n = len(alien_list) > 0
    m = len(meteor_list) > 0
    while n and (canvas.coords(alien_list[0])[1] >= screenheight):
        canvas.delete(alien_list[0])
        alien_list.remove(alien_list[0])
    while m and (canvas.coords(meteor_list[0])[1] >= screenheight):
        canvas.delete(meteor_list[0])
        meteor_list.remove(meteor_list[0])
    while len(bullets) > 0 and canvas.coords(bullets[0])[1] <= 0:
        canvas.delete(bullets[0])
        bullets.remove(bullets[0])


def clear_canvas_enemies():
    for i in alien_list:
        canvas.delete(i)
        alien_list.remove(i)
    for i in meteor_list:
        canvas.delete(i)
        meteor_list.remove(i)


bullets = list()
alien_list = list()
meteor_list = list()


def name_input():
    popup_window = Toplevel(window)
    Label(popup_window, text="Game Over!").pack()
    Label(popup_window, text="You got: " + str(score)).pack(pady=8)
    textbox = Entry(popup_window)
    textbox.pack()

    def submit_score():
        name = textbox.get()
        load_leaderboard().append((name, score))
        sort_leaderboard()
        save_leaderboard()
        show_leaderboard()

    button = Button(popup_window, text="Submit", command=submit_score).pack()


def show_leaderboard():
    leaderboard_window = Toplevel(window)
    tv = Treeview(leaderboard_window)
    tv["columns"] = ("name", "score")
    tv.heading("#0", text="Place")
    tv.column("#0", anchor="w", width=120)

    tv.heading("name", text="Name")
    tv.column("name", anchor="center", minwidth=120)

    tv.heading("score", text="Score")
    tv.column("score", anchor="center", minwidth=120)

    tv.pack(side="left", expand=True, fill="both")

    load_leaderboard()
    for place, (name, score) in enumerate(load_leaderboard()):
        tv.insert("", "end", text=place+1, values=(name, score))


# creating the meteor
def createmeteor():
    x = randint(0, screenwidth)
    y = 0
    meteor = canvas.create_image(x, y, anchor=S, image=meteor_image)
    meteor_list.append(meteor)


# creating the object
def createobject():
    x = randint(0, screenwidth)
    y = 0
    alien = canvas.create_image(x, y, anchor=N, image=alien_image)
    alien_list.append(alien)

to_shoot = True


def allow_shooting():
    global to_shoot
    to_shoot = True


def create_bullet(event):
    global to_shoot
    if to_shoot and not pause_is_on:
        to_shoot = False
        ship_x1 = canvas.coords(ship)[0] - 338 / 2
        ship_y1 = canvas.coords(ship)[1]
        ship_x2 = ship_x1 + 338
        ship_y2 = ship_y1 + 176
        x = (ship_x1 + ship_x2)/2
        y = (ship_y1 + ship_y2)/2
        bullet = canvas.create_rectangle(x, y, x+3, y+10, fill="blue")
        bullets.append(bullet)
        canvas.after(300, allow_shooting)


def move():
    for i in range(len(alien_list)):
        canvas.move(alien_list[i], 0, 2)
    canvas.pack()
    for i in range(len(bullets)):
        canvas.move(bullets[i], 0, -3)
    canvas.pack()
    for i in range(len(meteor_list)):
        canvas.move(meteor_list[i], 0, 3)


def collide():
    global GameOvertext
    global GameOver, gameOn, pauseOn, score, scoreText
    ship_x1 = canvas.coords(ship)[0] - 104 / 4
    ship_y1 = canvas.coords(ship)[1] + 15
    ship_x2 = ship_x1 + 104 / 2
    ship_y2 = ship_y1 + 90
    for i in range(len(alien_list)):
        current = canvas.coords(alien_list[i])
        alien_x1 = current[0] - 150 / 4
        alien_y1 = current[1]
        alien_x2 = alien_x1 + 150 / 2
        alien_y2 = alien_y1 + 48
        if (alien_y2 >= ship_y1 and alien_y1 <= ship_y2):
            if ((alien_x2 >= ship_x1 and alien_x1 <= ship_x2) or
               (ship_x2 >= alien_x1 and ship_x1 <= alien_x2)):
                GameOver = True
                print("alien hit")
                GameOvertext = canvas.create_text(screenwidth/2,
                                                  screenheight/2, fill="red",
                                                  font="arial 35",
                                                  text="Game Over")
                gameOn = False
                pauseOn = False
                clear_canvas_enemies()
                canvas.itemconfigure(scoreText, text="Score: " + str(score))
                afterGameOver()
                name_input()
                return True

    for i in range(len(meteor_list)):
        meteor = meteor_list[i]
        meteor_x1 = canvas.coords(meteor)[0]
        meteor_y1 = canvas.coords(meteor)[1]
        meteor_x2 = meteor_x1 + 37
        meteor_y2 = meteor_y1 + 50
        if ship_x1 < meteor_x1 < ship_x2 and ship_y1 < meteor_y1 < ship_y2:
            print('meteor hit')
            GameOver = True
            GameOvertext = canvas.create_text(screenwidth/2,
                                              screenheight/2, fill="red",
                                              font="arial 35",
                                              text="Game Over")
            gameOn = False
            pauseOn = False
            clear_canvas_enemies()
            score = 0
            canvas.itemconfigure(scoreText, text="Score: "+str(score))
            afterGameOver()
            name_input()
            return True

    return False


def hit():
    global score
    global level
    global scoreText
    global limit
    global cheat_1
    for i in range(len(alien_list)):
        for j in range(len(bullets)):
            current = canvas.coords(alien_list[i])
            alien_x1 = current[0] - 150 / 4
            alien_y1 = current[1] + 15
            alien_x2 = alien_x1 + 150 / 2
            alien_y2 = alien_y1 + 86
            bul = canvas.coords(bullets[j])

            if alien_x1 < bul[0] < alien_x2 and alien_y1 < bul[1] < alien_y2:
                canvas.delete(alien_list[i])
                canvas.delete(bullets[j])
                if cheat_1:
                    score += 150
                else:
                    score += 5
                canvas.itemconfigure(scoreText, text="Score: "+str(score))
                if (score >= limit):
                    level += 1
                    limit += 50
                    canvas.itemconfigure(levelText, text="Level: "+str(level))
                alien_list.remove(alien_list[i])
                bullets.remove(bullets[j])
                return True

    return False


def Game_start():
    global start_button, start_text, quit_button, quit_text, GameOver
    global pauseOn, score
    global cheat_2
    GameOver = False
    ballChance = randint(1, 40)
    if (ballChance == 5):
        createobject()

    move()
    cleararray()
    if collide():
        return
    has_hit = True
    while has_hit:
        has_hit = hit()

    meteorChance = randint(1, 30)
    if (meteorChance == 4 and not cheat_2):
        createmeteor()
    move()
    cleararray()

    if collide():
        return

    has_hit = True
    while has_hit:
        has_hit = hit()

    if (not pause_is_on):
        window.after(30, Game_start)


def afterGameOver():
    print("In")
    global again
    global again_text
    global exit_to_main
    global exit_text

    again_x1 = (screenwidth/2) - 150
    again_y1 = (screenheight/2) + 80
    again_x2 = again_x1 + 300
    again_y2 = again_y1 + 50

    again = canvas.create_rectangle(again_x1, again_y1, again_x2, again_y2,
                                    fill="purple")
    again_text = canvas.create_text((again_x1 + again_x2)/2,
                                    (again_y1 + again_y2)/2, fill="white",
                                    font="Times 20", text="Again?")

    exit_x1 = again_x1
    exit_y1 = again_y2 + 20
    exit_x2 = again_x2
    exit_y2 = exit_y1 + 50

    exit_to_main = canvas.create_rectangle(exit_x1, exit_y1, exit_x2,
                                           exit_y2, fill="purple")
    exit_text = canvas.create_text((exit_x1 + exit_x2)/2,
                                   (exit_y1 + exit_y2)/2, fill="white",
                                   font="Times 20", text="Exit to main menu")
    canvas.pack()
    return


def GameMenu():
    global start_button
    global start_text
    global quit_button
    global quit_text
    global save_load_button
    global save_load_text
    global leaderboard_button
    global leaderboard_text
    start_x1 = screenwidth / 2 - 200
    start_y1 = screenheight / 3 - 150
    start_x2 = start_x1 + 400
    start_y2 = start_y1 + 100

    start_button = canvas.create_rectangle(start_x1, start_y1,
                                           start_x2, start_y2, fill="purple")
    start_text = canvas.create_text((start_x1 + start_x2) / 2,
                                    (start_y1 + start_y2) / 2, fill="white",
                                    font="Times 30 bold", text="Start")
    quit_x1 = start_x1
    quit_y1 = start_y2 + 30
    quit_x2 = start_x2
    quit_y2 = quit_y1 + 100

    quit_button = canvas.create_rectangle(quit_x1, quit_y1, quit_x2, quit_y2,
                                          fill="purple")
    quit_text = canvas.create_text((quit_x1 + quit_x2) / 2,
                                   (quit_y1 + quit_y2) / 2, fill="white",
                                   font="Times 30 bold",
                                   text="Quit")

    save_load_x1 = start_x1
    save_load_y1 = quit_y1 + 130
    save_load_x2 = start_x2
    save_load_y2 = save_load_y1 + 100

    save_load_button = canvas.create_rectangle(save_load_x1, save_load_y1,
                                               save_load_x2, save_load_y2,
                                               fill="purple")
    save_load_text = canvas.create_text((save_load_x1 + save_load_x2) / 2,
                                        (save_load_y1 + save_load_y2) / 2,
                                        fill="white", font="Times 25 bold",
                                        text="Load last Saved Game")

    leaderboard_x1 = start_x1
    leaderboard_y1 = save_load_y1 + 130
    leaderboard_x2 = start_x2
    leaderboard_y2 = save_load_y1 + 230

    leaderboard_button = canvas.create_rectangle(leaderboard_x1,
                                                 leaderboard_y1,
                                                 leaderboard_x2,
                                                 leaderboard_y2,
                                                 fill="purple")
    a = (leaderboard_x1 + leaderboard_x2) / 2
    b = (leaderboard_y1 + leaderboard_y2) / 2
    leaderboard_text = canvas.create_text(a, b, fill="white",
                                          font="Times 30 bold",
                                          text="Leader Board")

    canvas.pack()
    return


def init():
    global ship
    global scoreText
    global levelText
    global background
    background = canvas.create_image(0, 0, image=canvas_image, anchor=NW)
    ship = canvas.create_image(screenwidth / 2 - 20, 3 * screenheight/4 - 20,
                               anchor=N, image=ship_image)
    scoreText = canvas.create_text(50, 50, fill="white", font="Times 20",
                                   text="Score: "+str(score))
    levelText = canvas.create_text(50, 80, fill="white", font="Times 20",
                                   text="Level: "+str(level))
    canvas.pack()
    Game_start()


def cheatcode_1(event):
    global cheat_1
    if cheat_1:
        cheat_1 = False
    else:
        cheat_1 = True


def cheatcode_2(event):
    global cheat_2
    if cheat_2:
        cheat_2 = False
    else:
        cheat_2 = True


window = Tk()
window.attributes("-fullscreen", True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

window.title("Space Bois")
canvas = Canvas(window, bg='black', width=screenwidth, height=screenheight)
canvas_image = PhotoImage(file='space.png')
background = canvas.create_image(0, 0, image=canvas_image, anchor=NW)
canvas.bind("<space>", create_bullet)
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Down>", downKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Button-1>", click)
canvas.bind("<Escape>", pauseGame)
canvas.bind("<q>", bossKey)
canvas.bind("<a><e><z><a><k><m><i>", cheatcode_1)
canvas.bind("<a><l><i><e><n>", cheatcode_2)
# enables the binding
canvas.focus_set()
# image for the space ship
ship_image = PhotoImage(file='space_ship_resized.png')
screenshotImg = PhotoImage(file="screenshot.png")
# image for the alien enemy
alien_image = PhotoImage(file='alien.png')
# image for the meteor enemy
meteor_image = PhotoImage(file='meteor.png')
ship = canvas.create_image(screenwidth / 2 - 20, 3 * screenheight/4 - 20,
                           anchor=N, image=ship_image)
scoreText = canvas.create_text(50, 50, fill="white", font="Times 20",
                               text="Score: "+str(score))
levelText = canvas.create_text(50, 80, fill="white", font="Times 20",
                               text="Level: "+str(level))
canvas.pack()

GameMenu()

window.mainloop()
