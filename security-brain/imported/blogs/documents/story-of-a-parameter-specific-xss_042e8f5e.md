---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-19_story-of-a-parameter-specific-xss.md
original_filename: 2017-09-19_story-of-a-parameter-specific-xss.md
title: Story of a Parameter Specific XSS!
category: documents
detected_topics:
- xss
- sso
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 042e8f5e6b35459665086d14cac3c58779deb6b09cca4bf6db24c3528ca0260f
text_sha256: 8b7b051431fac3eb999ac86e4969b81bfbeb65436cc684bbf10ebc50e5332f7e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a Parameter Specific XSS!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-19_story-of-a-parameter-specific-xss.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `042e8f5e6b35459665086d14cac3c58779deb6b09cca4bf6db24c3528ca0260f`
- Text SHA256: `8b7b051431fac3eb999ac86e4969b81bfbeb65436cc684bbf10ebc50e5332f7e`


## Content

---
title: "Story of a Parameter Specific XSS!"
url: "http://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html"
final_url: "https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html"
authors: ["Rahul Maini (@iamnoooob)"]
bugs: ["XSS"]
publication_date: "2017-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6101
---

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ September 19, 2017  ](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html "permanent link")

###  Story of a Parameter Specific XSS! 

# REDIRECTING TO THE NEW BLOG ... 

Hello Infosec folks!  

So I am going to start writing posts related to my bug hunting findings and share it with the community starting with this post.

  

So, this post is about a Reflected XSS I found in a Private Program which has been previously tested many times.This XSS was present on nearly every page of the domain (let's call this private-bounty.com) but wasn't found by anyone before.

  

When I was going through the Application, I found an endpoint which had following in URL:

https://www.private-bounty.com/Deactivate?view=**aaa** &utm_content=**foo** &utm_medium=**bar** &utm_source=**baz**

  

I checked the source code to see if the parameter "view" was reflected somewhere in the page and it was found that the whole URL was reflected in Javascript context(inside Script tags) but except for the parameter "view" and its value.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrVZc-FCL1ZfYWkmJABhXwkJ0G-rLAlizbKAx7ck9iIdNmASLuZuWjTciA9fJXvSMfMiVq76ZP1yur6M2OsSRQqlX3WlFWxGPi0D9RJUxjM-dbt9xt0LxaIMKMjlmCyD3MorWzx7YBoHbN/s1600/Screenshot+from+2017-09-19+17-00-24.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrVZc-FCL1ZfYWkmJABhXwkJ0G-rLAlizbKAx7ck9iIdNmASLuZuWjTciA9fJXvSMfMiVq76ZP1yur6M2OsSRQqlX3WlFWxGPi0D9RJUxjM-dbt9xt0LxaIMKMjlmCyD3MorWzx7YBoHbN/s1600/Screenshot+from+2017-09-19+17-00-24.png)

  

  

  

It got reflected as - 

https://www.private-bounty.com/Deactivate?utm_content=**foo** &utm_medium=**bar** &utm_source=**baz**

  

Then I tried to break out since **foo, bar** and**baz** values were also reflected in the page that but unfortunately, everything was properly encoded, 

  

https://www.private-bounty.com/Deactivate?utm_content=**foo****'" ><>\**&utm_medium=**bar****'" ><>\**&utm_source=**baz****'" ><>\**

**  
**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQi4-wK0k4qOWaW8jHheqkQQpJ9MkWSX8yDQrC-EnNnC5MI8Ufr5tVgPniIp6xZE1572Q4N0Pa8lY3F2TsxT2kyT9G06ReKpxUntj-yqCIDeF7QiJlUoaqvphy92U3HWzg02tH5QqmSVKP/s1600/Screenshot+from+2017-09-19+17-05-48.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQi4-wK0k4qOWaW8jHheqkQQpJ9MkWSX8yDQrC-EnNnC5MI8Ufr5tVgPniIp6xZE1572Q4N0Pa8lY3F2TsxT2kyT9G06ReKpxUntj-yqCIDeF7QiJlUoaqvphy92U3HWzg02tH5QqmSVKP/s1600/Screenshot+from+2017-09-19+17-05-48.png)

  

  

Then I tried to add quotes in the **path itself** but it was also encoded well, so I moved ahead to find something else after not being able to XSS this due to the proper encoding of user input.

  

https://www.private-bounty.com/Deactivate/**'"**?utm_content=foo'"><>\&utm_medium=bar'"><>\&utm_source=baz'"><>\  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9UKwpZChxGoJ6UqIQGTfXK0oBuDcjGppBU-A4ufBh4k1En-QWsvfJo9f-JtwOEUxbBC2x_OXJKxBFzagU0yS3R6BmXvVF8_s7EZ5WUGBJjgoe7tvR0CTbPbS2Z_DB-4LuYb5fHCO-ntMy/s1600/Screenshot+from+2017-09-19+17-09-38.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9UKwpZChxGoJ6UqIQGTfXK0oBuDcjGppBU-A4ufBh4k1En-QWsvfJo9f-JtwOEUxbBC2x_OXJKxBFzagU0yS3R6BmXvVF8_s7EZ5WUGBJjgoe7tvR0CTbPbS2Z_DB-4LuYb5fHCO-ntMy/s1600/Screenshot+from+2017-09-19+17-09-38.png)

  

  

I found this pattern of "utm_content=**foo** &utm_medium=**bar** &utm_source=**baz** " on every endpoint getting reflected and no other parameter will be reflected. I tried to append a custom parameter myself to see if it gets reflected, but it didn't work

  

https://www.private-bounty.com/Deactivate?view=**aaa** &utm_content=**foo** &utm_medium=**bar** &utm_source=**baz** &test=xxxxx

