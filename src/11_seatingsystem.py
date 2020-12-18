# Task 11: Seating System

from utilities import read_input
from copy import deepcopy

def init_grid_to_int(entries):
    """ Grid from char to int """
    mapping = {".":0, "L":-1, "#":1}
    grid = [
        [mapping[c] for c in row]
        for row in entries
    ]
    return grid
    
def get_adjacent_pairs(grid, r, c, rng=1):
    """ Find positions considered adjacent to the current position """
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    
    pairs = []
    
    direcs = zip(
        (-1,-1,-1, 0,0, 1,1,1),
        (-1, 0, 1,-1,1,-1,0,1)
    )
    for direc in direcs:
        i = 1
        while i <= rng:
            chk_pos = (r+direc[0]*i, c+direc[1]*i)
            if (chk_pos[0] < 0) or (chk_pos[0] >= grid_rows) \
                or (chk_pos[1] < 0) or (chk_pos[1] >= grid_columns):
                break
            elif grid[chk_pos[0]][chk_pos[1]] != 0:
                pairs.append(chk_pos)
                break
            else:
                i+=1
                continue
     
    return pairs

def gen_adjacency_array(grid, adj_rng):
    """ Collect adjacent positions for each grid position """
    adj_array = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            pairs = get_adjacent_pairs(grid, r, c, rng=adj_rng)
            adj_array[r][c] = pairs
    return adj_array
    
def get_next_state(grid, adj_array, item_r, item_c, occupancy_limit=4):
    """ Get next state for a single position """
    cur_state = grid[item_r][item_c]
    if cur_state == 0:
        return cur_state
    
    pairs = adj_array[item_r][item_c]
    all_empty = all([grid[r][c]<=0 for r,c in pairs])
    num_occupied = sum([grid[r][c]==1 for r,c in pairs])
    
    if cur_state == -1 and all_empty:
        return 1
    elif cur_state == 1 and num_occupied>=occupancy_limit:
        return -1
    else:
        return cur_state

def apply_step(grid, adj_array, occupancy_limit):
    """ Apply timestep to grid """
    next_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            next_grid[r][c] = get_next_state(grid, adj_array, r, c, occupancy_limit)
    return next_grid

def grids_equal(g1, g2):
    """ Compare grid elementwise """
    for r1, r2 in zip(g1, g2):
        for e1, e2 in zip(r1, r2):
            if e1!=e2:
                return False
    return True

def find_stable_grid(grid, adj_array, occupancy_limit):
    """ Apply timesteps until grid is stable """
    g_prev = grid
    grid = apply_step(grid, adj_array, occupancy_limit)
    while not grids_equal(grid, g_prev):
        g_prev = grid
        grid = apply_step(grid, adj_array, occupancy_limit)
    return grid

def count_occupied_seats(grid):
    """ Count occupied seats in grid """
    return sum([sum([e>0 for e in row]) for row in grid])

if __name__=="__main__":
    
    # Test data or real data
    # entries = read_input("11_test_input.txt")
    entries = read_input("11_input.txt")
    grid = init_grid_to_int(entries)
    
    adj_array = gen_adjacency_array(grid, adj_rng=1)
    stable_grid = find_stable_grid(grid, adj_array, occupancy_limit=4)
    print(f"Directly adjacent rule, Occupied seats when stable: {count_occupied_seats(stable_grid)}")
    
    adj_array = gen_adjacency_array(grid, adj_rng=1000)
    stable_grid = find_stable_grid(grid, adj_array, occupancy_limit=5)
    print(f"Line of sight rule, Occupied seats when stable: {count_occupied_seats(stable_grid)}")
    