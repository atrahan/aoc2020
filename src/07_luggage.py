# Task 7: Luggage

from utilities import read_input
from typing import List

"""
OOP is more complex than needed.
This could have been done more simply with a nested dict.
"""

class Bag():
    def __init__(self, rule_string:str):
        bag_str, contents_str = [s.strip() for s in rule_string.split("contain")]
        self.color = bag_str.replace("bags", "").strip()
        self.contents = self.get_bag_contents(contents_str)
    
    def get_bag_contents(self, contents_str:str) -> dict:
        contents = {}
        if "no other bags" in contents_str:
            pass
        else:
            bag_strs = [s.strip().replace(".", "") for s in contents_str.split(",")]
            for bag_str in bag_strs:
                bag_color = " ".join(bag_str.split()[1:-1])
                bag_count = int(bag_str.split()[0])
                contents.update({bag_color: bag_count})
                
        return contents
    
    def colors_contained(self):
        return list(self.contents.keys())
        
    def __repr__(self):
        s = self.color
        if len(self.contents) > 0:
            s += "\n"
        s += "\n".join([f"    {k} ({v})" for k,v in self.contents.items()])
        return s
        
        
def search_for_color(bags:dict, start_bag:Bag, search_color:str) -> bool:
    colors_contained = start_bag.colors_contained()
    if len(colors_contained) == 0:
        return False
    elif search_color in colors_contained:
        return True
    else:
        return any([
            search_for_color(bags=bags, start_bag=bags[c], search_color=search_color)
            for c in colors_contained
        ])

def get_total_bag_count(bags:dict, start_bag:Bag) -> bool:
    colors_contained = start_bag.colors_contained()
    bag_count = 1
    if len(colors_contained) == 0:
        return bag_count
    else:
        for color, count in start_bag.contents.items():
            bag_count += count * get_total_bag_count(bags=bags, start_bag=bags[color])
        # return 1 + sum([
        #     get_total_bag_count(bags=bags, start_bag=bags[c])
        #     for c in colors_contained
        # ])
        return bag_count

if __name__=="__main__":
    
    # entries = read_input("07_test_input.txt")
    entries = read_input("07_input.txt")
    
    bags = [Bag(entry) for entry in entries]
    bags = dict([(b.color,b) for b in bags])
    
    contains_shiny_gold = [search_for_color(bags=bags, start_bag=bag, search_color='shiny gold') for bag in bags.values()]
    print(f"Total containing shiny gold: {sum(contains_shiny_gold)}")
    
    count_in_gold = get_total_bag_count(bags=bags, start_bag=bags["shiny gold"]) - 1
    print(f"Total count in shiny gold: {count_in_gold}")
    
    # # Testing
    # for bag in bags.values():
        # print(bag)
        # print(f"Contains shiny gold: {search_for_color(bags=bags, start_bag=bag, search_color='shiny gold')}")
        # print()
