# projeto-trainee
Esse repositório é dedicado ao desenvolvimento do projeto de previsão de preços de imóveis (House Prices) para o processo de trainee da Cati Jr.

## Objetivo:
* Repositório dedicado ao acompanhamento do desenvolvimento do modelo de Machine Learning, análises estatísticas e tratamento de dados para a entrega do projeto trainee.

## Ferramentas utilizadas:
* Python
* VS Code / Jupyter Notebook
* Pandas
* Numpy
* Seaborn
* Matplotlib
* Scikit-Learn

## Estrutura do repositório:
* **README.md**: Documentação principal do projeto.
* **.gitignore**: Arquivo para ignorar arquivos desnecessários no controle de versão (como a pasta `.venv`).
* **projeto_trainee.ipynb**: Jupyter Notebook principal contendo a EDA e o modelo preditivo.
* **train.csv**: Base de dados para treino do modelo.
* **test.csv**: Base de dados para testes do modelo.
* **data_description.txt**: Arquivo descritivo com o significado de todas as colunas do dataset.
* **submission.csv**: Arquivo contendo o conteúdo final do projeto.

## Cronograma de Desenvolvimento:
* Bloco 01: Análise Exploratória de Dados (EDA) e Visualização das correlações.
* Bloco 02: Diagnóstico e Tratamento de Valores Ausentes (Missing Values).
* Bloco 03: Diagnóstico e Tratamento de Outliers.
* Bloco 04: Engenharia de Recursos (Feature Engineering) e Pré-processamento.
* Bloco 05: Construção, Treinamento e Avaliação dos Modelos de Machine Learning.

### Como Rodar o Projeto

Para reproduzir este projeto e rodar o notebook na sua máquina local, siga o passo a passo abaixo:

* 1. Clonar o Repositório

Abra o terminal e clone este repositório utilizando o Git:

git clone [https://github.com/JoaoAntoni07/projeto-trainee-2026.git](https://github.com/JoaoAntoni07/projeto-trainee-2026.git)
cd projeto-trainee-2026


* 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)

**No Linux/macOS**:

python3 -m venv .venv 

source .venv/bin/activate


**No Windows**:

python -m venv .venv 

.venv\Scripts\activate


* 3. Instalar as Dependências

pip install pandas numpy scikit-learn matplotlib seaborn notebook


* 4. Executar o Jupyter Notebook

jupyter notebook


### Como Rodar o app
* 1. Crie o arquivo: No seu VS Code, crie um novo arquivo .py na mesma pasta onde estão o notebook e o train.csv. Cole o código de main.py nele.
* 2. Instale o Streamlit com o comando: pip install streamlit
* 3. Rode o comando: streamlit run "seuarquivo".py (substitua "seuarquivo" pelo nome que você salvou o .py)