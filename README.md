## IA Câncer

O modelo foi construído usando **FASTAI**, que é uma API de alto nível para pytorch. O classificador foi treinado usando o [conjunto de imagens de Harvard](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000), que contém 10.015 imagens de sete categorias de lesões de pele pigmentadas. Como etapa de pré-processamento, apliquei subamostragem aleatória aos dados para aliviar o problema de desequilíbrio de classe. O classificador foi construído com a técnica de aprendizado de transferência usando um modelo **Densenet169** pré-treinado.

## Dependências

- Python <br/>
- Fastai 1.0.57 <br/>
- Flask <br/>
- Django <br/>
- Gunicorn <br/>
- jQuery <br/>
- Bootstrap 

## Instruções
Primeiro, baixe o modelo de imagens e coloque dentro da pasta models, após, instale as dependências e, rode o comando `python app.py`.<br/>
Acesse pelo local: http://localhost:8008
