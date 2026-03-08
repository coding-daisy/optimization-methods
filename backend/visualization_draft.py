import numpy as np
import plotly.graph_objects as go
from objective_functions import FUNCTIONS
import time
from optimizers.nelder_mead.simplexes_computation import get_nelder_mead_simplexes
from itertools import product # for getting cartesian product

# hardcoded for now!
# find out how to do this for more dimensions later!
function = FUNCTIONS["himmelblau"]
min_range = -5
max_range = 5
search_space = ((min_range, max_range), (min_range, max_range))
margin = max([abs(tuple[0] - tuple[1]) for tuple in search_space]) * 0.2
max_iter = 10
alpha=1
beta=2
gamma=0.5,
goal_delta=1e-6
xNumberOfPoints = 100
yNumberOfPoints = 100
levels = 20
plot_scaling = "log"

# ----------------
# COMPUTE "ALGORITHM STATES"
# ----------------


def function_scaled(X, Y, function, plot_scaling):
    Z = function((X, Y))
    if (not plot_scaling):
        return Z
    if (plot_scaling == "log"):
        return np.log(Z - Z.min() + 1)


# create grid
x = np.linspace(search_space[0][0] - margin, search_space[0][1] + margin, xNumberOfPoints)
y = np.linspace(search_space[1][0] - margin, search_space[1][1] + margin, yNumberOfPoints)

X, Y = np.meshgrid(x, y)
# X = grid of only x-coordinates
# Y = grid of only y-coordinates


Z = function_scaled(X, Y, function, plot_scaling)

fig = go.Figure()

fig.add_trace(go.Contour(
    x=x,
    y=y,
    z=Z,
    ncontours=levels,
    contours=dict(showlabels=False),
    colorscale="Blues"
))

# ----------------
# COMPUTE "ALGORITHM STATES"
# ----------------


simplexes = get_nelder_mead_simplexes(function, search_space, alpha=alpha, beta=beta, gamma=gamma,
                max_iter=max_iter, goal_delta=goal_delta)


fig.update_layout(
    yaxis=dict(scaleanchor="x"),
    title="Optimizer visualization prototype"
)


# ----------------
# INITAL SIMPLEX
# ----------------


fig.add_trace(go.Scatter(
    x= [p[0] for p in simplexes[0]] + [simplexes[0][0][0]],   # last point repeats first to close shape
    y= [p[1] for p in simplexes[0]] + [simplexes[0][0][1]],
    mode="lines+markers",
    line=dict(color="red", width=2)
))

# ----------------
# SEARCH SPACE
# ----------------

corners = [
    (search_space[0][0], search_space[1][0]),
    (search_space[0][1], search_space[1][0]),
    (search_space[0][1], search_space[1][1]),
    (search_space[0][0], search_space[1][1]),
    (search_space[0][0], search_space[1][0])
    ]
# we can't use cartesian product here, since the order is important
# -> we would manually have to reorder, which doesn't make it any easier


fig.add_trace(go.Scatter(
    x= [corner[0] for corner in corners],
    y=  [corner[1] for corner in corners],
    mode="lines+markers+text",
    text=["", "", "Search space", "", ""],
    textposition="top center",
    line=dict(color="grey", width=2),
    showlegend=False
))


# ----------------
# STEP THROUGH STATES
# ----------------

for simplex in simplexes:

    fig.data[1].x = [p[0] for p in simplex] + [simplex[0][0]]
    fig.data[1].y = [p[1] for p in simplex] + [simplex[0][1]]

    fig.show()

    time.sleep(0.5)






