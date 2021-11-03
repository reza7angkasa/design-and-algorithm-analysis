import pulp
model = pulp.LpProblem('ProfitMaximisingProblem', pulp.LpMaximize)
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0,cat='Integer')
model += 2 * A + 2 * B, 'Total'
model += 2 * A + 2 * B == 44
model += 2 * A + 2 * (A-6) == 44
model.solve()
pulp.LpStatus[model.status]
print (A.varValue)
print (B.varValue)
print (pulp.value(model.objective))
