# Relatório PIEVDCS

Este projeto contém o relatório do Projeto Plataforma - Violência Doméstica e Crimes Sexuais (PIEVDCS).

## Estrutura do Projeto
- `main.tex`: Arquivo principal com capa e sumário e outras componentes textuais
- `text/write.tex`: Arquivo do relatório em LaTeX
- `text/ref.bib`: Referências
- `figure/`: Imagens utilizadas no relatório
- `cod/`: Códigos e dados utilizados
- `structure/report.tex`: Estrutura do relatório
- `your_data.tex`: Metadados do documento (autor, título, local, ano)
- `make.sh`: Script para compilar o relatório
- `.github/copilot-instructions.md`: Instruções para o GitHub Copilot


## Como compilar o relatório

Para compilar o relatório, utilize o script `make.sh`: <br>
torne-se executável:

```bash
chmod +x make.sh
```

Em seguida, execute o script:

```bash
./make.sh

```

#### Pacotes necessarios para compilar o relatório:

``` sudo apt install texlive ```

#### Ou instale os pacotes necessarios para compilar o relatório:

``` sudo apt install texlive-latex-extra texlive-lang-portuguese abntex abntex2 texlive-science biber ``` 

## GitHub Copilot

Este repositório possui instruções configuradas para o GitHub Copilot em `.github/copilot-instructions.md`. Essas instruções orientam o Copilot sobre a estrutura do projeto, convenções de estilo, idioma (português brasileiro) e fluxo de compilação LaTeX.

# Relatório em .pdf
[relatorio-pievdcs](https://github.com/OgliariNatan/relatorio-pievdcs/blob/main/main.pdf)
