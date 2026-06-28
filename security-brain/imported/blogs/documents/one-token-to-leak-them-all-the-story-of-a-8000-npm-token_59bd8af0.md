---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-19_one-token-to-leak-them-all-the-story-of-a-8000-npm_token.md
original_filename: 2020-06-19_one-token-to-leak-them-all-the-story-of-a-8000-npm_token.md
title: 'One Token to leak them all : The story of a $8000 NPM_TOKEN'
category: documents
detected_topics:
- supply-chain
- idor
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- supply-chain
- idor
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 59bd8af02c1e6562cedc81a917fa5ffb45946c3a05829a80787404cb916436e5
text_sha256: 3c06405a897420d66620c6f3d8dca85fbce4a4c744d47a917c510aa7c236c945
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# One Token to leak them all : The story of a $8000 NPM_TOKEN

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-19_one-token-to-leak-them-all-the-story-of-a-8000-npm_token.md
- Source Type: markdown
- Detected Topics: supply-chain, idor, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `59bd8af02c1e6562cedc81a917fa5ffb45946c3a05829a80787404cb916436e5`
- Text SHA256: `3c06405a897420d66620c6f3d8dca85fbce4a4c744d47a917c510aa7c236c945`


## Content

---
title: "One Token to leak them all : The story of a $8000 NPM_TOKEN"
url: "https://medium.com/@aseem.shrey/one-token-to-leak-them-all-the-story-of-a-8000-npm-token-79b13af182a3"
authors: ["Aseem Shrey (@AseemShrey)"]
programs: ["Google"]
bugs: ["Information disclosure"]
bounty: "8,000"
publication_date: "2020-06-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4485
scraped_via: "browseros"
---

# One Token to leak them all : The story of a $8000 NPM_TOKEN

One Token to leak them all : The story of a $8000 NPM_TOKEN
Aseem Shrey (@aseemshrey)
Follow
8 min read
·
Jun 19, 2020

1.3K

2

Not long ago, I started a youtube channel, HackingSimplified.

Press enter or click to view image in full size
HackingSimplified Youtube Channel

So after a month of making videos on basics of web security attacks, I started another series on the channel namely, the bug bounty series. Here, I am going to talk about the 7 stages of bug bounty and how to go about it. Since, I had started making videos on bug bounty so I thought to brush up my bug bounty skills and automation tools.

Press enter or click to view image in full size
The two playlists

The last time I had browsed through hackerone to do some bug bounty was some time back in Jan 2019. But in the past one month I had been reading a lot of reports, and these reports kindled my interest again. I started looking at the hackerone program directory and my private invites too for a program that satisfied all the conditions I mentioned in my last video : “Scope Review and Bug Hunting Using Github Dorks -Bug Bounty -Ep -02” which are :

No. of reports resolved
Assets
Payout
Response efficiency
Time to triage and Time to bounty ( personal choice )

This program happened to have all the stars aligned :)

No. of reports resolved — Above 550
Assets — All subdomains
Payout — Crtical was $1000-$4000 and lowest was from $50-$200
Response Efficiency — 90%
Time to triage — 2days and Time to bounty — 10days

Since recently I had made a video on template injection so that was my main area of focus. I entered {{7*7}}and other payload, which was relevant to the templating engine being used on almost every input field. This didn’t work though.

Then I tried looking for IDORs and improper access control check using autorize, didn’t have much luck there either.

I started looking at JS files for other endpoints and some secrets getting leaked. Downloaded all the JS files first and then started grepping into it for secrets and url endpoints.

To download all JS files :

If you’ve BURP Suite pro you could straightaway extract all scripts to one file : But this extracts all file into one file with the js url in it, which might be good in most use cases but I also wanted them in their individual files.
So, I first extracted all JS urls and then wrote a small bash script to get all those files with their respective names :
cat urls.txt | xargs -I{} wget "{}"
# Assuming urls are clean i.e. they don't have any extra parameters in the end
# if the url is like this : https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-cacheable-response.prod.js?v=123122
# Then you need to cut the part after '?' like the following
cat urls.txt | cut -d"?" -f1 | xargs -I{} wget "{}"

Tomnomnom’s gf tool came handy here.Using gf urls to get url endpoints, I found private IP getting leaked : http://172.x.x.x . I tried looking near the place this was getting leaked and found there a NPM_TOKEN value. Immediately started looking for ways to use that. I hadn’t used npm much, only knew that it was node package manager . Had used it once, earlier while developing a VueJS application.

After researching for sometime I learnt the following :
1. CI i.e. Continuous Integration systems such as Jenkins pipelines or Travis CI etc use these tokens to build and deploy a webapp in an automated fashion. This token helps them to get access to npm private repository.

2. Different types of tokens such as —Read and publish only, Readonly, CIDR whitelisted i.e. tokens which can be used from a specified IP address range only

3. How to use npm tokens : So your npm tokens should be in the following format in .npmrc file —

