teas = {"G": 0, "C": 1, "E": 2, "P": 3, "L": 4, "S": 5}
preferences = [0] * len(teas)

people, hosts = map(int, input().split())

for _ in range(people):
    _, preference = input().split()
    idx = teas.get(preference)

    if idx is not None:
        preferences[idx] += 1

hits = {}

for _ in range(people):
    line = input().split()
    name = line[0]
    pantry = map(int, line[1:])

    total = 0
    for i, c in enumerate(pantry):
        total += min(c, preferences[i])

    hits[name] = total


def get_result(misses):
    if misses == 0:
        return "Successful"
    elif misses <= 2:
        return f"Mildly Successful ({misses})"
    return f"Disaster ({misses})"


for host in [input() for _ in range(hosts)]:
    misses = people - hits[host]
    print(host, get_result(misses))
