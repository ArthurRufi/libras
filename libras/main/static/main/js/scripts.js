document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os inputs de rádio dentro do formulário
    var inputs = document.querySelectorAll('#meuForm input[type="radio"]');
    
    // Adiciona um ouvinte de evento para cada input de rádio
    inputs.forEach(function(input) {
        input.addEventListener('click', function() {
            filtrarItens();
        });
    });
    
    // Adiciona um ouvinte de evento para o botão de limpar filtros
    var btnLimparFiltros = document.getElementById('limparFiltros');
    btnLimparFiltros.addEventListener('click', function() {
        limparFiltros();
    });
});

// Função para filtrar os itens com base na matéria selecionada
// Função para filtrar os itens com base na matéria selecionada
function filtrarItens() {
    // Obtém o valor da matéria selecionada e converte para inteiro
    var materiaSelecionada = parseInt(document.querySelector('#meuForm input[type="radio"]:checked').value);
    console.log("Matéria selecionada:", materiaSelecionada);

    // Seleciona todos os itens da seção
    var itens = document.querySelectorAll('.itens');
    console.log("Itens encontrados:", itens);

    // Itera sobre os itens para mostrar apenas os itens relacionados à matéria selecionada e ocultar os outros
    itens.forEach(function(item) {
        // Obtém o código do curso do item e converte para inteiro
        var codigoCurso = parseInt(item.dataset.codigodamateria);
        console.log("Código do curso:", codigoCurso);
        
        // Verifica se o código do curso do item corresponde à matéria selecionada
        if (codigoCurso == materiaSelecionada) {
            item.style.display = 'block'; // Exibe o item se corresponder
        } else {
            item.style.display = 'none'; // Oculta o item se não corresponder
        }
    });
}

// Função para limpar a seleção de rádio e reexibir todos os itens
function limparFiltros() {
    // Limpa a seleção de rádio
    var inputs = document.querySelectorAll('#meuForm input[type="radio"]');
    inputs.forEach(function(input) {
        input.checked = false;
    });
    
    // Reexibe todos os itens
    var itens = document.querySelectorAll('.itens');
    itens.forEach(function(item) {
        item.style.display = 'block';
    });
}
