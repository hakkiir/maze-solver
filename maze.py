from cell import Cell
import time, random


class Maze():
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

        self._cells = []
        if seed is not None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            column_cells = []
            for j in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1+(i*self._cell_size_x)
        y1 = self._y1+(j*self._cell_size_y)
        x2 = x1+self._cell_size_x
        y2 = y1+self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.025)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited=True
        while True:
            to_visit = []
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append("up")
            if j < self._num_rows-1:
                if not self._cells[i][j+1].visited:
                    to_visit.append("down")
            if i < self._num_cols-1:
                if not self._cells[i+1][j].visited:
                    to_visit.append("right")
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append("left")

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            else:
                dir = random.choice(to_visit)

            if dir == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)
            if dir == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)
            if dir == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            if dir == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
    
    def _reset_cells_visited(self):
        for cols in self._cells:
            for cell in cols:
                cell.visited = False


    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):
        self._animate()

        cur = self._cells[i][j]
        cur.visited = True

        #if 'end' cell return True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        #up
        if (j > 0 
        and not self._cells[i][j-1].visited 
        and not cur.has_top_wall
        ):
            cur.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else: #undo
                cur.draw_move(self._cells[i][j-1], True)
        #down       
        if (j < self._num_rows-1
        and not self._cells[i][j+1].visited 
        and not cur.has_bottom_wall
        ):
            cur.draw_move(self._cells[i][j+1])
            
            if self._solve_r(i, j+1):
                return True
            else: #undo
                cur.draw_move(self._cells[i][j+1], True)
        #right
        if (i < self._num_cols-1
            and not self._cells[i+1][j].visited 
            and not cur.has_right_wall
        ):
            cur.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else: #undo
                cur.draw_move(self._cells[i+1][j], True)
        #left
        if (i > 0 
            and not self._cells[i-1][j].visited 
            and not cur.has_left_wall
        ):
            cur.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else: #undo
                cur.draw_move(self._cells[i-1][j], True)
        return False
        
        