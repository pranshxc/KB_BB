---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-18_cross-window-forgery-a-web-attack-vector.md
original_filename: 2024-02-18_cross-window-forgery-a-web-attack-vector.md
title: 'Cross Window Forgery: A Web Attack Vector'
category: documents
detected_topics:
- clickjacking
- oauth
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- clickjacking
- oauth
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 752c34c648d04e3853cc30d1c9b9ac322a026887dcbacce5f487770861f91cab
text_sha256: d72b41b144b50b1495015df61221471f331fbee30a8f2e23e48343efcf9ee2ed
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Cross Window Forgery: A Web Attack Vector

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-18_cross-window-forgery-a-web-attack-vector.md
- Source Type: markdown
- Detected Topics: clickjacking, oauth, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `752c34c648d04e3853cc30d1c9b9ac322a026887dcbacce5f487770861f91cab`
- Text SHA256: `d72b41b144b50b1495015df61221471f331fbee30a8f2e23e48343efcf9ee2ed`


## Content

---
title: "Cross Window Forgery: A Web Attack Vector"
page_title: "Cross Window Forgery: A New Class of Web Attack - Paulos Yibelo - Hacking Research"
url: "https://www.paulosyibelo.com/2024/02/cross-window-forgery-web-attack-vector.html"
final_url: "https://www.evil.blog/2024/02/cross-window-forgery-web-attack-vector.html"
authors: ["Paulos Yibelo (@PaulosYibelo)"]
bugs: ["Cross Window Forgery", "Account takeover"]
publication_date: "2024-02-18"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 423
---

#  Cross Window Forgery: A New Class of Web Attack 

10:30 AM

I've uncovered a technique that exposes a new class of client side web vulnerability. By leveraging two seemingly unrelated browser features, an attacker can trick an unsuspecting user into performing actions on a different website with minimal user interaction. While browsers implementing SameSite: Lax/Strict by default eradicates vulnerability classes like CSRF, antiCSRF tokens and SameSite cookies will not defend against this attack as it uses top level navigation windows. Let's dive into the technical details of this attack vector.

Attack Methodology:

  
To execute this attack, the attacker can employ various methods for successful exploitation of this vector, including the target user pressing a key or holding down a key while on the attacker's website. another approach involves the target user double-clicking using 3 different windows in a trick I call the sandwich method. There are also a few ideas around different avenues other than either methods to exploit this behavior smoothly, and I am excited to see how the security community might evolve this. I want to give shout out to @Qab for improving some of the techniques here. 

  
How does the vulnerability work?  
  
In HTML, an "ID" attribute can be assigned to an HTML tag, serving as a reference. This attribute can also be utilized in the URL Fragment. For instance, if a webpage has an HTML tag similar to the following  
<input type="submit" id="important_button" onclick=dosomething()>,  
  
the button can be preselected by navigating to the URL victim.com/page#important_button. If a user navigates to such a URL and presses Enter or Space key, the browser automatically clicks on the newly focused ID attribute, triggering associated action on the website.  
  
