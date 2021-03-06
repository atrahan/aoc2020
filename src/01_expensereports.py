# Task 1 - Find bad expense reports

from utilities import read_input

target = 2020

entries = [int(s) for s in read_input("01_input.txt")]

# Pair sums to target
diffs = [target-x for x in entries]
for i, x in enumerate(diffs):
    if x in entries:
        print(f"{entries[i]} + {x} = {entries[i]+x}")
        print(f"{entries[i]} x {x} = {entries[i]*x}")
        
# Triple sums to target
for i in entries:
    for j in entries:
        for k in entries:
            if i+j+k == target:
                print(f"{i} + {j} + {k} = {i+j+k}")
                print(f"{i} x {j} x {k} = {i*j*k}")
                break