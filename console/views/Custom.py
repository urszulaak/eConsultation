import curses
import time
from curses.textpad import Textbox

class Custom():
    
    def __init__(self):
        self._initialize_colors()

    def initialize_colors(stdscr):
        #BLUE
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)

        #CYAN
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

        #RED
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_RED)

        #GREEN
        curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_GREEN)

        #GREY
        curses.init_color(11,220,220,220)
        curses.init_pair(11, 11, curses.COLOR_BLACK)
        curses.init_pair(12, curses.COLOR_WHITE, 11)

    def message(stdscr, message, message2, type):
        if type:
            color=curses.color_pair(8)
            color_back=curses.color_pair(10)
        else:
            color=curses.color_pair(5)
            color_back=curses.color_pair(6)
        h, w = stdscr.getmaxyx()
        win_shadow = curses.newwin(h // 3, w // 4, h // 2 - h // 6 + 1, w // 2 - w // 8 + 1)
        win_shadow.attron(color_back)
        win_shadow.box()
        win_shadow.refresh()
        win_shadow.attroff(color_back)

        win_frame = curses.newwin(h // 3, w // 4, h // 2 - h // 6, w // 2 - w // 8)
        win_frame.attron(color)
        win_frame.box()
        win_frame.refresh()
        win_frame.attroff(color)
        
        curses.curs_set(0)
        stdscr.attron(color)
        for i in range(3):
            if i%2:
                stdscr.addstr(h // 2, w // 2 - (len(message2) // 2) - 1, message2)
            else:
                stdscr.addstr(h // 2, w // 2 - (len(message) // 2) - 1, message)
            stdscr.refresh()
            time.sleep(0.6)
        stdscr.attroff(color)

    def clearContent(stdscr,start=12):
        h, w = stdscr.getmaxyx()
        start_y = start
        end_y = h
        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def list(stdscr, current_row, content, consult=0):
        curses.curs_set(0)
        menu_height = 12
        num_items = len(content)
        h, w = stdscr.getmaxyx()

        available_height = h - menu_height - 1
        box_height = available_height // num_items
        box_width = w - 2

        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * box_height

            win = curses.newwin(box_height, box_width, y, x)
            win.attron(curses.color_pair(4))
            win.box()
            win.attroff(curses.color_pair(4))

            text_x = (box_width - len(row)) // 2
            text_y = box_height // 2

            if id == current_row:
                color = curses.color_pair(7 if id == len(content) - 1 else 3)
                win.addstr(text_y, text_x, row, color)
            else:
                color = curses.color_pair(5 if id == len(content) - 1 else 0)
                win.addstr(text_y, text_x, row, color)

            win.refresh()

    def input(stdscr, content, passw=None, height=14):
        menu_height = height
        fields = []
        h, w = stdscr.getmaxyx()
        y = 0
        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * 3

            win = curses.newwin(3, w - 4, y, x)
            text_x = 2
            text_y = 1
            win.addstr(text_y, text_x, row,curses.color_pair(4))
            win.refresh()

            win_text = curses.newwin(1, w - len(row) - 6, y + 1, x + len(row) + 2)
            box = Textbox(win_text)
            win_text.refresh()

            stdscr.hline(y + 2, x + len(row) + 1, curses.ACS_HLINE, w - len(row))
            stdscr.refresh()
            password_input = []
            while True:
                key = win_text.getch()
                if key == 5:
                    return -1
                elif key == curses.KEY_ENTER or key == 10:
                    if passw and id == passw:
                        fields.append("".join(password_input))
                    else:
                        input_text = box.gather().strip()
                        fields.append(input_text)
                    break
                elif key in (curses.KEY_BACKSPACE, 127, 8):
                    if passw and id == passw and password_input:
                        password_input.pop()
                        win_text.clear()
                        win_text.addstr(0, 0, "\u2022" * len(password_input))
                    else:
                        box.do_command(key)
                else:
                    if passw and  id == passw:
                        password_input.append(chr(key))
                        win_text.addstr(0, len(password_input) - 1, "\u2022")
                    else:
                        box.do_command(key)
                    win_text.refresh()
        return fields
    
    def row(stdscr, content, menu_height, current, selected=None, more=None):
        h, w = stdscr.getmaxyx()
        id=0
        if more:
            available_width = w // 7
        else:
            available_width = w // len(content)
        for i, element in enumerate(content):
            if more:
                if i == 7:
                    id = 0
                    menu_height += 6
                x_position = available_width * id
            else:
                x_position = available_width * i
            win_block = curses.newwin(5, available_width, menu_height+2, x_position)
            win_block.attron(curses.color_pair(4))
            win_block.box()
            win_block.attroff(curses.color_pair(4))
            text = str(element)
            text_x = (available_width - len(text)) // 2
            text_y = 5 // 2
            if i == current:
                win_block.addstr(text_y, text_x, str(element),curses.color_pair(3))
            else:
                win_block.addstr(text_y, text_x, str(element))
            if more:
                if i in selected:
                    win_block.attron(curses.color_pair(8))
                    win_block.box()
                    win_block.addstr(text_y, text_x, str(element))
                    win_block.attroff(curses.color_pair(8))
                    if i == current:
                        win_block.addstr(text_y, text_x, str(element),curses.color_pair(9))
                id+=1
            win_block.refresh()