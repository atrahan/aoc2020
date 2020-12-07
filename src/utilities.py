# utilities for AoC 2020
from typing import List
import os

def read_input(fname:str, din:str="../input") -> List[str]:
    fdir = os.path.dirname(__file__)
    din = os.path.abspath(os.path.join(fdir, din))
    with open(os.path.join(din, fname), "r") as  f:
        rows = [l.strip() for l in f.readlines()]
        
    return rows
    
def split_blocks_on_blank_line(entries:List[str], delimiter:str=" ") -> List[str]:
    blocks = []
    buffer = ""
    for entry in entries:
        if len(entry) == 0:
            blocks.append(buffer)
            buffer = ""
        else:
            buffer = delimiter.join((buffer, entry))
            
    if len(buffer) != 0:
        blocks.append(buffer)
        
    return blocks