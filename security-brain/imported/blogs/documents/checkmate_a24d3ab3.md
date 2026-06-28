---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-16_checkmate.md
original_filename: 2023-03-16_checkmate.md
title: CHECKMATE
category: documents
detected_topics:
- cloud-security
- sso
- xss
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- cloud-security
- sso
- xss
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: a24d3ab3929a70d12c254d606308ab16be2bcd845f84c2af258aae62a1acf28a
text_sha256: 10b7e0920ae9424006fc285774d05c92a938f03bf7bff7d269b00f41aa0513b8
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# CHECKMATE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-16_checkmate.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, xss, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `a24d3ab3929a70d12c254d606308ab16be2bcd845f84c2af258aae62a1acf28a`
- Text SHA256: `10b7e0920ae9424006fc285774d05c92a938f03bf7bff7d269b00f41aa0513b8`


## Content

---
title: "CHECKMATE"
page_title: "CheckMate - Check Point Research"
url: "https://research.checkpoint.com/2023/checkmate/"
final_url: "https://research.checkpoint.com/2023/checkmate/"
authors: ["Oded Vaanunu", "Roman Zaikin (@R0m4nZ41k1n)", "Dan Lasker"]
programs: ["Chess.com"]
bugs: ["Websockets", "Logic flaw"]
publication_date: "2023-03-16"
added_date: "2023-03-18"
source: "pentester.land/writeups.json"
original_index: 1368
---

