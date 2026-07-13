# -*- coding: utf-8 -*-
"""Gera as 3 variações de carrossel a partir do template previdenciário."""
import io, sys

tpl = open("previdenciario-carrossel-01.html", encoding="utf-8").read()

def make(filename, replacements, extra_css=""):
    out = tpl
    for old, new in replacements:
        assert old in out, f"nao achou em {filename}: {old[:70]}"
        out = out.replace(old, new)
    if extra_css:
        out = out.replace("</style>", extra_css + "\n</style>")
    import unicodedata
    out = unicodedata.normalize("NFC", out)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(out)
    print("criado:", filename)

FOTO_A = 'src="ref/previdenciario-wide.webp" onerror="this.src=' + "'../../site/assets/img/ia/area-previdenciario.webp'" + '"'

# ============ CONSUMIDOR ============
make("consumidor-carrossel-01.html", [
    ("<title>Carrossel Previdenciário 01", "<title>Carrossel Consumidor 01"),
    (FOTO_A, 'src="../../site/assets/img/ia/area-consumidor.webp"'),
    ('class="bleed bleed-b"><img src="../../site/assets/img/ia/escritorio-interior.webp"',
     'class="bleed bleed-b"><img src="../../site/assets/img/ia/detalhe-biblioteca.webp"'),
    ('<p class="eyebrow">Direito Previdenciário</p>\n    <h1>O INSS <span class="hl">negou</span> seu benefício?</h1>\n    <p class="sub">Isso não precisa ser o fim da história. Em muitos casos, a decisão pode ser questionada.</p>',
     '<p class="eyebrow">Direito do Consumidor</p>\n    <h1>Apareceu um <span class="hl">desconto</span> no seu benefício que você não reconhece?</h1>\n    <p class="sub">Empréstimo que você nunca contratou? Cartão RMC/RCC que nunca pediu? Você não precisa aceitar.</p>'),
    ("<h2>Alguma dessas histórias parece a&nbsp;sua?</h2>", "<h2>Alguma dessas situações parece a&nbsp;sua?</h2>"),
    ('<div class="chk"><strong>Aposentadoria negada</strong> por idade, tempo de contribuição ou especial</div>',
     '<div class="chk"><strong>Empréstimo no seu nome</strong> que você nunca contratou</div>'),
    ('<div class="chk"><strong>Auxílio-doença cessado</strong> antes de você poder voltar a trabalhar</div>',
     '<div class="chk"><strong>Desconto de RMC ou RCC</strong> sem você ter pedido o cartão</div>'),
    ('<div class="chk"><strong>BPC/LOAS indeferido</strong> para você ou alguém da família</div>',
     '<div class="chk"><strong>Dívida renovada ou refinanciada</strong> sem a sua autorização</div>'),
    ('<div class="chk"><strong>Tempo rural ou doméstico</strong> que o INSS não reconheceu</div>',
     '<div class="chk"><strong>O banco ficando com quase todo</strong> o seu benefício ou salário</div>'),
    ('<h2>Em muitos casos, a negativa <span class="hl-light">pode ser revista</span>.</h2>',
     '<h2>Descontos indevidos <span class="hl-light">podem ser contestados</span>.</h2>'),
    ('<div class="via"><span class="n">1</span><span class="t">Recurso administrativo</span><span class="d">prazos a partir da ciência da decisão</span></div>',
     '<div class="via"><span class="n">1</span><span class="t">Cancelamento do contrato</span><span class="d">quando não houve contratação válida</span></div>'),
    ('<div class="via"><span class="n">2</span><span class="t">Ação judicial</span><span class="d">quando a via administrativa não resolve</span></div>',
     '<div class="via"><span class="n">2</span><span class="t">Devolução dos valores</span><span class="d">em determinados casos, em dobro</span></div>'),
    ('<div class="via"><span class="n">3</span><span class="t">Novo requerimento</span><span class="d">com a documentação adequada</span></div>',
     '<div class="via"><span class="n">3</span><span class="t">Revisão da margem consignável</span><span class="d">a lei limita quanto podem descontar</span></div>'),
    ('<p class="nota">Cada caso exige análise individual — e é exatamente isso que fazemos.</p>',
     '<p class="nota">Cada caso exige análise individual — comece pelo seu extrato do Meu&nbsp;INSS.</p>'),
    ('<div class="nome">Simone Bochnia dos Anjos</div>\n        <div class="cargo">Sócia-fundadora — Direito Previdenciário</div>\n        <p class="bio">Especialista em Direito Previdenciário, conduz cada caso com rigor técnico e acompanhamento próximo e humanizado.</p>',
     '<div class="nome">Equipe Santos &amp; Bochnia</div>\n        <div class="cargo">Direito do Consumidor — fraudes bancárias</div>\n        <p class="bio">Equipe coordenada pelos sócios-fundadores José Eduardo dos Santos e Simone Bochnia dos Anjos: rigor técnico e atendimento direto.</p>'),
    ('<h2>Vamos analisar o seu&nbsp;caso.</h2>\n    <p class="sub">Conte sua situação pelo WhatsApp e entenda seus direitos em linguagem simples.</p>',
     '<h2>Chega de descontos que você não&nbsp;pediu.</h2>\n    <p class="sub">Envie seu extrato pelo WhatsApp e entenda o que pode ser contestado.</p>'),
    ('<h1>O INSS negou seu benefício? <span class="hl">Você pode ter direito a recorrer.</span></h1>',
     '<h1>Empréstimo que você não contratou? <span class="hl">Desconto estranho no benefício?</span></h1>'),
    ('<div class="chk"><strong>Aposentadoria</strong> negada</div>', '<div class="chk"><strong>Empréstimo</strong> não contratado</div>'),
    ('<div class="chk"><strong>Auxílio-doença</strong> cessado</div>', '<div class="chk"><strong>Desconto de RMC/RCC</strong> no benefício</div>'),
    ('<div class="chk"><strong>BPC/LOAS</strong> indeferido</div>', '<div class="chk"><strong>Dívida renovada</strong> sem autorização</div>'),
    ('<img class="wm" src="../../site/assets/img/monograma-sb.webp" alt="">\n    <p class="eyebrow">Direito Previdenciário</p>',
     '<img class="wm" src="../../site/assets/img/monograma-sb.webp" alt="">\n    <p class="eyebrow">Direito do Consumidor</p>'),
])

