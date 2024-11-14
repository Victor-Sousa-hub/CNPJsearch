// Importa o módulo 'fs' para ler o arquivo JSON
const fs = require('fs');

// Caminho para o arquivo JSON
const filePath = './Enquadramento.json';

// Função para carregar e processar o JSON
function loadJSON() {
    try {
        console.log("Iniciando leitura do arquivo JSON...");

        // Lê o arquivo JSON de forma síncrona
        const fileData = fs.readFileSync(filePath, 'utf8');

        // Converte o conteúdo do arquivo para um objeto JavaScript
        const jsonData = JSON.parse(fileData);

        // Verifica se a chave "Planilha1" existe e é um array
        if (!jsonData.Planilha1 || !Array.isArray(jsonData.Planilha1)) {
            throw new Error("O arquivo JSON não contém um array válido na chave 'Planilha1'.");
        }

        // Imprime cada item do array no console
        console.log("Dados da Planilha1 carregados:");
        jsonData.Planilha1.forEach((atividade, index) => {
            console.log(`Atividade ${index + 1}:`);
            console.log(`  Código CNAE: ${atividade["Código CNAE"]}`);
            console.log(`  Descrição da Atividade: ${atividade["Descrição da Atividade"]}`);
            console.log(`  Enquadramento: ${atividade["Enquadramento da atividade"]}`);
            console.log("------------------------");
        });
    } catch (error) {
        console.error("Erro ao carregar o arquivo JSON:", error.message);
    }
}

// Chama a função para carregar e exibir os dados
loadJSON();
