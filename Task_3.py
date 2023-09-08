import itertools


items = {
    'спички': 1,
    'фонарик': 2,
    'еда': 5,
    'компас': 1,
    'палатка': 10
}


max_weight = 10

all_combinations = []
for r in range(1, len(items) + 1):
    for combination in itertools.combinations(items.items(), r):
        total_weight = sum(item[1] for item in combination)
        if total_weight <= max_weight:
            all_combinations.append(combination)

for combination in all_combinations:
    print(f"Комплектация: {[item[0] for item in combination]}, Вес: {sum(item[1] for item in combination)}")
