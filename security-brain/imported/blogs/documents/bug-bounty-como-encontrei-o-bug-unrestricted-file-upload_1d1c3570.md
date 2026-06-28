---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-02_bug-bounty-como-encontrei-o-bug-unrestricted-file-upload.md
original_filename: 2023-04-02_bug-bounty-como-encontrei-o-bug-unrestricted-file-upload.md
title: 'Bug Bounty: como encontrei o bug Unrestricted File Upload'
category: documents
detected_topics:
- sso
- idor
- command-injection
- file-upload
- api-security
- mobile-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- file-upload
- api-security
- mobile-security
language: en
raw_sha256: 1d1c3570449c17c4c609b3b1ccd007077de64c02bd2cfd846fa2b1a4dc75b676
text_sha256: 60541f6ea75d5d8ebd1b0cb1fee47af42b127ef26f71669dd8020497be19895c
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty: como encontrei o bug Unrestricted File Upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-02_bug-bounty-como-encontrei-o-bug-unrestricted-file-upload.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, file-upload, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `1d1c3570449c17c4c609b3b1ccd007077de64c02bd2cfd846fa2b1a4dc75b676`
- Text SHA256: `60541f6ea75d5d8ebd1b0cb1fee47af42b127ef26f71669dd8020497be19895c`


## Content

---
title: "Bug Bounty: como encontrei o bug Unrestricted File Upload"
url: "https://medium.com/@paulo_mota/bug-bounty-como-encontrei-o-bug-unrestricted-file-upload-dd1a61adc9fd"
authors: ["Paulo Mota"]
bugs: ["Unrestricted file upload"]
bounty: "100"
publication_date: "2023-04-02"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1311
scraped_via: "browseros"
---

# Bug Bounty: como encontrei o bug Unrestricted File Upload

Bug Bounty: como encontrei o bug Unrestricted File Upload
pm
Follow
3 min read
·
Apr 3, 2023

55

Press enter or click to view image in full size

Salve pessoal, faz um bom tempo que não escrevo artigos pois venho focando bastante nos meus estudos de pentest e pentest em web apps.

Meu intuito com este artigo é de contribuir com a comunidade de cybersegurança, para que desenvolvedores e empresas saibam como corrigir este tipo de vulnerabilidade, e contribuir com pesquisadores e ethical hackers a encontrarem vulnerabilidades deste tipo “in the wild”.

Contexto

A empresa (nome fictício) redacted.com é uma empresa de Recursos Humanos com várias aplicações web em URLs diferentes. A aplicação que explorei te permite criar um perfil profissional direcionado para a sua área de atuação, criação de um currículo diretamente no site e o upload do seu currículo.

O bug

Plataforma do programa: Intigriti

Nome original: CWE-602: Client-Side Enforcement of Server-Side Security

Criticidade: Média (Avaliação feita pela Intigriti)

Ferramenta que utilizei para encontrar: BurpSuite Community e Kali Linux

Bounty: 100€

Relato

Depois de conhecer o funcionamento do site e de todas as suas opções, foquei na parte de upload de currículos. O website apenas permite que arquivos em .pdf, .doc ou .docx

Get pm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Após alguns testes, notei que o site apenas restringe o formato dos arquivos pela extensão presente no nome do arquivo. Ou seja, eu tentei subir arquivos .exe, .php e sempre me retornavam erros.

Usando o Kali, criei alguns scripts de shell reverso (quem acredita sempre alcança rs) no formato .sh e .aspx e renomeei de reverse.aspx para reverse.aspx.pdf, e dessa forma consegui que os scripts subissem para o servidor.

Minha requisição PUT (resumida):

------WebKitFormBoundary xyz
Content-Disposition: form-data; name="uploadedFile"; filename="reverse.aspx.pdf"
Content-Type: application/pdf
...

Response do servidor (resumida):

HTTP/1.1 201 Created
Content-Length: 111
Connection: close
Content-Type: application/json; charset=utf-8
...

E assim consegui fazer o upload do arquivo.

Porém, desta forma, ainda não temos um arquivo executável do outro lado. Tentei baixar o arquivo pelo site e ele veio .aspx.pdf.

Analisando a requisição POST do arquivo “malicioso”, reparei que o cabeçalho HTTP Content-type (que indica o tipo do arquivo que está sendo tratado na requisição) é definido no lado do cliente, ou seja, no meu navegador. É como se o servidor confiasse no meu envio.

Então dentro do BurpSuite, enviei a rqeuisição POST para o Repeater e mudei o Content-type de application/pdf para text/html:

------WebKitFormBoundary xyz
Content-Disposition: form-data; name="uploadedFile"; filename="reverse.aspx.pdf"
Content-Type: text/html

e pronto! Baixei o arquivo de volta para o meu computador e ele voltou certinho, como .aspx:

Tentei com diversos outros tipos de arquivo: scripts shell (.sh), executáveis (.exe), .php, .jsp, e também funcionou. Com esta vulnerabilidade, é possível infectar a rede de computadores de uma empresa, envio de ransomware, dentre várias outras possibilidades.
