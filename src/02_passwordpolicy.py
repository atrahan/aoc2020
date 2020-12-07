# Task 2 - Find bad passsords

from utilities import read_input

# Explanation
# 1-3 b: qwerty
# needs 1-3 b's but has none -> bad!

def is_password_valid_rng(s, verbose=False):
    if verbose:
        print(f"Processing '{s}'...")
    
    policy, password = [c.strip() for c in s.split(":")]
    rng, val = policy.split(" ")
    ct_min, ct_max = [int(c) for c in rng.split("-")]
    
    if verbose:
        print(f"'{password}' must contain {ct_min} to {ct_max} of '{val}'... ", end="")
    
    val_count = len([c for c in password if c==val])
    is_valid = ct_min <= val_count <= ct_max
    
    if verbose:
        print(f"{is_valid}")
    
    return is_valid

def is_password_valid_pos(s, verbose=False):
    if verbose:
        print(f"Processing '{s}'...")
    
    policy, password = [c.strip() for c in s.split(":")]
    rng, val = policy.split(" ")
    pos1, pos2 = [int(c) for c in rng.split("-")]
    
    if verbose:
        print(f"'{password}' must contain '{val}' at {pos1} or {pos2} of... ", end="")
    
    is_valid = ((password[pos1-1] == val) or (password[pos2-1] == val)) \
       and not ((password[pos1-1] == val) and (password[pos2-1] == val))
    
    if verbose:
        print(f"{is_valid}")
    
    return is_valid

    
if __name__=="__main__":
    # Read entries
    entries = read_input("02_input.txt")
    
    # # Test entries
    # entries = [
    #     "1-3 a: abcde",
    #     "1-3 b: cdefg",
    #     "2-9 c: ccccccccc",
    # ]
    
    # Run password check
    valid_pwds = [is_password_valid_pos(entry, verbose=False) for entry in entries]
    print(sum(valid_pwds))

