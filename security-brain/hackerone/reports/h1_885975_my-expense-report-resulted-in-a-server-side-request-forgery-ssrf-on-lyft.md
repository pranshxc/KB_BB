---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '885975'
original_report_id: '885975'
title: My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft
team_handle: lyft
created_at: '2018-11-29T17:16:01.000Z'
disclosed_at: '2020-05-29T17:04:07.740Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 648
tags:
- hackerone
---

# My Expense Report resulted in a Server-Side Request Forgery (SSRF) on Lyft

## Metadata

- HackerOne Report ID: 885975
- Weakness: 
- Program: lyft
- Disclosed At: 2020-05-29T17:04:07.740Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

During a trip to a conference, I discovered that the **Lyft **app allowed users to create expense reports by exporting business ride history as a PDF or CSV file. Being an active Lyft user, this was excellent news to me since it made my life easier by simplifying the tedious process of work travel expenses. But it also begged the question: “Can I hack this thing?” Turned out, the answer is **yes, thanks to my collaboration with Cody Brocious (@Daeken)**


# How Does It Work?

Once you complete a ride and rate or tip your driver, you are prompted with the following image that allows you to attach an expense code and note to it. Naturally, as I ended my ride at the airport, I placed an HTML tag for my expense info which allowed me access to an entirely new interface under the “Ride History” tab on the Lyft app. It showed me a section where it allowed me to select which rides I wanted to export into my expense repor.Once I selected my rides for my expenses, the Lyft application sent out an email where I received my expenses in two formats: CVS and PDF. And by opening the PDF I was able to confirm that the html tag (<h1>test) placed inside the “Expense Notes” was successfully rendered within the PDF:

{F847937}

This immediately caught my attention. I wanted to see if I would be able to exploit the PDF generator with SSRF being the possible outcome.


## Exploring SSRF

Once we confirmed that we could insert HTML into the PDF generator, the next step was to see if we could actually get the app to fetch external resources to gather information (such as user-agent), which would help us understand the application better. Keep in mind that this also required us to take a Lyft each time we wanted to try our payloads. We dedicated a few rides to getting the user agent by forcing the PDF generator to fetch a remote file from a web server controlled by us, using tags like `<iframe>` and `<img>`. But, unfortunately, we weren’t able to get any of that information at the time.

A few weeks later, HackerOne was hosting a Live Hacking Event in New York, which allowed us to take a ton of rides using the Lyft app and it was a great opportunity to revisit this bug. Our focus this time was to understand why some tags like <h1> or <u> were working in comparison to <img> or <iframe>. As mentioned earlier, the email also contains a CSV file exposing the exact string set as the expense code without rendering it. "Seeing this showed us our phone typo entering the payload, ‘left/right double quotation mark’ “ vs a regular quotation mark ". Once we fixed this in our original payload, we took a ride, where we were able to get the PDF generator’s User-Agent, which shifted our focus from Lyft’s application to WeasyPrint instead.

{F847939}

# WeasyPrint

[WeasyPrint](https://weasyprint.org/) is a smart solution helping web developers create PDF documents. It turns simple HTML pages into gorgeous invoices, tickets, statistical reports… and it turns out it is also open sourced. Using WeasyPrint, you are able to create PDF files by feeding it an html template or URL. I have created a video on how to exploit WeasyPrint on YouTube,  you should definitely check it out!

Here’s how WeasyPrint works, it takes an html template and creates a pdf from it. You can do this locally with the following command:

`$> weasyprint input.html output.pdf`

After installing an instance of it locally, we were able to understand how it all worked. This made our testing a lot easier since we no longer needed to take rides in order to test our payloads.

After a few attempts without reviewing the source, we had an initial understanding of how WeasyPrint worked: 

*   It allows a small number of HTML tags 
*   No Javascript or event handlers were allowed
*   No iframe or similar tags were allowed either

After we reviewed a few files and discovered some interesting things in [html.py](https://github.com/Kozea/WeasyPrint/blob/b7a9fe7dcc9d0755a3324b74d0965e806bb87378/weasyprint/html.py), WeasyPrint had redefined a set of html tags including img, embed, object, and more. Based on our previous tests, we already knew that javascript was not an option in order to exploit this. At this point, our hopes were low and we started to think that the PDF generator was no longer exploitable until we discovered references to &lt;link> inside of several files including [pdf.py](https://github.com/Kozea/WeasyPrint/blob/b7a9fe7dcc9d0755a3324b74d0965e806bb87378/weasyprint/pdf.py). This allowed us to attach the content of any webpage or local file to our PDF by using “&lt;link rel=attachment href="file:///root/secret.txt">”. 

Using zlib and python, we created a script that helped us unpack the content of local files from our pdf.


```
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
```

# One Last Ride

This gave us a working POC on our localhost, so we took one last ride using the Lyft app to test our payload and we were able to confirm the existence of this bug. 

{F847938}

# Credits

A big thank you to the Lyft team, especially Vinay, for answering all of our questions and working closely with us to get this issue fixed. 

Thank you to Daeken for his brilliant ideas and being a great resource throughout this process.

And thank you to @d0nutptr for helping validate this vulnerability by taking a few rides for me while I was on an airplane.

If you want to hear more about the fun we had while exploiting this issue, check out my video on YouTube: [Exploiting a Server Side Request Forgery (SSRF) in WeasyPrint for Bug Bounty & HackerOne’s $50M CTF](https://www.youtube.com/watch?v=t5fB6OZsR6c) 

# Timeline

10.11.2018 - Initial finding by nahamsec

11.29.2018 - Working POC in NYC

11.29.2018 - Initial report to Lyft

11.29.2018 - Patch released by Lyft

11.30.2018 - Lyft notified us that the vulnerability was patched

12.05.2018 - Lyft awarded us with a max bounty on their program

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
