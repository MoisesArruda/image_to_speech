from tempfile import NamedTemporaryFile

import streamlit as st
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from app.tools import ImageCaptionTool, ObjectDetectionTool


##############################
### Inicie o agente. #########
##############################
tools = [ImageCaptionTool(), ObjectDetectionTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

llm = ChatOpenAI(
    openai_api_key='YOUR_API_KEY',
    temperature=0,
    model_name="gpt-3.5-turbo"
)

agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    max_iterations=5,
    verbose=True,
    memory=conversational_memory,
    early_stopping_method='generate'
)

# Título
st.title('Faça uma pergunta sobre a imagem!')

# Cabeçalho
st.header("Por favor carregue uma imagem.")

# Carregue uma imagem
file = st.file_uploader("", type=["jpeg", "jpg", "png"])

if file:
    # imagem de exibição
    st.image(file, use_column_width=True)

    # text input
    user_question = st.text_input('Faça uma pergunta sobre sua imagem:')

    ##############################
    ### Resposta do agente ###
    ##############################
    with NamedTemporaryFile(dir='.') as f:
        f.write(file.getbuffer())
        image_path = f.name

        # Escreva a resposta do agente.
        if user_question and user_question != "":
            with st.spinner(text="Em progresso..."):
                response = agent.run('{}, this is the image path: {}'.format(user_question, image_path))
                st.write(response)