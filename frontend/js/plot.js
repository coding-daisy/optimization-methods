export async function initialPlot(data) {

    const grid = data.grid;
    const frames = data.frames;
    const plotRange = data.plot_range;
    const searchRectangle = data.search_rectangle;

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

    const searchRectanglePlot = {
        type: "scatter",
        mode: "lines+markers+text",
        textposition: "top center",
        x: searchRectangle.map(point => point[0]),
        y: searchRectangle.map(point => point[1]),
        text: ["", "", "Search space", "", ""],
        line: {color: "black"}
    }

    Plotly.newPlot("plot", [contour, simplex, searchRectanglePlot], {
        xaxis: {
            range: [plotRange["x"][0], plotRange["x"][1]],
            constrain: "domain"
            // removes achsis outside plot
        },
        yaxis: {
            range: [plotRange["y"][0], plotRange["y"][1]],
            scaleanchor: "x",
            constrain: "domain"
        }
    },
    {
        responsive: true
        // adopting container size!
        // now holding div can change plot size
    }

);

}
