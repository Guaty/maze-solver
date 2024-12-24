from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_bottom_wall = False
    c1.draw(225, 225, 250, 250)

    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(300, 300, 500, 500)

    c1.draw_move(c2)

    win.wait_for_close()


main()
