# Santos & Bochnia Advogados — Site institucional + LPs de conversão

Projeto de site para o escritório de advocacia Santos & Bochnia (sócios: Dr. José Eduardo dos Santos — Penal Econômico; Dra. Simone Bochnia dos Anjos — Previdenciário/Família). Fundado em 2019, escritórios na Faria Lima (SP) e no Guarujá. Domínio: **santosbochnia.adv.br**.

## Estrutura

```
Logo/     → arquivos originais da marca (PDF vetorial, CDR, PNGs 13MB — NUNCA usar direto na web)
site/     → o site pronto para deploy (estático puro, sem build)
  index.html            → onepage institucional (hero 3D Three.js)
  previdenciario.html   → LP master (template das demais)
  consumidor.html, penal-economico.html, imobiliario.html → LPs clonadas
  css/base.css          → design system (tokens); home.css; lp.css
  js/main.js            → reveals/contadores/FAQ; js/hero3d.js → cena Three.js (só no index)
  assets/img/ia/        → imagens geradas por IA (Higgsfield Soul 2.0)
  assets/img/mapa-brasil-atuacao.svg → mapa dot-matrix (seção Alcance Nacional do index)
  LEIA-ME-PUBLICACAO.md → guia de publicação para o cliente
```

O mapa é gerado por script Python (dot-grid + point-in-polygon sobre GeoJSON dos estados) — para alterar os estados destacados, regenerar a partir do geojson `brazil-states` ajustando o set `COBERTOS`. Estados hoje NÃO destacados: AC, MA, RR, SE, TO.

## Identidade visual (extraída do PDF vetorial do logo — cores exatas)

- Navy da marca: `#0D3557` · degradê do monograma: `#519EAD → #77B9C9 → #9AD7E9`
- Tokens CSS em `site/css/base.css` (`--navy`, `--petrol #2E7590`, `--ice #F5F8FA` etc.)
- Fontes: Cormorant Garamond (títulos) + Archivo (corpo), via Google Fonts
- Verde WhatsApp `#25D366` é EXCLUSIVO dos CTAs de conversão — nada mais compete com ele
- `assets/img/monograma-sb.svg` foi vetorizado por potrace a partir do PNG (o PDF tem o monograma em raster)

## Regras do projeto

1. **Conversão**: todos os CTAs são links `wa.me/5511978992799` com mensagem pré-preenchida ÚNICA por página (rastreio de origem). Nunca depender de JS para conversão.
2. **Conformidade OAB (Provimento 205/2021)** — toda copy deve respeitar: sem promessa de resultado, sem estatísticas de êxito, sem valores/honorários/gratuidade (**nunca "consulta gratuita"** → usar "primeira conversa sem compromisso"), sem mercantilização, sem depoimentos inventados, sem superlativos, "especialista" só com especialização real. Urgência apenas por prazos legais reais. Linha de conformidade no rodapé de todas as páginas.
3. **Performance**: Three.js só no index (import dinâmico pós-load); LPs só GSAP (tráfego pago = mobile). Imagens WebP ≤160KB, lazy loading, width/height explícitos.
4. **Referências de design**: onepage = espírito Pinheiro Neto (editorial, sóbrio); LPs = mecânica Dolman Law comprimida (CTA repetido + sticky, prova numérica, FAQ de objeções).
5. Editar as LPs: `previdenciario.html` é o template master (pontos parametrizáveis marcados com `<!-- PARAM: -->`); mudanças estruturais devem replicar nas 4.

## Criativos de anúncio

Tarefas de criativos (carrossel/estático para tráfego pago): **ler `criativos/CRIATIVOS.md` primeiro** — contém o pipeline HTML→PNG (render.py), o conceito visual "O Fio", convenção de nomes e o inventário do que já foi produzido. Não gerar artes 100% por IA; os criativos são HTML/CSS renderizados com as cores/fontes do site.

## Deploy

- **GitHub**: https://github.com/luifegja/santosbochnia (repo = esta pasta inteira; o site fica em `site/`)
- **Cloudflare Pages**: projeto `santosbochnia`, deploy do diretório `site/` (`npx wrangler pages deploy site --project-name=santosbochnia`)
- Domínio final santosbochnia.adv.br: adicionar como custom domain no painel Cloudflare Pages

## Pendências (aguardando o cliente)

- Números OAB dos sócios → inserir nos pontos `<!-- TODO: incluir OAB/SP nº -->` (index + 4 LPs)
- **Confirmar o 23º estado de atuação**: a lista enviada pelo cliente tinha 22 UFs únicas (o item "RN/SP" duplicava estados); o contador diz 23. Faltam na lista: AC, MA, RR, SE, TO → destacar o confirmado no mapa
- Anos de experiência combinada (contador da home)
- Fotos profissionais (substituem os "retratos de monograma" JS/SB)
- Meta Pixel / Google Tag nas LPs quando as campanhas forem criadas

## Como testar localmente

```
cd site && python -m http.server 8741   # nunca file:// (módulos ES)
```
Testar: links wa.me de cada página, responsividade 390px, `prefers-reduced-motion` (hero deve cair no fallback estático), console limpo.
