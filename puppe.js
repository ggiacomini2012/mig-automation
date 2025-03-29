const puppeteer = require('puppeteer');

// Função personalizada que retorna uma promessa que resolve após o tempo especificado
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  // Lança o navegador
  const browser = await puppeteer.launch({ headless: false, defaultViewport: null }); // Define `headless: false` para ver o navegador e `defaultViewport: null` para evitar que a página tenha um tamanho fixo

  // Obtém todas as abas abertas
  const pages = await browser.pages(); // Isso retorna um array com todas as páginas abertas
  const page = pages[0]; // A primeira aba aberta

  // Define o tamanho da janela para maximizar
  // await page.setViewport({ width: 1920, height: 1080 }); // Maximiza a janela, ou ajusta para a resolução desejada

  // Navega para o site fornecido na primeira aba
  await page.goto('https://cli001.giver.com.br/agenda/#/home/');

  // Espera 2 segundos para garantir que a página tenha carregado
  await wait(2000);

  // Agora você pode interagir com a primeira aba, preencher campos ou realizar outras ações
  // Exemplo de interação: preencher um campo de login (ajuste os seletores conforme necessário)
  // await page.type('input[name="login"]', 'seu_login');
  // await page.type('input[name="senha"]', 'sua_senha');
  // await page.click('button[type="submit"]');

  // Remover ou comentar a linha abaixo para evitar que o navegador feche
  // await browser.close();
})();
