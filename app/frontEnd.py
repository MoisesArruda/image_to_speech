import streamlit as st


###############################
### Inicializando o agente ###
###############################

# Definir titulo
st.title('Faça uma pergunta sobre a imagem!')

# Definindo o cabeçalho
st.header('Por favor, envie uma imagem.')

# Enviar arquivo
file = st.file_uploader("", type=["jpeg","png", "jpg"])

if file:
    # Visualizar imagem
    st.image(file,use_column_width=True)

    # Input texto
    user_question= st.text_input("Pergunto algo sobre a imagem")

###############################
### Resposta do agente ###
###############################
    
    # Resposta do agente
    if user_question and user_question != "":
        st.write("Resposta não definida")



