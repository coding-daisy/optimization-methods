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

        init_temperature: parseFloat(document.getElementById("init_temperature").value),
        temperature_decrease: parseFloat(document.getElementById("temperature_decrease").value),
        speed_range: parseFloat(document.getElementById("speed_range").value),

        p_function: document.querySelector('input[name="p_function"]:checked').value,

        function_name: document.querySelector('input[name="function"]:checked').value,
        custom_function: document.querySelector('input[name="custom-function"]').value,
        // we do not need to parse as string -> string by default
    
    };
}