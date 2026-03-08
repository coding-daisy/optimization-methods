export async function sendOptimizerRequest(params) {

    const response = await fetch("http://localhost:8000/nelder_mead", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(params)
    });

    return await response.json();

}