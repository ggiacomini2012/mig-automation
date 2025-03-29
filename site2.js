const puppeteer = require('puppeteer');
require('dotenv').config(); // Para carregar variáveis de ambiente do arquivo .env

console.log(process.env.USERNAME_MIG);
console.log(process.env.PASSWORD);

(async () => {
  try {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    // Acessar a página de login
    await page.goto('https://cli.giver.com.br/administrador/login', { waitUntil: 'networkidle2' });

    // Digitar o usuário e senha a partir de variáveis de ambiente
    await page.type('input[placeholder="Usuário"]', process.env.USERNAME_MIG || 'seu_usuario');
    await page.type('input[placeholder="Senha"]', process.env.PASSWORD || 'sua_senha');

    // Clicar no botão "ENTRAR"
    const botao = await page.waitForSelector('button[type="submit"], button.btn-success, form button', { timeout: 5000 });
    if (botao) {
      await botao.click();
      console.log("✅ Botão 'ENTRAR' clicado com sucesso.");
    } else {
      throw new Error("⚠️ Botão de 'ENTRAR' não encontrado.");
    }

    // Aguarda a navegação completa após login
    await page.waitForNavigation({ waitUntil: 'networkidle0', timeout: 30000 });

    // Clicar no ícone do WhatsApp
    const botaoWhatsApp = await page.waitForSelector('img[src*="whatsapp"], div[class*="whatsapp"], button', { timeout: 10000 });
    if (botaoWhatsApp) {
      await botaoWhatsApp.click();
      console.log("✅ Ícone do WhatsApp clicado com sucesso.");
    } else {
      throw new Error("⚠️ Ícone do WhatsApp não encontrado.");
    }

    // Fechar navegador automaticamente após alguns segundos
    await new Promise(resolve => setTimeout(resolve, 5000)); // Espera 5 segundos antes de fechar
    await browser.close();
    console.log("✅ Navegador fechado com sucesso.");
  } catch (error) {
    console.error(`❌ Erro: ${error.message}`);
  }
})();
