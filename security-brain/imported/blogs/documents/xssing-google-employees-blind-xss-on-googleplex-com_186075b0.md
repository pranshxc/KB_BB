---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-15_xssing-google-employees-blind-xss-on-googleplexcom.md
original_filename: 2019-06-15_xssing-google-employees-blind-xss-on-googleplexcom.md
title: XSSing Google Employees — Blind XSS on googleplex.com
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
raw_sha256: 186075b0f8a418c1586cf0c231b1c648293e7b5ab0efb20f51182929c7c0e9c9
text_sha256: 911ef3132c375cfff3077642e4fa7ce1dae8154f62439409e50cc90a4c3be819
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# XSSing Google Employees — Blind XSS on googleplex.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-15_xssing-google-employees-blind-xss-on-googleplexcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `186075b0f8a418c1586cf0c231b1c648293e7b5ab0efb20f51182929c7c0e9c9`
- Text SHA256: `911ef3132c375cfff3077642e4fa7ce1dae8154f62439409e50cc90a4c3be819`


## Content

---
title: "XSSing Google Employees — Blind XSS on googleplex.com"
page_title: "XSSing Google employees: blind XSS on googleplex.com - Web Security Blog"
url: "https://websecblog.com/vulns/googleplex-com-blind-xss/"
final_url: "https://websecblog.com/vulns/googleplex-com-blind-xss/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["Blind XSS"]
publication_date: "2019-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5215
---

# XSSing Google employees: blind XSS on googleplex.com

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[June 12, 2019June 11, 2026](https://websecblog.com/vulns/googleplex-com-blind-xss/)

Google is an enormous company and it’s dependent on thousands of suppliers to keep it running.  
And since it needs some way to keep track and pay their suppliers, it offers a public online tool where suppliers upload their invoices to Google.

It is called **Google Invoice Submission Portal** and can be found on [gist-uploadmyinvoice.appspot.com](https://gist-uploadmyinvoice.appspot.com).

![](https://websecblog.com/wp-content/uploads/image-1-1024x646.png)Google Invoice Submission Portal

The first thing you’ve probably noticed is that the website is hosted on the **appspot.com** domain, which is publicly available for hosting Google App Engine projects.

Google often uses it for building some of their websites, where in the end the production version is transferred over to _google.com_ or some other domain.

In this case, they likely forgot to publish the _Invoice Upload_ site hosted on _appspot.com_ to _google.com_.

## Uploading invoices

The first thing it asks us to enter is a _Purchase Order Number_. It doesn’t really matter what we enter, just type a random number and click on the _Search_ button.

Then it wants to select an organization related to the invoice. This determines what country will the invoice be processed in. Again, just select some option and click on _Submit_.

Now we can see a form with multiple inputs, namely for _email_ , _invoice number_ , _invoice date,_ and a file select button for uploading the actual invoice in a PDF format.

![](https://websecblog.com/wp-content/uploads/image-2-737x1024.png)

## Finding the vulnerabilities

I tried filling these text fields with various XSS payloads hoping that somewhere in their invoices dashboard they haven’t correctly escaped the inputs which would trigger a blind XSS that would send me a notification. But this wasn’t the case. I haven’t received anything so the text fields were most likely handled correctly.

Apart from text input, there’s also the input for selecting a PDF file. But it’s configured so that **only PDF files** can be selected to upload.

![](https://websecblog.com/wp-content/uploads/image-5.png)

Since this is just a front-end validation, it doesn’t stop us from changing the file type when sending the upload _POST_ request.

Once we select any PDF file, an upload request is fired. We can intercept the request using a _web proxy debugger_ and **change** the filename and the contents from `.pdf` to `.html`.

![](https://websecblog.com/wp-content/uploads/google_invoices_vuln_upload_pdf.png)POST request for uploading the PDF file

First, we change the _filename_ property to `test.html`, the _Content-Type_ to `text/html` and the body to an XSS payload.

In the payload, I’ll use a `<script>` tag with `src` pointing to an endpoint on my domain that sends me an email every time it’s loaded. I’m using [ezXSS](https://github.com/ssl/ezXSS) for logging these blind XSS requests.

![](https://websecblog.com/wp-content/uploads/google_invoices_vuln_attachement.png)

Now the HTML file has been attached to the form and we can click on the _Submit Invoices_ button to send the form.

## Executing the blind XSS

Some days later I’ve received a notification that a blind XSS has been executed on the _googleplex.com_ domain.

Google uses _googleplex.com_ for hosting some internal tools. If you try to go to the domain, you’ll be redirected to a Google Corp login page (also know as MOMA login page) – which requires a valid google.com account. That means it’s accessible only by Google employees or partners.

![](https://websecblog.com/wp-content/uploads/google_invoices_xss_report.png)_googleplex.com_ blind XSS details

The DOM of the page matches the XSS payload that was put in place of the PDF file. We can see that this URL is used for displaying a PDF file. But since the `_Content-Type_` of the uploaded file was changed from `application/pdf` to `text/html`, it displayed and rendered the XSS payload instead of the PDF.

### Impact

Executing a custom JavaScript code on this _googleplex.com_ subdomain allows the attacker to gain access to Google’s invoices and other sensitive information.

~~Since the Google Employee is logged in using their company account, it should be possible to access other internal sites on their behalf as well.~~

**Update** : The previous paragraph is incorrect. I’ve received more information from Google’s Security Team:

> Access to a single googleplex.com app does not give you access to any other  
> googleplex.com apps, they are all independent from each other and isolated  
> and the credentials and cookies can’t be stolen or used against other sites.

This means the attacker could still access the subdomain where invoices are handled, but access to other apps on googleplex.com wasn’t possible.

### Fixing the vulnerability

I’ve sent details about this vulnerability to Google as soon as possible. After adding some additional information, four days later I’ve received an update that the report has been accepted.

![](https://websecblog.com/wp-content/uploads/google_invoices_response.png)

After about a month later I’ve been able to confirm that it has been fixed.

Although after it’s been fixed an XSS was still fired, it wasn’t on _googleplex.com_ , but on _storage.googleapis.com_ — which acts as a sandbox domain and is as well used (also like g _oogleusercontent.com_) for storing uploaded user content.

The XSS is now on a sandboxed domain where the XSS poses no risk for the user/employee.

* * *

Timeline|  
---|---  
2019-02-21| Vulnerability reported  
2019-02-22| Priority changed to P2  
2019-02-22| Added more information  
2019-02-25| Accepted and priority changed to P1  
2019-03-06| Reward issued  
2019-03-26| A fix has been implemented  
2019-04-11| Issue marked as fixed  
  
Written by [Thomas Orlita](https://thomasorlita.com/)
