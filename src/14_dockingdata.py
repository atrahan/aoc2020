# Task 14: Docking Data

from utilities import read_input
import re

def process_mask(s, size=36):
    """ Read mask and get non-x values """
    s = s.split("=")[-1].strip()
    return [
        (size-ix-1, int(c))
        for ix, c in enumerate(s)
        if c.isnumeric()
    ]
    
def set_bit(value, bit_index):
    """ Set bit to 1 """
    return value | (1 << bit_index)
    
def clear_bit(value, bit_index):
    """ Set bit to 0 """
     return value & ~(1 << bit_index)

def apply_value_mask(value, mask):
    """ Read position/overwrite pairs and set bits accordingly"""
    set_mapping = {0: clear_bit, 1:set_bit}
    for position, mode in mask:
        value = set_mapping[mode](value, position)
    return value

def update_memory_address(s, mem, mask):
    """ Update memory at a specific address with a value masked with the mask set """
    address, value = re.search("mem\[(\d*)\] = (\d*)", s).groups()
    address = int(address)
    value = int(value)
    
    # print(f"setting {address} to masked {value}", end="")
    value = apply_value_mask(value, mask)
    # print(f", masked to {value}")
    
    mem[address] = int(value)
    
    
def run_masked_address_update(s,mem,mask):
    """ Update memory at all possible addresses (based on floating mask) with value """
    main_address, value = re.search("mem\[(\d*)\] = (\d*)", s).groups()
    main_address = int(main_address)
    value = int(value)
    
    float_locs = []
    for pos, mode in enumerate(mask):
        if mode == "0":
            pass
        elif mode == "1":
            main_address = set_bit(main_address, (35-pos))
        else:
            float_locs.append(pos)
    
    # print(float_locs)        
    addresses = []    
    for settings in range(2**len(float_locs)):
        settings_str = bin(settings)[2:]
        settings_str = "0"*(len(float_locs) - len(settings_str)) + settings_str
        address = main_address
        # print(f"    {settings_str}")
        for float_loc, setting in zip(float_locs, settings_str):
            address = apply_value_mask(address, ((35-float_loc, int(setting)),))
        addresses.append(address)
    
    # print(s)
    for adr in addresses:
        # print(f"    {bin(adr)}")
        mem[adr] = value
    

if __name__ == "__main__":
    
    # Test data or real data
    # entries = read_input("14_test_input.txt")
    # entries = read_input("14_test_input_2.txt")
    entries = read_input("14_input.txt")
    
    # Value mask
    mem = {}
    mask = None
    for entry in entries:
        if entry.startswith("mask"):
            mask = process_mask(entry)
        else:
            update_memory_address(entry, mem, mask)
            
    print(f"Value Mask, Sum of values: {sum(mem.values())}")
    
    # Address mask
    mem = {}
    mask = None
    for entry in entries:
        if entry.startswith("mask"):
            mask = entry.split("=")[-1].strip()
        else:
            run_masked_address_update(entry, mem, mask)
            
    print(f"Address Mask, Sum of values: {sum(mem.values())}")
    
        
    
    