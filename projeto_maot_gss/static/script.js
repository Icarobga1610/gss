function analisarSGF(matricula, nroOs, dataOS) {
  const mat = document.querySelector('#analise #matricula');
  const os = document.querySelector('#analise #data_os');
  const nroOS = document.querySelector('#analise #nro_os');  // Campo para Nº OS

  if (mat) mat.textContent = matricula;
  if (os) os.textContent = dataOS;
  if (nroOS) nroOS.textContent = nroOs;  // Atualizando o campo Nº OS

  const tab = new bootstrap.Tab(document.querySelector('[data-bs-target="#abaAnalise"]'));
  tab.show();
}
