---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-25_missing-authorization-check-while-deleting-app-review-for-marketing-api.md
original_filename: 2019-04-25_missing-authorization-check-while-deleting-app-review-for-marketing-api.md
title: Missing Authorization check while deleting App Review for Marketing API
category: documents
detected_topics:
- access-control
- sso
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- sso
- command-injection
- api-security
language: en
raw_sha256: 46fdb6b259f671c9a1d2d65a599e1b8d1c7a8b7ac3745d8746fafe5b0d99558c
text_sha256: 741b007bb6078f5b3cb18732a594d923e7f57d44d1b4e357196efdd25fa0ec37
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Missing Authorization check while deleting App Review for Marketing API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-25_missing-authorization-check-while-deleting-app-review-for-marketing-api.md
- Source Type: markdown
- Detected Topics: access-control, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `46fdb6b259f671c9a1d2d65a599e1b8d1c7a8b7ac3745d8746fafe5b0d99558c`
- Text SHA256: `741b007bb6078f5b3cb18732a594d923e7f57d44d1b4e357196efdd25fa0ec37`


## Content

---
title: "Missing Authorization check while deleting App Review for Marketing API"
page_title: "Missing Authorization check while deleting App Review for Marketing API: Facebook Whitehat"
url: "https://whitehatfamilyguy.blogspot.com/2019/04/missing-authorization-check-while.html"
final_url: "https://whitehatfamilyguy.blogspot.com/2019/04/missing-authorization-check-while.html"
authors: ["Family guy"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5287
---

###  Missing Authorization check while deleting App Review for Marketing API: Facebook Whitehat 

[ April 25, 2015  ](https://whitehatfamilyguy.blogspot.com/2019/04/missing-authorization-check-while.html "permanent link")

##  Missing Authorization check while deleting App Review for Marketing API

Peter, was enjoying the weekend, and he heard Lois screaming.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLyjgGyUCL5jwJm9y6MQ1l7LGMnEPqT4zWfaXMslLwdRXb_qrxgdIZiacGQPBkAqL0nyYaC-s1tMz0mQ9ameWasn7WGf19GnWTnteXTk5jkZLgH_pyknFVCqmtZjpv9yWanhaiZH_D-x4/s400/peter-griffin-bored.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLyjgGyUCL5jwJm9y6MQ1l7LGMnEPqT4zWfaXMslLwdRXb_qrxgdIZiacGQPBkAqL0nyYaC-s1tMz0mQ9ameWasn7WGf19GnWTnteXTk5jkZLgH_pyknFVCqmtZjpv9yWanhaiZH_D-x4/s1600/peter-griffin-bored.gif)

Hey, Peter, when are we getting new Television:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqhLytLWgUhbuHsJGSxX80fF_bR4sjQ4VQbijhKN-_pK9CjtNeth8jeor7SUW314VSlhFnmq4QqiVL8TypkC7h83uBJC3kCnA-9rZjlBZMUjWffG8JzVqTaCZ7JxVn0XlPphlDP4v2UsQ/s400/giphy+%25284%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqhLytLWgUhbuHsJGSxX80fF_bR4sjQ4VQbijhKN-_pK9CjtNeth8jeor7SUW314VSlhFnmq4QqiVL8TypkC7h83uBJC3kCnA-9rZjlBZMUjWffG8JzVqTaCZ7JxVn0XlPphlDP4v2UsQ/s1600/giphy+%25284%2529.gif)

Well, huh!!! Alright…  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_u6mAcnk4MCqU0UpkB1nDQJxT2WyvoD9n8aARPsR-9bV3Ej4hCUXcHlmWFr9lRegiiH4_pZhDpDHY-Ks8bkgfSA9WaBDo4Scg0TS_HvTB6yGUtWNeZAgcBxV2UjhY9vVaEnOvbIRuvNE/s400/c69ef26d6df5ca89e3b5731d898ddd9e.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_u6mAcnk4MCqU0UpkB1nDQJxT2WyvoD9n8aARPsR-9bV3Ej4hCUXcHlmWFr9lRegiiH4_pZhDpDHY-Ks8bkgfSA9WaBDo4Scg0TS_HvTB6yGUtWNeZAgcBxV2UjhY9vVaEnOvbIRuvNE/s1600/c69ef26d6df5ca89e3b5731d898ddd9e.jpg)