registry=https://registry_link_here
//registry_link_here/:_authToken=auth_token_here

And a few more…

I tried accessing the npm registry using this token in my .npmrc file like this :

registry=https://registry.npmjs.org
//registry.npmjs.org/:_authToken=auth_token_here

But in vain. I couldn’t get reply of npm whoami, which I should’ve if the token was valid. Some articles also suggested that you could also keep the NPM_TOKEN value in encrypted form in .npmrc . So, I concluded that this must be an encrypted token. This was Wednesday — Day 1 of hacking on this target.

On the next day after office work, in the evening around 8pm I started looking into the program again. Earlier in January this year I was reading about CSWH i.e. Cross Site Websocket Hijacking ( however this might be unexploitable in sometime now, see this ) and this program was using websockets. So, I started looking into it.

Conditions for CSWH is that the websockets should be only communicating using cookies, like any other CSRF attack.

I practiced onto BURP suite labs to refresh what I had learnt 6 months back. This website also had similar conditions and only cookie was required to get the websocket communication up and running.

Press enter or click to view image in full size
CSRF but on weboscket requests

So I tried leaking the websocket messages but couldn’t get that. On closer inspection I found that it was also using a nonce and that nonce was given by the server to the client in a different request. So basically that acted as a CSRF token, which is usually used to thwart CSRF attacks. However I found some other bugs in their CSRF usage while looking for CSWH. Reported these on the same day. More on that in another post.

Get Aseem Shrey (@aseemshrey)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Friday — Day 3 — After spending around two hours and not finding anything I thought of looking back at the NPM_TOKEN again. I found the JS file and un-uglified it in the browser in the :

Press enter or click to view image in full size
Firefox pretty print
Press enter or click to view image in full size
Chromium based browsers Pretty Print

You could do it online as well : https://unminify.com/

There were around 17k lines but since I had some experience looking at these so I knew most of these were webpack generated code. So I skimmed through the code to find something interesting, mostly near where I found the NPM_TOKEN value.

Press enter or click to view image in full size
NPM_TOKEN

There I found a private registry link, then I realized, why didn’t I think of this 😅.

Press enter or click to view image in full size
Private Repo Link
Press enter or click to view image in full size
Private Registry’s Frontpage

I quickly replace the value of registry in the .npmrc file to this :

registry=https://private_registry_link_here
//private_registry_link_here/:_authToken=auth_token_here

And now to my command of npm whoami I got a reply : srv-npm-registry-ci

Then I tried fetching a list of all the packages in the private npm registry but that’s not possible i.e. you can’t just list all the packages on the private registy. Atleast I couldn’t find a way, let me know if it’s possible. So, I tried retrieving the private code of the company using the following command :

npm view private_repo
npm get private_repo
Press enter or click to view image in full size
Output of npm view command

Now, you might ask as to how I got to know the names of private repos. Well the repos were compiled into one js file which if the source map is available then any browser can easily decouple them in the sources tab in inspect element like this :

Press enter or click to view image in full size
If source map available — Then breakdown into separate components is possible

So from there I got some unminified source code of the private js files and in those were some other included which got me access to those and so on, I could’ve downloaded almost all of their source code.

I didn’t check whether the key had publish access or not as it would require me to publish a package on their private registry, which I thought wouldn’t be wise. Moreover it shouldn’t have publish rights as it was a CI key but you never know, people don’t generally follow the practice of least privilege.

The report was triaged in 17 hours and rewarded in another 7 days. The company handled it very professionally. I’ve asked them as to how these got leaked in the js file, still waiting on their reply.

Press enter or click to view image in full size
Highest bounty was $4000 but they awarded a bonus for this
Key Takeaways :
Look for secrets in JS files — Try building automation around it
Learn using your browser’s dev tools : They alone will help in a lot of ways
Stay updated with the tools — Even if you aren’t doing bug bounties, might help in some of your other work.
Persistence is the key :)

P.S.

There’s a video writeup which talks about this writeup alongwith some BURP automation to find these secret tokens too here :
https://youtu.be/9LBl-uFiYUE

I started to find something else, template injection, and ended up finding 6 other bugs out of which 3 have been duplicate. All in all it had been a wonderful learning experience regarding websockets, will soon post a writeup of that too.

Hope this was worth your time, do checkout my youtube channel : HackingSimplified , I post videos every weekend.

YouTube channel : HackingSimplified

Join the community, share, discuss, learn and grow. I post 3–4 article related to bug bounty and general cybersecurity daily here.

Press enter or click to view image in full size
HackingSimplified Subreddit

Join the subreddit here : HackingSimplified

Telegram here : HackingSimplified

Twitter : @AseemShrey

Thanks for reading :)

Update :

I got a nice suggestion from @darthvader_htb about downloading js files.
You could use another of tomnomnom’s tool to do this:
https://github.com/tomnomnom/fff

cat urls.txt | fff

I don’t suggest installing a plethora of tools and not using the built in tools. However, usage may vary.
