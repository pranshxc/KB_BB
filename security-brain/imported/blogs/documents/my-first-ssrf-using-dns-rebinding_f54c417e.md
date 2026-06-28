---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-11_my-first-ssrf-using-dns-rebinding.md
original_filename: 2019-11-11_my-first-ssrf-using-dns-rebinding.md
title: My First SSRF Using DNS Rebinding
category: documents
detected_topics:
- ssrf
- sso
- jwt
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- ssrf
- sso
- jwt
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: f54c417e41c723239b4be7c0848188cb526ac7ab4f704be64ac4ce29901016c8
text_sha256: bdd3602d7017433dd61af0f65d1342f32fc359f598a3105e464dff617f62548a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# My First SSRF Using DNS Rebinding

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-11_my-first-ssrf-using-dns-rebinding.md
- Source Type: markdown
- Detected Topics: ssrf, sso, jwt, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `f54c417e41c723239b4be7c0848188cb526ac7ab4f704be64ac4ce29901016c8`
- Text SHA256: `bdd3602d7017433dd61af0f65d1342f32fc359f598a3105e464dff617f62548a`


## Content

---
title: "My First SSRF Using DNS Rebinding"
page_title: "My First SSRF Using DNS Rebinding | marek.geleta"
url: "https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/"
final_url: "https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/"
authors: ["Marek Geleta (@marek_geleta)"]
bugs: ["SSRF", "DNS rebinding"]
publication_date: "2019-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4952
---

# My First SSRF Using DNS Rebinding

