from Joseph.joseph import joseph as jos
from Joseph.domain import person as ps
from Joseph.file_reader import file_reader
import curses
from typing import List, Iterator
#初始化窗口
stdscr = curses.initscr()

def display_info(str, x, y, color_num):
    stdscr.addstr(y, x, str, curses.color_pair(color_num))
    stdscr.refresh()

def set_color():
    '''''颜色设置'''
    #使用颜色首先需要调用这个方法
    curses.start_color()
    #文字和背景色设置，设置了两个color pair，分别为1和2
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


if __name__ == '__main__':  
    # jos.append(Person("Lisa", 13))
    # jos.append(Person("Aha", 15))
    # jos.append(Person("Bob", 12))
    # jos.append(Person("Cindy", 15))
    # jos.append(Person("Joan", 14))
    # jos.append(Person("Rose", 19))

    data = file_reader.TxtReader("person.txt")
    reader = data.read_data()
    ring = jos.JosephusRing(reader)
    ring.start = 1
    ring.step = 2
    length = len(ring.query_list())
    generator_people = ring.next()

    set_color()
    display_info("name", 0, 0, 2)
    display_info("out_name", 15, 0, 2)
    orinal_name_location = 1
    for j in reader:
        display_info(j.name, 0, orinal_name_location, 1)
        orinal_name_location = orinal_name_location + 1

    out_name_location = 1
    for i in range(length):   
        peo = generator_people.__next__()
        display_info(peo.name, 15, out_name_location, 1)
        out_name_location = out_name_location + 1
    stdscr.getkey()
    curses.endwin()
        



    