Let's find something Honey :p  
Facebook has an option for App Review for Marketing API:  
This privilege is only given to app admin:  
App Review can only be submitted by app admins. Please contact an admin on the app to submit this app for review.  
**Impact:**  
A developer can change the app submission settings which can only be done by an admin and can also play with current submission settings.  
here's the official documentation:  
[Facebook developer's documentation](https://developers.facebook.com/docs/marketing-api/access/)  
The authorization check for the developer is missing on backend for the add/delete requests.  
Peter being a developer was able to delete the added submissions(despite of having them disabled on front end)  

###  **_Steps to replicate:_**

1\. create a test app,  
2\. add admin A and developer B  
3\. from developer B’s account go to  
https://developers.facebook.com/apps/[APP_ID]/marketing-api/settings/  
you will see App Review for Marketing API with App Review can only be submitted by app admins. Please contact an admin on the app to submit this app for review.  
fair enough  
(Loise looks like we are not getting a television this week ☹ )  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMd56awAOqsjqNSC38JotDUT7UlHj5t0hjhq9sLY4MuHc91x_msrK6dDeaV1HayUYJN4h1LT8bmPWoKLm5ewjhavNf0nNPBjZ4H07bzW9CLawbh5AR2Ku_cSIYivEbb1H685A0lLs1Pdc/s400/hqdefault+%25281%2529.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMd56awAOqsjqNSC38JotDUT7UlHj5t0hjhq9sLY4MuHc91x_msrK6dDeaV1HayUYJN4h1LT8bmPWoKLm5ewjhavNf0nNPBjZ4H07bzW9CLawbh5AR2Ku_cSIYivEbb1H685A0lLs1Pdc/s1600/hqdefault+%25281%2529.jpg)

  
why not test the back-end access controls? Lets create a test app in B’s account with B as an admin, as in the request for adding/deleting marketing_API the submission_id remains same for all the apps and look for missing authorisation.(which makes this easy for the developer's to exploit the issue):  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHvJwzy1hDllMXOnKqY_3Ky0TYbOB9FlMFCXNYwgqeJM3TVsjlBuwxQljf-vViHKOKW9_vutkHNapw2KPmjzHgw3_E0lRe_ZzM2P21n3UdrCIebmFEubPqYxrkAdlz7PF3vocnzjkl1rQ/s400/giphy+%25285%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHvJwzy1hDllMXOnKqY_3Ky0TYbOB9FlMFCXNYwgqeJM3TVsjlBuwxQljf-vViHKOKW9_vutkHNapw2KPmjzHgw3_E0lRe_ZzM2P21n3UdrCIebmFEubPqYxrkAdlz7PF3vocnzjkl1rQ/s1600/giphy+%25285%2529.gif)

wait, okey dokey, we have something in here !!

  
this is request which is modified to add and delete submisson_IDs  
  
POST /apps/[app_ID]/review/product/async/add-item/?product_submission_type=marketing_api&submission_id=submisson_ID  
  
POST /apps/[app-ID]/review/product/async/remove-item/?product_submission_type=marketing_api&submission_item_id=submisson_ID  
  
* send the above request from app where B is an admin and in burp change the appID (where he is a developer), the marketing API settings are changed(added or deleted)  
**_Timeline:_**  
**_Reported: 27 March 2019_**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz2aYEvyRzAgkg1cUNP45AGmC87RSSXi_AjWcdjVr6HccVHwQNDjn5LmFfxL94HQmIdli4FFHNltanSmDzOF8lNn4epKtFujZhiM5pqkRnqzPZiSFjfm8oJG1ysfwahGmlPw5be0taTbU/s400/Capture112.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz2aYEvyRzAgkg1cUNP45AGmC87RSSXi_AjWcdjVr6HccVHwQNDjn5LmFfxL94HQmIdli4FFHNltanSmDzOF8lNn4epKtFujZhiM5pqkRnqzPZiSFjfm8oJG1ysfwahGmlPw5be0taTbU/s1600/Capture112.JPG)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5jo8PvM_xqTO5_HibQ8y0kTU__isM_CViYb3kGq9BTngZQGFoYuMMhqzwzeHXR3XnHaAxE4JWfTdjYvYA9LpHgt-Zp9ILhtJ99dSIEZjzdkLnlRQSWv7JFZu6alVFUizk05kvroxqi7Q/s400/Capture123.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5jo8PvM_xqTO5_HibQ8y0kTU__isM_CViYb3kGq9BTngZQGFoYuMMhqzwzeHXR3XnHaAxE4JWfTdjYvYA9LpHgt-Zp9ILhtJ99dSIEZjzdkLnlRQSWv7JFZu6alVFUizk05kvroxqi7Q/s1600/Capture123.JPG)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE_C442NJwIDEltUdmk09LG5TD_AGmHGydVs9-pmVX3ih2CKmIArpp5ADYVZXD0bW3varI5f8nzyOrTeQt-qnOglq5ttOZZ5_fIyBFhOzMSRjwGOsudRwDXOafpYGRzNPRaf5Qc18-Hhs/s400/Capture1234.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE_C442NJwIDEltUdmk09LG5TD_AGmHGydVs9-pmVX3ih2CKmIArpp5ADYVZXD0bW3varI5f8nzyOrTeQt-qnOglq5ttOZZ5_fIyBFhOzMSRjwGOsudRwDXOafpYGRzNPRaf5Qc18-Hhs/s1600/Capture1234.JPG)

