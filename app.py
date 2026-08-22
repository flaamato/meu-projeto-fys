import streamlit as st
from google import genai

# Configuração da página
st.set_page_config(page_title="Copiloto FYS", page_icon="🥤")

st.title("🥤 Copiloto de Vendas FYS")
st.markdown("Assistente tático para quebra de objeções no PDV.")

# Campo para o usuário colocar a chave da API com segurança
api_key = st.text_input("Sua API Key do Gemini (Cole aqui para testar):", type="password")

# Caixa de texto para o vendedor
relato = st.text_area("O que o cliente disse?", 
                      placeholder="Ex: O dono da padaria disse que tá na correria e que o cliente só toma a marca líder...")

if st.button("Analisar Objeção"):
    if not relato:
        st.warning("Por favor, digite o relato do cliente.")
    elif not api_key:
        st.error("⚠️ Você precisa inserir uma API Key do Gemini para a IA pensar.")
    else:
        with st.spinner("Analisando o perfil do cliente e buscando argumentos da FYS..."):
            try:
                # Inicializa o cliente do Gemini
                client = genai.Client(api_key=api_key)
                
                # Aqui nós enviamos o contexto que criamos no projeto para a IA
                prompt_sistema = "Você é o Copiloto Estratégico da marca FYS (refrigerante com menos açúcar do Grupo Heineken). Analise o relato do vendedor e gere uma resposta tática, classificando o humor do cliente e dando a frase exata para o vendedor falar."
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[prompt_sistema, relato]
                )
                
                st.success("✅ Análise Concluída:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro ao conectar com a IA: {e}")
