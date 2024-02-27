# Chat conversacional com sua imagem.

Este repositório tem o objetio de detalhar o desenvolvimento de um agente conversacional utilizando imagens como input.

# Instalação

1. Clone o repositório:

```bash
git clone 
```

2. Mude para o diretório do projeto:
 ```bash
cd 
```

3. Instale as depêndencias do projeto:
```bash
pip install -r requirements.txt
```

4. Obtenha sua OpenAI API key. Você pode realizar o login e acessar sua key em [OpenAi](https://platform.openai.com/).

5. Substitua a chade de API do espaço reservado no arquivo main.py pela sua chave de API OpenAI:
```bash
 llm = ChatOpenAI(
     openai_api_key='YOUR_API_KEY',
     temperature=0,
     model_name="gpt-3.5-turbo"
 )
```

6. Rode sua aplicação Streamlit:
```bash
 streamlit run main.py
```

7. Abra seu navegador de preferência e vá até http://localhost:8501 para acessar a aplicação.


# Como utilizar

1. Carregue uma imagem clicando no botão de upload.
2. A imagem será carregada.
3. Faça uma pergunta sobre a imagem na caixa de texto.
4. O agente conversacional de IA irá gerar uma resposta baseado na questão e na imagem.
5. A resposta irá aparecer.

# Tecnologias

Este projeto utiliza o OpenAI GPT-3.5 Turbo model. Visite [OpenAI](https://openai.com/) para mais informações.

A biblioteca Streamlit é utilizada para desenvolver a interface interativa. Visite a [documentação do Streamlit](https://docs.streamlit.io/) para mais informações.

A biblioteca do LangChain é usada para gerenciar o agente de IA conversacional e as tools. Visite o [repositório do LangChain no Github](https://github.com/langchain-ai/langchain) para mais informações.

A biblioteca do transformers é usada para inferir os recursos de IA. Visite [esta](https://huggingface.co/Salesforce/blip-image-captioning-large) e [esta](https://huggingface.co/facebook/detr-resnet-50) página do [HuggingFace](https://huggingface.co/) para acessar uma descrição dos modelos utilizados. 

# Tools

A aplicação utiliza as seguintes ferramentas:

* ImageCaptionTool: Gera uma legenda textual para a imagem carregada.
* ObjectDetectionTool: Executa a detecção de objetos na imagem carregada e identifica os objetos presentes.
