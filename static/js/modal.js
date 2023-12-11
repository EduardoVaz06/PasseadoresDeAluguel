const button = document.querySelector("button")
const modal = document.querySelector("dialog")
buttonClose = document.querySelector("dialog button")

button.onclick = function () {
    modal.show()
}

buttonClose.onclick = function () {
    modal.close()
}

/*
// Seleciona os botões pelo ID
const openButtonDetalhes = document.getElementById('ModalDetalhes');
const buttonCloseDetalhes = document.getElementById('FecharDetalhes');
const modalDetalhes = document.getElementById('modalDetalhes');

// Adiciona eventos de clique aos botões
openButtonDetalhes.onclick = function () {
    modalDetalhes.showModal();
};

buttonCloseDetalhes.onclick = function () {
    modalDetalhes.close();
};
*/
/* const modalButtons = document.querySelectorAll('.modal-button');
const fecharDetalhesButtons = document.querySelectorAll('.fechar-detalhes');

modalButtons.forEach(button => {
    button.onclick = function () {
        const targetId = button.getAttribute('data-target');
        const modal = document.getElementById(targetId);
        modal.showModal();
    };
});

fecharDetalhesButtons.forEach(button => {
    button.onclick = function () {
        const modal = button.closest('dialog');
        modal.close();
    };
}); */