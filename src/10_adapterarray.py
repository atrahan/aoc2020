# Task 10: Adapter Array

from utilities import read_input

def get_adapter_diff_counts(entries):
    diffs = [x2-x1 for x1, x2 in zip(entries[:-1], entries[1:])]
    
    diff_counts = dict(
        zip(
            set(diffs),
            [diffs.count(val) for val in set(diffs)],
        )
    )
    return diff_counts
            
def count_combinations(entries):
    paths = {}
    valid_steps = (1,2,3)
            
    for e in sorted(entries, reverse=True):
        if e == max(entries):
            paths[e] = 1
        else:
            paths[e] = sum([
                paths[e+step]
                for step in valid_steps
                if e+step in paths.keys()
            ])
    
    return paths[0]

"""
# Brute force approach. O(...lots...)
def count_combinations_by_force(entries, cur_val):
    valid_steps = (1,2,3)
    
    if cur_val == max(entries):
        return 1
    else:
        options = [e for e in entries if e-cur_val in valid_steps]
        if len(options) == 0:
            return 0
        else:
            return sum([count_combinations(entries, opt) for opt in options])
            

# First pass. Record each path. Not necessary. Abandoned before complete.
def get_combinations(entries, path, valid_paths):
    
    # print(f"path: {path}")
    cur_val = path[-1]
    valid_steps = (1,2,3)
    
    if cur_val == max(entries):
        valid_paths.append(path)
    else:
        options = [e for e in entries if e-cur_val in valid_steps]
        # print(f"options: {options}")
        if len(options)==0:
            pass
        else:
            for next_step in options:
                new_path = path.copy()
                new_path.append(next_step)
                valid_paths.append(get_combinations(entries, new_path, valid_paths))
    
    return valid_paths
"""    

if __name__=="__main__":
    
    # Test data or real data
    # entries = read_input("10_test_input_1.txt")
    # entries = read_input("10_test_input_2.txt")
    entries = read_input("10_input.txt")
    entries = [int(e) for e in entries]
    entries += [0, max(entries)+3] # Append start (0) and device adapter (+3)
    entries = sorted(entries)
    
    
    # Difference counts for all adapters
    diff_counts =  get_adapter_diff_counts(entries)
    print("Adapter difference counts:")
    for k,v in diff_counts.items():
        print(f"    {k}: {v}")
    print(f"Product of 1- and 3-jolt counts: {diff_counts[1]*diff_counts[3]}")
    
    # Number of valid combinations
    # combo_count = count_combinations_by_force(entries, 0)
    combo_count = count_combinations(entries)
    print(f"Number of combinations: {combo_count}")
    