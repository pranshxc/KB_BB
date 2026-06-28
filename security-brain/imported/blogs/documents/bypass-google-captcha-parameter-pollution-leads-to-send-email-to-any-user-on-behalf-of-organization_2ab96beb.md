---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-14_bypass-google-captchaparameter-pollution-leads-to-send-email-to-any-user-on-beha.md
original_filename: 2021-08-14_bypass-google-captchaparameter-pollution-leads-to-send-email-to-any-user-on-beha.md
title: Bypass Google Captcha+Parameter Pollution Leads to send email to any user on
  behalf of “Organization” with any desired content
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 2ab96beb3c1baa09f3d24e2add7b276c07eeeaea954dca8d3d3ee809faa918cd
text_sha256: c98996a363bdce437aadf910eeb9570f9881db4465d58e2e42c2a21c98eb59b3
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Google Captcha+Parameter Pollution Leads to send email to any user on behalf of “Organization” with any desired content

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-14_bypass-google-captchaparameter-pollution-leads-to-send-email-to-any-user-on-beha.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `2ab96beb3c1baa09f3d24e2add7b276c07eeeaea954dca8d3d3ee809faa918cd`
- Text SHA256: `c98996a363bdce437aadf910eeb9570f9881db4465d58e2e42c2a21c98eb59b3`


## Content

---
title: "Bypass Google Captcha+Parameter Pollution Leads to send email to any user on behalf of “Organization” with any desired content"
url: "https://medium.com/@viralbhatt100/bypass-google-captcha-parameter-pollution-leads-to-send-email-to-any-user-on-behalf-of-9013aebbabae"
authors: ["viral bhatt (@viralbhatt100)"]
bugs: ["HTTP parameter pollution", "Captcha bypass"]
publication_date: "2021-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3421
scraped_via: "browseros"
---

# Bypass Google Captcha+Parameter Pollution Leads to send email to any user on behalf of “Organization” with any desired content

Bypass Google Captcha+Parameter Pollution Leads to send email to any user on behalf of “Organization” with any desired content
viral bhatt
Follow
3 min read
·
Aug 14, 2021

179

3

Hi folks, I am Viral Bhatt. This is my first write-up so there might be possibilities of numerous mistakes but yeah it’s okay to make mistakes.. as long as you learn from them.

I only prefer hacker-one for bug bounty, may be because my eyes loves the UI of h1. After spending a lot of time in a public program ( where I didn’t have any proper methodology, I used to blindly select the target and start my work) I was invited in a private program. My friend 
Vitthal shinde
 suggested me to do the testing as we do in our daily routine life. A proper pen-testing of each and every URL with fuzzing. I did the same and landed up in top 1 in the hacker-one leader-board next to a few well known hackers :) (Current ranking is 3rd with 296* point)

Press enter or click to view image in full size

let’s get back to the write-up.

In the particular application I’ve submitted 16 vulnerabilities where 11 are the XSS(Not the basic one, need to bypass the WAF). So the program had to add this line there.

Press enter or click to view image in full size

But yeah who cares. Again I stated the testing and observed the “contact us” page where I was able to send the email to the company.

Steps to Reproduce :-

Get viral bhatt’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

STEP 1. I navigated to the contact page and filled the details.

Press enter or click to view image in full size

STEP 2. First approach here is to bypass the google captcha. As you can see after sending the same request again I’m getting an error “INVALID_CAPTCHA”.

Press enter or click to view image in full size

STEP 3. As you can see I’ve removed the “recaptcha” parameter and its value. Observe that without the captcha server giving me “SUCCESS:true” response.

Press enter or click to view image in full size

STEP 5. After completing the google captcha bypass I’ve added one more parameter “toEmail” with my email address. And I got the response “SUCCESS:true”.

Press enter or click to view image in full size

STEP 6. I opened my email and I received the email on behalf of the “Target_Company”. I was able to do email to any user with “Target_Company” email address.

Press enter or click to view image in full size

I’ve submitted the vulnerability to the private program and within a day they’ve patched the vulnerability with good bounty.

I hope you enjoyed reading the article as much as I enjoyed writing it.

Special thanks to 
Vitthal shinde
 (Twitter :- 0_1vitthals)
