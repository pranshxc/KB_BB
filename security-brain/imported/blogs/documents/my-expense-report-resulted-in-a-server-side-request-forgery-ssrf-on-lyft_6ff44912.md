---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-29_my-expense-report-resulted-in-a-server-side-request-forgery-ssrf-on-lyft.md
original_filename: 2020-05-29_my-expense-report-resulted-in-a-server-side-request-forgery-ssrf-on-lyft.md
title: My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
language: en
raw_sha256: 6ff44912da2c73ba8a0be7d57a39daa2c79a613549c8bf882969cbcf908ca8d0
text_sha256: 2ed56ac71adb629b80efce8956f51ed91bf5372156b6176f72ced7d30a2e2c54
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-29_my-expense-report-resulted-in-a-server-side-request-forgery-ssrf-on-lyft.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `6ff44912da2c73ba8a0be7d57a39daa2c79a613549c8bf882969cbcf908ca8d0`
- Text SHA256: `2ed56ac71adb629b80efce8956f51ed91bf5372156b6176f72ced7d30a2e2c54`


## Content

---
title: "My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft"
page_title: "My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft — NahamSec"
url: "https://www.nahamsec.com/posts/my-expense-report-resulted-in-a-server-side-request-forgery-ssrf-on-lyft"
final_url: "https://www.nahamsec.com/posts/my-expense-report-resulted-in-a-server-side-request-forgery-ssrf-on-lyft"
authors: ["Ben Sadeghipour (@nahamsec)", "Serafina (Sera) Tonin Brocious (@daeken)"]
programs: ["Lyft"]
bugs: ["SSRF"]
publication_date: "2020-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4549
---

# My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft

May 29

Written By [Ben Sadeghipour](/posts?author=5d543d375042ad0001fc1bc2)

## Introduction

