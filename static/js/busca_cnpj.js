function searchCNPJ() {
    const cnpj = document.getElementById("cnpj-input").value;

    // Validação simples do CNPJ
    if (!/^\d{14}$/.test(cnpj)) {
        document.getElementById("result").textContent = "Por favor, insira um CNPJ válido (14 dígitos).";
        return;
    }

    // Exibe mensagem de busca
    document.getElementById("result").textContent = "Buscando informações para o CNPJ: " + cnpj;

    // Chamada à API Flask
    fetch(`/api/busca_cnpj/${cnpj}/`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("result").textContent = "Informações encontradas: " + JSON.stringify(data.result);
            } else {
                document.getElementById("result").textContent = data.error;
            }
        })
        .catch(error => {
            document.getElementById("result").textContent = "Erro ao buscar informações do CNPJ.";
            console.error(error);
        });
}