Written by [Marek Geleta](https://geleta.eu) with ♥  on 11 November 2019 in __ [ Bug Bounty ](https://geleta.eu/categories/bug-bounty/) __8 min

# What is DNS Rebinding?

Imagine you are a comuter :D People give you URLs and you load them

Of course you won’t load url that points to your internal network… That would be stupid right?

Because of this some clever developer wrote code like this to prevent it from happening

To make explaining this easier

  * `ip_banlist` is list of IPs you are blocking

  * `domain` is the URL you are trying to fetch

  * `getHostname` is a function that resolves a domain/URL to actual IP address or translates it from eg. octal to IPV4/6
  
  import requests
  from core_funcs import getHostname
  from banlists import ip_banlist
  
  def secureFetch(domain):
  if getHostname(domain) not in ip_banlist:
  r = requests.get(domain)
  return r.text
  

> “You can’t just bypass this”
> 
> — a not so clever Developer

## Turns out I actually can!

And that’s what DNS Rebinding is about!

### Let’s go through the function line by line

  * Let’s say the function is ran with `domain='http://wtf.geleta.eu'` and that the `ip_banlist = ['169.254.169.254', '127.0.0.1']`
  * First it runs a DNS query with wtf.geleta.eu which returns 12.34.56.78 which is not in `ip_banlist` so our journey continues!!!
  * In the meantime the DNS record for wtf.geleta.eu magically changes to 127.0.0.1 🦹🏻‍
  * now the request is made to `http://wtf.geleta.eu` so again somewhere in the `requests.get()` the dns query is ran again and now with DNS record changed to 127.0.0.1 Soooo there’s nothing stopping us from retrieving localhost 🎉🎉🎉

So that’s the theory behind this whole thing. Pretty primitive right?

## What do we actually need to make this happen

  * Since we can’t manually change the dns record in milliseconds as the program runs, we need a custom DNS server configured to somehow figure out what IP should it resolve to and set TTL to 0 so no caching happens on the backend
  * Some “interface” to configure the domain - what should it resolve to, how many times, stuff like this
  * A fair bit of luck obviously

When I found this bug I used <https://lock.cmpxchg8b.com/rebinder.html> but later on I figured out that it’s not ideal, it only takes 2 IPs and resolves between them randomly so I have to send like 100 requests to get 1 that actually went to localhost :D

(This was about 7-8 months ago, I made my own tool for this. So expect little product placement at the end of the post!)

# How it went down with the actual vulnerability

I stumbled upon a service that I can configure to make a json request, set headers, etc. Then it gives me the http response

When i set the url to some internal/banned ip like `127.0.0.1` it gave me something like: `The request was blocked`

After few hours of trying to bypass it I was like “This is unbreakable, I’m gonna get some food”

Then I got some food and minute after that I remembered that my friend [Jan Masarik](https://masarik.sh) did one challenge when we were hacking Fireshell CTF 2019 ctf with our [CTF team](https://ctftime.org/team/53880) The challenge was about dns rebinding. Writeup: <https://ctftime.org/writeup/13005>

The actual ctf challenge was created by [ELB](https://twitter.com/Elber333) so If you are reading this I just want to say BIG thank you for making this challenge!

So I used the technique from writeup. I set the rebinding to 127.0.0.1/google ip and after sending 100 request with burp intruder 2 of them came back with different lenght than others, I click on one of them and see a html code with title which was name of the company

And I was like

![](/images/ring.svg)

NO WAY!!!!! IT ACTUALLY FUCKING WORKED WTFFFFFF I’M A 1337 HAXXXXXOR NOW

![](/images/ring.svg)

With dns rebinding confirmed, I didn’t actually know what to do… Everything I have ever hacked before were just ctfs - and this is where the challenge usually ends, you have the flag and your are good to go

## It doesn’t work that well IRL

Now all I had was some ssrf that I didn’t know what I can use it for.

Few hours went by and there I was sending keybase message to [Jan Masarik](https://masarik.sh) because I was stuck again. I told him that it was an amazon instance and he sent me some ip adress - 169.254.169.254 I clicked on it and nothing happened, that IP didn’t exist Then he told me that it is the aws metadata IP and if I can retrieve data from there, I basically own their whole aws (It wasn’t completely true as you find out in a while but I was really really excited) I immediately fired up intruder and in few seconds I recieved a response with aws keys

![](/images/ring.svg)

Now again I was like

![I love Pingu btw](/images/ring.svg)I love Pingu btw

And I love the ssrfs too!

## Back Into reality

Those were some trashy keys, I couldn’t do almost anything with them…

Turns out I can only r/w some buckets but there weren’t any useful, those that were hosted on frontend weren’t writable (my favorite was the one with cookbooks - see screenshot) It made me laugh but I was disappointed. I tried to escalate my privs for another few hours and-or figure out what else could I do but there wasn’t much of it :(

![](/images/ring.svg)

Ok so the vuln had _some_ Impact so I could report it. I set severity to P2 Now all left to do was enumerate and possibly get a RCE if I was lucky

## Fast forward a week

I didn’t have any response from the company,no fix, no lawsuit, nothing at all. Perhaps I should report it as P1. But whatever! It was good for me, I could enumerate more.

### AAAAND After chaining with other ssrf…

This was a bit easier - there was a ftp connection vulnerable to ssrf - When some other service than ftp was passed in, let’s say 127.0.0.1:22 server errored out with `Bad FTP RESPONSE: SSH-2.0-OpenSSH_someversion` So using this I was able to enumerate open internal ports on their server Another thing that was possible was bruteforcing ftp credentials on 127.0.0.1:21 since it was open too, I tried it with top-1k but it didn’t work out :(

So I just enumerated the ports…

## Fast forward another few hours

I found a Monit Admin interface I was able to interact with via dns rebinding ssrf It had an buffer overread vuln so I was able to read some memory (+1 point in impact :D) Aaand I could shut down the whole instance using shutdown function in Monit (+10 points)

Then I reported this too!

# I got a response in a fucking month………

Meanwhile I turned into skeleton

![](/images/ring.svg)

But eventually they responded! They fixed it, gave me a not that big bounty (It’s a small program), everyone was happy, life went on :D ![](/images/ring.svg)

# Lessons learned

  * Bugs exist everywhere

  * I you are stuck, go back few steps and start again

  * If you are stuck after doing the step above - message your mentor/more expirienced hacker they will always help you

  * Be patient AF

  * If you have free time, create some great tool! or contribute to other great tools

  * BB is not entirely about money, It’s more about the things you learn

# Now it’s time for some self-advertisment

## Are you tired of exploiting DNS Rebinding without gui?

This may sound Scriptkiddie-ish but I actually wanted something with gui and logs

### How it went down

I was on a vacation and I got sick probably from the food and I couldn’t go out swimming. So I pulled out my laptop and started working on a Flask api connected to modified dns server via SQL and Redis… And I Can’t forget the React frontend, It was the worst thing of it all. Sorry frontend fanboys, I just value my mental health.

After 1.5 days Everything except from the React app of course was done, You can actually check the code out [Here](https://github.com/makuga01/dnsFookup) and the Live Version with dns server and everything is [Here](http://rbnd.gl0.eu/) \- you can register, create rebind rules, use it to hack something, watch logs and stuff like that. Yes it’s and http link I know that and I hate myself for that but I’m too lazy to spend 2 minutes with certbot

For those who didn’t look thamselves what it does is

  * I tell it to make a subdomain that will resolve to `1.2.3.4` 3 times and then to `127.0.0.1` 1 time

  * It puts the data into db and gives me something like `y1982ehiuwqh82319j2139821.gel0.space`

  * when I make a query to this domain, dns server looks into db, loads the data into redis for quicker future access and then resolves it based on the rules given

#### If you have a bit of free time, don’t watch netflix - Hack, create and most importantly contribute to <https://github.com/makuga01/dnsFookup> 😇 I will be veryveryvery happy if someone adds some feature to it or adds something to the frontend, the BE api is nice and working but the frontend is a problem for me

Anyway thanks for reading! Hope you liked this writeup, If you have some questions/suggestions/you just wanna talk with some cringy script kiddie just DM me on twitter [@marek_geleta](https://twitter.com/marek_geleta) or anywhere else I will almost certainly respond to you in few minutes, I like talking to people 😄

I’m sorry for the amount of text/things learned I will get better I promise, I just like writing stories with incorrect grammar

PS.

sory for my Englandish, It not my primar languge

Author: Marek Geleta 

Words: 1545

Share: [ __](//twitter.com/share?url=https%3a%2f%2fgeleta.eu%2f2019%2fmy-first-ssrf-using-dns-rebinfing%2f&text=My%20First%20SSRF%20Using%20DNS%20Rebinding&via=marek_geleta "Share on Twitter") [ __](//reddit.com/submit?url=https%3a%2f%2fgeleta.eu%2f2019%2fmy-first-ssrf-using-dns-rebinfing%2f&title=My%20First%20SSRF%20Using%20DNS%20Rebinding "Share on Reddit")

Released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

__Tag:[ #bugbounty](https://geleta.eu/tags/bugbounty/) [ #ssrf](https://geleta.eu/tags/ssrf/) [ #writeup](https://geleta.eu/tags/writeup/) [ #security](https://geleta.eu/tags/security/) [ #bug](https://geleta.eu/tags/bug/) [ #bounty](https://geleta.eu/tags/bounty/) [ #dns rebinding](https://geleta.eu/tags/dns-rebinding/) [Back](javascript:window.history.back\(\);) · [Home](https://geleta.eu)

[A tale of verbose error message and a JWT token  __](https://geleta.eu/2020/a-tale-of-verbose-error-message-and-jwt-token/ "A tale of verbose error message and a JWT token")

[comments powered by Disqus](https://disqus.com/)
