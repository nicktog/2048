"""
Clone of 2048 game by Nick Togneri
"""

import poc_2048_gui
import random
import math

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line): 
    """ merges and sorts lines or columns """
    counter = 0
    merge_pos = 0
    slid_list = [0] * len(line)
    merged_list = [0] *len(line)
    merged_sorted = [0] *len(line)

    for zilch in line:
        if zilch != 0:
            slid_list[counter] = zilch
            counter +=1
    counter = 0        
    
    for _ in range(len(line)):
        #print slid_list[merge_pos], merge_pos, merged_list
        if len(line) - merge_pos >= 2:
            if slid_list[merge_pos] == slid_list[merge_pos+1]:
                merged_list[merge_pos] = slid_list[merge_pos] * 2

                merge_pos += 2
            else:
                merged_list[merge_pos] = slid_list[merge_pos]
                merge_pos +=1
        elif len(line) - merge_pos <= 0:
            break
        else:
            merged_list[merge_pos] = slid_list[merge_pos]
            
        counter += 1
        
    counter = 0
    
    for zilch2 in merged_list:
        if zilch2 != 0:
            merged_sorted[counter] = zilch2
            counter +=1


    # function that merges a list
    return merged_sorted


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
#        self.height = grid_height
#        self.width = grid_width
#        self.reset
        
        self._height, self._width = grid_height, grid_width                              
        self.reset()
        
        # indices for directions
        self._up_indices = [(0,'' )] * self._width
        self._down_indices = [(self._height -1,'' )] * self._width
        self._left_indices = [('',0)] * self._height
        self._right_indices =  [('',self._width -1 )] * self._height
        
        for _ in range(self._width):
            self._up_indices[_] = (0, _)
            self._down_indices[_] = (self._height-1, _)
        for _ in range(self._height):
            self._left_indices[_] = (_, 0)
            self._right_indices[_] = (_, self._width -1)
            
             
        self._directions = {UP: self._up_indices, 
                           DOWN: self._down_indices, 
                           LEFT: self._left_indices, 
                           RIGHT: self._right_indices,}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0] * self._width for _ in xrange(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        #print str(self.grid)
        self._str_list = []
        for row in range(len(self._grid)):
            self._str_list.append(str(self._grid[row]))
        return str(self._str_list)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        for start_cell in self._directions[direction]:
            temp_list = []
            for step in range(self._height):
                temp_list.append(self.get_tile(start_cell[0] + step * OFFSETS[direction][0], start_cell[1] + step * OFFSETS[direction][1]))
            merged_list = merge(temp_list)
            for step in range(self._width):
                self.set_tile(start_cell[0] + step * OFFSETS[direction][0], start_cell[1] + step * OFFSETS[direction][1], merged_list[step])
        self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        empty_list = []
        counter_1 = 0
        for _ in self._grid:
            counter_2 = 0
            line = _
            for blank in line:
                if blank == 0:
                    blank_tile = (counter_1, counter_2)
                    empty_list.append(blank_tile)
                    counter_2 += 1
                else:
                    counter_2 += 1
            counter_1 += 1
        #print empty_list
        
        self._tile = empty_list[random.randrange(len(empty_list))]
        
        value = [2,2,2,2,2,2,2,2,2,4]
        tile_value = value[random.randint(0,9)]
        
        self.set_tile(self._tile[0], self._tile[1], tile_value)  

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
