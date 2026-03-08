import numpy as np
import plotly.graph_objects as go
import time

xStart = -5
xEnd = 5
xNumberOfPoints = 10
yStart = -5
yEnd = 5
yNumberOfPoints = 10

# create grid
x = np.linspace(xStart,xEnd,xNumberOfPoints)
y = np.linspace(yStart, yEnd, yNumberOfPoints)

X, Y = np.meshgrid(x, y)
# X = grid of only x-coordinates
# Y = grid of only y-coordinates

# function
Z = X**2 + Y**2
# element-wise operation - NOT matrix multiplication!


# ----------------
# COMPUTE "ALGORITHM STATES"
# ----------------

states = []

numberOfStates = 1
startingX = -4
startingY = -4
goalX = 4
goalY = 4

if (numberOfStates != 1):
    for i in range(numberOfStates):

        px = startingX + i * (goalX - startingX) / (numberOfStates - 1)
        py = startingY + i * (goalY - startingY) / (numberOfStates - 1)
        states.append({
            "point": (px, py)
        })
else:
    states.append({
        "point": (startingX, startingY)
    })

# ----------------
# CREATE INITIAL FIGURE
# ----------------

fig = go.Figure()

fig.add_trace(go.Contour(
    x=x,
    y=y,
    z=Z,
    contours=dict(showlabels=True),
    colorscale="Blues"
))

fig.add_trace(go.Scatter(
    x=[states[0]["point"][0]],
    y=[states[0]["point"][1]],
    mode="markers",
    marker=dict(size=12, color="red")
))

fig.update_layout(
    yaxis=dict(scaleanchor="x"),
    title="Optimizer visualization prototype"
)


# ----------------
# THIS IS HOW TO ADD TRIANGLES
# ----------------


fig.add_trace(go.Scatter(
    x=[0, 1, 0.5, 0],   # last point repeats first to close shape
    y=[0, 0, 1, 0],
    mode="lines+markers",
    line=dict(color="blue", width=2)
))


# ----------------
# STEP THROUGH STATES
# ----------------

for state in states:

    px, py = state["point"]

    fig.data[1].x = [px]
    fig.data[1].y = [py]

    fig.show()

    time.sleep(0.5)