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

        w: parseFloat(document.getElementById("w").value),
        c_ind: parseFloat(document.getElementById("c_ind").value),
        c_group: parseFloat(document.getElementById("c_group").value),
        swarm_size: parseFloat(document.getElementById("swarm_size").value),
        init_max_speed: parseFloat(document.getElementById("init_max_speed").value),
        max_speed: parseFloat(document.getElementById("max_speed").value),

        max_iter: parseInt(document.getElementById("max_iter").value),

        function_name: document.querySelector('input[name="function"]:checked').value,
        custom_function: document.querySelector('input[name="custom-function"]').value,
        // we do not need to parse as string -> string by default
    
    };
}