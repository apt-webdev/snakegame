import random
import curses
from threading import Timer

curses.initscr()
curses.start_color()
curses.noecho()    # don't echo the keys on the screen
curses.cbreak()    # don't wait enter for input
curses.curs_set(0) # don't show cursor.

RED_TEXT = 1
GREEN_TEXT = 2 

curses.init_pair(RED_TEXT, curses.COLOR_RED, curses.COLOR_BLACK) # init-pair to change the definition of a color in terminal
curses.init_pair(GREEN_TEXT, curses.COLOR_GREEN, curses.COLOR_BLACK)

score = 0 
sh = 20 
sw = 60 

snakegame = curses.newwin(5,20,1,5) # height, width, y-coord, x-coord
snakegame.box()
snakegame.addstr(2,3, "SNAKEGAME", curses.color_pair(GREEN_TEXT))

scorebox = curses.newwin(5,20,1,38)
scorebox.box()
scorebox.addstr(2,3, "SCORE: " + str(score), curses.color_pair(RED_TEXT))

windowbox = curses.newwin(sh+1, sw+1, 7, 1)
windowbox.box()
windowbox.keypad(1)
windowbox.timeout(100)


snk_x = sw/4 # initial coords
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2] 
windowbox.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT # inicial direction move 

while True:
    scorebox.refresh()
    snakegame.refresh()
    next_key = windowbox.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        print("BEST SCORE: " + str(score))
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        windowbox.addch(food[0], food[1], curses.ACS_PI)
        score +=1
        scorebox.addstr(2,3, "SCORE: " + str(score), curses.color_pair(RED_TEXT))

    else:
        tail = snake.pop()
        windowbox.addch(int(tail[0]), int(tail[1]), ' ')
        
    windowbox.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

