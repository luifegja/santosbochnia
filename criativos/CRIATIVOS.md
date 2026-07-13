# Criativos de Anúncio — Santos & Bochnia (memória de produção)

Leia este arquivo ANTES de qualquer tarefa de criativos. Ele evita retrabalho e mantém a consistência entre sessões.

## Sistema de produção

Os criativos são **HTML/CSS renderizados em PNG** (nunca arte gerada 100% por IA — decisão do usuário: fugir do visual genérico de IA). Pipeline:

1. Editar/criar o HTML do criativo em `_fontes/` (um arquivo por carrossel/estático).
2. Renderizar com `python _fontes/render.py <arquivo.html> <pasta-destino> <prefixo>` — usa Edge headless via CDP, captura cada `.card` em 1080×1350 (4:5, feed Meta/Instagram).
3. Conferir visualmente cada PNG antes de entregar.

## Identidade (herdada do site — NUNCA improvisar cores/fontes)

- Navy `#0D3557` · navy-deep `#092A46` · petróleo `#2E7590` · turquesa `#77B9C9` · turquesa-clara `#9AD7E9` · gelo `#F5F8FA` · verde WhatsApp `#25D366` (EXCLUSIVO de CTA)
- Fontes Google: **Cormorant Garamond** (títulos/serifa, 500-700) + **Archivo** (apoio/corpo)
- Logos prontos: `../site/assets/img/logo-light.png` (p/ navy), `logo-dark.png` (p/ claro), `monograma-sb.svg`/`.webp` (degradê turquesa)
- Fotos on-brand existentes: `../site/assets/img/ia/*.webp` (8) + auxiliares wide em `_fontes/ref/`

## Conceito visual dos carrosséis — "O Fio" (v2, sutil)

Um **fio turquesa de 3.5px a 45% de opacidade** percorre a MARGEM INFERIOR dos 5 cards (rota "silenciosa" — nunca cruza texto; termina em ponto verde no card 5, abaixo da linha de contato). Continuidade reforçada por: fotos inclinadas **sangrando na emenda** (1→2 e 4→5), numerais fantasma (440px, opacidade ≤.05, zonas vazias das emendas) e pill "arraste ››". Narrativa fixa: **1 gancho (dor) → 2 situações → 3 o direito existe → 4 quem cuida → 5 CTA "Saiba mais →"** (botão verde imitando o CTA nativo do Meta; sem promessa de WhatsApp direto). Regra de ouro da v2 (feedback do usuário): elementos de continuidade NUNCA podem atrapalhar a leitura — em dúvida, esconda. Card 3 usa grid de 3 colunas alinhadas à esquerda (não zigue-zague). Auditoria de design por subagente é etapa obrigatória antes de entregar.

## Regras de copy (OAB Provimento 205/2021 — OBRIGATÓRIO)

Sem promessa de resultado, sem estatísticas de êxito, sem valores/honorários/"consulta gratuita" (usar "primeira conversa sem compromisso"), sem "o melhor", sem depoimentos, urgência só por prazos legais reais. Palavras do público por área: ver headlines das LPs em `../site/*.html`.

## Convenção de nomes

`<area>/carrossel-NN-card-N.png` (NN = número sequencial do carrossel na área, N = card 1-5) · `<area>/estatico-NN.png`. Fontes HTML: `_fontes/<area>-carrossel-NN.html` (o card estático é o `.card--static` no mesmo arquivo).

## Inventário (atualizar a cada entrega!)

| Data | Área | Arquivos | Conceito/observação |
|---|---|---|---|
| jul/2026 | previdenciario | carrossel-01 (5 cards) + estatico-01 | "O Fio" v1 · tema claro · foto ref/previdenciario-wide + escritorio-interior · Simone no card 4 |
| jul/2026 | consumidor | carrossel-01 (5 cards) + estatico-01 | "O Fio" v1 · copy fraudes consignado/RMC-RCC (mesma da LP) · foto area-consumidor (martelo) + detalhe-biblioteca · Equipe no card 4 |
| jul/2026 | penal-economico | carrossel-01 (5 cards) + estatico-01 | "O Fio" v1 · **card 1 escuro** (override CSS no arquivo) · foto ref/penal-wide + balanca-abstrata · José Eduardo no card 4 |
| jul/2026 | imobiliario | carrossel-01 (5 cards) + estatico-01 | "O Fio" v1 · foto area-imobiliario (chaves) + faria-lima-fachada · Equipe no card 4 |

Notas de produção: os 3 clones foram gerados por `_fontes/gerar_areas.py` (substituições sobre o template previdenciário — se editar o template, regerar e re-renderizar os 4). Imagens aux: só 3 geradas (créditos Higgsfield esgotaram); `ref/consumidor-wide.webp` tem pseudo-texto grande — NÃO usar sem tratar; imobiliário usa a foto do site. Pendência de melhoria: gerar `ref/imobiliario-wide.webp` quando houver créditos.
