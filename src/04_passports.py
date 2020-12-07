# Day 4: Passport processing

from utilities import read_input, split_blocks_on_blank_line
from typing import List
from string import hexdigits

def test_data():
    return (
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    )

def passport_str_to_dict(passport:str) -> dict:
    elems = passport.split()
    kvs = [elem.split(":") for elem in elems]
    pspt_dict = dict(kvs)
    return pspt_dict


def passport_is_valid(passport:dict, reqd_keys:List[str]=None) -> bool:
    if reqd_keys is None:
        reqd_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # "cid"
    
    pspt_keys = passport.keys()
    
    if len(pspt_keys) < len(reqd_keys):
        return False
    
    for rk in reqd_keys:
        if rk not in pspt_keys:
            return False
    
    return all([field_is_valid(k,v) for k,v in passport.items()])


def field_is_valid(key:str, val:str) -> bool:
    if key=="byr":
        is_valid = 1920 <= int(val) <= 2002
    elif key=="iyr":
        is_valid = 2010 <= int(val) <= 2020
    elif key=="eyr":
        is_valid = 2020 <= int(val) <= 2030
    elif key=="hgt":
        if len(val)<3:
            is_valid = False
        elif val[-2:] == "cm":
            is_valid = 150 <= int(val[:-2]) <= 193
        elif val[-2:] == "in":
            is_valid = 59 <= int(val[:-2]) <= 76
        else:
            is_valid = False
    elif key=="hcl":
        if val[0] != "#":
            is_valid = False
        else:
            is_valid = all([c in hexdigits for c in val[1:]])
    elif key=="ecl":
        is_valid = val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key=="pid":
        is_valid = (len(val)==9) and (val.isdigit())
    elif key=="cid":
        is_valid = True
    else:
        raise ValueError(f"Key '{key}' not recognized")
    
    if not is_valid:
        print(f"Invalid:  '{key}': '{val}'")
    return is_valid


if __name__=="__main__":
    
    # entries = test_data()
    # entries = read_input("04_invalid_passports.txt")
    entries = read_input("04_input.txt")
    
    passports = [passport_str_to_dict(p) for p in split_blocks_on_blank_line(entries)]
    valid = [passport_is_valid(passport) for passport in passports]
    
    print(f"Passports read: {len(valid)}\nValid Passports: {sum(valid)}")
    
    # # Testing
    # plines = len(passports)
    # for i in range(plines):
    #     print(entries[i])
        
    # # for i in range(plines):
    # #     print(passport_strs[i])
        
    # for i in range(plines):
    #     print(passports[i])
        
    # for i in range(plines):
    #     print(valid[i])