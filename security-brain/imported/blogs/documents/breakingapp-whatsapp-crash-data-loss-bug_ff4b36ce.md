---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-17_breakingapp-whatsapp-crash-data-loss-bug.md
original_filename: 2019-12-17_breakingapp-whatsapp-crash-data-loss-bug.md
title: BreakingApp – WhatsApp Crash & Data Loss Bug
category: documents
detected_topics:
- cloud-security
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- cloud-security
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: ff4b36cef4dd170c806bd5a5bca9a3d16093ea38c4e3849b98d41b5f3e18719f
text_sha256: 5081889926040035d05eddea9154c06e93b41908e80a16b5f5a2080ae4d2b75f
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# BreakingApp – WhatsApp Crash & Data Loss Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-17_breakingapp-whatsapp-crash-data-loss-bug.md
- Source Type: markdown
- Detected Topics: cloud-security, mobile-security, sso, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `ff4b36cef4dd170c806bd5a5bca9a3d16093ea38c4e3849b98d41b5f3e18719f`
- Text SHA256: `5081889926040035d05eddea9154c06e93b41908e80a16b5f5a2080ae4d2b75f`


## Content

---
title: "BreakingApp – WhatsApp Crash & Data Loss Bug"
page_title: "BreakingApp – WhatsApp Crash & Data Loss Bug - Check Point Research"
url: "https://research.checkpoint.com/2019/breakingapp-whatsapp-crash-data-loss-bug/"
final_url: "https://research.checkpoint.com/2019/breakingapp-whatsapp-crash-data-loss-bug/"
authors: ["Dikla Barda", "Roman Zaikin", "Yaara Shriki"]
programs: ["Meta / Facebook"]
bugs: ["DoS"]
publication_date: "2019-12-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4883
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

![](https://research.checkpoint.com/wp-content/uploads/2019/12/whatsappcrashBlog.jpg)

# BreakingApp – WhatsApp Crash & Data Loss Bug

December 17, 2019 

[](https://www.linkedin.com/shareArticle?mini=true&url=https://research.checkpoint.com/2019/breakingapp-whatsapp-crash-data-loss-bug/ -  https://research.checkpoint.com/?p=22925;source=LinkedIn "Share on LinkedIn!") [](http://www.facebook.com/sharer.php?u=https://research.checkpoint.com/2019/breakingapp-whatsapp-crash-data-loss-bug/ - https://research.checkpoint.com/?p=22925  "Share on Facebook!") [](http://twitter.com/home/?status=BreakingApp – WhatsApp Crash & Data Loss Bug - https://research.checkpoint.com/?p=22925 via @kenmata  "Tweet this!")

https://research.checkpoint.com/2019/breakingapp-whatsapp-crash-data-loss-bug/

By Dikla Barda, Roman Zaikin and Yaara Shriki

# Background:

**Some of the latest news regarding WhatsApp vulnerabilities are relating to a manipulation of the WhatsApp protocol using a tool built by Check Point Research in order to validate WhatsApp security without jeopardizing WhatsApp end to end encryption. This tool allows a user to modify WhatsApp messages before being sent and change the general parameters, such as participant’s phone number.**

In the blog post (<https://research.checkpoint.com/black-hat-2019-whatsapp-protocol-decryption-for-chat-manipulation-and-more/>) we discussed how a threat vector could **manipulate** messages to their own advantage. In this blog post we will further investigate how a threat vector can use the tool in order to obstruct access to WhatsApp messenger for a group of users by causing a crash-loop.

The bug was discovered in August 2019 and responsibly reported to WhatsApp whose developers fixed the bug in the update for version 2.19.58 and onwards.

# Technical Details:

A year after the previous WhatsApp research, the team was eager to dig back in and find new vulnerabilities in the app. We set up the WhatsApp Manipulation Tool and started testing new ways to manipulate WhatsApp protocol.

In this blog we will describe in detail the technique used in our testing where one can crash WhatsApp on multiple phones in a shared group.

We will briefly go over how to set everything up so we can start the manipulation (More details in previous blog post).

First, we need to browse to WhatsApp Web and open Chrome’s DevTools. We will need to set a few breakpoints in places where the encryption keys are generated and then obtain them during the login process.

Second, we need to get the “secret” parameter from the traffic passing through Burp Suite Web Socket tab after the QR is scanned. This parameter holds the necessary data required for the manipulation part which was explained in the previous blog post.

Third, we need to start the local python server (can be found in the GitHub project) which awaits a connection. Once the python server receives a message, it decrypts it (by using our encryption keys) and sends it back to the Burp Suite WhatsApp Manipulation Tool in clear text.

Lastly, both the private and public keys, and the “secret” parameter obtained in the preceding steps are used within the Burp Suite Extension to connect to the python server.

We should now be able to start decrypting and modifying messages **in a conversation where we participate**. Now that we have everything set up correctly, we can start **intercepting our messages**. Once a message is intercepted we can decrypt it by using the extension.

We should see the decrypted message in JSON format:

![](//research.checkpoint.com/wp-content/uploads/2019/12/image1-1024x311.jpg)

The bug resides in XMPP (Extensible Messaging and Presence Protocol), a communication protocol for instant messaging.

When we attempt to send a message where the parameter “participant” receives a value of “null” a ‘Null Pointer Exception’ is thrown.

![](//research.checkpoint.com/wp-content/uploads/2019/12/Image2.png)

As can be seen in the stack trace, the function d.g.ba.ba.run handles all the message data, such as message id, participant’s details, etc.

The parser for the participant’s phone number mishandles the input when an illegal phone number is received. When it receives a phone number with length

not in the ranger 5-20 or a non-digit character it would read it as a ‘null’ string.

![](//research.checkpoint.com/wp-content/uploads/2019/12/image3-1.png)

In a typical scenario, when a user in a WhatsApp group sends a message to the group, the application will examine the parameter participant to

identify who sent the message. While using our tool we were able to access this parameter and edit it.

In order to exploit this bug we would need to replace the participant’s parameter from the sender phone number to any non-digit character(s) e.g. ‘[[email protected]](/cdn-cgi/l/email-protection)’ as can be seen below:

![](//research.checkpoint.com/wp-content/uploads/2019/12/image4-1024x391.jpg)

Which will look like this:

![](//research.checkpoint.com/wp-content/uploads/2019/12/image5-1-1024x509.png)

By sending this message WhatsApp application will crash in every phone that is a member of this group.

The bug will crash the app and it will continue to crash even after we reopen WhatsApp, resulting in a crash loop. Moreover, the user will not be able to return to the

group and all the data that was written and shared in the group is now gone for good. The group cannot be restored after the crash has happened and will have to be deleted in order to stop the crash.

![](//research.checkpoint.com/wp-content/uploads/2019/12/image6-1-1024x724.png)

In WhatsApp there are many important groups with valuable content. If an attacker uses this technique and crashes one of these groups all chat history will be gone and further communication would be impossible.

The impact of this vulnerability is potentially tremendous, since WhatsApp is the main communication service for many people. Thus, the bug compromises the availability of the app which is a crucial for our daily activities.

In order to recover from the issue, the user have to uninstall WhatsApp, install it again and remove the group which contains the malicious payload.

Here is the PoC video with reproduction steps

[//research.checkpoint.com/wp-content/uploads/2019/12/whatsapp_crash_v6.mp4](//research.checkpoint.com/wp-content/uploads/2019/12/whatsapp_crash_v6.mp4)

[![](//research.checkpoint.com/wp-content/uploads/2019/12/whatsappcrashBlog.jpg)](https://research.checkpoint.com/)

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
