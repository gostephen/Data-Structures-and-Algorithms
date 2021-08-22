# Solving assignment problem using the Hungarian method
from hungarian_algorithm import algorithm


H = {
        'C1': {'J1': 13, 'J2': 16, 'J3': 12, 'J4': 11},
        'C2': {'J1': 15, 'J2': 17, 'J3': 12, 'J4': 12},
        'C3': {'J1': 14, 'J2': 14, 'J3': 13, 'J4': 13},
        'C4': {'J1': 13, 'J2': 10, 'J3': 10, 'J4': 11},
    }

print(algorithm.find_matching(H, matching_type = 'min', return_type = 'list' ))



