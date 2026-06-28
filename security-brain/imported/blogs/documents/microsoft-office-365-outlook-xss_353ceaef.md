---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-19_microsoft-office-365-outlook-xss.md
original_filename: 2019-07-19_microsoft-office-365-outlook-xss.md
title: Microsoft Office 365 - Outlook XSS
category: documents
detected_topics:
- sso
- jwt
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- sso
- jwt
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 353ceaef3b831e8556ddd6a2a64c49408379f22a986c9ee2b72a122fa5933117
text_sha256: 32f41fa3a6fbe55e2f4f3682486374c9a67813a22449ebdea84d5896fb90a7bc
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Office 365 - Outlook XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-19_microsoft-office-365-outlook-xss.md
- Source Type: markdown
- Detected Topics: sso, jwt, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `353ceaef3b831e8556ddd6a2a64c49408379f22a986c9ee2b72a122fa5933117`
- Text SHA256: `32f41fa3a6fbe55e2f4f3682486374c9a67813a22449ebdea84d5896fb90a7bc`


## Content

---
title: "Microsoft Office 365 - Outlook XSS"
url: "https://leucosite.com/Microsoft-Office-365-Outlook-XSS/"
final_url: "https://leucosite.com/Microsoft-Office-365-Outlook-XSS/"
authors: ["Abdulrahman Alqabandi (@Qab)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2019-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5136
---

![](../q.png)

[Home](../) [About](../About) [Tools](../Tools) [Links](../Links) [Twitter](https://www.twitter.com/qab) [Stuff](../Stuff)

# Microsoft Office 365 - Outlook XSS

  

Outlook was the first website I have found and participated in a bug bounty for back in 2015. I ended up finding several bugs which I have showcased [here](/Various-bugs-in-Microsoft-Office-365-Outlook/) (updated videos.)

  

So I thought it would be nice to revisit Outlook and see what I can find and possibly see a pattern in how bugs evolve over time. I was able to find a few bugs of which two I will be writing about here. These two bugs are XSS bugs which are a little more complex than the 2015 bugs I found.

## Outlook XSS using SVG emoji

It's been a while since I delve into Outlook, so I went to basics and just started to look for different use cases and on the way check for common bugs. One such use cases is pretty common in mail providers - Setting email signature. I simple created a signature and by mere chance had put an emoji within it, just to see how signatures are handled.

  

I noticed that after setting a signature, every new email you create will have that signatures valid html added on the end of your emails body. One thing stood out when looking at this HTML code, I noticed the emoji I chose was added in a peculiar way.

  

  
  
  <img class="EmojiInsert" src="data:image/gif;base64,{BASE64 emoji}" />
  

  
I was expecting to see the unicode based emoji, but instead I am seeing this tag in the mail body before being sent. After sending it, the reciever would get the emoji except it would have been uploaded to Outlooks attachment service. The HTML ends up turning into:

  

  
  
  <img originalsrc="cid:5q3e7cdf-c63f-4f7b-8975-cq66e59d5639"
  size="2128" 
  contenttype="image/jpeg" id="img710290" crossorigin="use-credentials" 
  src="https://attachments.office.net/owa/alqabandi@test/service.svc/s/GetFileAttachment?id={ID}&X-OWA-CANARY={TOKEN}" tabindex="0" style="max-width: 99.9%; user-select: none;">
  

  

So what's happening is that the base64 data in the draft email is being used to create an attachment on Outlooks servers. The first test is to open the `'``src'` of the image and see if the image is downloaded or served inline and rendered in the browser. It does!

  

So the obvious test here is to manipulate `'``EmojiInsert'` to contain a base64 encoded SVG image that contains our JS. Which I did and it worked! SVG was created as an attachment and renders in the browser. However, the was a small issue. `'``attachments.office.net'` was the domain my JS loaded SVG file was being hosted on, and this domain is NOT part of Microsofts bug bounty. 

  

I thought it was a smart move to host all attachments in a cross-origin subdomain, this will benefit everyone. But I did not give up here, one idea came to mind after looking at the resulting `'``src'` URL. I noticed that two parameters are sent, `'``id'` and `'``X-OWA-CANARY'`.

  

You see, for some reason normal attachments in emails (the ones that usually are not images and have no preview within emails body) are still hosted on the main `'``outlook.office.com'` domain. They also take the same two parameters, so immediately I tried to use the `'``id'` and `''''X-OWA-CANARY`'` from `'attachments.office.net' `and to `''''outlook.office.com`'` and it worked, the SVG still displayed inline but this time in a bounty worthy domain scope.

  

Here is the full PoC as well as a video. 

  

  
  
  <?xml version="1.0" standalone="no"?>
  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
  "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
  <svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="50pt" height="53pt" viewBox="0 0 50 53" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
  <filter id="image">
  <feImage xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD4AAAA4CAIAAAAq+twOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQESURBVGhD7ZfbTiJBEIZ9Lh6It9jNekJFhQHPnByQ9W5veZG9WWPceGNWwMTEZDkIq/t3V/VM98wQ6dagBv780Z4+1HwUxXTP0vOn1fyhf5dqNptnUo1Go15v+PW67/unUrVarVqtVarVcqVSKpeFS+WTk9JZs9npdDjK6zSX6P9iGuse6xZ6eno6Pz+/vr6uNxpvQu+IjnyDdTQaPZIfyY/DwEPxdzAkD2HQA/3h4eHq6vep77c7HZjDOckRHUUSR1fcaIwmod/f39/d3f26uKjWTuF2u80R7eWIjuIGOnNH0AEtrbgN9G63C9ybm5ufUpVKlSPayxEdP0qg/7ARoe+Y8opFjmgvR3Q8TETWucTNaqGsU7UMkG/OOtq37fafW/Jtt3sHe4UCR7TXHKL7PqErYpNb4AaW3BK9H7g/GI3GcN6bOTo2HTy8uYqdROi5vMcR7eWIjs0S6Pwc1JLNdcLJVilH2egpHwx6Kuu7uTxHtJcjOjZ5bJMhsQY9lAo/gOTW0AeolgB9J5fjiPZyRMfh5E0KZnt3lyPaa/7QcR5EwaiqkKbCoCJJLvGwWoKC2d6ZOToOsdgdw1IOP8NU3AF6dnuHI9rLFb0E9FcWjNBWdpsj2ssRHS8NnHUzzbFMwyLZer7JdG7bzGY5or0c0Y9PTgS6wp0ADSdAC/f6hL6xtUCfXkfHx6PxmMvWSYSe2dziiPZyRD88OgJ6LMfkwaT6Fu71/0oz+sYmR7SXI/rBYQRd4iriZGhYcQfo65kNjmgvV/SDQzyV+bt3EqGvZTIc0V6O6PsHB0CPJjXRWqZ1E/rq+szR9/b3X0aP4eom9JW1dY5or/lDL+4JdC5bJxH68uoaR7SXI3qhuIcTSK/fR2rJkaS+aEZfWeWI9nJE94pF3DhCY2VC//YO6IUC3fuV/rq8whHt5Yie9wp4mcdLMV4uYbzs4KUBh28cYnEYhHE4wSaPzRKbDh7eMJ6D+FGiuFEkSDag4S/fljmiveYP/SNogf4eWqC/hxbo7yFCb6WXltIt2XwDvW20ifpoWcfHTnmXfBGTMfrp0YMu2Wh5qSWh4Es3VmgXaLKM20Wnm1MuObq5RigYgdItcaWvSaX0UXTG0VVM0VTwaGtNGtdD63O1Kfqcy1bLjIoxtVxTuJZWi7nqvzmamHUei7SDxQlRtH5qx6OR9J5EdnOJnOIl5E1oSnRxIdbzv7BDKXFhZA6EHl1hfCU9jpBYEMYwRqdFF1ey/lQcc5SGw3Y8GineE5E5QWQ9nVblEhmdGl1eIpCegWBctJNyo/XHaj1UON9sqxoPK0sftUAX15G7ih5SdGJwLW5PUkvDRWqWcSNekG7ptwvawSjahP4ptUCfvZ6f/wMV2V3jXyWFvwAAAABJRU5ErkJggg=="/>
  </filter>
  </defs>
  <rect x="10%" y="10%" width="80%" height="80%"
  style="filter:url(#image);"/>
  <script type="text/javascript">
  //<![CDATA[
  if(location.hostname=="attachment.outlook.office.net"){
  var qsplit=location.search.split("&");
  location='https://outlook.office.com/owa/service.svc/s/GetFileAttachment'+qsplit[0]+'&'+qsplit[1];
  }else{
  alert('XSS by @qab, location.hostname='+location.hostname);
  }
  //]]>
  </script>
  </svg>
  

  
<https://www.youtube.com/watch?v=VE8WqprZVh4>

  

## Outlook XSS using vCalendar

Outlook comes with an integrated calendar, this is useful as it can be used to mark dates and create meetings. Once someone creates a calendar item for a specific day they can then forward it to a victim and through it create a meeting with that person. Going through the use cases I stumbled on an import function for calendars and this caught my eye.

  

The calendar import tool asked for a `'``.ICS'` file, which is a vCalendar format plain text file which looks like HTTP response and request headers with values.  

  

![](./calendar.png)

  

So I started to create my own vCalendars and importing them hoping to catch a mistake, but I could'nt at first. I went through all the possible keys and values and did not find much. I thought that since there is an import function there should be a way to export.

  

I had to see how Microsoft would generate its own vCalendars where I may find something I can use to my advantage. So I exported a forwarded calendar event/meeting. See, when you forward a calendar item to someone, what's happening is that an email is sent with a file attachment but that file attachment is marked as a calendar item (because its an .EML file) thus is displayed differently.  

  

Within this attached EML file I found our generated vCalendar data. Decoding it from base64 revealed the information I needed. Microsoft generated vCalendars contain certain non-standard values and keys, these started with `'``X-'` which makes it obvious. Before I go into what I found, I'd like to mention Outlook meetings.

  

Outlook meetings is essentially a forwarded calendar event, within this meeting/event one can set up an online meeting. Once a user marks it as an online meeting, Microsoft creates a Lync URL and then attaches it on the meeting so that both parties can access the same link from each side.

  

![](./xsscal.png)

  

So what I found when I looked at the custom vCalendar entries was the value of the generated Lync URL. So all I did was replace the HTTPs URL to a JAVASCRIPT one and I was able to get an XSS. All a user would need to do is accept a meeting with me then click on the`'``Join online meeting'` button and I would have JS executed.  
  
![](./xss2.png)  

  

Video of it in action.  
<https://www.youtube.com/watch?v=L_XdplWMpgA>

  

### Conclusion

It was nice to see the evolution of these types of bugs from ~4 years ago. This is either a good sign that Microsoft is headed in the right direction or my skills and patience has improved over the years. It was definitely fun to look at Office 365 again, though I don't think I am done yet as I feel I barely scratched the surface.  

  

Hit me up @qab if you have any questions.