**_New Television_ 21.04.2019**  
**  
**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnRnXyjhjVOyC_Omy2R5SkUtAa0LmjW2-txy2Zy67z3xIoMZCZxwDPHr1J77ylNTG04UUtKA6v1j-5vR-O36ZmpaOTAQpu4WwhnazXms1ELw7EwzJ0UyLSrQYCGQFLTxMSW8ARXfF_PPs/s400/family-guy-ss1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnRnXyjhjVOyC_Omy2R5SkUtAa0LmjW2-txy2Zy67z3xIoMZCZxwDPHr1J77ylNTG04UUtKA6v1j-5vR-O36ZmpaOTAQpu4WwhnazXms1ELw7EwzJ0UyLSrQYCGQFLTxMSW8ARXfF_PPs/s1600/family-guy-ss1.jpg)

  
  

**Thanks Facebook Security for the quick resolution and an awesome program:**

**_./Family Guy_**

**_  
_**

  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[March 4, 2022 at 8:23 AM](https://whitehatfamilyguy.blogspot.com/2019/04/missing-authorization-check-while.html?showComment=1646411019447#c2027031969239796402)

Casinos Near Casinos Near Hollywood, FL - JT Hub  
Explore [통영 출장샵](https://drmcd.com/%ed%86%b5%ec%98%81%ec%a3%bc%eb%b3%80-%ea%b0%80%ea%b9%8c%ec%9a%b4%ec%b6%9c%ec%9e%a5%ec%95%88%eb%a7%88.html) a list [의정부 출장안마](https://www.mapyro.com/%ec%9d%98%ec%a0%95%eb%b6%80%ec%b6%9c%ec%9e%a5%ec%83%b5.html) of casinos [광명 출장안마](https://drmcd.com/%ea%b4%91%eb%aa%85%ec%b5%9c%ec%83%81%ec%9d%98-%ea%b4%80%eb%a6%ac%ec%b6%9c%ec%9e%a5%eb%a7%88%ec%82%ac%ec%a7%80.html) in Hollywood, FL, [경산 출장안마](https://www.jtmhub.com/%ea%b2%bd%ec%82%b0%ec%b5%9c%ea%b3%a0%ec%9d%98%ec%b6%9c%ec%9e%a5%eb%a7%88%ec%82%ac%ec%a7%80%eb%b0%9b%ec%95%84%eb%b3%b4%ec%84%b8%ec%9a%94.html) revenue, [양주 출장안마](https://www.jtmhub.com/%ec%96%91%ec%a3%bc%ec%b5%9c%eb%8c%80%ea%b7%9c%eb%aa%a8%ec%b6%9c%ec%9e%a5%ec%95%88%eb%a7%88.html) industry and

Reply[Delete](https://www.blogger.com/comment/delete/181979799605168940/2027031969239796402)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[shabnam bhagat](https://www.blogger.com/profile/16205802289076332779)[April 13, 2022 at 4:02 AM](https://whitehatfamilyguy.blogspot.com/2019/04/missing-authorization-check-while.html?showComment=1649847735104#c504220451610571911)

At [Digital Marketing](javascript:void\(0\);) Thanks for this amazing content.  

Reply[Delete](https://www.blogger.com/comment/delete/181979799605168940/504220451610571911)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/181979799605168940?po=3676501500491009928&hl=en&saa=85391&origin=https://whitehatfamilyguy.blogspot.com&skin=notable)