# ============ PENAL ============
make("penal-economico-carrossel-01.html", [
    ("<title>Carrossel Previdenciário 01", "<title>Carrossel Penal Econômico 01"),
    (FOTO_A, 'src="ref/penal-wide.webp"'),
    ('class="bleed bleed-b"><img src="../../site/assets/img/ia/escritorio-interior.webp"',
     'class="bleed bleed-b"><img src="../../site/assets/img/ia/balanca-abstrata.webp"'),
    ('<p class="eyebrow">Direito Previdenciário</p>\n    <h1>O INSS <span class="hl">negou</span> seu benefício?</h1>\n    <p class="sub">Isso não precisa ser o fim da história. Em muitos casos, a decisão pode ser questionada.</p>\n    <div class="brandmark"><img src="../../site/assets/img/logo-dark.png" alt="Santos & Bochnia"></div>\n    <div class="swipe"><span>arraste</span><span class="chev">››</span></div>',
     '<p class="eyebrow eyebrow--light">Direito Penal Econômico</p>\n    <h1>Intimação, investigação ou busca e apreensão? <span class="hl-light">Cada hora importa.</span></h1>\n    <p class="sub">Defesa técnica e sigilosa em casos de natureza econômica — desde o primeiro contato.</p>\n    <div class="brandmark"><img src="../../site/assets/img/logo-light.png" alt="Santos & Bochnia"></div>\n    <div class="swipe swipe--dark"><span>arraste</span><span class="chev">››</span></div>'),
    ("<h2>Alguma dessas histórias parece a&nbsp;sua?</h2>", "<h2>Você precisa de defesa técnica&nbsp;se…</h2>"),
    ('<p class="eyebrow">Situações comuns</p>', '<p class="eyebrow">Situações que exigem urgência</p>'),
    ('<div class="chk"><strong>Aposentadoria negada</strong> por idade, tempo de contribuição ou especial</div>',
     '<div class="chk"><strong>Recebeu intimação</strong> da Polícia Federal, do MP ou da Receita</div>'),
    ('<div class="chk"><strong>Auxílio-doença cessado</strong> antes de você poder voltar a trabalhar</div>',
     '<div class="chk"><strong>Sua empresa está sob fiscalização</strong> com potencial desdobramento penal</div>'),
    ('<div class="chk"><strong>BPC/LOAS indeferido</strong> para você ou alguém da família</div>',
     '<div class="chk"><strong>Foi citado</strong> em investigação ou operação</div>'),
    ('<div class="chk"><strong>Tempo rural ou doméstico</strong> que o INSS não reconheceu</div>',
     '<div class="chk"><strong>Teve bens ou contas bloqueados</strong> judicialmente</div>'),
    ('<h2>Em muitos casos, a negativa <span class="hl-light">pode ser revista</span>.</h2>',
     '<h2>Agir cedo <span class="hl-light">preserva alternativas</span>.</h2>'),
    ('<div class="via"><span class="n">1</span><span class="t">Recurso administrativo</span><span class="d">prazos a partir da ciência da decisão</span></div>',
     '<div class="via"><span class="n">1</span><span class="t">Avaliação sigilosa</span><span class="d">situação, fase processual e riscos imediatos</span></div>'),
    ('<div class="via"><span class="n">2</span><span class="t">Ação judicial</span><span class="d">quando a via administrativa não resolve</span></div>',
     '<div class="via"><span class="n">2</span><span class="t">Defesa técnica</span><span class="d">no inquérito e na ação penal</span></div>'),
    ('<div class="via"><span class="n">3</span><span class="t">Novo requerimento</span><span class="d">com a documentação adequada</span></div>',
     '<div class="via"><span class="n">3</span><span class="t">Compliance preventivo</span><span class="d">para empresas expostas a riscos</span></div>'),
    ('<p class="nota">Cada caso exige análise individual — e é exatamente isso que fazemos.</p>',
     '<p class="nota">O sigilo profissional protege tudo o que você nos relatar — desde a primeira conversa.</p>'),
    ('<div class="mono">SB</div>', '<div class="mono">JS</div>'),
    ('<div class="nome">Simone Bochnia dos Anjos</div>\n        <div class="cargo">Sócia-fundadora — Direito Previdenciário</div>\n        <p class="bio">Especialista em Direito Previdenciário, conduz cada caso com rigor técnico e acompanhamento próximo e humanizado.</p>',
     '<div class="nome">José Eduardo dos Santos</div>\n        <div class="cargo">Sócio-fundador — Direito Penal Econômico</div>\n        <p class="bio">Especialização em Direito Penal Econômico pela FGV. Conduz casos complexos com visão estratégica e discrição.</p>'),
    ('<span class="chip">Sigilo profissional</span>', '<span class="chip">Sigilo absoluto</span>'),
    ('<span class="chip">Primeira conversa sem compromisso</span>\n      <span class="chip">Atendimento em todo o Brasil</span>',
     '<span class="chip">Urgências tratadas com prioridade</span>\n      <span class="chip">Atendimento em todo o Brasil</span>'),
    ('<h2>Vamos analisar o seu&nbsp;caso.</h2>\n    <p class="sub">Conte sua situação pelo WhatsApp e entenda seus direitos em linguagem simples.</p>',
     '<h2>Fale com&nbsp;discrição.</h2>\n    <p class="sub">Canal direto e sigiloso, direto com o advogado responsável.</p>'),
    ('<h1>O INSS negou seu benefício? <span class="hl">Você pode ter direito a recorrer.</span></h1>',
     '<h1>Intimado ou sob investigação? <span class="hl">Aja antes do primeiro depoimento.</span></h1>'),
    ('<div class="chk"><strong>Aposentadoria</strong> negada</div>', '<div class="chk"><strong>Intimação</strong> da PF, MP ou Receita</div>'),
    ('<div class="chk"><strong>Auxílio-doença</strong> cessado</div>', '<div class="chk"><strong>Operação</strong> ou bloqueio de bens</div>'),
    ('<div class="chk"><strong>BPC/LOAS</strong> indeferido</div>', '<div class="chk"><strong>Empresa</strong> sob fiscalização</div>'),
    ('<img class="wm" src="../../site/assets/img/monograma-sb.webp" alt="">\n    <p class="eyebrow">Direito Previdenciário</p>',
     '<img class="wm" src="../../site/assets/img/monograma-sb.webp" alt="">\n    <p class="eyebrow">Direito Penal Econômico</p>'),
], extra_css="""
  /* tema penal: card 1 escuro */
  .bg-1 { background: radial-gradient(900px 500px at 88% 0%, rgba(119,185,201,.14), transparent 60%), linear-gradient(168deg, #10344F 0%, var(--navy-deep) 100%) !important; }
  .card-1 h1 { color: #fff; }
  .card-1 .sub { color: #B9CFDD !important; }
  .ghost-2 { color: rgba(255,255,255,.07) !important; }
  .bleed-b { width: 520px; height: 340px; }
  .bleed-b img { object-position: 50% 42%; }
""")

