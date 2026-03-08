export function connectSlider() {

    const adjustments = document.querySelectorAll(".parameter-adjustment");


    adjustments.forEach(adj => {

        const inputSlider = adj.querySelector("input[type='range']");
        const display = adj.querySelector(".val-display");

        
        // initializing the label !
        display.textContent = inputSlider.value; // the value we have pre-initialized

        // move slider -> update
        inputSlider.addEventListener("input", () => {
            display.textContent = inputSlider.value;
        });

    });

}

export function getParameters() {

    return {
        function_name: "himmelblau", 
        plot_scaling: "log",
        // THESE SHOULD ALSO BECOME CHOOSABLE !

        min_x: parseFloat(document.getElementById("min_x").value),
        max_x: parseFloat(document.getElementById("max_x").value),
        min_y: parseFloat(document.getElementById("min_y").value),
        max_y: parseFloat(document.getElementById("max_y").value),

        alpha: parseFloat(document.getElementById("alpha").value),
        beta: parseFloat(document.getElementById("beta").value),
        gamma: parseFloat(document.getElementById("gamma").value),

        max_iter: parseInt(document.getElementById("max_iter").value),
        delta: parseFloat(document.getElementById("delta").value),

        
    };
}