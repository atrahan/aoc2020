# Day 3: Toboggan Trees

from utilities import read_input

def get_row_value(row, row_num, horiz_step):
    return row[row_num*horiz_step%len(row)]

def get_tree_count(rows, horiz_step, vert_step):
    tree_count = 0
    for row_num, row in enumerate(rows[0::vert_step]):
        if get_row_value(row, row_num, horiz_step) == "#":
            tree_count+=1
    return tree_count
    
if __name__=="__main__":
    # Read entries
    rows = read_input("03_input.txt")
        
    # # Test entries
    # rows = [
    #     "..##.......",
    #     "#...#...#..",
    #     ".#....#..#.",
    #     "..#.#...#.#",
    #     ".#...##..#.",
    #     "..#.##.....",
    #     ".#.#.#....#",
    #     ".#........#",
    #     "#.##...#...",
    #     "#...##....#",
    #     ".#..#...#.#",
    # ]
    
    # Run tree check
    result = 1
    for horiz_step, vert_step in zip(
        (1,3,5,7,1),
        (1,1,1,1,2),
    ):
        tree_count = get_tree_count(rows, horiz_step, vert_step)
        result *= tree_count
        print(f"Horiz: {horiz_step}; Vert: {vert_step}; Trees: {tree_count}")
    
    print(f"Product: {result}")
    
    ##-- From part 1
    # vert_step = 1
    # horiz_step = 3
    # width = len(rows[0])
    # entries = [get_row_value(row, row_num, horiz_step) for row_num, row in enumerate(rows)]
    # trees = [1 for c in entries if c=="#"]
