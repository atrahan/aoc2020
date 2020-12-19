# Task 13: Shuttle Search

from utilities import read_input

def get_bus_wait(start, bus_id):
    return bus_id - (start%bus_id)

def get_min_bus_wait(start, bus_ids):
    waits = [get_bus_wait(start, bus_id) for bus_id in bus_ids]
    min_wait = min(waits)
    min_wait_bus_id = bus_ids[waits.index(min_wait)]
    
    return min_wait_bus_id, min_wait

def get_start_pos(entries):
     start_pos, bus_id = zip(*[
         (i, int(e))
         for i, e in enumerate(entries)
         if e.isnumeric()
     ])
     return list(start_pos), list(bus_id)

def get_bus_series(bus_ids, start_pos):
    cur_pos = list(start_pos)
    for i in range(len(bus_ids)):
        step = product(bus_ids[:i])
        bus_id = bus_ids[i]
        print(f"Fitting {bus_id}, step {step}...")
        
        while cur_pos[i]%bus_id != 0:
            cur_pos = [p+step for p in cur_pos]
        print(f"    {cur_pos}")
    print(f"Done:  {cur_pos}")
    
    return cur_pos
    
def product(l):
    r = 1
    for x in l:
        r*=x
    return r

if __name__ == "__main__":
    
    # Test data or real data
    # entries = read_input("13_test_input.txt")
    entries = read_input("13_input.txt")
    
    start = int(entries[0])
    entries = entries[1].split(',')
    start_pos, bus_ids = get_start_pos(entries)
    
    # Find earliest bus
    min_wait_bus_id, min_wait = get_min_bus_wait(start, bus_ids)
    print(f"Min wait: {min_wait} min for bus {min_wait_bus_id}.  Product: {min_wait*min_wait_bus_id}\n")
    
    # Find bus sequences
    print (f"Bus IDs: {bus_ids}")
    print (f"Offsets: {start_pos}")
    cur_pos = get_bus_series(bus_ids, start_pos)
    print(f"\nStart for series: {cur_pos[0]}\n")
    