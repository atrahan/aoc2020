# # Task 6: Customs

from utilities import read_input, split_blocks_on_blank_line
from typing import List

def get_set_union(block):
    return set(block.replace(" ", ""))
    
def get_set_intersection(block):
    sets = [set(ele) for ele in block.split()]
    isect = set.intersection(*sets)
    return isect
    

if __name__=="__main__":
    
    # entries = read_input("06_test_input.txt")
    entries = read_input("06_input.txt")
    
    blocks = split_blocks_on_blank_line(entries=entries, delimiter=" ")
    
    union_lens = [len(get_set_union(block)) for block in blocks]
    isect_lens = [len(get_set_intersection(block)) for block in blocks]
    print(f"Total union set lengths: {sum(union_lens)}")
    print(f"Total intersection set lengths: {sum(isect_lens)}")
    