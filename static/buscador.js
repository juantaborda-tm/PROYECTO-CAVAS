document.addEventListener("keyup", e => {
    if (e.target.matches("#barra_busqueda")) {
        const filas = document.querySelectorAll(".productos"); // NodeList
        filas.forEach(fila => {
            fila.textContent.toLowerCase().includes(e.target.value.toLowerCase())
                ? fila.classList.remove("filtro")
                : fila.classList.add("filtro");
        });
    }
});