**So how is this behavior exploitable?  
Vector 1: Holding/****pressing****Enter/Space key while on attacker website**

  
Using new windows that are very small, an attacker can open the target page with the sensitive button in a new window with its sensitive button's ID referenced in the URL Fragment. The attacker can instruct the target user to hold a key, tricking them into interacting with unintended elements on the target website.  
  
While testing this around in the wild on websites like Coinbase and Yahoo, I found that this can lead to an account takeover if a victim that is logged into either site goes to an attacker website and holds a key. This is possible because both sites allow a potential attacker to create an OAuth application with wide scope to access their API, and they both set a static and / or predictable “ID” value to the “Allow/Authorize” button that is used to authorize the application into the victim's account.  
  
To pull off the attack, the attacker will prepare a website that will open the attacker’s malicious OAuth authorization prompt URL in a new window when the target user holds Enter/Space keys or another gesture that causes affirmation (like a mouse click). 

  

![](https://lh7-us.googleusercontent.com/DCion4slGPTz97LVqDg_ulFp4hXCNlx1J6WtRlvKLkMieOpJfsA3Fq0xFQf11HHcKfZbhcnVY0f11nSo2RCnad72qIlsJPZnhFY5ZeaRTJcsteK2Ay7M0aliUL2EjDVQitlTh88oR6r5E-rIYdI-xs8)  
  

The opened window preferably stays as a very small window in the corner of the screen or hidden using pop-under tricks so the victim doesn’t realize they have interacted with a different site. Here is an (ultra simplified) example: 

  

> 
>  function attack(){
>  //open new window with smallest possible height and width for a window
>  var win = window.open('https://target.com/oauth/allow?appId=attackerApp#allow-button','a','width=1,heght=1');
>  //attempt to resize the window to even smaller size (works better for Safari and IE/Edge/Opera)
>  win.resizeTo(1, 1);
>  //sleight of hand to move the new window to the edge of the screen so it doesn't capture the eye.
>  win.moveTo(4000, 4000);
>  //close the new window as fast as possible to hide what happened
>  //(the faster the page loads, the faster the window can close) 
>  setTimeout(()=>{win.close()},1290);
>  //show target user a message their expected action is complete
>  setTimeout(()=>{document.getElementById('div').innerText = "Cookies approved! welcome to our site!";},1500);
>  //setTimeout(()=>{location.reload();},4000);
>  }
>  //when target presses and holds Enter/Space key launch the attack
>  window.onkeypress=e=>{
>  attack();
>  }

The above simplifies the understanding of the attack process. Various techniques can be employed to reduce the attack's detectability and dramatically improve the likelihood of success. For example the attack appears less suspicious when a target doesn't need to hold their key for more than approximately 1 second. The effectiveness relies on how quickly we can close the target window, a factor influenced by the speed at which the target page loads. The accompanying video demonstrates the code in action. 

  

**How It Can Be Exploited**

  * ******OAuth & API Permissions**: Attackers could trick targets into authorizing a malicious application with extensive privileges. This technique has unfortunately led to account takeovers in almost every site that supports OAuth - which is pretty much all major websites with an API support because it is common to have static ID attributes on these buttons. And even if by some miracle it is detected and the user tries to revoke the a malicious attacker app, it would already be too late since it could perform its malicious actions the instant it is authorized.

_Authorizing malicious attacker app into a target user's Yahoo account (Chrome):_  
  
  

Vector 2: The Sandwich Technique 

  

An attacker website creates a sandwich-like scenario by opening two windows in sequence. The attacker's website occupies the top window, while the target website, with sensitive fragment in URL, sits in the middle. 

  

![](https://lh7-us.googleusercontent.com/ix3EKSj6-eXz2MlU-V0w7RJp-rlSikp36XIkvipEehPAazkw-z5r488sNr6zmtE4vJMtQZYK_jecChZWHRm_2B2x1oH292Yp5WJhrURvPUh4KORsfVM_kXHbD2WXJZQ_DEB0N5QPjx6k43GxOg_D9fQ)

  

Below you will find the code to perform this attack  
1: index.html

![](https://lh7-us.googleusercontent.com/KtuMsGaZdlZCLvoGaszd05f3vF3eOOenG8EE5VScrur9AwMGu9-6nyEp926OKLRVnWjub091jjRrOtM0xPcjF9a0Nf3FG0fQQf0fclRpdM8RHJ_WOw5m4UpqiYRHi7D5A8kZAMJVA9cbCKyZDnbwY1A)

  
2: click.html  
![](https://lh7-us.googleusercontent.com/Q2xPYflPu6iHEOcIOO1DsgNllL5Ig6ruSNuc5GfSe8U96ayr_iAlkgV1A8blgj5GeUgSdIezCTFjTU873KnhF_IfJqF_i9qUSdofdS30dsAc4r6dPgCO0pVB54RNxigI4tKLV9RnfjXznuCFkTGWvNk)  

**Attack Improvement ideas for key press vector:**

Prerendering: Using the <link rel="prerender" href="https://example.com/content/to/prerender"> tag, an attacker website can instruct a browser to prefetch and render the target page in the background before initiating an attack. This significantly accelerates the loading process of the target page in a new window.

  

Prefetching: Leveraging <link rel="prefetch" href="https://example.com/content/to/prerender">, an attacker page can notably boost the response time of the target page. Prefetch, a new browser feature, speeds up webpage load times by performing DNS resolutions before a link is opened or clicked. However, similar to prerender, prefetch requires an absolute URL to function. Unfortunately, if the final URL of the OAuth request is unknown due to multiple redirection, prefetching becomes impractical.

  

Caching Sub-Resources: Sub-resources of a page loaded through window.open() are cached by the browser, resulting in faster loading when opened in a new window. This allows the attacker to open the target page in a new hidden window, close it, and then reload it with the desired preselected fragment. This strategy significantly accelerates page loading as the newly opened window retrieves the target page's sub-resources from the cache.

  

Pop-unders: Pop-unders, often exploited by tracking and adware websites, involve displaying ads in a window hidden behind the main window. Although browser vendors actively address known methods of creating pop-unders, they are not deemed security vulnerabilities. Pop-unders become valuable when combined with this attack vector. 

  

Forced Caching: In instances where forced caching is possible across origins (or the page caches itself), an attacker can compel the victim's browser to cache the target page before opening it in a new window. This dramatically reduces load time as the target page is loaded from the cache rather than the internet. 

  

Safari Window Tricks: Browsers like Safari and Opera, when opened with a new window of 1x1 width and height, do not display the URL bar or title of a window. This can be paired with prompts like "Allow cookies"/"Allow Javascript" on the attacker's website to convince the victim that they haven't interacted with a different origin. In scenarios with slower prompts, this window may appear for less than 1 seconds, creating uncertainty of what might've happened, especially if the victim hasn't interacted with OAuth before.  

![](https://lh7-us.googleusercontent.com/H2YSie5TqS8kMKalzNQCXkQJYBvv-T20mwHpkZCI_rG90Y8wJcAdnDlS_N3xiKhm5EPqXg935ReO9Qli-vdEBtC5vzWjSD2DyYrfSqh13bOpoI3vXl3MJYYArVv34zZl31YwGPY6mdJiLWPJhpbaoYA)  

  

Attack Limitations: 

Performing the attack improvement ideas above can become challenging under certain conditions, such as when the target page experiences slow loading, involves redirects, utilizes dynamically generated URLs, or has an unpredictable final URL. To address these challenges, current solutions involve using preload, prefetch, or pop-unders to load the page before initiating the attack. However, if the final URL is unpredictable or includes redirects, the use of preload or prefetch may not be feasible.

  
Known Mitigations:  
1\. The easiest way to mitigate this is by randomizing ID attributes so they can't be guessed cross origin. So, an example of this would be renaming the ID "allow" to "allow234b" where 234b is a dynamically generated value either from the server or client unique for that particular user and can't be predicted by an attacker. You might observe Facebook doing the same thing regarding these buttons.  
2\. Another way to mitigate this is by removing ID attributes from important buttons and actively moderating for abuse. This is another mitigation technique implemented by Coinbase and Dropbox. 3\. For the double click vector, requiring a mouse gesture before enabling a button or waiting few ms to activate a button is one way to mitigate the vector.  
FAQ Section:  

  

Q: Is this considered a browser bug?

A: No, it's not. Both my opinion and the stance of browser vendors align on this. It's an intended behavior of browsers. Currently I am not aware of any plans to change it as it is not considered a browser bug per the RFC and Web Platform guidelines.

Q: If I want to fix this, what do I do?

A: To address this issue, consider adding or using unpredictable and hard-to-guess values for the "id" attribute. Alternatively, you may want to explore using the "name" attribute.  

Q: Can I randomize the ID?

A: While randomizing the "id" attribute can enhance security, be cautious. [Previous research](https://portswigger.net/research/xs-leak-leaking-ids-using-focus) by Gareth Hayes has demonstrated a method for leaking "id" attributes cross-domain. Unless the "id" value has sufficient entropy, there might be a risk of brute-forcing across sites, especially if the target site lacks iframe protection using X-Frame-Options.

Q: Who is vulnerable?

If your web application uses ID attribute to reference to a sensitive state changing action, you might be vulnerable.

Q: Can popup blockers address this vulnerability class?

No, the "pop-ups" occur after a user performs a gesture, such as clicking or pressing a key while on an attacker's website. Popup blockers in all modes still permit new windows to open following such user-initiated events. Content last updated in 2024 [https://evil.blog/2024/02/cross-window-forgery-web-attack-vector.html](https://www.evil.blog/2024/02/cross-window-forgery-web-attack-vector.html)

### Share This Story

  * [__ Share on Facebook](https://www.facebook.com/sharer.php?u=https://www.evil.blog/2024/02/cross-window-forgery-web-attack-vector.html&title= Cross Window Forgery: A New Class of Web Attack)
  * [__ Share on Twitter](https://twitter.com/share?url=https://www.evil.blog/2024/02/cross-window-forgery-web-attack-vector.html)
  * [__ Pin this Post](https://pinterest.com/pin/create/button/?url=https://www.evil.blog/2024/02/cross-window-forgery-web-attack-vector.html&media=https://lh7-us.googleusercontent.com/DCion4slGPTz97LVqDg_ulFp4hXCNlx1J6WtRlvKLkMieOpJfsA3Fq0xFQf11HHcKfZbhcnVY0f11nSo2RCnad72qIlsJPZnhFY5ZeaRTJcsteK2Ay7M0aliUL2EjDVQitlTh88oR6r5E-rIYdI-xs8&description= Cross Window Forgery: A New Class of Web Attack)

**__Tags:**

[ Newer Post ](https://www.evil.blog/2024/12/doubleclickjacking-what.html "Newer Post") [ Older Post ](https://www.evil.blog/2021/04/this-man-thought-opening-txt-file-is.html "Older Post")

#### You Might Also Like

####  0 comments 

Note: Only a member of this blog may post a comment.

[](https://www.blogger.com/comment/frame/8591474299777249503?po=9013784452795753003&hl=en&saa=85391&origin=https://www.evil.blog)
