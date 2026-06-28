---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-01_the-journey-from-google-honorable-mention-to-hall-of-fame.md
original_filename: 2021-08-01_the-journey-from-google-honorable-mention-to-hall-of-fame.md
title: The journey from Google Honorable Mention to Hall of Fame.
category: documents
detected_topics:
- command-injection
- password-reset
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- information-disclosure
- api-security
language: en
raw_sha256: 0797b66c3fd8ab31bb8713c4318c574f98b9a0263c06d2c246e8633b1a034c4f
text_sha256: 70b1db9455c27fe62bd04ad5bd91e04670cab2c9dbcc9076ae3de48c9735e5e7
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# The journey from Google Honorable Mention to Hall of Fame.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-01_the-journey-from-google-honorable-mention-to-hall-of-fame.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `0797b66c3fd8ab31bb8713c4318c574f98b9a0263c06d2c246e8633b1a034c4f`
- Text SHA256: `70b1db9455c27fe62bd04ad5bd91e04670cab2c9dbcc9076ae3de48c9735e5e7`


## Content

---
title: "The journey from Google Honorable Mention to Hall of Fame."
url: "https://medium.com/pentesternepal/the-journey-from-google-honorable-mention-to-hall-of-fame-f62d9d5882ea"
authors: ["Akash basnet (@noneofyou007)"]
programs: ["Google"]
bugs: ["Referer leakage", "Information disclosure", "Password reset"]
publication_date: "2021-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3455
scraped_via: "browseros"
---

# The journey from Google Honorable Mention to Hall of Fame.

The journey from Google Honorable Mention to Hall of Fame.
Akash basnet
Follow
3 min read
·
Aug 1, 2021

153

1

Earlier I found a valid bug in google but that doesn’t meet the bar for reward & I have to satisfy myself to be Enlisted in Honorable Mention only.

Then after few months, I was again searching for a bug to take a leap from Honorable Mention to Hall of Fame. I was searching in google main domains but no luck! then I started hunting on the google acquisition site.

I found a domain name waze.com & started searching for bugs. I didn’t find anything interesting than I took a break.

One day, I met a friend named 
Saugat Pokharel
 & discussed the vulnerabilities. He told me about Password Reset Link Leaked In Refer Header In Request To Third Party Sites bug. I thought of testing this bug in the domain where I was searching for the bug.

During the test I successfully detected this bug and reported it to google which would have not been possible without the help of 
Saugat Pokharel
. So, thanks to him! ❤

Reported From the link below:-

Google - Security Bug Report
Edit description

www.google.com

Summary:-

Password Reset Link Leaked In Refer Header In Request To Third Party Sites

Steps To Reproduce:
Step 1 — Go To https://www.waze.com/forgot_password?redirect=%2F&we_episode_id=1618203286605
Step 2 — Enter Your Email And Click On send an email.
Step 3 — Go To Email & Click on Password Reset Link
Step 4 — On Password Reset Page Click On Social Media Links Given Below And Capture The Request Using Burp Suite
Step 5 — You May Observe Full Password Reset Link Is Exposed To Third Party Sites.

Impact:-

Social Media Page Can Also Exploit like if they have enabled page analytics then they may see from where users are referring onto their page and from there they see that password reset link and can reset the password for the victim.

Get Akash basnet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Google triaged my report after 12 days of initial report & finally rewarded me with Bounty $$$ also enlisted in Google Hall of Fame. That’s how I made it into the google hall of fame.

Press enter or click to view image in full size
Reward email from google.
Press enter or click to view image in full size
Enlisted in Google hall of fame
Bughunter
Edit description

bughunter.withgoogle.com

Timeline of the report:-

April 12, 2020: Initial report sent

April 12, 2020: Report Triaged

April 23, 2020: Bounty Rewarded $$$

May 21, 2020: Confirmation of fix

Proof of concept video file in a link below:-

https://www.youtube.com/watch?v=I311-Os8eDs

Thank you for taking the time to read my article, Have a nice day!

you can follow me on Facebook

Log In or Sign Up to View
See posts, photos and more on Facebook.

www.facebook.com

Below is the coverage of this issue.

नेपालका आकाशजङ्ग बस्नेतले पत्ता लगाए गुगलको सुरक्षा कमजोरी
काठमाडौं । २४ वर्षीय नेपाली युवा आकाशजङ्ग बस्नेतले गुगलको सुरक्षा कमजोरी पत्ता लगाएका छन् । गुगलको एक्युजिसन साइटमा…

www.techpana.com
