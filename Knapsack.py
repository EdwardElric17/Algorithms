items = list()
cost_of_items = list()
all_cost = float()
n, W = map(int, input().split())
for i in range(n):
    items.append([float(i) for i in input().split()])
for item in items:
    cost_of_items.append(float(item[0]/item[1]))
while W > 0:
    if W - items[cost_of_items.index(max(cost_of_items))][1] >= 0:
        W -= items[cost_of_items.index(max(cost_of_items))][1]
        all_cost += items[cost_of_items.index(max(cost_of_items))][0]
        items.remove(items[cost_of_items.index(max(cost_of_items))])
        cost_of_items.remove(max(cost_of_items))
    else:
        all_cost += W * max(cost_of_items)
        break
    if len(cost_of_items) == 0:
        break
print(f"{all_cost:.3f}")