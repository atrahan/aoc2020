# # Task 5: Seat assignment

from utilities import read_input
from typing import List

def test_data():
    return (
        "FBFBBFFRLR",
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    )

def str_to_binary(s:str, val0:str, val1:str) -> str:
    lookup = {val0:'0', val1:'1'}
    return "".join([lookup[ix] for ix in s])

def get_row_number(seat_str):
    row_num = int(
        str_to_binary(s=seat_str[:7], val0='F', val1='B'), 2
        )
    return row_num

def get_seat_number(seat_str):
    seat_num = int(
        str_to_binary(s=seat_str[-3:], val0='L', val1='R'), 2
        )
    return seat_num
    
def get_seat_id(seat_str):
    row_num = get_row_number(seat_str)
    seat_num = get_seat_number(seat_str)
    seat_id = row_num * 8 + seat_num
    return seat_id

if __name__=="__main__":
    
    # entries = test_data()
    entries = read_input("05_input.txt")
    
    seat_ids = [get_seat_id(entry) for entry in entries]
    print(f"Max seat ID: {max(seat_ids)}")
    
    seat_ids = sorted(seat_ids)
    issue_sids = []
    for ix, sid in enumerate(seat_ids[1:-1]):
        if (sid - seat_ids[ix])==1 and (seat_ids[ix+2] - sid)==1:
            continue
        else:
            issue_sids.append(sid)
            print(f"Gap found: {sid}")
    print(f"Your seat: {sum(issue_sids)/len(issue_sids):.0f}")
    
    
    # # Testing
    # rows = [get_row_number(entry) for entry in entries]
    # seats = [get_seat_number(entry) for entry in entries]
    
    # plines = len(entries)
    # for i in range(plines):
    #     print(entries[i])
    
    # for i in range(plines):
    #     print(rows[i])
        
    # for i in range(plines):
    #     print(seats[i])
        
    # for i in range(plines):
    #     print(seat_ids[i])