import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    
    def test_maze_generation(self):
        maze1 = Maze(10, 10, 5, 5, 2, 2, seed=42)
        maze2 = Maze(10, 10, 5, 5, 2, 2, seed=42)
        
        for i in range(maze1._num_cols):
            for j in range(maze1._num_rows):
                cell1 = maze1._cells[i][j]
                cell2 = maze2._cells[i][j]
                
                assert cell1.visited == cell2.visited
                assert cell1.has_left_wall == cell2.has_left_wall
                assert cell1.has_right_wall == cell2.has_right_wall
                assert cell1.has_top_wall == cell2.has_top_wall
                assert cell1.has_bottom_wall == cell2.has_bottom_wall

    def test_valid_maze_cells(self):
        maze = Maze(0,0, 12, 10, 5, 5, seed=42)
        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                cell = maze._cells[i][j]

                one_wall_present = (
                    cell.has_bottom_wall or
                    cell.has_left_wall or
                    cell.has_right_wall or
                    cell.has_top_wall
                )

                all_walls_present = (
                    cell.has_bottom_wall and
                    cell.has_left_wall and
                    cell.has_right_wall and
                    cell.has_top_wall
                )

                self.assertTrue(one_wall_present, f"Cell at {i},{j} has no walls!")
                self.assertFalse(all_walls_present, f"Cell at {i},{j} is completely surrounded!")

    def test_adjacent_cell_walls_match(self):
        maze = Maze(0,0, 12, 10, 5, 5, seed=42)
        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                cell = maze._cells[i][j]

                if i > 0:
                    left_cell = maze._cells[i-1][j]
                    self.assertEqual(cell.has_left_wall, left_cell.has_right_wall)

                if i < maze._num_cols - 1:
                    right_cell = maze._cells[i+1][j]
                    self.assertEqual(cell.has_right_wall, right_cell.has_left_wall)

                if j > 0:
                    top_cell = maze._cells[i][j-1]
                    self.assertEqual(cell.has_top_wall, top_cell.has_bottom_wall)

                if j < maze._num_rows - 1:
                    bottom_cell = maze._cells[i][j+1]
                    self.assertEqual(cell.has_bottom_wall, bottom_cell.has_top_wall)
    

if __name__ == "__main__":
    unittest.main()
