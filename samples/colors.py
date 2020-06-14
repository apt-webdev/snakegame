import sys
import curses


curses.initscr()

if not curses.has_colors():
    curses.endwin()
    print("no colors")
    sys.exit()
else:
    curses.start_color()

curses.noecho()    # don't echo the keys on the screen
curses.cbreak()    # don't wait enter for input
curses.curs_set(0) # don't show cursor.

RED_TEXT = 1
curses.init_pair(RED_TEXT, curses.COLOR_RED, curses.COLOR_BLACK)

window = curses.newwin(20, 20, 0, 0)
window.box()
staticwin = curses.newwin(5, 10, 1, 1)
staticwin.box()

staticwin.addstr(1, 1, "test", curses.color_pair(RED_TEXT))

cur_x = 10
cur_y = 10
while True:
    window.addch(cur_y, cur_x, '@')
    window.refresh()
    staticwin.box()
    staticwin.refresh()
    inchar = window.getch()
    window.addch(cur_y, cur_x, ' ')
    # W,A,S,D used to move around the @
    if inchar == ord('w'):
        cur_y -= 1
    elif inchar == ord('a'):
        cur_x -= 1
    elif inchar == ord('d'):
        cur_x += 1
    elif inchar == ord('s'):
        cur_y += 1
    elif inchar == ord('q'):
        break
curses.endwin()