# Task 12: Rain Risk

from utilities import read_input
from math import sin, cos, radians, atan2

def apply_command(cmd, position, direction):
    """ Use command to move the ship directly """
    # Split action and value
    action, value = cmd[0], int(cmd[1:])
    
    # Apply action to position and direction
    if action == "E":
        position[0] += value
    elif action == "N":
        position[1] += value
    elif action == "W":
        position[0] -= value
    elif action == "S":
        position[1] -= value
    elif action == "F":
        position[0] += round(cos(radians(direction)) * value, 0)
        position[1] += round(sin(radians(direction)) * value, 0)
    elif action == "L":
        direction += value
    elif action == "R":
        direction -= value
    else:
        raise ValueError(f"Command '{cmd}' contains an unknown action '{action}'")

    # Clean up direction if it crosses 0
    while direction < 0:
        direction += 360
    direction = direction % 360

    return position, direction

def apply_waypoint_command(cmd, ship_position, waypoint_position):
    """ Use command to move the waypoint or the ship based on the waypoint """
    
    # Split action and value
    action, value = cmd[0], int(cmd[1:])
    
    # Apply action to position and direction
    if action == "E":
        waypoint_position[0] += value
    elif action == "N":
        waypoint_position[1] += value
    elif action == "W":
        waypoint_position[0] -= value
    elif action == "S":
        waypoint_position[1] -= value
    elif action == "F":
        ship_position[0] += value*waypoint_position[0]
        ship_position[1] += value*waypoint_position[1]
    elif action == "L":
        r = (waypoint_position[0]**2 + waypoint_position[1]**2)**0.5
        direction = atan2(waypoint_position[1], waypoint_position[0]) + radians(value)
        waypoint_position[0] = round(r*cos(direction), 0)
        waypoint_position[1] = round(r*sin(direction), 0)
    elif action == "R":
        r = (waypoint_position[0]**2 + waypoint_position[1]**2)**0.5
        direction = atan2(waypoint_position[1], waypoint_position[0]) - radians(value)
        waypoint_position[0] = round(r*cos(direction), 0)
        waypoint_position[1] = round(r*sin(direction), 0)
    else:
        raise ValueError(f"Command '{cmd}' contains an unknown action '{action}'")

    return ship_position, waypoint_position

def manhattan_dist(position):
    """ Compute manhattan distance for a point """
    return sum([abs(x) for x in position])
    
if __name__ == "__main__":
    # Test data or real data
    # entries = read_input("12_test_input.txt")
    entries = read_input("12_input.txt")
    
    # Ship navigation
    position = [0, 0]
    direction = 0
    
    for cmd in entries:
        # print(f"p: {position}  d: {direction}, applying {cmd}...")
        position, direction = apply_command(cmd, position, direction)
    
    print(f"Final p: {position}  d: {direction}")
    print(f"Final Manhattan Dist: {manhattan_dist(position)}")
    
    
    # Waypoint navigation
    ship_position = [0, 0]
    waypoint_position = [10,1]
    
    for cmd in entries:
        # print(f"ship: {ship_position}  waypoint: {waypoint_position}, applying {cmd}...")
        ship_position, waypoint_position = apply_waypoint_command(cmd, ship_position, waypoint_position)
    
    print(f"Final ship: {ship_position}  waypoint: {waypoint_position}")
    print(f"Final Manhattan Dist: {manhattan_dist(ship_position)}")
