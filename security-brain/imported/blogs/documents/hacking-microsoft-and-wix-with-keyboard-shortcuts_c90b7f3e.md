---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-15_hacking-microsoft-and-wix-with-keyboard-shortcuts.md
original_filename: 2024-02-15_hacking-microsoft-and-wix-with-keyboard-shortcuts.md
title: Hacking Microsoft and Wix with Keyboard Shortcuts
category: documents
detected_topics:
- xss
- csrf
- jwt
- clickjacking
- sso
- command-injection
tags:
- imported
- documents
- xss
- csrf
- jwt
- clickjacking
- sso
- command-injection
language: en
raw_sha256: c90b7f3e37e535befe2cc9b7a79795d8f5bd6c48b30c33550d52c9884e3b9462
text_sha256: 344fbadba52604c2e488c7b9bb32da602b95aa2a5d56ce95fdb057b13b3d5650
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Microsoft and Wix with Keyboard Shortcuts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-15_hacking-microsoft-and-wix-with-keyboard-shortcuts.md
- Source Type: markdown
- Detected Topics: xss, csrf, jwt, clickjacking, sso, command-injection
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `c90b7f3e37e535befe2cc9b7a79795d8f5bd6c48b30c33550d52c9884e3b9462`
- Text SHA256: `344fbadba52604c2e488c7b9bb32da602b95aa2a5d56ce95fdb057b13b3d5650`


## Content

---
title: "Hacking Microsoft and Wix with Keyboard Shortcuts"
page_title: "Hacking Microsoft and Wix with Keyboard Shortcuts | Imperva"
url: "https://www.imperva.com/blog/hacking-microsoft-and-wix-with-keyboard-shortcuts/"
final_url: "https://www.imperva.com/blog/hacking-microsoft-and-wix-with-keyboard-shortcuts/"
authors: ["Ron Masas (@RonMasas)"]
programs: ["Microsoft", "Wix"]
bugs: ["Stored XSS", "SSO", "Account takeover"]
publication_date: "2024-02-15"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 427
---

Browser vendors continuously tweak and refine browser functionalities to improve security. Implementing same-site cookies is a prime example of vendors’ efforts to mitigate Cross-Site Request Forgery (CSRF) attacks. However, not all security measures are foolproof. In their quest to combat Cross-Site Scripting (XSS), browser vendors introduced features that, while well-intentioned, sometimes fall short of their promise. Additionally, a browser’s behavior can sometimes be perceived as a security feature when, in reality, it is simply a peculiar behavior.

This blog post focuses on the humble anchor tag, specifically, how it behaves with different target attributes and protocols. We’ll observe how its inconsistent behavior can confuse security teams, allowing bugs to go unnoticed and potentially become targets for exploitation.

Many websites allow users to input URLs, such as links to social media profiles or personal websites. These links are then displayed on the website, which can create opportunities for exploitation through Cross-Site Scripting (XSS). A common method for such attacks involves using the JavaScript pseudo protocol in URLs. Successful exploitation of this method generally hinges on the server having inadequate URL validation.

I’ve encountered an intriguing scenario on several websites where, despite successfully getting a JavaScript protocol URL into an anchor tag, the browser blocks its execution. This happened when the anchor tag had the target attribute set to “_blank”. In these instances, clicking the link opened a new tab showing ‘ _about:blank#blocked_ ‘, rather than executing the JavaScript payload. I decided to delve deeper into this issue to see if there might be a workaround.

## Who Said There Are No Shortcuts in Security?

Well, keyboard shortcuts can be used to exploit this. There are some differences between Chrome and Firefox. Still, holding CTRL while clicking the link successfully executes the JavaScript payload even when the anchor tag has the target attribute set to “_blank.” Other shortcuts, like clicking the mouse middle button or CTRL+ENTER, also work.

