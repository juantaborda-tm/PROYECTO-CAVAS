function abrirVentana() {

    const abrir_eliminar = document.querySelectorAll(".icono_eliminar");

    const flotante = document.getElementById("ventana");

    const flotante_2 = document.getElementById("ventana_editar");

    const cancelar = document.getElementById("btn_cancelar");

    const cancelar_2 = document.getElementById("btn_cancelar_editar");

    const abrir_editar = document.querySelectorAll(".icono_editar");

    abrir_eliminar.forEach(eliminar => {

        eliminar.addEventListener("click", () => {

        flotante.style.display = "flex"

        if (flotante.style.display === "flex") {

            cancelar.addEventListener("click", () => {

                flotante.style.display = "none"

            });

        }

        });

    });

    abrir_editar.forEach(editar => {

        editar.addEventListener("click", () => {

            flotante_2.style.display = "flex"

        if (flotante_2.style.display === "flex") {

            cancelar_2.addEventListener("click", () => {

                flotante_2.style.display = "none"

            });

        }

        });

    });
}

function buscadorDeArticulos() {
    document.addEventListener("keyup", e => {
        if (e.target.matches("#barra_busqueda")) {

            const filas = document.querySelectorAll("#informacion");
            let coincidencias = 0;

            filas.forEach(fila => {
                const texto = fila.textContent.toLowerCase();
                const busqueda = e.target.value.toLowerCase();

                if (texto.includes(busqueda)) {
                    fila.style.display = "";
                    coincidencias++;
                } else {
                    fila.style.display = "none";
                }
            });

            let mensaje = document.getElementById("mensaje_no_encontrado");

            if (!mensaje) {

                e.target.parentNode.appendChild(mensaje);
            }

            if (coincidencias === 0) {
                mensaje.style.display = "block";
            } else {
                mensaje.style.display = "none";
            }
        }
    });
}

function abrirMenuLateral() {
    const menu_hamburguesa = document.getElementById('menu_hamburguesa');
    const menu = document.getElementById('barra_menu');

    menu_hamburguesa.addEventListener('click', () => {

        menu_hamburguesa.classList.toggle('active');

        menu.classList.toggle('open');
    });
}

function abrirCrearEspacios () {

    const abrir_crear_nevera = document.getElementById("btn_crear_nevera");

    const abrir_crear_estante = document.getElementById("btn_crear_estanteria");

    const abrir_crear_espacio = document.getElementById("btn_crear_espacio");

    const flotante_nevera = document.getElementById("ventana_crear_nevera");

    const flotante_estante = document.getElementById("ventana_crear_estanteria");

    const flotante_espacio = document.getElementById("ventana_crear_espacio");

    const cancelar = document.querySelectorAll("#btn_cancelar");

    const crear_nevera = document.getElementById("btn_nombre_nevera");

    const crear_estante = document.getElementById("btn_nombre_estante")

    const nombre_nevera = document.getElementById("ventana_nombre_nevera");

    const nombre_estante = document.getElementById("ventana_nombre_estanteria")

    const cerrar = document.querySelectorAll("#ic_atras");


    abrir_crear_nevera.addEventListener("click", () => {

        flotante_nevera.style.display = "flex"

        if (flotante_nevera.style.display === "flex") {

            cancelar.forEach(btn => {

                btn.addEventListener("click", () => {

                    flotante_nevera.style.display = "none"

                });

            });

        };

    });

    abrir_crear_estante.addEventListener("click", () => {

        flotante_estante.style.display = "flex"

        if (flotante_estante.style.display === "flex") {

            cancelar.forEach(btn => {

                btn.addEventListener("click", () => {

                    flotante_estante.style.display = "none"

                });

            });

        }

    });

    abrir_crear_espacio.addEventListener("click", () => {

        flotante_espacio.style.display = "flex"

        if (flotante_espacio.style.display === "flex") {

            cancelar.forEach(btn => {

                btn.addEventListener("click", () => {

                    flotante_espacio.style.display = "none"

                });

            });

        }

    });

}

function agregarNombre () {

    const flotante_nevera = document.getElementById("ventana_crear_nevera");

    const flotante_estante = document.getElementById("ventana_crear_estanteria");

    const flotante_espacio = document.getElementById("ventana_crear_espacio");

    const nombre_nevera = document.getElementById("ventana_nombre_nevera");

    const crear = document.getElementById("btn_crear_nevera");

    if (flotante_nevera.style.display === "flex") {

        crear.addEventListener("click", () => {

            nombre_nevera.style.display = "flex"

        })
    }

}

/* ---------------------------------------------------------- */

document.addEventListener("DOMContentLoaded", ()=> {

        abrirVentana();

    if (document.getElementById("barra_busqueda")) {

        buscadorDeArticulos();

    }

    if (document.getElementById('menu_hamburguesa')) {

        abrirMenuLateral();

    }

    abrirCrearEspacios();


});

