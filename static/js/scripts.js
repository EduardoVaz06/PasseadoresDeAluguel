const registros = document.querySelectorAll('.container-resultados-lista');
const anterior = document.getElementById('anterior');
const proximo = document.getElementById('proximo');
const paginaAtual = document.getElementById('pagina-atual');
const registrosPorPagina = 5;
let pagina = 1;

function mostrarLista() {
    var containerLista = document.querySelector('.container-lista');
    containerLista.style.display = 'flex';
}

var botaoBuscar = document.querySelector('.botao-busca');
botaoBuscar.addEventListener('click', mostrarLista);

function exibirRegistros() {
    const inicio = (pagina - 1) * registrosPorPagina;
    const fim = inicio + registrosPorPagina;

    registros.forEach((registro, indice) => {
        if (indice >= inicio && indice < fim) {
            registro.style.display = 'block';
        } else {
            registro.style.display = 'none';
        }
    });

    paginaAtual.textContent = pagina;
}

function paginaAnterior() {
    if (pagina > 1) {
        pagina--;
        exibirRegistros();
    }
}

function proximaPagina() {
    const totalPaginas = Math.ceil(registros.length / registrosPorPagina);
    if (pagina < totalPaginas) {
        pagina++;
        exibirRegistros();
    }
}

anterior.addEventListener('click', paginaAnterior);
proximo.addEventListener('click', proximaPagina);
exibirRegistros();