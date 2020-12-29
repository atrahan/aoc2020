# Task 16: Ticket Translation

from utilities import read_input, split_blocks_on_blank_line
from copy import deepcopy
import re

def separate_entry_blocks(entries):
    """ Break up the pieces of the input file """
    notes, my_ticket, other_tickets = [
        blk.split("|")
        for blk in split_blocks_on_blank_line(entries, delimiter="|")
    ]
    notes = notes[1:]
    my_ticket = my_ticket[2:]
    other_tickets = other_tickets[2:]
    
    return notes, my_ticket, other_tickets

def notes_to_rules(notes):
    """ Convert a note string to a rule dict """
    rules = {}
    for note in notes:
        # print(note)
        fld, l1, h1, l2, h2 = re.search("(.*): (\d*)-(\d*) or (\d*)-(\d*)", note).groups()
        rules[fld] = {"l1":int(l1),"h1":int(h1),"l2":int(l2),"h2":int(h2),}
        # list(range(int(l1),int(h1)+1)) + list(range(int(l2),int(h2)+1))
    return rules

def check_valid(rule, value):
    """ Check if a value meets the rule dict """
    return (rule["l1"] <= value <= rule["h1"]) or (rule["l2"] <= value <= rule["h2"])

def get_invalid_entries(tickets, rules):
    """ Find invalid entries and ticket indexes in a set of tickets """
    invalid_entries = []
    invalid_tickets = []
    for ix, ticket in enumerate(tickets):
        for value in [int(e) for e in ticket.split(',')]:
            is_valid = any([check_valid(rule, value) for rule in rules.values()])
            if not is_valid:
                invalid_entries.append(value)
                invalid_tickets.append(ix)
    return invalid_entries, set(invalid_tickets)

def pivot_ticket_values(tickets):
    """ Pivot so all values for a given rule are in sub-lists """
    vals = [[int(v) for v in ticket.split(",")] for ticket in tickets]
    return list(zip(*vals))

def rules_and_values_to_matrix(rules, value_lists):
    """ Create a binary matrix based on valid entries for each rule (rules x tickets)"""
    mat = []
    for rule in rules.values():
        row = []
        for cat_vals in value_lists:
            row.append(int(
                all([check_valid(rule, val) for val in cat_vals])
                ))
        mat.append(row)
    return mat

def get_rule_position_pairs(mat):
    """ Reduce the (rule x tickets) validity matrix to get the set of rule/position pairs """
    mat = deepcopy(mat)
    counts = [sum(row) for row in mat]
    pairs = []
    while len(pairs) < len(mat):
        for row_ix, row in enumerate(mat):
            if sum(row) == 1:
                rule_index = row_ix
                pos_index = row.index(1)
                pairs.append((rule_index, pos_index))
                for r in mat:
                    r[pos_index] = 0
    return pairs
        

if __name__ == "__main__":
    
    # Test data or real data
    # entries = read_input("16_test_input.txt")
    # entries = read_input("16_test_input_2.txt")
    entries = read_input("16_input.txt")
    notes, my_ticket, other_tickets = separate_entry_blocks(entries)
    
    # Process notes into rule values
    rules = notes_to_rules(notes)
    
    # Find invalid entries in other tickets
    invalid_entries, invalid_tickets = get_invalid_entries(other_tickets, rules)
    
    # Part 1: sum of invalid entries
    print(f"Invalid entry score: {sum(invalid_entries)}")
    
    # Valid tickets
    valid_tickets = my_ticket + [other_tickets[i] for i in range(len(other_tickets)) if i not in invalid_tickets]
    cat_vals = pivot_ticket_values(valid_tickets)
    
    # Get matrix and solve
    mat = rules_and_values_to_matrix(rules, cat_vals)
    # for row in mat:
    #     print(sum(row))
    # for row in mat:
    #     print(row)
    pairs = get_rule_position_pairs(mat)
    
    # Link field names to my ticket values
    fields = list(rules.keys())
    values = [int(e) for e in my_ticket[0].split(",")]
    my_ticket_fields = {}
    for p in pairs:
        my_ticket_fields[fields[p[0]]] = values[p[1]]
    # print(my_ticket_fields)
    
    # Find departure entries and multiply together
    prod = 1
    for k, v in my_ticket_fields.items():
        if "departure" in k:
            prod *= v
    print(f"Product of departure fields on my ticket: {prod}")
    