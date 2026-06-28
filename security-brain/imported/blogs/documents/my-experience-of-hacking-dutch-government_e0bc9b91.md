---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-19_my-experience-of-hacking-dutch-government.md
original_filename: 2022-02-19_my-experience-of-hacking-dutch-government.md
title: My Experience of Hacking Dutch Government
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: e0bc9b9190778ec2eb8926d3b454c308489b6f0776083f872c4752ce955c8ce5
text_sha256: b88bd6658efab7f01c4a4239e8def26fa1cee4bc01fc73607ec8b27c4b91bcc5
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# My Experience of Hacking Dutch Government

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-19_my-experience-of-hacking-dutch-government.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `e0bc9b9190778ec2eb8926d3b454c308489b6f0776083f872c4752ce955c8ce5`
- Text SHA256: `b88bd6658efab7f01c4a4239e8def26fa1cee4bc01fc73607ec8b27c4b91bcc5`


## Content

---
title: "My Experience of Hacking Dutch Government"
page_title: "My Experience of Hacking Dutch Government | remonsec"
url: "https://remonsec.com/posts/hacking-dutch-gov/"
final_url: "https://remonsec.com/posts/hacking-dutch-gov/"
authors: ["remonsec (@remonsec)"]
programs: ["Dutch Government"]
publication_date: "2022-02-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2888
---

## My Experience of Hacking Dutch Government __

_Bismillahi-r-Rahmani-r-Rahim_ _(In the name of Allah, the Compassionate, the Merciful) Assalamu Alaikum (peace be upon you)_

## **Background** __

Long story short, I just get started with Bug Bounty in 2020 and saw this Bounty Boy ([**Mohammad Abdullah**](https://www.facebook.com/Abdul1ah)) with his Dutch Government swag.

[](https://postimg.cc/vcZscgdX)

Just look at the Quote line. The word government was the killer one. So now what, I need this swag badly. But wait, i just get started few weeks ago even don’t know how to run burpsuite. As like all other newbie i DM that guy for the tip how he got that. Then he just gave me a github repo and told me to try harder. Seriously man i was expecting he will give me something by running that script i will get the swag, at least some secret method. But what he gave me a list of domain for Dutch Gov websites. Here is the [**repo**](https://gist.github.com/random-robbie/f985ad14fede2c04ac82dd89653f52ad). It contain 650+ host to find bugs.

## My Approach __

If i be honest i was so confuse coz i have to look into 650+ host and i dont know how to do basic vulnerability assesment. So i just reported some SPF & Clickjack but no luck they close as N/A. Fine, i have to do something else. After passing couple of days i understood that, with this knowledge it’s not possible to break into their security. I took a step back and start learning about some basics. Please note that during that whole week i visited most of that websites and saw that there is no authentication for those hosts so it means no more authentication related easy bugs. From a beginner point of view, it just sound insane and damn hard to hit. But we don’t care how hard it is right !

During that break time i start learning about Recon. Yes, you hear it right recon. This PentesterLand [**resources**](https://pentester.land/cheatsheets/2019/04/15/recon-resources.html) just worked awesome for me. I read all of them, every single one. After study couple of weeks i got a good basic understanding about how to approach a target in general

## Final Methodology __

So we have lot’s of hosts with no authentication. So i call this workflow is, fly over the target

**Get Only Live Hosts**

`while read domain; do if host “$domain” > /dev/null; then echo $domain;fi;done<DutchGov.txt >> domains.txt`

**Get All Subdomain**

`for sub in $(cat domains.txt);do subfinder -d $sub -o $sub.dutch;done`

**Gather All Subdomain**

`cat *.dutch > all.sub`

**Fuzz All The Things**

`for i in $(cat all.sub); do echo””; echo “Subdomain of $i”;echo “”;gobuster dir -w wordlist.txt -u $i -e -o tmp ;cat tmp >> dutch.fuzz; echo “”; done`

**Server Details for CVE**

`for sub in $(cat all.sub);do echo “[*] Domain Name is => “ $sub;echo “[*] Server Header is => “ $(http — verify=no -h $sub | grep Server);echo “ “;done`

**Scan Ports** well when i was doing i have done this process with nmap manually, i only scanned those hosts where i found juicy staff during previous steps But now there lots of fast scanner available to automate this process. I didn’t check them yet, so do some research yourself

**Web ScreensShot** I already have visited all of those sites so no need for me, but you can try

You may notice i didn’t check for any parameter or any kind of Injection attack. The truth is, that time i actually didn’t know how to test parameters. If you want you can follow this one

**Wayback Machine Urls**

`cat domains.txt | waybackurls | urlprobe -t 50 -c 100 | grep “=”`

## **End Story** __

I had a vps so for me it was not that much hard to do. every nigh i run them with tmux and in morning i got juicy staff. After reporting couple of bugs one got triage as High impact and finally Alhamdulillah (All praise is due to Allah alone) i got that lousy T-Shirt

[](https://postimg.cc/Wt1rD0LN)

##  Author __

**Name** : Mehedi Hasan Remon **Handle** : @remonsec

* * *

wanna support my work! well just buy me a coffee

[](https://www.buymeacoffee.com/remonsec)
