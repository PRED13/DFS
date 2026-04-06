async function resolver() {

    const inicio = document
        .getElementById("inicio")
        .value.split(",")
        .map(Number);

    const meta = document
        .getElementById("meta")
        .value.split(",")
        .map(Number);

    const response = await fetch("/api/solver", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            inicio,
            meta
        })

    });

    const data = await response.json();

    document.getElementById("resultado").innerText =
        JSON.stringify(data, null, 2);
}