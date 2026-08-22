# Copiloto de Vendas FYS: Analisador de Humor e Objeções 🥤

Este projeto é a minha entrega para o desafio "Copiloto de Vendas com IA para Atendimento ao Cliente" da DIO. 

Optei por utilizar o contexto real da marca **FYS** (Grupo HEINEKEN) para criar um assistente focado no time de vendas B2B (Business-to-Business).

## 🎯 Qual tema eu escolhi
Escolhi focar em **Vendas e Objeções**, utilizando o caso real da FYS sugerido no desafio.

## 👤 Quem é o usuário principal da solução
O usuário principal é o **Vendedor de Rota / Executivo de Vendas** que visita padarias, bares e mercados diariamente para tentar introduzir a FYS nos estabelecimentos.

## 💡 Qual problema de vendas ela resolve
O maior desafio do vendedor é lidar com clientes que têm diferentes humores e objeções (pressa, ceticismo, foco em preço). A IA resolve isso **analisando o perfil emocional do cliente** relatado pelo vendedor e entregando um argumento de venda rápido, certeiro e no tom "sem frescura" da FYS.

## ⚙️ Qual abordagem eu usei
Utilizei a abordagem de um **Copiloto Estratégico de Vendas**. Em vez de apenas responder dúvidas, ele cruza os dados do produto com o estado de espírito do cliente, usando o padrão `AGENTS.md` para definir a persona, as regras de classificação (Apressado, Cético, Desconfiado, Aberto) e o formato de saída.

## 📚 Quais informações foram usadas como base de conhecimento
Utilizei a transcrição da live da FYS fornecida no desafio. Ela foi salva na pasta `knowledge/` e instrui a IA sobre os diferenciais da marca:
- Pertence ao portfólio HEINEKEN.
- Tem menos açúcar.
- Comunicação irreverente, direta e menos "corporativa".

## 💬 Exemplo de conversa e resposta gerada

**Vendedor (Input):**
> "Fui na Padaria do João, ele mal olhou na minha cara, disse que tava fechando o caixa e não ia colocar produto novo que não tem saída garantida."

**Copiloto FYS (Output da IA):**
> **Classificação:** Apressado / Cético
> **Por que escolhi essa estratégia:** O cliente quer me dispensar e tem medo de encalhar produto. Vou direto ao ponto falando de grana e giro rápido, sem papo furado.
> **O que dizer ao cliente:** *"João, sei que seu tempo é dinheiro, então serei rápido. Quem compra Heineken com você já procura um produto premium. FYS tem menos açúcar, atrai esse público e deixa uma margem maior no seu caixa. Vamos fazer um teste pequeno de giro rápido sem risco pra você?"*

**Exemplo 2: Cliente Aberto / Comercial**

**Relato do Vendedor (Input):**
> "A dona da hamburgueria artesanal adorou a lata. Ela disse: 'Gostei do visual, mas o que vocês têm de material de marketing pra me ajudar a vender isso junto com os meus combos de hambúrguer'"

**Copiloto FYS (Output da IA):**
> **Classificação:** Aberto / Comercial ("Buscando novidade para atrair público")
>
> **Por que escolhi essa estratégia:** Ela já comprou a estética do produto e, por ser uma hamburgueria artesanal, tem o cenário perfeito. A tática é jogar o charme da marca e mostrar como a FYS eleva o nível do combo dela, atraindo um público que foge do básico.
> 
> **O que dizer ao cliente:** "Você já sacou que a lata tem presença, né? Nós temos um material de ponto de venda super estiloso que foge daquela poluição visual de sempre e vai casar perfeitamente com o seu ambiente. Imagina o combo: seu hambúrguer artesanal com uma FYS gelada. É exatamente a pegada premium e com menos açúcar que atrai o público mais jovem direto pro seu balcão."

## 🚀 Possíveis melhorias futuras
- Integrar esse prompt a um bot de WhatsApp para o vendedor usar via áudio.
- Criar um dashboard onde o gerente de vendas consiga ver quais objeções (preço, pressa, etc.) estão aparecendo mais na rua.
