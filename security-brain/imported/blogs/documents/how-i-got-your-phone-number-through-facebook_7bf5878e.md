---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-20_how-i-got-your-phone-number-through-facebook.md
original_filename: 2017-02-20_how-i-got-your-phone-number-through-facebook.md
title: How I got your phone number through Facebook
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- mfa
- automation-abuse
- business-logic
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- mfa
- automation-abuse
- business-logic
language: en
raw_sha256: 7bf5878e69bb2278c8a5f0b235b0cdd71ff789e83e64c8584b9ab71d8da57d66
text_sha256: 6f05cd905d65cb87fb4d461e1141a2fda137ac61cda6cecb79e7943094da4a5b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I got your phone number through Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-20_how-i-got-your-phone-number-through-facebook.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, mfa, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `7bf5878e69bb2278c8a5f0b235b0cdd71ff789e83e64c8584b9ab71d8da57d66`
- Text SHA256: `6f05cd905d65cb87fb4d461e1141a2fda137ac61cda6cecb79e7943094da4a5b`


## Content

---
title: "How I got your phone number through Facebook"
url: "https://medium.com/intigriti/how-i-got-your-phone-number-through-facebook-223b769cccf1"
authors: ["Inti De Ceukelaire (@securinti)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2017-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6218
scraped_via: "browseros"
---

# How I got your phone number through Facebook

1

How I got your phone number through Facebook
Inti De Ceukelaire
Follow
10 min read
·
Feb 21, 2017

1.4K

28

Don’t have the time to read the entire article? Go to the FAQ section below for everything you should know.

Update: someone pointed out that PayPal actually reveals the last four digits of the phone numbers, so this technique may work for large countries as well if the target has its phone linked to its PayPal account.

Press enter or click to view image in full size
Verifying one of the phone numbers I discovered

Last month, I discovered it is relatively simple to reveal private phone numbers on Facebook, uncovering some phone numbers of Belgian celebs and politicians. Even though this trick only seems to work in small countries such as Belgium (+/- 11.2 million people), a significant number of people is affected by this simple, yet effective privacy leak.

When I notified the fine folks of the Facebook Security team with my concerns, I got an answer I didn’t quite expect:

Press enter or click to view image in full size
Not an issue, according to Facebook

When the “who can look me up by phone” setting is set to public, your phone number is public.

There are a few issues with this:

The setting is set to public by default
It’s confusing: even though your phone number on your profile is set to ‘only me’, the ‘who can look me up’-setting overrules this. While people think their phone number is private, it’s not:
Press enter or click to view image in full size
This setting only indicates whether the phone number is visible on your profile. It does not indicate whether your phone number is public.
Press enter or click to view image in full size
If this setting is set to ‘Everyone’, which is the default value, your phone number is considered public.

‘Who can look me up’ also implies the person ‘looking you up’ already has your phone number. It implies that someone if looking for your specific Facebook profile based on your phone number, and not the other way around.

There is simply no only me setting
Press enter or click to view image in full size
If you link your phone number to Facebook and want to lock down your privacy settings, you can not prevent your ‘friends’ will still have access

Despite sharing my concerns with the security team, they decided not to fix the issue. Even though I do not agree I respect their decision. I did decide the write about it nonetheless — I think people have the right to know.

Many people don’t even know Facebook has their phone number. While Facebook can not just extract your phone number from your phone, it will repeatedly ask you to confirm and save your number upon launching Facebook for mobile. After a colleague deleted his phone number following my findings, Facebook immediately asked him to re-enter it:
Click the button to share your phone number with the world again

How it works

My technique uses the graph search. Most people knows that you can enter a phone number in the Graph Search to get the corresponding user:

Press enter or click to view image in full size
Verifying a Belgian celeb’s phone number I found using my technique

Simply testing every number is an impossible job that would take months. Facebook also has some strong rate limiting in place that will temporarily block additional requests after +/- 1000 lookups. Sure, you could use a botnet with valid Facebook accounts, but I’m sure Facebook has some restrictions to tackle these, too.

STEP 1: The last two numbers (1 minute)

I had to find a way to test thousands of phone numbers at once. The less phone numbers I’d have to test, the quicker I could get to the full number. To eliminate the last two numbers, I used Facebook’s password reset functionality:

Press enter or click to view image in full size
Facebook reveals the last two digits of the minister our home affairs, a highly ranked politician
STEP 2: The provider number (5–35 minutes)

Here’s a typical Belgian phone number, where X equals any number from 0–9, and PP equals the provider number. I already filled in the last two digits we got in the previous step.

04PPXXXX50

(Less than 400,000 possible numbers)

Provider numbers are linked to the mobile phone provider:

Press enter or click to view image in full size

Some provider numbers are more widely used than others. People working for the government most likely have a 047 number, as Proximus is the state-sponsored provider.

Get Inti De Ceukelaire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this point, I wrote a program that would make a contact list with every possible number starting with, let’s say, 0479:

Press enter or click to view image in full size
It took less than a second to generate a list with all 10,000 possible numbers

Then imported this list in the ‘find friends’ functionality and checked the suggested friends

Press enter or click to view image in full size
There were a couple of “Jan”’s in the list, but my target was not. Don’t mind the ‘500’ number — more contacts were in imported.

No luck for 0478, either. I had to switch accounts at this time because Facebook only allows 20,000 contacts to be imported in a short timespan. I logged into another test account, tried with 0477 got “third time lucky”:

Press enter or click to view image in full size
0477 it is!

So at this moment we can add the provider number:

0477XXXX50

We also have a list of 10,000 numbers of which one is the minister’s number.

STEP 3: Narrowing down (10–15 minutes)

The last part only consists of some simple math: we have 10,000 possible numbers left, so if we test half of those numbers we can narrow down our pool to a handful of numbers, for example:

0477 0000 50 — 0477 5000 50

Press enter or click to view image in full size
Still bingo!

The target was present in this range, so this means that the fifth number is either 0, 1, 2, 3 or 4. 5000 [0000–5000] possible numbers left.

Let’s divide the 5000 numbers that are left by two again.

Testing for 0477 0000 50 – 0477 2500 50:

Press enter or click to view image in full size
No results found

No luck with the 0000 – 2500 range, so we can be sure the phone number is in the 2500–5000 range. We got 2500 numbers left, split the pool in a half so we have 1250, 750, 325, 162, 81 and ultimately 40 numbers left. We can continue to do trial-and-error testing by spitting the pool in a half to 20, 10 and 5 numbers, but with less than 50 numbers left you can also test all numbers individually in the graph search.

STEP 4: The final countdown (1 minute)

With only 40 possible phone numbers left, it is pretty easy to test all the numbers that are still in the pool. Just enter them in the search bar until you hit the profile you were looking for.

Press enter or click to view image in full size
Testing all numbers left manually until I got the right one.

I informed the minister about this privacy leak. In a statement he said he didn’t know Facebook was leaking is phone number, but he personally doesn’t really mind as long as there’s no abuse.

In cooperation with a local radio station we called another Belgian celebrity on air to inform him about the fact that I found his phone number through Facebook. We had a nice chat and he removed his phone number from Facebook immediately afterwards.

FAQ
What’s the problem?
In small countries phone numbers on Facebook are easily discoverable. Facebook argues that whenever the setting “who can look me op by phone number” is set to public (which is the default setting), your phone number is considered public (even though it is not displayed on your profile). This is confusing and Facebook offers too little measures to prevent this. Setting your phone number entirely to ‘only me’ is simply not possible.
Who is affected?
Anyone in a small country that (perhaps unknowingly) added their phone number and did not change the default setting. It is hard to give an exact list of affected countries, but if you have a 10-digit phone number and the list of provider numbers (first two) is rather limited, it should work.
How can I test whether Facebook knows my phone number?
Go to https://www.facebook.com/settings?tab=mobile. All known phone numbers should be listed there.
How can I test whether I’m affected?
(Only if you live in a country with a rather small population, like Belgium):
Check whether Facebook knows your phone number (question above).
Go to https://www.facebook.com/settings?tab=privacy and check the setting “Who can look you up using the phone number you provided”. If it’s set to “Public”, anyone could retrieve your phone number if conditions above are met. If it’s set to “Friends”, only your friends can. Note that there’s no “Only me” setting.
How does it work?
The process consists of four steps and requires a program that is able to generate a specific range of phone numbers
1. Getting the last two numbers using password reset (takes 2 minutes)
2. Getting the provider number (if any, depends on luck, takes 15–35 minutes for a Belgian phone number) by generating a list of possible numbers and importing them though the ‘find friends’-functionality.
3. Narrowing down the pool by splitting it in half and trial and error (15–20 minutes).
4. Testing the numbers left (40) manually in the Graph search (2 minutes)
It is impossible to predict how long it takes to discover a phone number as it depends on the amount of possible phone numbers, prerequisites (test accounts, phone number generator) and some luck, however I think it’s safe to say that in my testings it took only30 minutes to 60 minutes to crack most numbers.
What can (or should) Facebook do about this?
It all comes down to informing people. The biggest problem with this is that most people don’t know about this as it is the default behaviour. Things would be different if the ‘who can look me up’ feature is set to ‘only me’ (which doesn’t exists, yet), in the first place. Facebook could also hide the two numbers that are revealed in a password reset request whenever the user does not frequently log in from that particular computer. They could also limit the amount of ‘friends’ you can import further (I don’t see why anyone would import 10.000 numbers at once).
I’m affected. Should I remove my phone number?
That’s a tough question, because phone numbers provide an excellent form of two-factor authentication which is a recommended privacy safeguard. You can still limit your ‘who can look me up’-setting to ‘only friends’.
I don’t care my phone number is public
Good for you. I personally don’t mind either — but I’m quite sure others do. Most politicians and Belgian celebs I contacted about this issue were glad I made them aware of this and removed their phone number right away.
Caring whether your phone number is public or not, it doesn’t really matter. To me, a more concerning part is that users seem to be misinformed by vague privacy settings. If you set your phone number to ‘only me’ it shouldn’t be overruled by some other default setting. It proves that despite its efforts, Facebook still faces some tough challenges concerning privacy and usability.
Timeline
> Jan, 9th — Me: Initial report to Facebook
< Jan, 9th — Facebook: Automated reply
> Jan, 9th — Me: Some additional info
< Jan, 9th — Facebook: “No tangible security or privacy impact.”
> Jan, 9th — Me: Are you sure? Further clarification
< Jan, 10th — Facebook: Yes.
> Jan, 12th — Me: Thanks — I don’t agree but I respect the decision. (1/2)
> Jan, 12th — Me: Ask if I can blog about it in February (2/2)
< Jan, 12th — Facebook: further clarification (see the screenshot above)
Are you mad at Facebook?
Not at all. Facebook has one of the best bug bounty programs and security teams available to hackers. I respect their decision but I also think it’s our right to be informed of the design decisions which may impact our privacy.
I found a vulnerability in Facebook. Where do I start?
Cool! Make sure you read their Bug Bounty Rules and are reporting a valid bug. After reporting the issue here, they may decide to honor you in their Hall of Fame and reward you with a bounty starting at $500 USD.
Who are you?
I’m Inti and I live in Oilsjt, Belgium — the country known for its beer, fries, chocolate and terrorists. As a kid, I was extremely skilled at breaking stuff. I’m 21 now, student, and still doing more or less the same being an ethical hacker with references as Google, Facebook, Microsoft, Yahoo and so on. I don’t really consider this as a ‘hack’ or a ‘vulnerability’ though — more like a privacy issue people should know about.
Any other projects?
I recently hijacked a Trump tweet, made StalkScan.com that highlights the creepy side of the Facebook graph search and wrote a similar blogpost before that eventually got Facebook to fix the addressed issue.

If you liked this article, make sure to follow me on Twitter: @securinti(English) and @intidc (Dutch)

Hacker Noon is how hackers start their afternoons. We’re a part of the @AMI family. We are now accepting submissions and happy to discuss advertising & sponsorship opportunities.

If you enjoyed this story, we recommend reading our latest tech stories and trending tech stories. Until next time, don’t take the realities of the world for granted!