[![](https://research.checkpoint.com/wp-content/uploads/2024/06/CPR-by-Check-Point-logo.svg)](https://research.checkpoint.com)

  * [CONTACT US](https://research.checkpoint.com/contact/)
  * [DISCLOSURE POLICY](https://research.checkpoint.com/disclosure-policy/)
  * [CHECKPOINT.COM](https://www.checkpoint.com/)
  * [UNDER ATTACK?](https://www.checkpoint.com/about-us/contact-incident-response/)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

[![](https://research.checkpoint.com/wp-content/uploads/2024/06/CPR-by-Check-Point-logo.svg)](https://research.checkpoint.com)

  * [Latest Publications](https://research.checkpoint.com/latest-publications/)
  * [CPR Podcast Channel](https://research.checkpoint.com/cpr-podcast-channel/)
  * [AI Research](https://research.checkpoint.com/ai-research/)
  * [Web 3.0 Security](https://research.checkpoint.com/category/web3/)
  * [Intelligence Reports](https://research.checkpoint.com/intelligence-reports/)
  * Resources
  * [ThreatCloud AI](https://www.checkpoint.com/ai/)
  * [Threat Intelligence & Research](https://www.checkpoint.com/solutions/threat-intelligence-research/)
  * [Zero Day Protection](https://www.checkpoint.com/infinity/zero-day-protection/)
  * [Sandblast File Analysis](http://threatemulation.checkpoint.com/)
  * [About Us](https://research.checkpoint.com/about-us/)
  * [SUBSCRIBE](https://research.checkpoint.com/subscription/)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

SUBSCRIBE

## CATEGORIES

  * [ AI Research 16 ](https://research.checkpoint.com/category/ai-research/)
  * [ Android Malware 23 ](https://research.checkpoint.com/category/android-malware/)
  * [ Artificial Intelligence 5 ](https://research.checkpoint.com/category/artificial-intelligence-2/)
  * [ ChatGPT 3 ](https://research.checkpoint.com/category/chatgpt/)
  * [ Check Point Research Publications 460 ](https://research.checkpoint.com/category/threat-research/)
  * [ Cloud Security 1 ](https://research.checkpoint.com/category/cloud-security/)
  * [ CPRadio 44 ](https://research.checkpoint.com/category/cpradio/)
  * [ Crypto 2 ](https://research.checkpoint.com/category/crypto/)
  * [ Data & Threat Intelligence 2 ](https://research.checkpoint.com/category/data-threat-intelligence/)
  * [ Data Analysis 0 ](https://research.checkpoint.com/category/data-analysis/)
  * [ Demos 22 ](https://research.checkpoint.com/category/demos/)
  * [ Global Cyber Attack Reports 412 ](https://research.checkpoint.com/category/threat-intelligence-reports/)
  * [ How To Guides 13 ](https://research.checkpoint.com/category/how-to-guides/)
  * [ Ransomware 5 ](https://research.checkpoint.com/category/ransomware/)
  * [ Russo-Ukrainian War 1 ](https://research.checkpoint.com/category/russo-ukrainian-war/)
  * [ Security Report 1 ](https://research.checkpoint.com/category/security-report/)
  * [ Threat and data analysis 0 ](https://research.checkpoint.com/category/threat-and-data-analysis/)
  * [ Threat Research 175 ](https://research.checkpoint.com/category/threat-research-2/)
  * [ Web 3.0 Security 11 ](https://research.checkpoint.com/category/web3/)
  * [ Wipers 0 ](https://research.checkpoint.com/category/wipers/)

![](https://research.checkpoint.com/wp-content/uploads/2023/03/chess-1059x529-1.jpg)

# CheckMate

March 16, 2023 

[](https://www.linkedin.com/shareArticle?mini=true&url=https://research.checkpoint.com/2023/checkmate/ -  https://research.checkpoint.com/?p=27626;source=LinkedIn "Share on LinkedIn!") [](http://www.facebook.com/sharer.php?u=https://research.checkpoint.com/2023/checkmate/ - https://research.checkpoint.com/?p=27626  "Share on Facebook!") [](http://twitter.com/home/?status=CheckMate - https://research.checkpoint.com/?p=27626 via @kenmata  "Tweet this!")

https://research.checkpoint.com/2023/checkmate/

**_Research by :Oded Vaanunu / Roman Zaikin / Dan Lasker_**

Chess.com is the world leading platform for online chess games. It is an internet chess server, news website, and social networking website.**** Chess.com has a strong focus on community-based forums and blogs. These social features allow players to connect with each other, become friends, share their thoughts and experiences, and learn from each other.

There are over 93 million members from all around the world and over 2.5 million active members daily.

One of the largest chess platforms in the world, Chess.com has hosted online tournaments such as the “Chess.com Global Championship,” in which the winner wins $1,000,000.

**What happened in 2022?**

In 2022, Magnus Carlsen (Norwegian World champion since 2013) decided to withdraw from a tournament because he believed that Hans Niemann (American Grand Master) was a cheater.

Chess.com [claimed](https://www.chess.com/news/view/chesscom-hans-niemann-report-cheating) : _“Niemann has likely cheated in more than 100 Online Chess Games_ ___[…] he is the fastest rising top player in classical OTB chess in modern history”._

Chess.com decided to remove Niemann from the platform and from the Global Chess Championship the day after he beat GM Magnus Carlsen. This decision has been made because Hans admitted that **he cheated in chess games on the popular website** in 2020. Chess.com used its cheating-detection software and discovered suspicious play.

_Websites for reference:_

<https://edition.cnn.com/2022/10/05/sport/hans-niemann-chess-cheating-allegations-intl-hnk-spt/index.html>

<https://www.nytimes.com/2022/12/04/business/chess-cheating-scandal-magnus-carlsen-hans-niemann.html>

<https://www.bbc.com/news/world-63010107>

Chess.com invests a lot of money in trying to detect cheaters that use various kinds of technique. Cheating in chess is a deliberate violation of the rules of chess or other behavior that is intended to give an unfair advantage to a player or team. It can occur in many forms and can take place before, during, or after a game.

Chess.com [AP1] participation relates to the rating of players to participate in games and win bigger prizes. For example, tournaments are based on ratings.

We decided to test the popular online platform Chess.com to try to check if it is possible to cheat in the games by abusing a security vulnerability.

  1. We found out that it is possible to win by **decreasing the opponent’s time** **and** **winning the game over time,** without the opponent noticing what happened.

  * In addition, it is possible to **extract successful chess moves to solve online puzzle challenges and win puzzle ratings**. In this method, we simply need to catch the communication between the client side (player) and the server (Chess.com website). The server accidentally sends the correct solution to the puzzle! We can then abuse and cheat on puzzle championships (in which the winner gets prize money) by simply submitting the correct moves that we found. Moreover, it is possible to modify the elapsed time it took to think about the solution.

**_Technical Details:_**

Chess.com uses **WebSocket** for inner-game communication and various tasks; each game contains a game id which can be seen in the URL:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture1.png)

If the game is played by friends, Chess.com provides an additional feature to the gameplay, that allows to **“Add 15 Seconds”** to the opponent:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture2-1024x178.png)

Pressing on the button will add 15 seconds to the opponent, and the request looks like that:

* * *

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture3-1-1024x551.png)

Let’s dive into the parameters that are sent to the server:

  * **channel** – path to the game itself.
  * **data** – contains 4 attributes:
  * **adjustclock** – how much time we want to add to the opponent (150 = 15 seconds)
  * **gid** – Identifier of the current game.
  * **tid** – current task to perform, in this case it is _adjustclocks_ in order to add time to the opponent.
  * **uid** – Identifier of the opponent.
  * **id** – socket sequence number which is auto-incremented every time a WebSocket request is sent.
  * **clientId** – user click id (in this example, this is the attacker id).

We have found that it is possible to **win any game** if the attacker sends a friend request during/before the game to the opponent, and the opponent approves it.

We can think of a scenario in which the attacker-friendly chats with its opponent during the game. The innocent opponent (victim) approves the friend request without a doubt. Finally, the option of “adding time” is provided, and the attacker abuses it in order to reduce the timing clock of the victim to 0.

The attacker is ab

le to intercept the WebSocket request with any proxy tool (e.g. BurpSuite) and to change the sending request to <https://live2.chess.com/cometd> with the following _adjustclock_ data:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture4-1024x591.png)

In this request the sending _adjustclock_ value is _-8990_ and as a result the opponent will have just 10 seconds to play and will certainly lose the game without noticing that its time on the clock has been considerably reduced:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture5-1024x767.png)

In conclusion, it is possible to win any game if the opponent **approves** the friend request:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture6.png)

Because rating is very important in chess and the integrity of the game and the puzzles the player solves, we also looked at the puzzle’s logic and found out that it is also possible to solve the puzzle with only one modified request.

Explanation of the puzzle’s logic based on two requests:

First is an HTTP request [ _https://www.chess.com/callback/tactics/rated/next_](https://www.chess.com/callback/tactics/rated/next) which contains the following important parameters:

  1. **id** – the challenge identifier to be submitted
  1. **tcnMoveList** – the challenge solution, the expected solution to be sent to the server
  1. **averageSeconds** – the average solve rate

_Here is an example of this request._

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture7-1024x444.png)

The _MoveList_ is the actual solution for the puzzle and is expected by the server in order to confirm that the challenge is correctly solved.

All the attacker needs to do in order to solve the puzzle is to send that list of movers to the request to [_https://www.chess.com/callback/tactics/submitMoves_](https://www.chess.com/callback/tactics/submitMoves) __ with the 3 modified parameters:

  * _tacticsProblemId_ – identifier of the challenge.
  * _totalTime_ – time that took us to solve the challenge, which can be the average time from the previous request.
  * _moves_ – the value of _tcnMoveList,_ which is the actual solution to the puzzle.

By sending those parameters without even playing allows the attacker to raise his score:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture8-1024x478.png)

This is how it is possible to cheat in puzzles and to win ranking without playing:

![](https://research.checkpoint.com/wp-content/uploads/2023/03/Picture9-1024x288.png)

**Responsible disclosure:**

CPR has disclosed this information to the chess.com teams which acknowledged the vulnerability and applied a fix

to it.

![](https://research.checkpoint.com/wp-content/uploads/2022/10/back_arrow.svg) GO UP 

[BACK TO ALL POSTS](/latest-publications/)

## POPULAR POSTS

[ ![](https://research.checkpoint.com/wp-content/uploads/2023/01/AI-1059x529-copy.jpg) ](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/)

  * Artificial Intelligence
  * ChatGPT
  * Check Point Research Publications

[OPWNAI : Cybercriminals Starting to Use ChatGPT](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/)

[ ![](https://research.checkpoint.com/wp-content/uploads/2019/01/Fortnite_1021x580.jpg) ](https://research.checkpoint.com/2019/hacking-fortnite/)

  * Check Point Research Publications
  * Threat Research

[Hacking Fortnite Accounts](https://research.checkpoint.com/2019/hacking-fortnite/)

[ ![](https://research.checkpoint.com/wp-content/uploads/2022/12/OpenAIchatGPT_header.jpg) ](https://research.checkpoint.com/2022/opwnai-ai-that-can-save-the-day-or-hack-it-away/)

  * Artificial Intelligence
  * ChatGPT
  * Check Point Research Publications

[OpwnAI: AI That Can Save the Day or HACK it Away](https://research.checkpoint.com/2022/opwnai-ai-that-can-save-the-day-or-hack-it-away/)

### BLOGS AND PUBLICATIONS

[ ![](https://research.checkpoint.com/wp-content/uploads/2020/02/CheckPointResearchTurkishRat_blog_header.jpg) ](https://research.checkpoint.com/2020/the-turkish-rat-distributes-evolved-adwind-in-a-massive-ongoing-phishing-campaign/)

  * Check Point Research Publications
  * Global Cyber Attack Reports
  * Threat Research

February 17, 2020

### “The Turkish Rat” Evolved Adwind in a Massive Ongoing Phishing Campaign

[ ![](https://research.checkpoint.com/wp-content/uploads/2017/08/WannaCry-Post-No-Image-1021x450.jpg) ](https://research.checkpoint.com/2017/the-next-wannacry-vulnerability-is-here/)

  * Check Point Research Publications

August 11, 2017

### “The Next WannaCry” Vulnerability is Here

[ ![](https://research.checkpoint.com/wp-content/uploads/2026/03/Handala-void-1-scaled.png) ](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)

  * Check Point Research Publications

March 12, 2026

### “Handala Hack” – Unveiling Group’s Modus Operandi

[![](https://research.checkpoint.com/wp-content/uploads/2022/12/CheckPointResearchLogo_white-1-e1671590634727.png)](https://research.checkpoint.com)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

  * Publications
  * [Global cyber attack reports](/category/threat-intelligence-reports/)
  * [Research publications](/category/threat-research/)
  * [IPS advisories](https://advisories.checkpoint.com/advisories/)
  * [Check point blog](https://blog.checkpoint.com/)
  * [Demos](/category/demos/)
  * Tools
  * [Sandblast file analysis](http://threatemulation.checkpoint.com/)
  * [ThreatCloud](https://www.checkpoint.com/infinity/threatcloud/)
  * [Threat Intelligence](https://www.checkpoint.com/solutions/threat-intelligence-research/)
  * [Zero day protection](https://www.checkpoint.com/infinity/zero-day-protection/)
  * [Live threat map](https://threatmap.checkpoint.com/)
  * [About Us](https://research.checkpoint.com/about-us/)
  * [Contact Us](https://research.checkpoint.com/contact/)

### Let’s get in touch

Subscribe for cpr blogs, news and more

[Subscribe Now](/subscription/)

© 1994-2026 Check Point Software Technologies LTD. All rights reserved.

Property of [CheckPoint.com](https://www.checkpoint.com/)

[Privacy Policy](/privacy-policy/)

![](https://research.checkpoint.com/wp-content/uploads/2022/10/popup-side-image.jpg)

## SUBSCRIBE TO CYBER INTELLIGENCE REPORTS

First Name

Last Name

Country—Please choose an option—ChinaIndiaUnited StatesIndonesiaBrazilPakistanNigeriaBangladeshRussiaJapanMexicoPhilippinesVietnamEthiopiaEgyptGermanyIranTurkeyDemocratic Republic of the CongoThailandFranceUnited KingdomItalyBurmaSouth AfricaSouth KoreaColombiaSpainUkraineTanzaniaKenyaArgentinaAlgeriaPolandSudanUgandaCanadaIraqMoroccoPeruUzbekistanSaudi ArabiaMalaysiaVenezuelaNepalAfghanistanYemenNorth KoreaGhanaMozambiqueTaiwanAustraliaIvory CoastSyriaMadagascarAngolaCameroonSri LankaRomaniaBurkina FasoNigerKazakhstanNetherlandsChileMalawiEcuadorGuatemalaMaliCambodiaSenegalZambiaZimbabweChadSouth SudanBelgiumCubaTunisiaGuineaGreecePortugalRwandaCzech RepublicSomaliaHaitiBeninBurundiBoliviaHungarySwedenBelarusDominican RepublicAzerbaijanHondurasAustriaUnited Arab EmiratesIsraelSwitzerlandTajikistanBulgariaHong Kong (China)SerbiaPapua New GuineaParaguayLaosJordanEl SalvadorEritreaLibyaTogoSierra LeoneNicaraguaKyrgyzstanDenmarkFinlandSlov***REDACTED-AWS-KEY***istanNorwayLebanonCosta RicaCentral African RepublicIrelandGeorgiaNew ZealandRepublic of the CongoPalestineLiberiaCroatiaOmanBosnia and HerzegovinaPuerto RicoKuwaitMoldovMauritaniaPanamaUruguayArmeniaLithuaniaAlbaniaMongoliaJamaicaNamibiaLesothoQatarMacedoniaSloveniaBotswanaLatviaGambiaKosovoGuinea-BissauGabonEquatorial GuineaTrinidad and TobagoEstoniaMauritiusSwazilandBahrainTimor-LesteDjiboutiCyprusFijiReunion (France)GuyanaComorosBhutanMontenegroMacau (China)Solomon IslandsWestern SaharaLuxembourgSurinameCape VerdeMaltaGuadeloupe (France)Martinique (France)BruneiBahamasIcelandMaldivesBelizeBarbadosFrench Polynesia (France)VanuatuNew Caledonia (France)French Guiana (France)Mayotte (France)SamoaSao Tom and PrincipeSaint LuciaGuam (USA)Curacao (Netherlands)Saint Vincent and the GrenadinesKiribatiUnited States Virgin Islands (USA)GrenadaTongaAruba (Netherlands)Federated States of MicronesiaJersey (UK)SeychellesAntigua and BarbudaIsle of Man (UK)AndorraDominicaBermuda (UK)Guernsey (UK)Greenland (Denmark)Marshall IslandsAmerican Samoa (USA)Cayman Islands (UK)Saint Kitts and NevisNorthern Mariana Islands (USA)Faroe Islands (Denmark)Sint Maarten (Netherlands)Saint Martin (France)LiechtensteinMonacoSan MarinoTurks and Caicos Islands (UK)Gibraltar (UK)British Virgin Islands (UK)Aland Islands (Finland)Caribbean Netherlands (Netherlands)PalauCook Islands (NZ)Anguilla (UK)Wallis and Futuna (France)TuvaluNauruSaint Barthelemy (France)Saint Pierre and Miquelon (France)Montserrat (UK)Saint Helena, Ascension and Tristan da Cunha (UK)Svalbard and Jan Mayen (Norway)Falkland Islands (UK)Norfolk Island (Australia)Christmas Island (Australia)Niue (NZ)Tokelau (NZ)Vatican CityCocos (Keeling) Islands (Australia)Pitcairn Islands (UK)

Email

## We value your privacy!

BFSI uses cookies on this site. We use cookies to enable faster and easier experience for you. By continuing to visit this website you agree to our use of cookies.

ACCEPT

REJECT
