---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-21_how-to-break-saml-if-i-have-paws.md
original_filename: 2023-09-21_how-to-break-saml-if-i-have-paws.md
title: How to break SAML if I have paws?
category: documents
detected_topics:
- sso
- saml
- access-control
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- sso
- saml
- access-control
- ssrf
- xss
- command-injection
language: en
raw_sha256: af96a2f4d2bb1de203c1e99d28b670402cda7b6cb064e4e372a66da1f04e9af0
text_sha256: 274ef0382e193b078cc4d499f22040bbd09140005e4f0c652bbf4aefa84ad851
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# How to break SAML if I have paws?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-21_how-to-break-saml-if-i-have-paws.md
- Source Type: markdown
- Detected Topics: sso, saml, access-control, ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `af96a2f4d2bb1de203c1e99d28b670402cda7b6cb064e4e372a66da1f04e9af0`
- Text SHA256: `274ef0382e193b078cc4d499f22040bbd09140005e4f0c652bbf4aefa84ad851`


## Content

---
title: "How to break SAML if I have paws?"
page_title: "How to break SAML if I have paws? - Speaker Deck"
url: "https://speakerdeck.com/greendog/how-to-break-saml-if-i-have-paws"
final_url: "https://speakerdeck.com/greendog/how-to-break-saml-if-i-have-paws"
authors: ["Aleksei Tiurin"]
bugs: ["SAML"]
publication_date: "2023-09-21"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 754
---

[ Upgrade to Pro — share decks privately, control downloads, hide ads and more … ](/pro?utm_campaign=upgrade_to_pro&utm_medium=web&utm_source=talk_show)

