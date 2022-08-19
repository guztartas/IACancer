## Geral

O modelo foi construído usando **fastai**, que é uma API de alto nível para pytorch. O classificador foi treinado usando o [conjunto de imagens Kaggle MNIST HAM10000](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000), que contém 10.015 imagens de sete categorias de lesões de pele pigmentadas. Como etapa de pré-processamento, apliquei subamostragem aleatória aos dados para aliviar o problema de desequilíbrio de classe. O classificador foi construído com a técnica de aprendizado de transferência usando um modelo **Densenet169** pré-treinado. O classificador final obteve uma precisão de **91,2%** e um F1-score de **91,7%** nos dados de validação. Você pode conferir o jupyter que acompanha todos os passos que foram dados para construir o modelo. 

## Prints
![Skin Cancer Detector](url) 
![Skin Cancer Detector](url)

## Dependências

- Python <br/>
- Fastai 1.0.57 <br/>
- Flask <br/>
- Django <br/>
- Gunicorn

## Instructions
Instale as dependências e depois, rode o comando `python app.py`. Acesse pelo local: http://localhost:8008.