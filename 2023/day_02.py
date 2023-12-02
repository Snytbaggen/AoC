from utils import *

red = 12
green = 13
blue = 14

valid_rounds_count = 0
total_power_count = 0

for index, game in enumerate(splitFile("day_02_input.txt", "\n")):
    rounds = game.split(": ")[1]
    game_is_impossible = False
    red_min = 0
    green_min = 0
    blue_min = 0
    for round in rounds.split("; "):
        for color in round.split(", "):
            color_pair = color.split(" ")
            if color_pair[1] == "red":
                if not game_is_impossible:
                    game_is_impossible = int(color_pair[0]) > red
                red_min = max(red_min, int(color_pair[0]))
            elif color_pair[1] == "green":
                if not game_is_impossible:
                    game_is_impossible = int(color_pair[0]) > green
                green_min = max(green_min, int(color_pair[0]))
            elif color_pair[1] == "blue":
                if not game_is_impossible:
                    game_is_impossible = int(color_pair[0]) > blue
                blue_min = max(blue_min, int(color_pair[0]))
            else:
                print("Parsing error")
    if not game_is_impossible:
        valid_rounds_count += index + 1
    total_power_count += red_min * green_min * blue_min
    
print(valid_rounds_count)
print(total_power_count)
    