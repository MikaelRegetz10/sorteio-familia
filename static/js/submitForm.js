window.onload = function() {
  document.getElementById('loading-screen').style.display = 'none';
};

function submitForm() {
  // Chama a função de validação de e-mails do arquivo `validateEmails.js`
  const isValid = validateEmails();

  if (isValid) {
    // Se a validação for bem-sucedida, mostra a tela de carregamento
    document.getElementById('loading-screen').style.display = 'flex';

    // Envia o formulário após um pequeno atraso
    setTimeout(() => {
      document.getElementById('sorteio-form').submit();
    }, 500);
  } else {
    // Se a validação falhar, não envia o formulário nem mostra a tela de carregamento
    document.getElementById('loading-screen').style.display = 'none';
  }
}
