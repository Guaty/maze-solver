from cell import Cell
import time
import random


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._cells = self._create_cells()

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)

        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        return [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            #list cells to visit. remember: i = columns = horizontal, j = rows = vertical
            #check left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #check right
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            #check up
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            #check down
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            
            #if nowhere to go, break out; we're done
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            #pick a direction, then set a destination
            next_direction = random.randrange(len(to_visit))
            next_destination = to_visit[next_direction]

            #break some walls. remember rules above
            #left
            if next_destination[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            #right
            if next_destination[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            #up
            if next_destination[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            #down
            if next_destination[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            #move to the next cell
            self._break_walls_r(next_destination[0], next_destination[1])

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self._x1 + (i * self._cell_size_x)
        cell_y1 = self._y1 + (j * self._cell_size_y)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _reset_cells_visited(self):
        for cell_col in self._cells:
            for cell in cell_col:
                cell.visited = False
