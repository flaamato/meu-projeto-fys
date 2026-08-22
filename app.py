import streamlit as st
from google import genai
import os

st.set_page_config(page_title="Copiloto FYS", page_icon="🥤")

st.title("🥤 Copiloto de Vendas FYS")
st.markdown("Assistente tático para quebra de objeções no PDV.")

api_key = st.text_input("Sua API Key do Gemini:", type="password")
relato = st.text_area("Relato do Vendedor:", placeholder="Ex: O cliente achou caro e não tem espaço.")

# Função para ler os arquivos de contexto dinamicamente
def carregar_contexto():
    agente_regras = ""
    conhecimento = ""
    
    if os.path.exists("AGENTS.md"):
        with open("AGENTS.md", "r", encoding="utf-8") as f:
            agente_regras = f.read()
            
    if os.path.exists("knowledge/fys-context.md"):
        with open("knowledge/fys-context.md", "r", encoding="utf-8") as f:
            conhecimento = f.read()
            
    return agente_regras + "\n\n" + conhecimento

if st.button("Analisar Objeção"):
    if not relato or not api_key:
        st.error("⚠️ Preencha o relato e a API Key para continuar.")
    else:
        with st.spinner("Lendo AGENTS.md e analisando perfil..."):
            try:
                client = genai.Client(api_key=api_key)
                
                # O Sistema agora carrega a inteligência direto dos seus arquivos MD!
                contexto_completo = carregar_contexto()
                prompt_sistema = f"Aja estritamente com base nas seguintes regras e base de conhecimento:\n{contexto_completo}\n\nAnalise o seguinte relato:\n{relato}"
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt_sistema
                )
                
                st.success("✅ Estratégia Pronta:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
