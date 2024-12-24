from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    l = Line(Point(3, 250), Point(526, 480))
    l2 = Line(Point(367, 400), Point(400, 300))
    win.draw_line(l, "blue")
    win.draw_line(l2)
    win.wait_for_close()


main()
