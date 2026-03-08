let currentRun = 0;
// variable to keep track of current run 
// -> prevents multiple parallel runs

async function run() {

    const runId = ++currentRun;

    const response = await fetch("http://localhost:8000/nelder_mead", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        // hard-coded for now 
        body: JSON.stringify({
            function_name: "himmelblau",
            min_x: -5,
            max_x: 5,
            min_y: -5,
            max_y: 5,
            alpha: 1,
            beta: 2,
            gamma: 0.5,
            max_iter: 10,
            goal_delta: 1e-6,
            plot_scaling: "log"
        })
    });

    const data = await response.json();

    const grid = data.grid;
    const frames = data.frames;

    const contour = {
        type: "contour",
        x: grid.x,
        y: grid.y,
        z: grid.z,
        colorscale: "Blues",
        ncontours: 20
    };

    const simplex = {
        type: "scatter",
        mode: "lines+markers",
        x: frames[0].x,
        y: frames[0].y,
        line: {color: "red"}
    };

    // "plot" is the id of where we want to put the plot!
    Plotly.newPlot("plot", [contour, simplex], {
        yaxis: {scaleanchor: "x"}
    });

    for (let frame of frames) {

        if (runId !== currentRun) {
            return;
        }

        await Plotly.restyle("plot", {
            x: [frame.x],
            y: [frame.y]
        }, [1]);

        // frame.x is the list of (4) x-values for simplex vertices by definition

        // this means: update trace index 1 !

        await new Promise(r => setTimeout(r, 500));
        
    }
}