let familiaCount = 1;

function addFamilia() {
  familiaCount++;
  const familiaDiv = document.createElement('div');
  familiaDiv.classList.add('familia', 'mb-4');
  familiaDiv.setAttribute('data-familia-id', familiaCount);
  familiaDiv.innerHTML = `
    <h5>Família ${familiaCount}</h5>
    <div class="mb-3">
      <input type="email" name="familia_${familiaCount}_email" class="form-control" placeholder="Email Família" aria-label="Email Família" required>
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" name="familia_${familiaCount}_membro" placeholder="Nome Integrante" aria-label="Nome Integrante" required>
      <button class="btn btn-outline-secondary" type="button" onclick="addMembro(this)">Adicionar membro</button>
    </div>
    <div class="membros-adicionados"></div>
    <button type="button" class="btn btn-danger mt-3" onclick="removeFamilia(this)">Remover Família</button>
  `;
  document.getElementById('familias').appendChild(familiaDiv);
}

function addMembro(button) {
  const membroInput = document.createElement('div');
  membroInput.classList.add('input-group', 'mb-3');
  membroInput.innerHTML = `
    <input type="text" class="form-control" name="familia_${button.closest('.familia').getAttribute('data-familia-id')}_membro" placeholder="Nome Integrante" aria-label="Nome Integrante" required>
    <button class="btn btn-outline-secondary" type="button" onclick="removeMembro(this)">Remover</button>
  `;
  button.parentElement.parentElement.querySelector('.membros-adicionados').appendChild(membroInput);
}