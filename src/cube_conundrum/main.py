import random

total_cubes = {'red':12, 'green':13, 'blue':14}

def is_game_possible(game_entry):
    fewest_required = {}
    for round in game_entry[1]:
        for cube, quantity in round.items():
            if quantity > total_cubes[cube]:
                return False
    return True


def process_game_line(line):
    ''' splits each string into game information '''
    id_and_info = line.split(": ")
    game_id = id_and_info[0]
    game_information = []
    for round in id_and_info[1].split("; "):
        entry = {} 
        for cube in round.split(", "):
            cube = cube.split()
            num_cubes = int(cube[0])
            color = cube[1]
            # if already in the dictionary, add the value to the existing value
            if color in entry:
                print("duplicate")
                entry[color] = entry[color] + num_cubes 
            else:
                entry[color] = num_cubes
        print(entry)
        game_information.append(entry)

    game_object = (game_id, game_information)
    return game_object


def main():
    file_lines = []
    with open("./input", "r") as file:
        file_lines = file.readlines()
    debuggy = False 
    if (debuggy):
        for line in file_lines:
            game_info = process_game_line(line)
            game_result = is_game_possible(game_info)
            print(f"{game_info[0]} | {line.split(": ")[1]} | {game_info[1]} {'possible' if game_result == True else 'not possible'}")
    else:
        sum_of_gameids = 0
        for line in file_lines:
            game_info = process_game_line(line)
            game_result = is_game_possible(game_info)
            if game_result:
                sum_of_gameids += int(game_info[0].split()[1])
        print(sum_of_gameids)
      
        

if __name__ == '__main__':
    main()




        
        
        