[ ![Speaker Deck](https://d1eu30co0ohy4w.cloudfront.net/assets/mark-f4be6df1e05965cac9f98e664a6c35f5ffdd0207385d07464a9214d6cdf76082.svg) Speaker Deck ](/)

  * [ Features ](/features)
  * [ Speaker Deck PRO ](/pro?utm_campaign=speakerdeck_pro&utm_medium=web&utm_source=nav_unauthenticated)
  * [ Sign in ](/signin)
  * [ Sign up for free ](/signup)
  *  * Search

  * Search

  * 

[ ![Speaker Deck](https://d1eu30co0ohy4w.cloudfront.net/assets/mark-white-8d908558fe78e8efc8118c6fe9b9b1a9846b182c503bdc6902f97df4ddc9f3af.svg) ](/)

####  How to break SAML if I have paws? 

Search

[ Sponsored · ![](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTkwMDg2LCJwdXIiOiJibG9iX2lkIn19--047929f304419cf6f1beb66c5b05d8fcf9acdff6/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzIwLDIwXX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--6692fd05d267f6c83fd935c6b3ce6d61a961fcaa/avatar.jpg) Your Podcast. Everywhere. Effortlessly. Share. Educate. Inspire. Entertain. You do you. We'll handle the rest. → ](https://fireside.fm/speakerdeck?utm_source=speakerdeck&utm_medium=house_ad&utm_campaign=fireside&utm_content=detail)

[ ![Avatar for GreenDog](https://secure.gravatar.com/avatar/0eb5ff24722856be0e9c4f66faf363be?s=47) GreenDog  ](/greendog)

September 21, 2023 

[ Education ](/c/education)

3k

[ 1 ](/signin?return_to=%2Fgreendog%2Fhow-to-break-saml-if-i-have-paws "Star How to break SAML if I have paws?")

[](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/KazHackStan._SAML_Hacking.pdf "Download PDF")

Share

* * *

Embed

Copy iframe code Copy JS code

* * *

Copy link

Start on current slide 

# How to break SAML if I have paws?

Overview of "how to hack SAML" from a security conference - KazHackStan <https://kazhackstan.com/en/>

In this talk, we will figure out how to break Single Sign On(SSO) based on SAML. Let's look at the components of SAML and the associated attack vectors, current vulnerabilities and methods of their exploitation. Everything a pentester needs to pohakat SAML without soiling the fur.

![Avatar for GreenDog](https://secure.gravatar.com/avatar/0eb5ff24722856be0e9c4f66faf363be?s=128)

##  [GreenDog](/greendog)

September 21, 2023 

## More Decks by GreenDog

[ See All by GreenDog ](/greendog)

[ Weird proxies/2 and a bit of magic  ](/greendog/2-and-a-bit-of-magic " Weird proxies/2 and a bit of magic ")

[ ![Avatar for GreenDog](https://secure.gravatar.com/avatar/0eb5ff24722856be0e9c4f66faf363be?s=24) greendog ](/greendog)

3 

10k

[ Reverse proxies & Inconsistency  ](/greendog/reverse-proxies-and-inconsistency "Reverse proxies & Inconsistency")

[ ![Avatar for GreenDog](https://secure.gravatar.com/avatar/0eb5ff24722856be0e9c4f66faf363be?s=24) greendog ](/greendog)

3 

5.9k

[ MITM Attacks on HTTPS: Another Perspective  ](/greendog/mitm-attacks-on-https-another-perspective "MITM Attacks on HTTPS: Another Perspective")

[ ![Avatar for GreenDog](https://secure.gravatar.com/avatar/0eb5ff24722856be0e9c4f66faf363be?s=24) greendog ](/greendog)

2 

890

[ Deserialization vulnerabilities  ](/greendog/deserialization-vulnerabilities "Deserialization vulnerabilities ")

[ ![Avatar for GreenDog](https://secure.gravatar.com/avatar/0eb5ff24722856be0e9c4f66faf363be?s=24) greendog ](/greendog)

1 

1.1k

## Other Decks in Education

[ See All in Education ](/c/education)

[ BITCOIN : Les fondamentaux !  ](/rlifchitz/bitcoin-les-fondamentaux "BITCOIN : Les fondamentaux !")

[ ![Avatar for Renaud Lifchitz](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5OCwicHVyIjoiYmxvYl9pZCJ9fQ==--b74a45353caf5ced96d70571ff5dcec9e0b0873a/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/rli2.jpg) rlifchitz ](/rlifchitz)

0 

180

[ Curso de Consagração ao Sagrado Coração de Jesus - O Sagrado Coração na História (Aula 01)  ](/cm_manaus/curso-de-consagracao-ao-sagrado-coracao-de-jesus-o-sagrado-coracao-na-historia-aula-01 "Curso de Consagração ao Sagrado Coração de Jesus - O Sagrado Coração na História \(Aula 01\)")

[ ![Avatar for Congregação Mariana da Imaculada Conceição e Santo Afonso de Ligório](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDU2ODQsInB1ciI6ImJsb2JfaWQifX0=--c7c7325b036a4d098b68bbf6cb54148883b9eab0/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/15da9fc679a095a86bd46a422773c25e.png) cm_manaus ](/cm_manaus)

0 

230

[ We部コミュニティスライド2026-04-24  ](/junhat6/webu-komiyuniteisuraido2026-04-24 "We部コミュニティスライド2026-04-24")

[ ![Avatar for junhat6](https://secure.gravatar.com/avatar/9eab81ae2cb018bbdf32745c0468efc0?s=24) junhat6 ](/junhat6)

0 

180

[ AI-Based Speaking Assessment of a Short-Term Study Abroad Program  ](/uranoken/celes2026-urano "AI-Based Speaking Assessment of a Short-Term Study Abroad Program")

[ ![Avatar for Ken Urano](https://secure.gravatar.com/avatar/bac20b7719109838d6be162a560272a0?s=24) uranoken ](/uranoken)

0 

320

[ アラムコSTEAMチャレンジ 実践報告書  ](/codeforeveryone/aramukosteamtiyarenzi-shi-jian-bao-gao-shu "アラムコSTEAMチャレンジ　実践報告書")

[ ![Avatar for みんなのコード](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjI5MjkwLCJwdXIiOiJibG9iX2lkIn19--d1539972fef80775f2300a92444979a44e712a56/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/X%E3%82%A2%E3%82%A4%E3%82%B3%E3%83%B3%20\(1\).png) codeforeveryone ](/codeforeveryone)

0 

140

[ 「機械学習と因果推論」入門 ② 回帰分析から因果分析へ  ](/masakat0/ji-jie-xue-xi-toyin-guo-tui-lun-ru-men-hui-gui-fen-xi-karayin-guo-fen-xi-he "「機械学習と因果推論」入門 ② 回帰分析から因果分析へ")

[ ![Avatar for MasaKat0](https://secure.gravatar.com/avatar/bb6c3fc8c577710c72d03aeb4fa56bf6?s=24) masakat0 ](/masakat0)

0 

710

[ Catecismo 26 #2 - Do Credo; Introdução ao 1º artigo  ](/cm_manaus/catecismo-26-number-2-do-credo-introducao-ao-1o-artigo "Catecismo 26 #2 - Do Credo; Introdução ao 1º artigo")

[ ![Avatar for Congregação Mariana da Imaculada Conceição e Santo Afonso de Ligório](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDU2ODQsInB1ciI6ImJsb2JfaWQifX0=--c7c7325b036a4d098b68bbf6cb54148883b9eab0/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/15da9fc679a095a86bd46a422773c25e.png) cm_manaus ](/cm_manaus)

0 

120

[ 勝手にCULTIBASE で広げよう、探究の輪！ - CULTIVAL 2026  ](/hiroc_sk/katteni-cultibase-cultival-2026 "勝手にCULTIBASE で広げよう、探究の輪！ - CULTIVAL 2026")

[ ![Avatar for Hiroshi SAKAI](https://secure.gravatar.com/avatar/457794fa44d2a93a8ec8d4fcd3352ab0?s=24) hiroc_sk ](/hiroc_sk)

1 

220

[ [2026前期火５] 論理学（京都大学文学部 前期 第5回）「 ならばの問題演習・proof net・かつの規則」  ](/yatabe/2026qian-qi-huo-5-lun-li-xue-jing-du-da-xue-wen-xue-bu-qian-qi-di-5hui-narabanowen-ti-yan-xi-proof-netkatunogui-ze "\[2026前期火５\] 論理学（京都大学文学部 前期 第5回）「  ならばの問題演習・proof net・かつの規則」")

[ ![Avatar for Shunsuke Yatabe](https://secure.gravatar.com/avatar/e631690252d8cf471756c107ace2a1e8?s=24) yatabe ](/yatabe)

0 

290

[ コミュニティを通じた_キャリア設計のススメ_20260424.pdf  ](/masakiokuda/komiyuniteiwotong-zita-kiyariashe-ji-nosusume-20260424 "コミュニティを通じた_キャリア設計のススメ_20260424.pdf")

[ ![Avatar for モブエンジニア（Masaki Okuda）](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjU0NTE2LCJwdXIiOiJibG9iX2lkIn19--f16f724b8e549cd0f1caab41a6c8df69427d4bfe/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGVnIiwicmVzaXplX3RvX2ZpbGwiOlsyNCwyNF19LCJwdXIiOiJ2YXJpYXRpb24ifX0=--b48c0a77ba540dff89d4e01c944dfca4119c9e28/IMG_6032.jpeg) masakiokuda ](/masakiokuda)

0 

330

[ 勾配ブースティングと決定木の話 / gradient boosting and decision trees  ](/kaityo256/gradient-boosting-and-decision-trees "勾配ブースティングと決定木の話 / gradient boosting and decision trees")

[ ![Avatar for kaityo256](https://secure.gravatar.com/avatar/a10e41b0a61d59f2258d7f6172c33479?s=24) kaityo256 ](/kaityo256)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

6 

1.3k

[ The Lotus and the Frog  ](/vyadav/the-lotus-and-the-frog "The Lotus and the Frog")

[ ![Avatar for Vikash Yadav](https://secure.gravatar.com/avatar/78da2c6f045fc451b65ddcda1fe6b401?s=24) vyadav ](/vyadav)

0 

120

## Featured

[ See All Featured ](/p/featured)

[ Mind Mapping  ](/helmedeiros/mind-mapping "Mind Mapping")

[ ![Avatar for Hélio Medeiros](https://secure.gravatar.com/avatar/b870070e35cb43df68fceaee71755106?s=24) helmedeiros ](/helmedeiros)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

1 

250

[ Agile Leadership in an Agile Organization  ](/kimpetersen/agile-leadership-in-an-agile-organization "Agile Leadership in an Agile Organization")

[ ![Avatar for Dr. Kim W Petersen](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExNTk5LCJwdXIiOiJibG9iX2lkIn19--c839f1398dd16406fd4e226a0a615c938c7e32fd/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/Screenshot%20Kim-reduced.jpg) kimpetersen ](/kimpetersen)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

0 

170

[ New Earth Scene 8  ](/popppiees/new-earth-scene-8 "New Earth Scene 8")

[ ![Avatar for Sydney Stone](https://secure.gravatar.com/avatar/b5fe4b96725af20fb5f6b47f89310cea?s=24) popppiees ](/popppiees)

3 

2.3k

[ Breaking role norms: Why Content Design is so much more than writing copy - Taylor Woolridge  ](/uxyall/breaking-role-norms-why-content-design-is-so-much-more-than-writing-copy-taylor-woolridge "Breaking role norms: Why Content Design is so much more than writing copy - Taylor Woolridge")

[ ![Avatar for UX Y'all](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTk3NTksInB1ciI6ImJsb2JfaWQifX0=--5fe8c23b57cf841408c2f2b9ce98cbc1684cf410/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/Social%20Avatar%204.jpg) uxyall ](/uxyall)

0 

320

[ Let's Do A Bunch of Simple Stuff to Make Websites Faster  ](/chriscoyier/lets-do-a-bunch-of-simple-stuff-to-make-websites-faster "Let's Do A Bunch of Simple Stuff to Make Websites Faster")

[ ![Avatar for Chris Coyier](https://secure.gravatar.com/avatar/8081b26e05bb4354f7d65ffc34cbbd67?s=24) chriscoyier ](/chriscoyier)

508 

140k

[ Distributed Sagas: A Protocol for Coordinating Microservices  ](/caitiem20/distributed-sagas-a-protocol-for-coordinating-microservices "Distributed Sagas: A Protocol for Coordinating Microservices")

[ ![Avatar for Caitie McCaffrey](https://secure.gravatar.com/avatar/9128d500301ae51524e887bb680f471d?s=24) caitiem20 ](/caitiem20)

333 

22k

[ Stop Working from a Prison Cell  ](/hatefulcrawdad/stop-working-from-a-prison-cell "Stop Working from a Prison Cell")

[ ![Avatar for Chris Michel](https://secure.gravatar.com/avatar/c1daf20e5c49ff910745198ef9869ac2?s=24) hatefulcrawdad ](/hatefulcrawdad)

274 

21k

[ brightonSEO & MeasureFest 2025 - Christian Goodrich - Winning strategies for Black Friday CRO & PPC  ](/cargoodrich/brightonseo-and-measurefest-2025-christian-goodrich-winning-strategies-for-black-friday-cro-and-ppc "brightonSEO & MeasureFest 2025 - Christian Goodrich - Winning strategies for Black Friday CRO & PPC")

[ ![Avatar for Christian Goodrich](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjgyMDU1LCJwdXIiOiJibG9iX2lkIn19--d48c7fbfb3f0b2943e520d9b3091cdd08add5fbb/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/christian-goodrich-portrait-2026-2%20\(1\).jpg) cargoodrich ](/cargoodrich)

3 

730

[ Navigating the moral maze — ethical principles for Al-driven product design  ](/skipperchong/navigating-the-moral-maze "Navigating the moral maze — ethical principles for Al-driven product design")

[ ![Avatar for Skipper Chong Warson](https://secure.gravatar.com/avatar/766b9746b59e6f09e280cd33cf4ed419?s=24) skipperchong ](/skipperchong)

2 

390

[ We Are The Robots  ](/honzajavorek/we-are-the-robots "We Are The Robots")

[ ![Avatar for Honza Javorek](https://secure.gravatar.com/avatar/7b2e4bf7ecca28e530e1c421f0676c0b?s=24) honzajavorek ](/honzajavorek)

0 

250

[ The #1 spot is gone: here's how to win anyway  ](/tamaranovitovic/the-number-1-spot-is-gone-heres-how-to-win-anyway "The #1 spot is gone: here's how to win anyway")

[ ![Avatar for Tamara Novitovic](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTg5NzUsInB1ciI6ImJsb2JfaWQifX0=--09b4a33635d5c681f1a5ae8b8f1c77092ef781bb/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/shared_image-removebg-preview.png) tamaranovitovic ](/tamaranovitovic)

2 

1.1k

[ Code Review Best Practice  ](/trishagee/code-review-best-practice "Code Review Best Practice")

[ ![Avatar for Trisha Gee](https://secure.gravatar.com/avatar/3d6ace9554821d552146413bcdf874f6?s=24) trishagee ](/trishagee)

74 

20k

## Transcript

  1. ###  [Суповой набор №5а. Как ломать SAML, если у меня лапки?](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_0.jpg "How to break SAML if I have paws? Суповой набор №5а. Как ломать SAML, если у меня...")

How to hack SAML if I have paws? Aleksei “GreenDog” Tiurin 

  2. ###  [WHOAMI? - Security researcher - Invicti Security (Acunetix) - Зеленые](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_1.jpg "How to break SAML if I have paws? WHOAMI? - Security researcher - Invicti Securit...")

лапки расслабленности t.me/greenrelaxpaws agrrrdog.blogspot.com github.com/GrrrDog/ Aleksei Tiurin GreenDog 

  3. ###  [SAML - Security Assertion Markup Language • SSO • Authentication](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_2.jpg "How to break SAML if I have paws? SAML - Security Assertion Markup Language ● SSO...")

and authorization • Everywhere 

  4. ###  [SAML - Security Assertion Markup Language • Very old standards](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_3.jpg "How to break SAML if I have paws? SAML - Security Assertion Markup Language ● Ver...")

(~2002-2005) ◦ SAML 1.0 / 2.0 • Based on ◦ HTTP ◦ XML ◦ XML Schema ◦ XML Digital Signature (XML DSig) ◦ XML Encryption • Complicated standards ◦ Protocols/Bindings/Profiles ◦ Full specs - hundreds of pages 

  5. ###  [“10 Years later” • Old technologies -> old libs ◦](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_4.jpg "How to break SAML if I have paws? “10 Years later” ● Old technologies -&gt; old libs...")

xmlsec (java / c) • Complex configurations • Many Implementations https://en.wikipedia.org/wiki/SAML-based_products_and_services • ZeroNights 2012 • (almost) All the same attacks ^_^ 

  6. ###  [Identity Provider (IdP) - where user creds are stored -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_5.jpg "How to break SAML if I have paws? Identity Provider \(IdP\) - where user creds are ...")

Okta, OneLogin, PingIdentity, MS AAD, etc - OpenAM, Keycloak, Oracle OAM, Shibboleth, etc Service Provider (SP) - an application that a user wants to access - … Jira, WordPress, AWS ... 

  7. ###  [\- One IdP - many SPs - Corporate SSO -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_6.jpg "How to break SAML if I have paws? - One IdP - many SPs - Corporate SSO - One SP -...")

One SP - many IdPs - SaaS that needs to support multiple organizations 

  8. ###  [Flows - SP initiated - IdP initiated (from 4) SAML](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_7.jpg "How to break SAML if I have paws? Flows - SP initiated - IdP initiated \(from 4\) S...")

Request SAML Response 

  9. ###  [SAMLRequest - From SP toIdP - Redirect Binding (GET) /](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_8.jpg "How to break SAML if I have paws? SAMLRequest - From SP toIdP - Redirect Binding ...")

POST Binding (HTML Form) - Base64 

  10. ###  [SAMLResponse - From IdP to SP - POST Binding HTML](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_9.jpg "How to break SAML if I have paws? SAMLResponse - From IdP to SP - POST Binding HT...")

form - Base64 + Deflate 

  11. ###  [SAMLResponse - Signed Response - Signed Assertion - Both](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_10.jpg "How to break SAML if I have paws? SAMLResponse - Signed Response - Signed Asserti...")

  12. ###  [How does the signature work?](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_11.jpg "How to break SAML if I have paws? How does the signature work?")

  13. ###  [Situations: - Anonymous attacks - A user in IdP -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_12.jpg "How to break SAML if I have paws? Situations: - Anonymous attacks - A user in IdP...")

Malicious SP - Malicious IdP Core tool - SAML Raider extension in Burp 

  14. ###  [Anonymous attacks 1. SAMLRequest - Detect that SAML is used](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_13.jpg "How to break SAML if I have paws? Anonymous attacks 1. SAMLRequest - Detect that ...")

2\. From SAMLRequest - Issuer (IdP) - AssertionConsumerServiceURL (ACS) - where SP expects SAMLResponse - SP’s SAML lib name - id generator - format, name, etc - Destination (IdP) 

  15. ###  [SAML Metadata - Configuration exchange for SP and IdP -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_14.jpg "How to break SAML if I have paws? SAML Metadata - Configuration exchange for SP a...")

Names, endpoints, certificates… - Signature, encryption, additional attributes… SP doesn’t expose it (usually) IdP: - know endpoints - oamfed/idp/metadata - from Destination - okta.com/app/appname/RND/sso/saml-> \- okta.com/app/RND/sso/saml/metadata Now, we have almost everything to create a good SAMLResponse from nothing 

  16. ###  [Creating SAML Response - POST to ACS url - Known](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_15.jpg "How to break SAML if I have paws? Creating SAML Response - POST to ACS url - Know...")

SAML schemas - Info from SAMLRequest - Destination - ACS url - InResponseTo - ID - Issue Timestamp - Issuer - From metadata - Both Response and Assertion - Subject / NameID - email? - Conditions - NotBefore + NotOnOrAfter - AudienceRestriction - ? - AuthnStatement - ? http://www.datypic.com/sc/saml2/e-samlp_Response.html http://www.datypic.com/sc/saml2/e-saml_Assertion.html 

  17. ###  [1\. XML -> XXE (+XSD/NS injection?) - https://nvd.nist.gov/vuln/detail/CVE-2022-35741 2. XSS](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_16.jpg "How to break SAML if I have paws? 1. XML -&gt; XXE \(+XSD/NS injection?\) - https://nv...")

\- Often show errors for debug - Before Sign check - Issuer, Destination, StatusCode, etc - using the created SAML Response - XSS payload -> every “field” - encode/CDATA Destination="&gt;&lt;img/src/onerror=alert(1)&gt;" SAML Response 

  18. ###  [Authentication bypass - Disabled sign check - common misconfig -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_17.jpg "How to break SAML if I have paws? Authentication bypass - Disabled sign check - c...")

No <Signature/> tag - no Sign check https://hackerone.com/reports/136169 - Complicated specifications - - nobody uses advanced features - Documentation (SP/IdP)? - NameID - email - Find a registered email? - Auto provisioning - Create SAML Response(s) - Try them - Error messages https://mishresec.wordpress.com/2017/10/13/uber-bug-bounty-gaining-access-to-an-inter nal-chat-system/ 

  19. ###  [KeyInfo - Info about the key - ds:Signature - Self-Signed](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_18.jpg "How to break SAML if I have paws? KeyInfo - Info about the key - ds:Signature - S...")

certificate SAML Response 

  20. ###  [Certificate faking for Authentication bypass - Take Certificate from Metadata](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_19.jpg "How to break SAML if I have paws? Certificate faking for Authentication bypass - ...")

\- Import in SAML Raider - Sign the created SAML Response(s) - Incorrect certificate match - Trust KeyInfo certificate https://epi052.gitlab.io/notes-to-self/blog/2019-03-13-how-to-test-saml-a-methodology-part-two/#certificate-faking SAML Response 

  21. ###  [Dupe Key Confusion (.NET) - Alvaro Muñoz, Oleksandr Mirosh at](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_20.jpg "How to break SAML if I have paws? Dupe Key Confusion \(.NET\) - Alvaro Muñoz, Oleks...")

BlackHat 2019 https://i.blackhat.com/USA-19/Wednesday/us-19-Munoz-SSO-Wars-The-Token-Menace.pdf - Better with a valid SAML Response SAML Response 

  22. ###  [Certificate validation to SSRF - Trust KeyInfo certificate - Certificate](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_21.jpg "How to break SAML if I have paws? Certificate validation to SSRF - Trust KeyInfo ...")

validation - SSRF in X509 cert - Michael Stepankin at BlackHat 2023 https://github.com/onhexgroup/Conferences/blob/main/Black%20Hat%20USA%202023%20slides/Michael %20Stepankin_mTLS%20When%20Certificate%20Authentication%20is%20Done%20Wrong.pdf - Java - AIA, SIA, CRL DP - Created SAML Response - Add KeyInfo with SSRF cert - Windows? .NET? 

  23. ###  [Reference dereferencing - Data location - URI - remote files](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_22.jpg "How to break SAML if I have paws? Reference dereferencing - Data location - URI -...")

(http, https, etc) - local files - (Blind) SSRF - Everywhere! - XML DSig - XML Enc - Metadata - … SAML Response 

  24. ###  [Reference dereferencing (XML DSig) - Reference https://github.com/IdentityPython/pysaml2/issues/510 - KeyInfo -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_23.jpg "How to break SAML if I have paws? Reference dereferencing \(XML DSig\) - Reference ...")

Java xmlsec. SecureValidation bypass (CVE-2021-40690) https://blog.tint0.com/2021/09/pinging-xmlsec.html SAML Response 

  25. ###  [Reference dereferencing (XML Enc) - CipherReference - DataReference - +](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_24.jpg "How to break SAML if I have paws? Reference dereferencing \(XML Enc\) - CipherRefer...")

EncryptedKey -> KeyInfo 

  26. ###  [Transformations - XML “normalization” - Additional “preparations” - Base64 -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_25.jpg "How to break SAML if I have paws? Transformations - XML “normalization” - Additio...")

XPath - XPath-Filter - XSLT (optional) - … 

  27. ###  [Base64 http://www.w3.org/2000/09/xmldsig#base64 - .NET XXE CVE-2022-34716 - Decode Reference +](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_26.jpg "How to break SAML if I have paws? Base64 http://www.w3.org/2000/09/xmldsig#base64...")

Parse XML - XXE inside https://bugs.chromium.org/p/project-zero/issues/detail?id=2313 

  28. ###  [XPath http://www.w3.org/TR/1999/REC-xpath-19991116 - Blind SSRF - Mix with Reference (xml](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_27.jpg "How to break SAML if I have paws? XPath http://www.w3.org/TR/1999/REC-xpath-19991...")

files) - Error - Modified version of a payload for PingIdentity from https://blog.tint0.com/2021/09/pinging-xmlsec.html 

  29. ###  [XSLT http://www.w3.org/TR/1999/REC-xslt-19991116 - Java / Santuario (xmlsec) <= 1.4.1 (~](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_28.jpg "How to break SAML if I have paws? XSLT http://www.w3.org/TR/1999/REC-xslt-1999111...")

2010) - via Xalan - RCE ManageEngine ServiceDesk CVE-2022-47966 

  30. ###  [xmlsec >= 1.4.2 - Secure-processing - true - Xalan CVE-2014-0107](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_29.jpg "How to break SAML if I have paws? xmlsec &gt;= 1.4.2 - Secure-processing - true - Xa...")

< 2.7.2 - Arbitrary class instantiation https://blog.viettelcybersecurity.com/saml-show-stopper/ 

  31. ###  [XSLT https://blog.viettelcybersecurity.com/saml-show-stopper/](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_30.jpg "How to break SAML if I have paws? XSLT https://blog.viettelcybersecurity.com/saml...")

  32. ###  [How can we test dereference/transformations? - Acunetix - No manual](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_31.jpg "How to break SAML if I have paws? How can we test dereference/transformations? - ...")

tools - SAML Raider - no Algorithm - unparsed-text - XSLT 2.0 - it won’t detect CVE-2022-47966 (java xmlsec) 

  33. ###  [Attacks on IdP - Signed SAMLRequest (AuthnRequest) - SP->IdP -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_32.jpg "How to break SAML if I have paws? Attacks on IdP - Signed SAMLRequest \(AuthnReque...")

Redirect-POST -> POST-POST bindings - SAML protocol: LogoutRequest, etc - Metadata import (Malicious SP/IdP) - Same attack vectors 

  34. ###  [With creds / Malicious SP/IdP - Transformation after Sign check](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_33.jpg "How to break SAML if I have paws? With creds / Malicious SP/IdP - Transformation ...")

\- Post-auth - “Malicious” SP/IdP - Generate a valid signature for arbitrary transformations - How? SAML Response 

  35. ###  [More attacks on IdP (w/ creds) ACSSpoofing Attack - Change](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_34.jpg "How to break SAML if I have paws? More attacks on IdP \(w/ creds\) ACSSpoofing Atta...")

SAMLRequest ACS url to an attacker’ server - Old https://web-in-security.blogspot.com/2015/04/on-security-of-saml-based-identity.html - is it string or url comparison? XML injection - SAMLRequest is not signed - Values from SAMLRequest reflected in SAMLResponse - copy as string - add new tags/attributes - correctly signed https://research.nccgroup.com/2021/03/29/saml-xml-injection/ 

  36. ###  [Attacks on SP (w/ creds) - Sign check, Cert-related, etc](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_35.jpg "How to break SAML if I have paws? Attacks on SP \(w/ creds\) - Sign check, Cert-rel...")

\- XSW (w/ SAML Raider) - XML parsing - Comment injection https://duo.com/blog/duo-finds-saml-vulnerabilities-affecting-multiple-implementations - ~ 2017 - [[email protected]](/cdn-cgi/l/email-protection)<!---->.attacker.pw - [[email protected]](/cdn-cgi/l/email-protection) vs [[email protected]](/cdn-cgi/l/email-protection) \- <? anything ?> \- processing instructions inside XML - Much more - Logic vulnerabilities - “how to put things together” - very common 

  37. ###  [Session handling RelayState - State Preservation - URL - “Open](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_36.jpg "How to break SAML if I have paws? Session handling RelayState - State Preservatio...")

Redirect” https://hackerone.com/reports/1923672 https://www.anitian.com/owning-saml/ 

  38. ###  [Multitenant (1 SP - many IdPs) Don’t trust IdP -](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_37.jpg "How to break SAML if I have paws? Multitenant \(1 SP - many IdPs\) Don’t trust IdP ...")

Auth based on SAML Response - Manipulate NameId, Issuer, ACS - Email from another tenant -> access IdP confusion https://hackerone.com/reports/976603 - IdP victim - “IdP1” - IdP attacker - “IdP1 ” (with a space at the end) - Sign check w/ victim’s IdP, log in to the attacker’s account 

  39. ###  [Recommendations - Don’t implement SAML “lib” yourself - Use 3rd](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_38.jpg "How to break SAML if I have paws? Recommendations - Don’t implement SAML “lib” yo...")

party libs - Update libs systematically - Show a generic error - Disable unnecessary features - KeyInfo? XML Enc? - Be careful w/ metadata - Always pentest your SAML implementation in SP - Pentest your IdP if it’s not SaaS - Write me if you have any questions 

  40. ###  [Big thanks to the researchers of mentioned articles/white papers/tools](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_39.jpg "How to break SAML if I have paws? Big thanks to the researchers of mentioned arti...")

  41. ###  [New cheat sheet about SAML? https://github.com/GrrrDog/ Зеленые лапки расслабленности https://t.me/greenrelaxpaws](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_40.jpg "How to break SAML if I have paws? New cheat sheet about SAML? https://github.com/...")

  42. [None](https://files.speakerdeck.com/presentations/f2029aa5aedd40bc8c863cd7a0c9f8d1/slide_41.jpg)

![](https://d1eu30co0ohy4w.cloudfront.net/assets/mark-f4be6df1e05965cac9f98e664a6c35f5ffdd0207385d07464a9214d6cdf76082.svg)

[ ![Speaker Deck](https://d1eu30co0ohy4w.cloudfront.net/assets/mark-f4be6df1e05965cac9f98e664a6c35f5ffdd0207385d07464a9214d6cdf76082.svg) SpeakerDeck ](/) [](https://www.facebook.com/speakerdeck "SpeakerDeck on Facebook") [](https://x.com/speakerdeck "SpeakerDeck on Twitter")

## Top Categories

  * [Programming](/c/programming)
  * [Technology](/c/technology)
  * [Storyboards](/c/storyboards)
  * [Featured decks](/p/featured)
  * [Featured speakers](/s/featured)

## Use Cases

  * [Storyboard Artists](/pro/storyboard-artists)
  * [Educators](/educators)
  * [Students](/student-pricing)

## Resources

  * [Help Center](https://help.speakerdeck.com/)
  * [Blog](https://blog.speakerdeck.com/)
  * [Compare Speaker Deck](/slideshare-alternative)
  * [Advertising](/advertising)

## Features

  * [Private URLs](/features/privacy-controls)
  * [Password Protection](/features/password-protection)
  * [Custom URLS](/features/custom-urls)
  * [Scheduled publishing](/features/scheduled-publishing)
  * [Remove Branding](/features/remove-branding)
  * [Restrict embedding](/features/restrict-embedding)
  * [Notes](/features/slide-notes)

Copyright © 2026 Speaker Deck, LLC.

All slide content and descriptions are owned by their creators.

  * [About](/about)
  * [Terms](/tos)
  * [Privacy](/privacy)
  * [DMCA](/dmca)
  * [Accessibility Statement](/accessibility)
