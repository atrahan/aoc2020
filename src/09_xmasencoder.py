# Task 9: XMAS Encoder

from utilities import read_input
from typing import List

def is_sum_from_group(value, group):
    group = [x for x in group if x<=value]
    for i, x1 in enumerate(group):
        test = [x2+x1 for x2 in group]
        test[i] = None
        if value in test:
            return True
    return False

def find_invalid_entry(entries:List[int], preamble:int=25) -> int:
    for i in range(preamble, len(entries)):
        is_valid = is_sum_from_group(
            group=entries[i-preamble:i],
            value=entries[i],
        )
        if not is_valid:
            invalid_entry = entries[i]
            print(f"Invalid entry {entries[i]} found at position {i}")
            break
    
    return invalid_entry

def find_contiguous_sums_to_value(entries:List[int], value:int) -> List[int]:
    
    for start_ix, start_entry in enumerate(entries):
        contig_entries = [start_entry]
        
        for entry in entries[start_ix+1:]:
            contig_entries.append(entry)
            if sum(contig_entries) == value:
                print(f"Found {len(contig_entries)} contiguous entries summing to {value}.")
                return contig_entries
            elif sum(contig_entries) > value:
                break
            
    if sum(contig_entries) != value:
        print(f"No contiguous entries summing to {value} found.")
        return []
    return []

if __name__=="__main__":
    
    # Test data or real data
    # entries = read_input("09_test_input.txt")
    # preamble = 5
    entries = read_input("09_input.txt")
    preamble = 25
    
    # Cast to int
    entries = [int(x) for x in entries]
    
    # Find invalid entry
    invalid_entry = find_invalid_entry(entries, preamble)
    
    # Find contiguous numbers summing to invalid entry
    contig_entries = find_contiguous_sums_to_value(entries, invalid_entry)
    print(f"\nContiguous Entries: {contig_entries}")
    print(f"Sum of smallest and largest: {min(contig_entries)+max(contig_entries)}")

    