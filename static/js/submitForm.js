window.onload = function() {
  document.getElementById('loading-screen').style.display = 'none';
};

function submitForm() {
  document.getElementById('loading-screen').style.display = 'flex';

  setTimeout(() => {
    document.getElementById('sorteio-form').submit();
  }, 500);
}