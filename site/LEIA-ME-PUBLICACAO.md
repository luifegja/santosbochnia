# Site Santos & Bochnia Advogados — Guia de Publicação

## O que está nesta pasta

| Arquivo | Função |
|---|---|
| `index.html` | Site institucional onepage |
| `previdenciario.html` | LP de conversão — tráfego pago Previdenciário |
| `consumidor.html` | LP de conversão — tráfego pago Consumidor |
| `penal-economico.html` | LP de conversão — Penal Econômico |
| `imobiliario.html` | LP de conversão — Imobiliário |
| `css/` `js/` `assets/` | Estilos, animações (Three.js/GSAP) e imagens |
| `robots.txt` `sitemap.xml` | SEO |

## Como publicar

Site 100% estático — basta subir **todo o conteúdo desta pasta** para a raiz de qualquer hospedagem (Hostinger, cPanel/FTP, Vercel, Netlify, Cloudflare Pages) apontando o domínio `santosbochnia.adv.br`. Não há build nem banco de dados.

Depois de publicar:
1. Testar cada página no celular e clicar em todos os botões de WhatsApp.
2. Cadastrar `sitemap.xml` no Google Search Console.
3. Criar o Perfil da Empresa no Google (Google Business Profile) para os 2 endereços.

## Rastreio das campanhas

Cada página envia uma mensagem de WhatsApp diferente — assim vocês sabem de onde veio o lead sem precisar de ferramenta extra:

- Site: "Olá! Vim pelo site do Santos & Bochnia…"
- Cada LP: "Olá! Vim pela página de Direito X…"

Para tráfego pago, aponte cada campanha para a LP da área correspondente (ex.: anúncios de INSS → `/previdenciario.html`).

## Pendências para completar (aguardando o cliente)

1. **Números de OAB** dos sócios (e da sociedade, se registrada) — inserir nos cards dos sócios (`index.html`, seção Sócios) e nos cards "Quem cuida do seu caso" das LPs. Os pontos estão marcados no código com `<!-- TODO: incluir OAB/SP nº quando o cliente enviar -->`.
2. **Anos de experiência combinada** — se quiserem usar esse número no contador da home.
3. **Fotos profissionais** — quando existirem, podem substituir os "retratos de monograma" dos sócios.
4. Instalar **Meta Pixel / Google Tag** nas LPs quando as campanhas forem criadas (basta colar o snippet antes de `</head>`).

## Observação de conformidade

Toda a copy foi escrita dentro do Provimento nº 205/2021 do CFOAB: sem promessa de resultado, sem menção a honorários ou gratuidade, sem depoimentos, urgência apenas por prazos legais reais e linha de conformidade no rodapé de todas as páginas.
