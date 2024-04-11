document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os inputs de rádio dentro do fieldset
    var inputs = document.querySelectorAll('#meuFieldset input[type="radio"]');
    
    // Adiciona um ouvinte de evento para cada input de rádio
    inputs.forEach(function(input) {
        input.addEventListener('click', function() {
            // Array para armazenar os valores selecionados
            var valoresSelecionados = [];
            
            // Itera sobre os inputs para verificar se estão selecionados e obter seus valores
            inputs.forEach(function(input) {
                if (input.checked) {
                    valoresSelecionados.push(input.value);
                }
            });
            
            // Exibe os valores selecionados no console (você pode fazer outra coisa com eles)
            console.log(valoresSelecionados);
        });
    });
});