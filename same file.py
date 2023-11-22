from pyomo.environ import *
import pyomo.opt as po

model = ConcreteModel()

model.x = Var(Within= NonNegativeReals)
model.y = Var(Within= NonNegativeReals)

model.maximizeZ = Objective(expr=model.x + 10*model.y)

model.Contraint1 = Constraint(expr = 0.2*model.x + 4 >= model.y)

model.Contraint2 = Constraint(expr = -0.2*model.x + 6 >= model.x)

model.Constraint3 = Constraint(expr = 10*model.x + 1 >= model.y)

solver = po.SolverFactory('glpk')

solver.solve(model)

model.display()