**  
**

After that, I tried to append a parameter named utm_foobarbaz=xxxxx 

  

https://www.private-bounty.com/Deactivate?utm_content=**foo** &utm_medium=**bar** &utm_source=**baz** &**utm_foobarbaz=xxxxx**

**  
**

and it was reflected! into the page, so the application only reflected the parameters beginning with "utm"  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy8kh1JmKbgAc6RBKTQ8gYbaEn7lLCx0iXpQ1zXf_s56t6Q6zE_QupboDzW8p1LyX2P_-V81sOMeJM7UXg0-2SUnMOFRJcL3P1hWWIPzT4oHmlW1IgF0TClQgZ062iym5PjDJf6_hIsnUl/s1600/Screenshot+from+2017-09-19+17-11-40.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy8kh1JmKbgAc6RBKTQ8gYbaEn7lLCx0iXpQ1zXf_s56t6Q6zE_QupboDzW8p1LyX2P_-V81sOMeJM7UXg0-2SUnMOFRJcL3P1hWWIPzT4oHmlW1IgF0TClQgZ062iym5PjDJf6_hIsnUl/s1600/Screenshot+from+2017-09-19+17-11-40.png)

  

so I tried again to break the context to achieve XSS using this parameter's value but it was also encoded well :(

  

Then the last try I did was to break the context by putting the payload in the parameter name itself 

  

https://www.private-bounty.com/Deactivate?utm_content=**foo** &utm_medium=**bar** &utm_source=**baz &utm_foobarbaz'"</>=xxxxx**

  

and boom! it worked :D, the parameter names beginning with "utm" were not being encoded when reflected in the page.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnUe_hx0J-isgzU24cypZAtMyrFW8HC8aMS2FHgOE38Ty8gvJWHjE9gLOW9BqljuQnW-Om8OZDuj2MPEFWu4IiITOzf-AdAWyDLtewUEi3ZEBpQp5Cv_zCSrPKHojR602MAUMZcWlLo7KS/s1600/Screenshot+from+2017-09-19+17-13-47.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnUe_hx0J-isgzU24cypZAtMyrFW8HC8aMS2FHgOE38Ty8gvJWHjE9gLOW9BqljuQnW-Om8OZDuj2MPEFWu4IiITOzf-AdAWyDLtewUEi3ZEBpQp5Cv_zCSrPKHojR602MAUMZcWlLo7KS/s1600/Screenshot+from+2017-09-19+17-13-47.png)

  

  

and That's how we alert :p , 

  

https://www.private-bounty.com/Deactivate?utm_content=foo&utm_medium=bar&utm_source=baz&**utm_foobarbaz');alert(1)//**

**  
**

The lesson is that we should also always try to inject/fuzz the parameter names themselves and this was just a special case of such an XSS in parameter name beginning with a specific keyword "utm".

**  
**

\- Rahul Maini

  

  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[a](https://www.blogger.com/profile/15746623282071164188)[19 September 2017 at 07:37](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1505831853331#c4076525391038661378)

Awesome :)  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/4076525391038661378)

Replies

Reply

  2. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7TRGHCUc0GM2xiCWkONitbN1Ppd1I63SCd9UbpfMw0SLMH2Yu0elLH-9Dujs98tBs5FKSazQbAC6LQUKH9zrRbkd2KdExKJvlhvuOMZd2fChKcVwdCTinw20oSOHvXK8/s45-c/32.jpg)

[jack sparrow](https://www.blogger.com/profile/08965184577924670817)[19 September 2017 at 08:40](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1505835602333#c6133719117721559597)

:O awesone :) 

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/6133719117721559597)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Mahender Singh](https://www.blogger.com/profile/09500417054468675084)[19 September 2017 at 11:52](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1505847125723#c8005518390406001288)

Good  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/8005518390406001288)

Replies

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[aaaaaaaaaaaaaaaaaa](https://www.blogger.com/profile/07104183383423526255)[20 September 2017 at 08:15](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1505920502320#c4955003711439540900)

awesome work! :P  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/4955003711439540900)

Replies

Reply

  5. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/00485848492644818505)[21 September 2017 at 07:57](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1506005845485#c2933102106374732351)

Good one mate (y)  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/2933102106374732351)

Replies

Reply

  6. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/12949956222375457113)[22 September 2017 at 11:40](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1506105653341#c6451771448183115736)

Gazzab

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/6451771448183115736)

Replies

Reply

  7. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/03468955457467721526)[26 September 2017 at 02:02](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1506416565145#c7353146545395400154)

keep it up !!!  

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/7353146545395400154)

Replies

Reply

  8. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/04998164884915961417)[8 November 2017 at 20:18](https://www.noob.ninja/2017/09/story-of-parameter-specific-xss.html?showComment=1510201104343#c3647162313178138970)

gazzab kiye ho maini saaab

Reply[Delete](https://www.blogger.com/comment/delete/7318948769938379972/3647162313178138970)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7318948769938379972?po=1212901225088768042&hl=en-GB&saa=85391&origin=https://www.noob.ninja&skin=soho)

###  Popular Posts 

[ ![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7VodlIxskfhxs_IAhV5gn-pKxLSR8ExxXjeCIKQKBuXBJz7rBE-8VVVhq-2C0xTrUyifVnznfyaRkXYtIaYx62sPPSpRbcklCXmOBczGIzAAqIkJybxBTle-4GIzY2JQLchOts8xNCA5J/s1600/Screenshot+from+2017-11-08+14-29-18.png) ](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html)

[ November 08, 2017  ](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html "permanent link")

### [Local File Read via XSS in Dynamically Generated PDF](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ 23 comments ](https://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html#comments)

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
