import pulp
model = pulp.LpProblem('ProfitMaximisingProblem', pulp.LpMaximize)
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0,cat='Integer')

model += 3 * A + 4 * B == 11000
model += 1 * A + 7 * B == 15000
model += 2 * A + 6 * B, 'Profit'
model.solve()
pulp.LpStatus[model.status]
print (A.varValue)
print (B.varValue)
print (pulp.value(model.objective))
