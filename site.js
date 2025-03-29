const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // Acessar a página de login
  await page.goto('https://cli.giver.com.br/administrador/login', { waitUntil: 'networkidle2' });

  // Digitar o usuário e senha
  await page.type('input[placeholder="Usuário"]', 'madeinguarda.balneario'); // Ajuste se o seletor for diferente
  await page.type('input[placeholder="Senha"]', 'migsoul1234');

  async function waitForSeconds(seconds) {
    return new Promise(resolve => setTimeout(resolve, seconds * 1000));
  }


  // Tentar diferentes seletores para o botão de "ENTRAR"
  const selectors = [
    'button[type="submit"]',
    'button.btn-success',
    'button',  // Caso seja o único botão na página
    'form button' // Se for o único botão dentro de um formulário
  ];

  let found = false;
  for (const selector of selectors) {
    const buttonExists = await page.$(selector);
    if (buttonExists) {
      await page.click(selector);

      found = true;
      console.log(`Botão encontrado e clicado: ${selector}`);
      break;
    }
  }

  if (!found) {
    console.log("Botão de 'ENTRAR' não encontrado. Verifique os seletores.");
  }

async function clicarWhatsApp(page) {
  // Aguarda um pouco para garantir que todos os elementos carreguem
  await waitForSeconds(20);

  // Captura todos os botões ou ícones disponíveis na página
  const elementos = await page.$$('button, img, div');

  for (const elemento of elementos) {
    const texto = await page.evaluate(el => el.innerText || '', elemento);
    const alt = await page.evaluate(el => el.getAttribute('alt') || '', elemento);
    const ariaLabel = await page.evaluate(el => el.getAttribute('aria-label') || '', elemento);

    // Verifica se algum botão ou ícone tem relação com WhatsApp
    if (texto.includes('WhatsApp') || alt.includes('WhatsApp') || ariaLabel.includes('WhatsApp')) {
      await elemento.click();
      console.log("Ícone do WhatsApp clicado com sucesso.");
      return;
    }
  }

  console.log("Ícone do WhatsApp não encontrado.");
}


  await clicarWhatsApp();

  // Aguardar um tempo para ver o resultado antes de fechar o navegador
  await waitForSeconds(5);

  // Fechar navegador (opcional, descomente caso queira fechar automaticamente)
  // await browser.close();
})();