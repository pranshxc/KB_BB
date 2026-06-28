---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-28_15k-rce-through-monitoring-debug-mode.md
original_filename: 2024-08-28_15k-rce-through-monitoring-debug-mode.md
title: $15k RCE Through Monitoring Debug Mode
category: documents
detected_topics:
- command-injection
- ssrf
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- ssrf
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: a2b8f78245dfc52e0a08aaaf8c2fea4585415d59c49791a65840e242f5d5ca9a
text_sha256: b7877e426727b712bc3cad1625ddef2aaf931db758ec18d2c7f0d821e0c49fb8
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# $15k RCE Through Monitoring Debug Mode

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-28_15k-rce-through-monitoring-debug-mode.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `a2b8f78245dfc52e0a08aaaf8c2fea4585415d59c49791a65840e242f5d5ca9a`
- Text SHA256: `b7877e426727b712bc3cad1625ddef2aaf931db758ec18d2c7f0d821e0c49fb8`


## Content

---
title: "$15k RCE Through Monitoring Debug Mode"
url: "https://medium.com/@0xold/15k-rce-through-monitoring-debug-mode-4f474d8549d5"
authors: ["Omar (@0x0ld)"]
bugs: ["RCE", "LFI", "Debug mode enabled"]
bounty: "15,000"
publication_date: "2024-08-28"
added_date: "2024-09-04"
source: "pentester.land/writeups.json"
original_index: 35
scraped_via: "browseros"
---

# $15k RCE Through Monitoring Debug Mode

Top highlight

$15k RCE Through Monitoring Debug Mode
0xold
Follow
6 min read
·
Aug 27, 2024

1.5K

15

Have you ever come across an endpoint that you instinctively knew was vulnerable, but you couldn’t quite understand what was happening on the backend or how to exploit it? In this writeup, I’ll guide you through a technique that transformed my black box testing into a semi-white box testing. This approach led to the discovery of multiple vulnerabilities and eventually resulted in achieving remote code execution on the system.

Discovering the endpoint

During reading one of the javascript files i found an endpoint called ExtraServices so i opened up burp and requested the endpont in burp repeater However the endpoint returned a 404 status code but slightly different from the 404 that the host is always returning so i thought maybe it is a different host and i statred fuzzing the endpoint using ffuf

Press enter or click to view image in full size

using the command below

ffuf -c -w <(cat customwordlist.txt ) -u https://company.com/Extraserivce/FUZZ

The <() syntax, known as process substitution, acts as an input where programs can read from stdin. I often use it when fuzzing targets because it allows me to adjust or modify my wordlist on the fly.

For example, if you find an endpoint like api/users/:user:id and you want to dump all user IDs, instead of creating a new file to save all the user IDs and then fuzzing it, you can simply use

ffuf -c -w <(seq 1 1337) -u https://company.com/api/users/FUZZ

back to the Extraserivce endpoint fuzzing this endpoint didn’t yield any results so i decided to leave it for now then a few hours later i found out that some of the endpoints that were working before now almost all of them return a custom 404 response so i knew the developer had implement a functionality that returns 404 response for some endpoints i knew that because the 404 response was different from the screenshot above so i grabbed one of the endpoints that was working before and addeed a backslash before the begining of the path \ for example /\purl/test and it returned 200 OK. so i grabbed the Extraserivce endpoint and added a backslash before it and started fuzzing it again

ffuf -c -w <(cat customwordlist.txt ) -u https://company.com/\Extraserivce/FUZZ

shortly after i recevied a very interesting endpoint with a very interesting name callAny

Press enter or click to view image in full size

Based on the endpoint name and the response i thought that this endpoint was taking a parameter then executing it inside a call_user_func or eval or any similar function that executes code so i started fuzzing the endpoint for both GET,POST requests params with a couple of values such as

FUZZ=phpinfo

FUZZ=phpinfo()

FUZZ=phpinfo();

and many more then thought mabye it takes from POST request directly without requests params using something like php://input wrapper

Get 0xold’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so i started trying injecting things like phpinfo <?php phpinfo(); ?> ls etc in the body

Press enter or click to view image in full size

and nothing really worked i also tried things like ssrf/lfi but i couldn’t really figure out what was happening on the backend so i gave up on it.

Monitoring debug mode to figure out what’s happening on the backend

A few days later while browsing the website and testing other functionality i recevied the error below this is an indicator that the developer turned on debug mode in production since debug mode is enabled if navigated to any endpoint that returns an error it will show the error details thus i will be able to know whats wrong so i quickly navigated to Extraserivce/callany endpoint again however i was too late the developer turned off the debug mode after a few secs.

Press enter or click to view image in full size

an idea sparked to my head why don’t i monitor this endpoint and grab the response if the developer turned on debug mode again? so i decided to monitor the endpoint and check if the response size is different it will send the response details to my discord channel. if you want to learn how to monitor your targets i recommend the video below

Shortly After i received the following 3 errors on my discord

Warning: Undefined array key “Model” in redacted on line
Warning: Undefined array key “Method” in redacted on line
Warning: include_once(Models/): Failed to open stream: No such file or directory in redacted on line

you probably now know whats happening the developer was taking a param called Model to include a specific Model then uses the method param to trigger a specific function on the included model. Did you spot the vulnerablitiy? it is an lfi! you might think okay you can include any file but still you will get an error because you need a valid file and a valid method otherwise the server will return 500 status again. well… you are partially right

Press enter or click to view image in full size
Press enter or click to view image in full size

Except the fact that the code will trigger the method after including the file not before so it doesn’t really matter at this point because we already achieved an lfi.

Escalating the LFI to a remote code execution

one of my favorite/quickest ways to escalate an lfi to rce is through php filter chain from https://www.synacktiv.com/publications/php-filters-chain-what-is-it-and-how-to-use-it.html but since we can’t control the first part of the file we can’t really use php wrappers so we will have to work a little bit harder. using the classic methods such as log poisong php session injection, reading proc/self/environ etc didn’t really return any result so i decided to fuzz the web directory looking for clues that may indicate a way to write into the host

Model=../FUZZ

Press enter or click to view image in full size

I then recevied 3 results. reading .gitignore revealed some interesting files

Press enter or click to view image in full size

in particular the log and LOG_Path directories because it is probably going to log some stuff the user can control such as headers/params/path etc

so i decided to fuzz those 2 directories however luckily while fuzzing i forgot to include the log directory so instead of doing

Model=../log/FUZZ.txt

i did Model= ../FUZZ.txt

and when i looked at the response i found out that content of test.txt stores the entire http request of X-ORIGINAL_URL endpoint

Press enter or click to view image in full size

so i requested the path in test.txt file and added a webshell in the header

T: <?php system($_GET[‘cmd-old’]); ?> then executed the ls command as a proof of concept

Press enter or click to view image in full size

hackerone: https://hackerone.com/0xold

twitter : https://twitter.com/0x0ld
