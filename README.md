# Chat conversacional com sua imagem.

Este repositório tem o objetivo de detalhar o desenvolvimento de um agente conversacional utilizando imagens como input.

![Aplicação](https://github.com/MoisesArruda/image_to_speech/blob/main/images/Screenshot_1.png)

# Instalação

1. Clone o repositório:

```bash
git clone https://github.com/MoisesArruda/image_to_speech
```

2. Mude para o diretório do projeto:
 ```bash
cd image_to_speech
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

4. Obtenha sua OpenAI API key. Faça login e acesse sua chave em [OpenAi](https://platform.openai.com/).

5. Substitua a chave de API no espaço reservado no arquivo main.py pela sua chave de API OpenAI:
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
4. O agente conversacional de IA irá gerar uma resposta ccom base na pergunta e na imagem.
5. A resposta irá aparecer.

# Tecnologias

Este projeto utiliza o OpenAI GPT-3.5 Turbo model. Visite [OpenAI](https://openai.com/) para mais informações.

A interface interativa é desenvolvida com a biblioteca Streamlit. Consulte a [documentação do Streamlit](https://docs.streamlit.io/) para mais detalhes.

O agente de IA conversacional e as ferramentas são gerenciados pela biblioteca LangChain. Confira o [repositório do LangChain no Github](https://github.com/langchain-ai/langchain) para obter mais informações.

A biblioteca transformers é empregada para inferir recursos de IA. Visite [esta](https://huggingface.co/Salesforce/blip-image-captioning-large) e [esta](https://huggingface.co/facebook/detr-resnet-50) página no [HuggingFace](https://huggingface.co/) para obter descrições detalhadas dos modelos utilizados.

# Tools

A aplicação utiliza as seguintes ferramentas:

* ImageCaptionTool: Gera uma legenda textual para a imagem carregada.
* ObjectDetectionTool: Executa a detecção de objetos na imagem carregada e identifica os objetos presentes.
