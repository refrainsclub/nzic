teas = {"G": 0, "C": 1, "E": 2, "P": 3, "L": 4, "S": 5}
preferences = [0] * len(teas)

people, hosts = map(int, input().split())

for _ in range(people):
    _, preference = input().split()
    idx = teas.get(preference)

    if idx is not None:
        preferences[idx] += 1

scores = {}

for _ in range(people):
    line = input().split()
    name = line[0]
    pantry = map(int, line[1:])

    score = 0
    for i, c in enumerate(pantry):
        score += min(c, preferences[i])

    scores[name] = score


def get_result(disgruntled):
    if disgruntled == 0:
        return "Successful"
    elif disgruntled <= 2:
        return f"Mildly Successful ({disgruntled})"
    return f"Disaster ({disgruntled})"


for host in [input() for _ in range(hosts)]:
    disgruntled = people - scores[host]
    print(host, get_result(disgruntled))
