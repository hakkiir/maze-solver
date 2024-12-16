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

    def test_maze_create_more_cells(self):
        num_cols = 20
        num_rows = 50
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_even_more_cells(self):
        num_cols = 70
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_even_more_cells_bigger_cells(self):
        num_cols = 70
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 70
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_maze_break_entrance_and_exit_reverse(self):
        num_cols = 70
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertNotEqual(
            m1._cells[0][0].has_top_wall,
            True,
        )
        self.assertNotEqual(
            m1._cells[-1][-1].has_bottom_wall,
            True,
        )

    def test_maze_break_entrance_and_exit_reverse2(self):
        num_cols = 70
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            m1._cells[0][0].has_bottom_wall,
            True,
        )
        self.assertEqual(
            m1._cells[-1][-1].has_top_wall,
            True,
        )
if __name__ == "__main__":
    unittest.main()
