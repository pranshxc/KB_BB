---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-23_my-first-bug-is-rce-via-sql-injection.md
original_filename: 2023-06-23_my-first-bug-is-rce-via-sql-injection.md
title: My First Bug is RCE via SQL injection!
category: documents
detected_topics:
- sqli
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 428b929038bcbcd4aa3e9fca16f552e77397db3e6a947bb1151100469e706856
text_sha256: 870d011283b90309b90fb375e392b85a4c00e59a02afb425f18a33542a92ed0f
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug is RCE via SQL injection!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-23_my-first-bug-is-rce-via-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `428b929038bcbcd4aa3e9fca16f552e77397db3e6a947bb1151100469e706856`
- Text SHA256: `870d011283b90309b90fb375e392b85a4c00e59a02afb425f18a33542a92ed0f`


## Content

---
title: "My First Bug is RCE via SQL injection!"
url: "https://medium.com/@karimelsayed0x1/my-first-bug-is-rce-via-sql-injection-dfee9c4d4c01"
authors: ["z3r0xk (@z3r01k)"]
bugs: ["SQL injection", "RCE"]
publication_date: "2023-06-23"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 1017
scraped_via: "browseros"
---

# My First Bug is RCE via SQL injection!

Top highlight

My First Bug is RCE via SQL injection!
z3r0xk.h
Follow
5 min read
·
Jun 22, 2023

979

11

Press enter or click to view image in full size
Photo by Arget on Unsplash
$ Whoami

Hello friend, you can call me z3r0xk. I am over the moon to share that I have found my first bug, which turned out to be an RCE via SQL injection!

As a beginner, this moment is like a dream come true for me. I can’t explain how happy I am about this finding. I wish you the best of luck in finding your first bug soon! :”)

$ cat methodology.txt

As I started about 9 months ago as a bug hunter, I tried a lot to find bugs in targets that offered bounties. However, I received 10 N/A and 3 duplicates, which was a lot of failure.

After some days of confusion, I decided to ask my friend for advice. He told me about private programs and how it might be easier to find some bugs there. But first, I needed to earn some points to qualify for an invitation. So, I decided to move forward and hunt on VDPs. I randomly chose target.com, and this is where my dream was achieved.

I found my first bug, and surprisingly, it was an RCE via SQL injection!

$ cat Bug.txt
var target.com = "actual_target.com";

First, I collected subdomains from the awesome website https://chaos.projectdiscovery.io/. Since I didn’t want to waste my time collecting all the subdomains, I needed to focus on hunting. After that, I wrote a small bash script to collect all the files.txt in one file, which I called “allDomains.txt”.
Maybe it’s not the best solution, but as a beginner it works for me :)

sed -i 's/\*\.//g' *.txt

for file in *.txt; do  
  mv "$file" "${file%.*}_domains.txt"
done

cat *_domains.txt |sort -u|tee allDomains.txt 
rm *_domains.txt

After that, I decided to collect all the live domains and take screenshots of them using httpx.
It can be done in one line but for other things, I did it in two lines.

httpx -l allDomains.txt -o liveDomains.txt
httpx -l liveDomains.txt -srd subsScreens -ss

Now that we have all the screenshots in the directory ‘subsScreens’, I decided to look for easy bugs to hunt, such as finding login panels, search banners, etc. I moved through these screens and tried to find something interesting to me.

Press enter or click to view image in full size
Photo by Marten Newhall on Unsplash

I found some login panels, but their design looks traditional. Let’s look for some jewelry instead.

Press enter or click to view image in full size

Let’s intercept this request. Usually, at this step, three scenarios come to mind: response manipulation, default credentials, and injection attacks.
I have tried to manipulate the response, for example, changing “true” to “false,” but I was unsuccessful.
Additionally, I have been unable to find any default credentials. :(

Get z3r0xk.h’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so let’s do some INJECTIONS!

Press enter or click to view image in full size
Photo by Diana Polekhina on Unsplash

Usually, I use blind testing as the first test. I tried using boolean conditions to identify if there was any SQL injection, but unfortunately, I couldn’t find anything.
It’s now 3:00 AM, so I decided to go to bed with a heavy heart and take a note about this panel to hunt for it the next day. Now, with a fresh mind and some coffee, let’s hack this target. Why not try using the time-based approach? Maybe it will work.
After trying some payloads for different DBMS, it worked! BOOOOOOM!

admin');SELECT PG_SLEEP(5)--
Press enter or click to view image in full size

Now, let’s use our arsenal, SQLmap, to write a PoC of this finding and prove that it may be harmful to the target. I got a lot of N/A because I didn’t write a strong impact of my finding, so let’s start by proving it has a HIGH impact. I fire up my SQLmap and use this command.
Note that this is a POST request, and if we need SQLmap to inject in a specific point, we put * in it like this:

login=admin*

The SQLmap command:

sqlmap -r target.txt --banner --current-user
Press enter or click to view image in full size

Now that we’re in High Impact, let’s report this to avoid duplicates and classify it as critical later. After I reported this bug, I read many write-ups describing how other researchers found RCE via SQLi. Let’s follow the masters. I got an idea from a write-up that said if the current user is a DBA but it’s not an Oracle DBMS, then we can use SQLmap to produce an OS shell and achieve RCE.”

sqlmap -r target.txt --os-shell

And BOOOOOOOOOOM RCE!!

Press enter or click to view image in full size

I reported it as an update to my report. Finally, I got my first valid bug classified as critical.

It is now in the trigger step and awaiting acceptance. I hope that you can learn something from this write-up, and my advice is to always try, try again, and also read a lot of write-ups. This is a must-read place where you can learn from. Finally, I wish to see this bug accepted.

When report become public, i will put it’s link here :”)

a lot of thanks to my awesome friends to help me a lot 
Mohamed reda
 
Ahmed Mahmoued

Twitter: https://twitter.com/z3r01k
Linkedin: https://www.linkedin.com/in/karim-elsayed-a70921250/
