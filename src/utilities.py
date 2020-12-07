# utilities for AoC 2020
from typing import List
import os

def read_input(fname:str, din:str="../input") -> List[str]:
    fdir = os.path.dirname(__file__)
    din = os.path.abspath(os.path.join(fdir, din))
    with open(os.path.join(din, fname), "r") as  f:
        rows = [l.strip() for l in f.readlines()]
        
    return rows
    