During a trip to a conference, I discovered that the **Lyft** app allowed users to create expense reports by exporting business ride history as a PDF or CSV file. Being an active Lyft user, this was excellent news to me since it made my life easier by simplifying the tedious process of work travel expenses. But it also begged the question: “Can I hack this thing?” Turned out, the answer is **yes, thanks to my collaboration with Cody Brocious (@**[**Daeken**](https://twitter.com/daeken)**)**

## How Does It Work?

Once you complete a ride and rate or tip your driver, you are prompted with the following image that allows you to attach an expense code and note to it. Naturally, as I ended my ride at the airport, I placed an HTML tag for my expense info which allowed me access to an entirely new interface under the “Ride History” tab on the Lyft app. It showed me a section where it allowed me to select which rides I wanted to export into my expense repor.Once I selected my rides for my expenses, the Lyft application sent out an email where I received my expenses in two formats: CVS and PDF. And by opening the PDF I was able to confirm that the html tag (<h1>test) placed inside the “Expense Notes” was successfully rendered within the PDF:

![](https://images.squarespace-cdn.com/content/v1/5d5441803b4c5600017dae9c/1590731980328-Q8I4BC0203X3PT5XBVTN/lyft3.png)

This immediately caught my attention. I wanted to see if I would be able to exploit the PDF generator with SSRF being the possible outcome. 

## Exploring SSRF

Once we confirmed that we could insert HTML into the PDF generator, the next step was to see if we could actually get the app to fetch external resources to gather information (such as user-agent), which would help us understand the application better. Keep in mind that this also required us to take a Lyft each time we wanted to try our payloads. We dedicated a few rides to getting the user agent by forcing the PDF generator to fetch a remote file from a web server controlled by us, using tags like <iframe> and <img>. But, unfortunately, we weren’t able to get any of that information at the time.

A few weeks later, HackerOne was hosting a [Live Hacking Event](https://www.hackerone.com/blog/live-hacking-events-stats-invitations-and-whats-next) in New York, which allowed us to take a ton of rides using the Lyft app and it was a great opportunity to revisit this bug. Our focus this time was to understand why some tags like `<h1> or <u>` were working in comparison to `<img>` or `<iframe>`. As mentioned earlier, the email also contains a CSV file exposing the exact string set as the expense code without rendering it. "Seeing this showed us our phone typo entering the payload, ‘left/right double quotation mark’ `“` vs a regular quotation mark `**".**`Once we fixed this in our original payload, we took a ride, where we were able to get the PDF generator’s User-Agent, which shifted our focus from Lyft’s application to WeasyPrint instead.

![](https://images.squarespace-cdn.com/content/v1/5d5441803b4c5600017dae9c/1590732262098-BFGIGSKS5WD6JH9LW1QN/lyft4.png)

## WeasyPrint 

[WeasyPrint](https://weasyprint.org/) is a smart solution helping web developers create PDF documents. It turns simple HTML pages into gorgeous invoices, tickets, statistical reports… and it turns out it is also open sourced. Using WeasyPrint, you are able to create PDF files by feeding it an html template or URL. I have created a video on how to exploit WeasyPrint on YouTube, you should definitely check it out!

Here’s how WeasyPrint works, it takes an html template and creates a pdf from it. You can do this locally with the following command:

`$> weasyprint input.html output.pdf`

After installing an instance of it locally, we were able to understand how it all worked. This made our testing a lot easier since we no longer needed to take rides in order to test our payloads. After a few attempts without reviewing the source, we had an initial understanding of how WeasyPrint worked: 

  * It allows a small number of HTML tags 

  * No Javascript was allowed

  * No iframe or similar tags were allowed 

After we reviewed a few files and discovered some interesting things in [html.py](https://github.com/Kozea/WeasyPrint/blob/b7a9fe7dcc9d0755a3324b74d0965e806bb87378/weasyprint/html.py), WeasyPrint had redefined a set of html tags including img, embed, object, and more. Based on our previous tests, we already knew that javascript was not an option in order to exploit this. At this point, our hopes were low and we started to think that the PDF generator was no longer exploitable until we discovered references to <link> inside of several files including [pdf.py](https://github.com/Kozea/WeasyPrint/blob/b7a9fe7dcc9d0755a3324b74d0965e806bb87378/weasyprint/pdf.py). This allowed us to attach the content of any webpage or local file to our PDF by using `<link rel=attachment href="file:///root/secret.txt">`. 

Using zlib and python, we created a script that helped us unpack the content of local files from our pdf.
  
  
  import sys, zlib
  
  def main(fn):
  data = open(fn, 'rb').read()
  i = 0
  first = True
  last = None
  while True:
  i = data.find(b'>>\nstream\n', i)
  if i == -1:
  break
  i += 10
  try:
  last = cdata = zlib.decompress(data[i:])
  if first:
  first = False
  else:
  pass#print cdata
  except:
  pass
  print(last.decode('utf-8'))
  
  if __name__=='__main__':
  main(*sys.argv[1:])
  

## One Last Ride

This gave us a working POC on our localhost, so we took one last ride using the Lyft app to test our payload and we were able to confirm the existence of this bug. 

![](https://images.squarespace-cdn.com/content/v1/5d5441803b4c5600017dae9c/1590732453577-GHK1PTNG70U744BRM49V/lyft5.jpg)

## Credits

A big thank you to the Lyft team, especially [Vinay](https://www.linkedin.com/in/vinayendra/), for answering all of our questions and working closely with us to get this issue fixed. 

Thank you to Daeken for his brilliant ideas and being a great resource throughout this process.

Thank you to @d0nutptr for helping validate this vulnerability by taking a few rides for me while I was on an airplane.

If you want to hear more about the fun we had while exploiting this issue, check out my video on YouTube: [Exploiting a Server Side Request Forgery (SSRF) in WeasyPrint for Bug Bounty & HackerOne’s $50M CTF](https://www.youtube.com/watch?v=t5fB6OZsR6c)

## Timeline

10.11.2018 - Initial finding by NahamSec

11.29.2018 - Working POC in NYC with @Daeken

11.29.2018 - Initial report to Lyft

11.29.2018 - Patch released by Lyft

11.30.2018 - Lyft notified us that the vulnerability was patched

12.05.2018 - Lyft awarded us with a max bounty on their program

[ Ben Sadeghipour ](/posts?author=5d543d375042ad0001fc1bc2)
