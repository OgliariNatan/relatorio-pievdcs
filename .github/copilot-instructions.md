# Copilot Instructions

## Visão Geral do Repositório

Este repositório contém o relatório técnico do **PIEVDCS** (Plataforma Integrada de Ações para Enfrentamento à Violência Doméstica e Crimes Sexuais), escrito em LaTeX.

## Estrutura do Projeto

- `main.tex` — Arquivo principal do documento LaTeX (capa, sumário, referências).
- `your_data.tex` — Dados personalizados: nome do autor, título, local, ano, nota explicativa.
- `text/write.tex` — Conteúdo principal do relatório (seções, texto, figuras).
- `text/ref.bib` — Referências bibliográficas em formato BibTeX.
- `text/anexo.tex` — Anexos do relatório.
- `structure/report.tex` — Pacotes LaTeX, configurações de estilo e macros reutilizáveis.
- `figure/` — Imagens e figuras utilizadas no documento.
- `cod/` — Arquivos de código-fonte referenciados no relatório.
- `make.sh` — Script de compilação do documento.

## Como Compilar

```bash
chmod +x make.sh
./make.sh
```

O script executa a sequência: `pdflatex → bibtex → pdflatex → pdflatex` para gerar o `main.pdf`.

**Pacotes necessários (Debian/Ubuntu):**
```bash
sudo apt install texlive-latex-extra texlive-lang-portuguese abntex abntex2 texlive-science biber
```

## Convenções e Boas Práticas

- **Idioma:** Todo o conteúdo do relatório é escrito em **português brasileiro**.
- **Estilo:** Seguir as normas ABNT para formatação de documentos acadêmicos (já configurado em `structure/report.tex`).
- **Macros:** Utilizar as macros definidas em `structure/report.tex` e `your_data.tex` em vez de repetir valores manualmente.
- **Figuras:** Adicionar imagens na pasta `figure/` e referenciá-las com `\includegraphics`.
- **Código-fonte:** Arquivos de código devem ser colocados em `cod/` e incluídos com `\lstinputlisting`.
- **Referências:** Adicionar entradas em `text/ref.bib` e citar com `\cite{}` ou `\citeonline{}`.
- **Não editar** `main.pdf` diretamente — ele é gerado automaticamente pela compilação.

## Observações para o Copilot

- Ao sugerir alterações no conteúdo do relatório, mantenha o português formal e a estrutura LaTeX existente.
- Ao modificar `structure/report.tex`, verifique se os pacotes já estão importados antes de adicionar novos.
- Ao adicionar novas seções em `text/write.tex`, siga o padrão `\section{}` / `\subsection{}` já em uso.
- O arquivo `your_data.tex` centraliza metadados do documento; prefira alterá-lo a duplicar definições.
