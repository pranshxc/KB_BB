---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-08_stored-xss-in-appgitbookcom.md
original_filename: 2022-08-08_stored-xss-in-appgitbookcom.md
title: Stored XSS in app.gitbook.com
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
language: en
raw_sha256: 45f118dc2e4084d9d29f0a5c6794121ef110161327017614033679efb9ff3978
text_sha256: 96c1608589a7f5310da862d47bc9464bceb128a994a6b91f1c5ffc55e0e2e7e7
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in app.gitbook.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-08_stored-xss-in-appgitbookcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `45f118dc2e4084d9d29f0a5c6794121ef110161327017614033679efb9ff3978`
- Text SHA256: `96c1608589a7f5310da862d47bc9464bceb128a994a6b91f1c5ffc55e0e2e7e7`


## Content

---
title: "Stored XSS in app.gitbook.com"
url: "https://alpinnnnnn13.medium.com/stored-xss-in-app-gitbook-com-6349f42661f7"
authors: ["Mohammad Alfin Hidayatullah (@Alpinbrainsec)"]
programs: ["GitBook"]
bugs: ["Stored XSS"]
publication_date: "2022-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2355
scraped_via: "browseros"
---

# Stored XSS in app.gitbook.com

Stored XSS in app.gitbook.com
Mohammad Alfin Hidayatullah
Follow
2 min read
·
Aug 8, 2022

8

Halo teman teman, Perkenalkan nama saya Mohammad Alfin Hidayatullah dan saya adalah seorang bug bounty hunter. Kali ini saya ingjn berbagi cerita tentang temuan bug yang saya temukan di [app.gitbook.com]

Apa itu gitbook?? GitBook merupakan sebuah layanan yang membangun format buku yang bersifat open source dengan menggunakan serangkaian alat yang sederhana dan kokoh untuk menulis buku dengan format tersebut. (Codepolitan)

Saya akan langsung menjelaskan bagaimana saya menemukan bug XSS/Cross Site Scripting di website [app.gitbook.com], Sebelumnya saya juga pernah melaporkan bug HTML INJECTION (In email) di Gitbook dan mendapatkan apresiasi berupa swag yang katanya masih dalam antrian.

Get Mohammad Alfin Hidayatullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Saya menemukan bug XSS ini di sebuah kolom yang sangat identik dengan XSS yaitu kolom insert link, Karena kolom ini biasanya ada yang tidak di filter untuk menggunakan HTTP/HTTPS, Saya coba memasukan code javascript biasa seperti javascript:alert() dan ternyata benar kolom tersebut tidak memiliki filter HTTP/HTTPS.

Press enter or click to view image in full size
Kolom insert link
Press enter or click to view image in full size
XSS Pop Up

Setelah mendapatkan respond seperti ini saya langsung mencoba untuk melaporkan nya, selang beberapa hari saya mendapatkan izin untuk membuat artikel tentang temuan saya dan bug nya juga sudah di perbaiki oleh team GitBook.

Kurang lebih seperti itu cerita tentang temuan XSS/Cross Site Scripting yant saya temukan di GitBook, Saya harap bisa bermanfaat untuk teman teman yang ingin mempraktikkan dan saya mohon maaf bila ada salah kata tentant artikel yang saya buat ini. Sekian dan terimakasih.

Contact:alpinbrainsec@gmail.com
