---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-30_using-xampp-and-burp-intruder-when-scanning-for-subdomains-to-look-for-interesti.md
original_filename: 2020-07-30_using-xampp-and-burp-intruder-when-scanning-for-subdomains-to-look-for-interesti.md
title: Using XAMPP and Burp Intruder when scanning for subdomains to look for interesting
  behaviour & code
category: documents
detected_topics:
- api-security
- xss
- command-injection
- information-disclosure
- mobile-security
tags:
- imported
- documents
- api-security
- xss
- command-injection
- information-disclosure
- mobile-security
language: en
raw_sha256: 6c8a51b4331581d14bada823616c4b3ea4e7ec0783ecba5062dc379ce125119a
text_sha256: f775f318b16125a57e3e9c945543cfbeb9016dc3d889c6d424151ec797516cca
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Using XAMPP and Burp Intruder when scanning for subdomains to look for interesting behaviour & code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-30_using-xampp-and-burp-intruder-when-scanning-for-subdomains-to-look-for-interesti.md
- Source Type: markdown
- Detected Topics: api-security, xss, command-injection, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `6c8a51b4331581d14bada823616c4b3ea4e7ec0783ecba5062dc379ce125119a`
- Text SHA256: `f775f318b16125a57e3e9c945543cfbeb9016dc3d889c6d424151ec797516cca`


## Content

---
title: "Using XAMPP and Burp Intruder when scanning for subdomains to look for interesting behaviour & code"
url: "https://medium.com/@zseano/using-xampp-and-burp-intruder-when-scanning-for-subdomains-to-look-for-interesting-behaviour-code-f24c511d15ed"
authors: ["Zseano (@zseano)"]
bugs: ["Information disclosure"]
publication_date: "2020-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4366
scraped_via: "browseros"
---

# Using XAMPP and Burp Intruder when scanning for subdomains to look for interesting behaviour & code

Using XAMPP and Burp Intruder when scanning for subdomains to look for interesting behaviour & code
Sean (zseano)
Follow
5 min read
·
Jul 30, 2020

587

3

Do any of you use Intruder when checking out subdomains? For me personally I use a tool called “XAMPP” which lets me run PHP locally combined with intruder. From here I then create a simple redirect script inside index.php, <?php $url=$_GET[‘url’]; header(“Location: “.$url); ?>. Next I modify my /etc/hosts/ file and add “anydomain.com 127.0.0.1” and now anytime I visit http://anydomain.com/?url=https://www.google.com/ it will redirect to google.com. Perfect.

So where does intruder come into this.. or more, why? Well the beauty of Burp Suite is you can easily see the Response and that’s exactly what i’m interested in. I love to see what it’s in front of me, understand the code, the flow. I will manually scroll through results to check for anything interesting on the first page, does it make use of much JS, what is referenced, how many redirects occurred etc. (yes it can be tedious.. but hey, i’m motivated, interested & curious. I want to know what’s going on).

To get started doing this I will simply visit http://www.anydomain.com/?url=https://www.example.com/ and send this request to Intruder. I will then load a list of subdomains I have scraped, set burp to follow all redirects (and process cookies), untick payload encoding and then simply start the attack!

(This can also be great for mass testing for XSS & other bugs and using Grep to mass check across the results. Perhaps I will write a detailed post on this some day)

Press enter or click to view image in full size
Press enter or click to view image in full size

So how did this end up with me finding a P1? Well after the scan had completed I simply started browsing each result and on a certain domain I noticed the use of lots of JavaScript. Curiosity gets the better of me and I want to go have a look at this page and see what it does. It redirected to /login after browsing the root domain so there may be something interesting here.

As you can see the above code will send a POST request to /login with the users login information and if its successful, redirect to /dashboard. As a hacker you should always try visit these URLs anyway to see what happens. In my case it redirected instantly back to /login however Burp says the content length was 224137… that’s pretty big considering it just redirected? Or did it..?!

Well the redirect was via META Refresh however the page contents had also loaded and this refresh was merely at the top. If I paused the page mid-redirect then I could see what the admin dashboard looked like but nothing worked (due to me pausing page mid-load). Close, but damn! Browsing the contents (view-source:) of the page I noticed again the use of more JavaScript code referencing even more endpoints, except this time they were on AppSpot.com. Since it was now making calls to an external domain, I just knew there would be no session handling.. oh and the fact that the API-KEY needed to make calls was referenced also. Let’s test this!

After sending a request to the appspot URL with the required API-KEY it responded with what looked like an encrypted string. Hmm.. interesting, what does this do? We’re getting closer, but nothing interesting to report so far.

You know me, I love my notes. Anytime I see interesting encryption being used, IDs, parameter names etc.. I note it down. In this case there was another endpoint on a completely different subdomain which took this encrypted ID as an parameter value and it would respond with PII information about the user in a PDF format. And now it’s worth reporting..! ;) I was rewarded with their top bounty within 20 minutes of reporting.

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To sum this up, I simply:

Scraped for subdomains using basic tools
Ran these through burp intruder to check results and mass grep for certain keywords (“url:” for example to look for any potential ajax requests. “xmlhttprequest”, “POST” etc.)
Found an interesting domain which made use of ajax requests, saw after it had authenticated it would redirect to /dashboard
Visited /dashboard and was automatically redirected but noticed it was simply a META refresh and the contents had actually loaded as well.
Browsed the contents loaded (view-source:) and saw even more javascript code making requests to an appspot.com domain which took a users ID as a parameter. What does this do..?
Attempted to query this endpoint and discovered I could reveal information on any user fully unauthenticated using the encrypted ID it responded with on another endpoint on a separate subdomain.

TLDR: I input any users ID, it responds with encrypted ID, I use this ID to reveal their PII information.

Take aways

Just because a page redirects, find out how & why. Is it because you are not authenticated?Does it load via 302 header, or is it redirecting via some javascript/meta refresh? If so, is there anything of interest in the code the page is redirecting away from?

How many of you dork for “.appspot.com” on places like github & google? (Something as simple as companyname “appspot.com” has got me results) Or even just monitoring subdomains of .appspot.com. Companies like to host interesting APIs on there either for testing purposes (which they may forget about), or used in production (in which case you may find api keys referenced in .js files somewhere? Swagger is popular to find.

Take notes, even if you think it isn’t interesting now, the longer you spend on a program the more your notes will help. They don’t need to make sense, you just need to mentally log “there is an [xyz] being used here, seems interesting”. You never know when the final piece of the puzzle will be needed. ;)

The more you can see, the better. Don’t just trust screenshots of your subdomains, check what’s under the hood!

Happy hacking!

-zseano
