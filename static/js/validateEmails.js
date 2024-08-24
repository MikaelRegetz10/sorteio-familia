function validateEmails() {
  const emails = document.querySelectorAll('input[type="email"]');
  let isValid = true;

  emails.forEach(function(emailInput) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const email = emailInput.value;

    if (!emailPattern.test(email)) {
      isValid = false;
      emailInput.classList.add('is-invalid');
      alert('Por favor, insira um e-mail válido.');
    } else {
      emailInput.classList.remove('is-invalid');
    }
  });

  return isValid;
}