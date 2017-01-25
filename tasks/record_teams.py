import json
import time

def write_team_file(pkmn_numbers):

    time_string = time.strftime('%Y-%m-%d_%H_%M_%S')
    f = open('teams/' + time_string + '.json', 'w')
    json.dump(pkmn_numbers[0:6], f)
    json.dump(pkmn_numbers[6:12], f)
    f.close()

