---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-20_is-mathrandom-safe-from-missing-rate-limit-to-bypass-2fa-and-possible-sqli.md
original_filename: 2021-02-20_is-mathrandom-safe-from-missing-rate-limit-to-bypass-2fa-and-possible-sqli.md
title: Is Math.random() Safe? from missing rate limit to bypass 2fa and possible sqli
category: documents
detected_topics:
- sqli
- rate-limit
- race-condition
- command-injection
- mfa
- otp
tags:
- imported
- documents
- sqli
- rate-limit
- race-condition
- command-injection
- mfa
- otp
language: en
raw_sha256: 84a53e99985381fc3a2d355860adc7f950fb0f5bf1da803a221bad4935c03b12
text_sha256: e1c416a38e05233ea96f96dc51960e4926650e81873f8c52439c0d8b3c8aaa4e
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Is Math.random() Safe? from missing rate limit to bypass 2fa and possible sqli

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-20_is-mathrandom-safe-from-missing-rate-limit-to-bypass-2fa-and-possible-sqli.md
- Source Type: markdown
- Detected Topics: sqli, rate-limit, race-condition, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `84a53e99985381fc3a2d355860adc7f950fb0f5bf1da803a221bad4935c03b12`
- Text SHA256: `e1c416a38e05233ea96f96dc51960e4926650e81873f8c52439c0d8b3c8aaa4e`


## Content

---
title: "Is Math.random() Safe? from missing rate limit to bypass 2fa and possible sqli"
url: "https://neroli.medium.com/is-math-random-safe-from-missing-rate-limit-to-bypass-2fa-and-possible-sqli-2a4ea66f82c5"
authors: ["Yasser Mohammed (@boomneroli)"]
bugs: ["Race condition", "Lack of rate limiting", "OTP bypass", "SQL injection"]
publication_date: "2021-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3878
scraped_via: "browseros"
---

# Is Math.random() Safe? from missing rate limit to bypass 2fa and possible sqli

Is Math.random() Safe? from missing rate limit to bypass 2fa and possible sqli
Yasser Mohammed (@n3r0li)
Follow
4 min read
·
Feb 20, 2021

106

Hi everyone It’s Yasser Again,

First of all i wanted to thank you all for sharing my last write-up and I got a lot of positive responses so I decided to write about another nice finding that i found lately.

I was testing a mobile application which was written in React-Native for private program on 
HackerOne
 about 5 months ago,

While my server-side testing I didn’t found a lot of functions but as always I was working on developing a similar application as school project, and i got some problems with Synchronization, so while testing 2fa functionality I was asked to confirm the OTP which was sent to my phone number,

so let’s see if the back end is going to crash if we sent a lot of requests,

So using the intruder i sent a lot of requests and waited for the corresponding messages to fill my phone with many OTPs

and yeah I got a lot of confirmation codes, this is a missing rate limit but i never submit it if I didn’t got high impact scenario from it,

remembering that while I was developing my application I had to use Math.random() to generate these codes, but is it really that random ??

pseudo-randoms

Let’s have a closer look on how this function works,

we cannot generate a pure random numbers since there is a lot of factors that could affect our randomization process which can make is so predictable,

and that’s what is called pseudo-random, it’s so unpredictable but it’s not impossible since it depends on something called seed ,

to understand how is it working this video is so useful

as in the video the if we inserted 2 duplicate seed’s into math.random we will get the same sequence,

so if i was able to use this seed and send the request at the same time I will be able to guess the OTP,

but this is soo hard to implement since it depends on the system clock on the server and my system clock.

Synchronous vs Asynchronous

the server was using asynchronous functions to handle our requests

you can read this great article to understand how does js synchronous/asynchronous works,

shortly synchronous means if we run this code:

const second = () => {
  console.log('Hello there!');
}const first = () => {
  console.log('Hi there!');
  second();
  console.log('The End');
}first();

the output will be:

Hi there!
Hello there!
The End

since the call stack got to execute function first and stop until the code in the function second executed then back to execute the rest of function first

in asynchronous we can execute 2 functions as above but the 2 functions will be executed in parallel with no blocking,

read the above article for more details.

Exploitation

in this case our answer is simple, Race-Condition

using turbo intruder in burp with this race condition script I will be able to send multiple requests in the same time so it will be executed on the server in the same time

so we will call Math.random() many times this could give us a duplicate result in if the length of the result is not too long,

Get Yasser Mohammed (@n3r0li)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

here is a sample for a vulnerable code written in nodejs

var http = require("http");
async function asyncCall() {
var x = Math.floor(Math.random() * 1000).toString();
return x;
}
http.createServer(function (request, response) {
response.writeHead(200, {'Content-Type': 'text/plain'});
asyncCall().then((value) =>{
console.log(value);
response.end(value);
});
}).listen(8081);

with sample turbo intruder script:

def queueRequests(target, wordlists):
  engine = RequestEngine(endpoint=target.endpoint,
  concurrentConnections=30,
  requestsPerConnection=100,
  pipeline=False
  )

  for i in range(30):
  engine.queue(target.req, "", gate='race1')

  engine.openGate('race1')
engine.complete(timeout=60)
def handleResponse(req, interesting):
  table.add(req)

we will notice that we got duplicate numbers

POC
Notes

this scenario have a lot of aspects and depends on a lot of things to apply a successful Attack Like:

length of the OTP
internet connection speed
number of requests
concurrent Connections
the back-end framework

this slide by OWASP is so useful to understand the attack more concurrency Vulnerabilities

Life Example (Exposing the OTP and sqli)

applying the above steps on the target leads to expose the OTP Generated code

but the reason why we got a valid Code is that the query inserts our user_id which is the primary key in this case so we got a valid OTP

Press enter or click to view image in full size
Press enter or click to view image in full size
SQL error

And as always I was like

I noticed that phone number was not being validated well which lead to sqli.

this endpoint was responsible for all the OTP generation in the whole application so 2fa, number confirmation, reset password ..etc

I hope u enjoyed and thanks for reading again.

References
Google Chrome Attack
http://davidbau.com/archives/2010/01/30/random_seeds_coded_hints_and_quintillions.html
https://www.veracode.com/security/race-condition
https://blog.bitsrc.io/understanding-asynchronous-javascript-the-event-loop-74cd408419ff
https://www.youtube.com/watch?v=GtOt7EBNEwQ
concurrency Vulnerabilities