I later learned this technique was already documented by DCLabs’ blog post, “[The curious case of XSS and the mouse middle button](http://blog.dclabs.com.br/2021/05/the-curious-case-of-xss-and-mouse.html).” With that said, they did not offer any practical way to exploit it other than hoping the user would accidentally use one of those shortcuts.

A more systematic approach to exploitation can be employed, particularly through iFrames in conjunction with clickjacking attacks. This method is viable if the vulnerable page can be embedded into another website. Using an invisible iframe and precise positioning using CSS, the iframe can be aligned so that clicking anywhere on the screen—while holding the CTRL button—can trigger the exploit. This setup can be facilitated on a malicious website, where a user might be instructed to hold the CTRL button as part of an interactive element, such as an online game or a fake CAPTCHA challenge.

I contacted Google to report this behavior as a potential bug since I could not determine whether this behavior was introduced as a security feature. Google clarified that this is not a security defense, making having an anchor tag with a JavaScript URL unsafe. They agreed that it would be beneficial to fix this to ensure more consistent handling of JavaScript URLs.

The remainder of this post will cover two stored XSS vulnerabilities I reported to Microsoft and Wix based on the above mentioned technique.

## The Microsoft Apps Portal

The myapps.microsoft.com website, or My Apps portal, is used by enterprises for managing and accessing organizational applications, allowing users to discover, request, and organize applications, including creating bookmarks for websites.

This vulnerability was easy to find but extremely hard to exploit. The API endpoint responsible for creating new bookmarks lacked server-side validation for the user-provided URL.

The server allows any URL, including the JavaScript protocol, that leads to stored XSS. However, as I explained earlier, the anchor tag where our URL is used has the attribute _target=_blank,_ which makes exploitation harder. Additionally, I could not find any way to share those bookmarks across accounts, which means the stored XSS is only on our account, which is not very useful.

## Reverse Account Takeover

The Microsoft My Apps website allows users to log into multiple accounts simultaneously and switch between accounts as needed. Since we can only exploit our account, getting a target to take it over would give us access to their account since all the accounts have the same origin. The idea was to find a way to automatically log any Microsoft account into our malicious account that already had the stored XSS payload.

The SSO integration was a perfect vector to test this hypothesis. Normally, Microsoft redirects the user to the organization domain, which controls authentication, which means we could create such an organization and automatically sign in any user. I quickly created a proof of concept demonstrating how this could be done in a background tab without user interaction.

## The Exploit

Now that we had a method to share our stored XSS with any Microsoft user, we needed to ensure we could also embed our stored XSS in an iframe. Fortunately, myapps.microsoft.com does not use the x-frame-options header, nor does it have a CSP policy that forbids other origins from embedding the site.

Since the user is logged into our account, we know exactly where our malicious bookmark is, allowing us to position it perfectly inside the iframe. With a bit of CSS, we can scale the iframe and make it invisible, so any click inside our malicious site would result in the user clicking our bookmark. To prevent the user from clicking the link without using a shortcut, I added the “sandbox” attribute to the iframe, which blocks all popups. Clicking on the link would focus on the anchor tag, which is helpful for a shortcut such as CTRL+ENTER. That shortcut opens the link of the currently selected anchor tag in a new tab or in our case, executes our arbitrary JavaScript.

In the proof of concept I made for Microsoft, I first got the user to click anywhere on the screen (focusing on the anchor tag) and then requested the user to press CTRL+ENTER on their keyboard. If the user followed the instructions, arbitrary JavaScript would execute.

It’s important to remember that when the JavaScript is executed, the target is logged into our account, which isn’t very useful. So, more work was needed to make this exploit affect other accounts.

Some access tokens for all connected accounts are stored in localStorage. These tokens persist even when a user switches between accounts. The scope of these access tokens includes:

  * email
  * openid
  * profile
  * application.readwrite.all
  * directory.read.all
  * https://graph.microsoft.com/user.read
  * https://graph.microsoft.com/.default
  * https://webshell.suite.office.com/shellinfo.read
  * https://webshell.suite.office.com/.default

I used the leaked access tokens to access a user’s company’s active directory records, sites, personal data, and more using the Microsoft Graph API.

## The Wix Marketplace

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2024/02/wix-poc.mp4>

Wix, one of the most popular website-building platforms in the world, features a marketplace that lets developers create components for use on Wix websites.

While exploring the Wix developer platform, I discovered that certain URL input fields, such as the “Demo site URL” or “Term & Conditions URL,” lacked proper server-side validation, allowing the use of the JavaScript protocol.

I also found that Wix allows developers to preview their app listing before they are published using a JSON Web Token (JWT) generated with the following request:

A new window is opened to the following URL, which renders our links.

_https://www.wix.com/market?appMarketParams={JWT Token}_  
  
The resulting URL can be shared with anyone if the JWT is valid.

Again, the anchor tags for our URL with the XSS payload have the target attribute set to “_blank.” Similar to Microsoft, Wix allowed the embedding of the vulnerable page. I quickly created a proof of concept: I loaded the page within an iframe and positioned the link so that when a user held CTRL and clicked on it, our JavaScript code would execute in the context of [www.wix.com](http://www.wix.com).

## Closing Thoughts

I suspect that the reason why these relatively easy-to-detect bugs were not addressed sooner was due to confusing browser behavior. I recall encountering this kind of bug on a high-profile website a few years ago and never reported it, as I believed it couldn’t be exploited. The browser opening a new tab to “about:blank#blocked” made me think the attack was “detected,” so I simply moved on.

I believe it’s important to change this browser behavior. It likely confuses security teams, bug bounty hunters, and security researchers, which, in my opinion, results in a net increase in unreported bugs and heightened security risks.

I would like to thank Microsoft and Wix for addressing our findings. It was rewarding to help make those platforms more secure.

### Try Imperva for Free

Protect your business for 30 days on Imperva.

[Start Now](https://www.imperva.com/free-trial/)
