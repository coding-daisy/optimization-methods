export function getParameters() {


    return {

        plot_scaling: document.querySelector('input[name="plot_scaling"]:checked').value,

        // the level count is NOT sent to backend: used directly for frontend plotting!
        // levels: parseInt(document.querySelector('input[name="levels"]').value),

        min_x: parseFloat(document.getElementById("min_x").value),
        max_x: parseFloat(document.getElementById("max_x").value),
        min_y: parseFloat(document.getElementById("min_y").value),
        max_y: parseFloat(document.getElementById("max_y").value),
        margin_ratio: parseFloat(document.getElementById("margin_ratio").value),

        alpha: parseFloat(document.getElementById("alpha").value),
        beta: parseFloat(document.getElementById("beta").value),
        gamma: parseFloat(document.getElementById("gamma").value),

        max_iter: parseInt(document.getElementById("max_iter").value),
        delta: parseFloat(document.getElementById("delta").value),

        function_name: document.querySelector('input[name="function"]:checked').value,
        custom_function: document.querySelector('input[name="custom-function"]').value,
        // we do not need to parse as string -> string by default
    
    };
}