
# Copilot Instructions

## Visão Geral do Repositório

Este repositório contém o relatório técnico do **PIEVDCS** (Plataforma Integrada de Informações para Enfrentamento à Violência Doméstica e Crimes Sexuais), escrito em LaTeX.

## Estrutura do Projeto

- `main.tex` — arquivo principal do documento LaTeX.
- `your_data.tex` — metadados do documento, como autor, título, local e ano.
- `text/write.tex` — conteúdo principal do relatório.
- `text/ref.bib` — referências bibliográficas em BibTeX.
- `text/anexo.tex` — anexos do relatório.
- `structure/report.tex` — configuração de estilo, pacotes e macros reutilizáveis.
- `figure/` — figuras e imagens utilizadas no relatório.
- `cod/` — códigos-fonte referenciados no texto.
- `make.sh` — script de compilação do PDF.

## Como Compilar

Use:

```bash
chmod +x make.sh
./make.sh
```

O script executa a sequência:

`pdflatex -> bibtex -> pdflatex -> pdflatex`

## Dependências no Linux (Debian/Ubuntu)

```bash
sudo apt install texlive-latex-extra texlive-lang-portuguese abntex abntex2 texlive-science biber
```

## Regras de Edição

- Todo o conteúdo deve ser escrito em **português brasileiro**.
- Manter **tom formal, técnico, objetivo e assertivo**.
- Seguir o padrão acadêmico e a estrutura já existente no relatório.
- **Não modificar** `structure/report.tex`.
- **Não modificar** `your_data.tex`, salvo solicitação explícita.
- Ao adicionar conteúdo em `text/write.tex`, seguir o padrão:
  - `\section{}`
  - `\subsection{}`
  - `\par`
- Ao sugerir texto, preservar compatibilidade com LaTeX e ABNT.
- Ao sugerir referências, adicionar entradas em `text/ref.bib` e usar `\cite{}` ou `\citeonline{}`.
- Não editar `main.pdf` diretamente.

## Fonte Técnica para Atualização do Relatório

Ao atualizar o relatório da plataforma, usar como base o repositório:

- **Projeto:** `pievdcs`
- **Branch:** `63-ogliari`
- **Referência:** https://github.com/OgliariNatan/pievdcs/tree/63-ogliari

## Objetivo Principal

Atualizar o relatório de implementação da plataforma com base no que **está efetivamente implementado** na branch `63-ogliari`.

Isso inclui:

- identificar funcionalidades já implementadas;
- descrever fluxos e módulos existentes;
- registrar tecnologias efetivamente utilizadas;
- remover afirmações não comprovadas pelo código;
- evitar promessas futuras apresentadas como funcionalidades prontas.

## Diretrizes de Conteúdo

- Preferir verbos como:
  - **registrar**
  - **consolidar**
  - **sistematizar**
  - **integrar**
  - **monitorar**
  - **evidenciar**
- Evitar termos vagos como:
  - “moderno”
  - “inovador”
  - “robusto”, sem evidência técnica no código
- Evitar expressões que sugiram criação artificial de fatos, como:
  - “produzir dados”
- Preferir formulações como:
  - “consolidar dados já registrados”
  - “sistematizar informações”
  - “compilar ocorrências registradas pelas instituições”

## Conduta do Copilot

Ao analisar ou propor alterações:

1. verificar o que existe no código da branch `63-ogliari`;
2. descrever apenas funcionalidades confirmáveis;
3. manter consistência terminológica entre relatório e sistema;
4. preservar a estrutura do documento em LaTeX;
5. propor textos prontos para substituição, quando possível.

## Saída Esperada

Quando sugerir alterações:

- indicar o arquivo de destino;
- entregar trechos prontos em LaTeX;
- manter redação formal, técnica e direta;
- usar citações bibliográficas quando houver fonte externa;
- diferenciar claramente:
  - funcionalidade implementada;
  - funcionalidade planejada;
  - contexto teórico ou jurídico.

## Restrições

- Não inventar módulos, telas ou fluxos não verificados.
- Não alterar a configuração estrutural do template.
- Não reescrever o relatório inteiro sem necessidade.
- Não usar linguagem promocional.