# ============ IMOBILIÁRIO ============
make("imobiliario-carrossel-01.html", [
    ("<title>Carrossel Previdenciário 01", "<title>Carrossel Imobiliário 01"),
    (FOTO_A, 'src="../../site/assets/img/ia/area-imobiliario.webp"'),
    ('class="bleed bleed-b"><img src="../../site/assets/img/ia/escritorio-interior.webp"',
     'class="bleed bleed-b"><img src="../../site/assets/img/ia/faria-lima-fachada.webp"'),
    ('<p class="eyebrow">Direito Previdenciário</p>\n    <h1>O INSS <span class="hl">negou</span> seu benefício?</h1>\n    <p class="sub">Isso não precisa ser o fim da história. Em muitos casos, a decisão pode ser questionada.</p>',
     '<p class="eyebrow">Direito Imobiliário</p>\n    <h1>Vai assinar a compra de um imóvel? <span class="hl">Antes, deixe um advogado&nbsp;ler.</span></h1>\n    <p class="sub">O imóvel é o maior patrimônio da sua vida — proteja-o antes de assinar.</p>'),
    ("<h2>Alguma dessas histórias parece a&nbsp;sua?</h2>", "<h2>Esta história pode ser a&nbsp;sua…</h2>"),
    ('<div class="chk"><strong>Aposentadoria negada</strong> por idade, tempo de contribuição ou especial</div>',
     '<div class="chk"><strong>A construtora atrasou</strong> a entrega da sua obra</div>'),
    ('<div class="chk"><strong>Auxílio-doença cessado</strong> antes de você poder voltar a trabalhar</div>',
     '<div class="chk"><strong>Você quer desfazer a compra</strong> (distrato) e não sabe seus direitos</div>'),
    ('<div class="chk"><strong>BPC/LOAS indeferido</strong> para você ou alguém da família</div>',
     '<div class="chk"><strong>O imóvel está sem escritura</strong> ou precisa de regularização</div>'),
    ('<div class="chk"><strong>Tempo rural ou doméstico</strong> que o INSS não reconheceu</div>',
     '<div class="chk"><strong>Você possui o imóvel há anos</strong> e pensa em usucapião</div>'),
    ('<h2>Em muitos casos, a negativa <span class="hl-light">pode ser revista</span>.</h2>',
     '<h2>A segurança vem <span class="hl-light">antes da assinatura</span>.</h2>'),
    ('<div class="via"><span class="n">1</span><span class="t">Recurso administrativo</span><span class="d">prazos a partir da ciência da decisão</span></div>',
     '<div class="via"><span class="n">1</span><span class="t">Due diligence</span><span class="d">certidões do imóvel e de quem vende</span></div>'),
    ('<div class="via"><span class="n">2</span><span class="t">Ação judicial</span><span class="d">quando a via administrativa não resolve</span></div>',
     '<div class="via"><span class="n">2</span><span class="t">Revisão do contrato</span><span class="d">cláusulas, prazos e garantias</span></div>'),
    ('<div class="via"><span class="n">3</span><span class="t">Novo requerimento</span><span class="d">com a documentação adequada</span></div>',
     '<div class="via"><span class="n">3</span><span class="t">Regularização e usucapião</span><span class="d">inclusive pela via extrajudicial (cartório)</span></div>'),
    ('<p class="nota">Cada caso exige análise individual — e é exatamente isso que fazemos.</p>',
     '<p class="nota">Um contrato revisado hoje evita anos de litígio amanhã.</p>'),
    ('<div class="nome">Simone Bochnia dos Anjos</div>\n        <div class="cargo">Sócia-fundadora — Direito Previdenciário</div>\n        <p class="bio">Especialista em Direito Previdenciário, conduz cada caso com rigor técnico e acompanhamento próximo e humanizado.</p>',
     '<div class="nome">Equipe Santos &amp; Bochnia</div>\n        <div class="cargo">Direito Imobiliário</div>\n        <p class="bio">Coordenação dos sócios-fundadores — José Eduardo dos Santos (especialização em Contratos pelo Insper) e Simone Bochnia dos Anjos.</p>'),
    ('<span class="chip">Sigilo profissional</span>', '<span class="chip">Análise antes de assinar</span>'),
    ('<h2>Vamos analisar o seu&nbsp;caso.</h2>\n    <p class="sub">Conte sua situação pelo WhatsApp e entenda seus direitos em linguagem simples.</p>',
     '<h2>Assine com&nbsp;segurança.</h2>\n    <p class="sub">Envie o contrato ou conte sua situação pelo WhatsApp.</p>'),
    ('<h1>O INSS negou seu benefício? <span class="hl">Você pode ter direito a recorrer.</span></h1>',
     '<h1>Obra atrasada? Imóvel sem escritura? <span class="hl">Proteja seu patrimônio.</span></h1>'),
    ('<div class="chk"><strong>Aposentadoria</strong> negada</div>', '<div class="chk"><strong>Atraso de obra</strong> e distrato</div>'),
    ('<div class="chk"><strong>Auxílio-doença</strong> cessado</div>', '<div class="chk"><strong>Usucapião</strong> e regularização</div>'),
    ('<div class="chk"><strong>BPC/LOAS</strong> indeferido</div>', '<div class="chk"><strong>Análise completa</strong> antes de comprar</div>'),
    ('<img class="wm" src="../../site/assets/img/monograma-sb.webp" alt="">\n    <p class="eyebrow">Direito Previdenciário</p>',
     '<img class="wm" src="../../site/assets/img/monograma-sb.webp" alt="">\n    <p class="eyebrow">Direito Imobiliário</p>'),
])

print("concluído")
