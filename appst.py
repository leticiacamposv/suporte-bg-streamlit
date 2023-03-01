import streamlit as st
#import torch
#from transformers import pipeline, GPTJForCausalLM, AutoTokenizer
import openai
import os

# Page config
st.set_page_config(page_title='Suporte UTUA', page_icon=':eyeglasses:', layout='wide')

# Primary title on page
st.title('Suporte UTUA')

# Sidebar
st.sidebar.markdown("Selecione os parâmetros")
max_length = st.sidebar.number_input('Max length', min_value=1, max_value=2048, value=500, step=1, help='Quantidade máxima de tokens ou "limite de palavras" da resposta. Quanto maior o número de tokens, mais demorada a resposta')
temperature = st.sidebar.slider('Temperature', min_value=0.00, max_value=1.00, step=0.01, help='Controla a aleatoriedade do texto gerado. Quanto maior a temperatura, mais "criativo" e arriscad será o modelo. ')
top_p = st.sidebar.slider('Top P', min_value=0.00, max_value=1.00, step=0.01, help='Grau de consideração de inclusão de palavras com probabilidades menores aparecerem no texto. Também controla a criatividade')
freq_penalty = st.sidebar.slider('Frequency penalty', min_value=0.00, max_value=2.00, step=0.01, help='Grau de penalidade para repetição da mesma palavra em texto')
#epsilon_cutoff =st.sidebar.slider('Epsilon cutoff', min_value=0.000, max_value=1.000, step=0.001, help='Determina um limite mínimo de probabilidade para os tokens a serem usados. Ex: epsilon > 0.7 -> Apenas tokens com mais de 70 porcento de probabilidade serão impressos')
best_of = st.sidebar.slider('Best of', min_value=1, max_value=20, step=1, help='Quantidade de respostas diferentes geradas. Use para efeito de variedade na resposta')
#end = st.sidebar.text_input('Stop sequence')
#Inject start text
#prob = st.sidebar.checkbox('Quantidade de tokens mais provaveis a ser :')

#Playground
prompt = st.text_area('Digite aqui a sua dúvida', height=200)
btn_submit = st.button('Enviar')

#Modelo
os.environ["OPENAI_API_KEY"] = st.secrets["open_api_key"]
openai.api_key = os.getenv("OPENAI_API_KEY")
model_id='davinci:ft-personal:sup-v2-lr0-1-epcs100-dv-2023-02-25-01-27-09'
#default_model = "text-davinci-003"
#Predict
if btn_submit:
    response = openai.Completion.create(model=model_id, 
                                        prompt=(f'Question: {prompt} ->'), 
                                        temperature=temperature, 
                                        top_p=top_p, 
                                        n=best_of, 
                                        frequency_penalty = freq_penalty,
                                        max_tokens=max_length, 
                                        stop=[' END'])
    answer = ':computer: : ' + response.choices[0].text.strip()
  

    st.write(answer)
