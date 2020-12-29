# Task 15: Rambunctious Recitation

def get_next_value(values):
    """ Initial value search; slow """
    prev_val = values[-1]
    if prev_val not in values[:-1]:
        cur_val = 0
    else:
        # idxs = find_all_idx(values, prev_val)
        # cur_val = idxs[-1]-idxs[-2]
        idx_back_two = values[-2::-1].index(prev_val)
        cur_val = idx_back_two + 1
    return cur_val

def find_all_idx(vals, target):
    """ Helper for initial value search; slow """
    return [i for i, x in enumerate(vals) if x==target]

def initialize_value_dict(entries):
    """ Build recent entries lookup dict from initial numbers """
    val_dict = {}
    for i,x in enumerate(entries):
        val_dict[x] = [i+1]
    return val_dict

def update_value_dict(val_dict, prev_val, cur_idx):
    """ Update recent entries lookup dict """
    if len(val_dict[prev_val]) == 1:
        cur_val = 0
    else:
        cur_val = cur_idx - 1 - val_dict[prev_val][-2]
        
    if cur_val in val_dict.keys():
        val_dict[cur_val] = [val_dict[cur_val][-1], cur_idx]
    else:
        val_dict[cur_val] = [cur_idx]
    
    return cur_val
        
if __name__ == "__main__":
    
    # Test data or real data
    # entry_lists = [
    #     [0,3,6],
    #     [1,3,2],
    #     [2,1,3],
    #     [1,2,3],
    #     [2,3,1],
    #     [3,2,1],
    #     [3,1,2],
    # ]
    entry_lists = [[7,12,1,0,16,2]]

    # For each test (or real) entry, find num_iter'th entry
    num_iter = 30000000
    for entries in entry_lists:
        
        # # Intiial value search; slow
        # values = entries.copy()
        # while len(values) < num_iter:
        #     values.append(get_next_value(values))
        # print(f"The {num_iter}th value is: {values[-1]}")
        
        # Value search with recent entries dict
        val_dict = initialize_value_dict(entries)
        prev_val = entries[-1]
        for cur_idx in range(len(entries)+1, num_iter+1):
            prev_val = update_value_dict(val_dict, prev_val, cur_idx)
            # print(val_dict)
        print(f"The {num_iter}th value is: {prev_val}")
        