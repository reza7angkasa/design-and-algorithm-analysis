import pulp
model = pulp.LpProblem('ProfitMaximisingProblem', pulp.LpMaximize)
X = pulp.LpVariable('X', lowBound=0, cat='Integer')
Y = pulp.LpVariable('Y', lowBound=0,cat='Integer')
model += 4 * X + 3 * Y == 34
model += 5 * X + Y == 37
model.solve()
pulp.LpStatus[model.status]
print (X.varValue)
print (Y.varValue)
