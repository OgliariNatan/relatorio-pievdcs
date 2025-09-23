# Relatório PIEVDCS

Este projeto contém o relatório do Projeto Plataforma - Violência Doméstica e Crimes Sexuais (PIEVDCS).

## Estrutura do Projeto
- `main.tex`: Arquivo principal com capa e sumário e outras componentes textuais
- `text/write.tex`: Arquivo do relatório em LaTeX
- `text/ref.bib`: Referências
- `figure/`: Imagens utilizadas no relatório
- `cod/`: Códigos e dados utilizados
- `structure/report.tex`: Estrutura do relatório
- `make.sh`: Script para compilar o relatório


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
