---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-29_bingbang-the-aad-misconfiguration-that-led-to-bingcom-results-manipulation-and-a.md
original_filename: 2023-03-29_bingbang-the-aad-misconfiguration-that-led-to-bingcom-results-manipulation-and-a.md
title: 'BingBang: The AAD misconfiguration that led to Bing.com results manipulation
  and account takeover explained'
category: documents
detected_topics:
- sso
- access-control
- oauth
- jwt
- xss
- command-injection
tags:
- imported
- documents
- sso
- access-control
- oauth
- jwt
- xss
- command-injection
language: en
raw_sha256: 2e6512d6c4cd73482047e25e7091749c7020a0aa0b7291f1a92ccafc3b37198e
text_sha256: 655ab8857641dd07c5766b33a3f2023ed3ec60232bcb04ea292a5e1da4febb80
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# BingBang: The AAD misconfiguration that led to Bing.com results manipulation and account takeover explained

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-29_bingbang-the-aad-misconfiguration-that-led-to-bingcom-results-manipulation-and-a.md
- Source Type: markdown
- Detected Topics: sso, access-control, oauth, jwt, xss, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `2e6512d6c4cd73482047e25e7091749c7020a0aa0b7291f1a92ccafc3b37198e`
- Text SHA256: `655ab8857641dd07c5766b33a3f2023ed3ec60232bcb04ea292a5e1da4febb80`


## Content

---
title: "BingBang: The AAD misconfiguration that led to Bing.com results manipulation and account takeover explained"
page_title: "BingBang: AAD misconfiguration led to Bing.com results manipulation and account takeover | Wiz Blog"
url: "https://www.wiz.io/blog/azure-active-directory-bing-misconfiguration"
final_url: "https://www.wiz.io/blog/azure-active-directory-bing-misconfiguration"
authors: ["Hillai Ben-Sasson (@hillai)"]
programs: ["Microsoft (Bing)"]
bugs: ["Account takeover", "Azure AD", "Cloud", "XSS", "Privilege escalation"]
publication_date: "2023-03-29"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1327
---

## 

Executive summary

  * Wiz Research discovered a new attack vector in Azure Active Directory that exposed misconfigured applications to unauthorized access. 

  * These misconfigurations are fairly popular, especially with Azure App Services and Azure Functions. Based on our scans, about 25% of multi-tenant applications turned out to be vulnerable. 

  * We found several high-impact, vulnerable Microsoft applications. One of these apps is a content management system (CMS) that powers Bing.com and allowed us to not only modify search results, but also launch high-impact XSS attacks on Bing users. Those attacks could compromise users’ personal data, including Outlook emails and SharePoint documents. 

  * All issues were reported to the MSRC team. It fixed the vulnerable applications, updated customer guidance, and patched some AAD functionality to reduce customer exposure. MSRC’s blog can be found [here](https://msrc.microsoft.com/blog/2023/03/guidance-on-potential-misconfiguration-of-authorization-of-multi-tenant-applications-that-use-azure-ad/).

  * To check whether your environment has been affected by this misconfiguration, please refer to the “Customer Remediation Guidelines” section of the blog.

_BingBang attack flow_

## 

**Introduction**

From Amazon Cognito to Google Firebase or Microsoft Azure Active Directory, there are many cloud-based identity providers on the market serving various business needs. The complexity of each IdP facilitates misconfigurations, which can potentially be leveraged by threat actors to compromise organizations’ production environments. 

In this blog post, we will demonstrate how Microsoft itself fell prey to AAD’s configuration challenges, and inadvertently exposed internal applications to external attackers. These applications allowed us to view and change various types of sensitive Microsoft data. In one particular case, we were able to manipulate search results on Bing.com and perform XSS attacks on Bing users, potentially exposing customers’ Office 365 data such as emails, chats, and documents. This blog will also provide details about the misconfigurations, and how to detect and mitigate them in your environment.

## 

**Azure Active Directory (AAD)**

Microsoft offers its own SSO service in Azure, AAD, which is the most common authentication mechanism for apps created in Azure App Services or Azure Functions. AAD provides different types of account access: single-tenant, multi-tenant, personal accounts, or a combination of the latter two. Single-tenant applications only allow users from the same tenant to issue an OAuth token for the app. Multi-tenant applications on the other hand, allow any Azure tenant to issue an OAuth token for them. Therefore, app developers must inspect the tokens within their code and decide which user should be allowed to log in. 

In the case of Azure App Services and Azure Functions, we see a textbook example of [Shared Responsibility confusion](https://www.wiz.io/academy/shared-responsibility-model). These managed services enable users to add an authentication function with the click of a button, a seemingly smooth process for the application owner. However, the service only ensures the token’s validity. It’s not clear to application owners that it’s their responsibility to validate the user’s identity via OAuth claims and provision access accordingly. 

With single-tenant authentication, the impact is limited to the application’s tenant – all users from the same tenant could connect to the application. 

But with multi-tenant applications, the exposure is as wide as it gets – without proper validation, any Azure user will be able to log in to the application.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AJeAJACT/9k=)

Configuring tenancy in Azure App Services

This complicated architecture is not always evident to developers, and the responsibility to validate the end-users’ tokens is unclear. As a result, configuration and validation mistakes are quite prevalent. 

Upon recognizing these issues and their potential impact, we started scanning the internet for exposed applications. The results surprised us: 25% of all the multi-tenant apps we scanned were vulnerable to authentication bypass. 

The following case study on the “Bing Trivia” application, which we have dubbed “#BingBang,” illustrates how Microsoft itself fell victim to misconfiguration pitfalls and exposed one of its most critical apps to any individual on the internet.

## 

**The BingBang case study**

### 

**Part 1 – Reconnaissance**

To measure how common this misconfiguration was, we started scanning Azure App Services and Azure Functions for exposed endpoints. The scan yielded many potentially vulnerable websites, so to narrow the scope of the research, we decided to focus on Microsoft’s own tenant. 

We spotted several Microsoft apps, but the first domain that caught our eyes was `bingtrivia.azurewebsites.net`. Given Bing is a very popular product these days, anything related to it was of interest to us. To validate the exposure, we created a new user called “Wiz Research” in our own tenant and tried logging in to Bing Trivia with it.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABcAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAAAAv/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AK2ApIAAAAAD/9k=)

Multi-tenant authentication allows any Azure user to issue an OAuth token

Even though we did not belong to the Microsoft tenant, we successfully logged in and landed on the Bing Trivia home page. 

We started to examine the page in front of us. At first glance it appeared a bit unremarkable – just a simple CMS with lots of sections crammed into it. To determine whether the system was intentionally open, we needed to understand its purpose.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhAPEQgLCg4NDhgLDQ0ODh0NEBEYFxUZGCITFhUaKyslGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDgoOGg0NGC8cFhwvLy8vLy8vNS8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAAAgMH/8QAHhAAAgEDBQAAAAAAAAAAAAAAAAEyAgQFAxETMVH/xAAWAQEBAQAAAAAAAAAAAAAAAAACAQD/xAAWEQEBAQAAAAAAAAAAAAAAAAAAEhH/2gAMAwEAAhEDEQA/ANWeMtm+w8Ta+ivRarkyfC2pMsDql4m13kCdWg95sCln/9k=)

The Bing Trivia admin panel, after a successful login

Given the app was named “Bing Trivia”, we assumed it was intended for trivia content. However, upon browsing the app, we noticed several interesting sections related to core Bing content. One of these sections was the “Carousels” section, which contained a table with search result suggestions appearing on Bing. Another section showcased quizzes and background images, which appeared on the Bing.com homepage that same day. This raised the question – can this panel enable us to modify Bing’s search results?

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoXDhgQDg0NDh0VFhEYFysiHRYkFiEiJSsmGh0tHRYlJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHA0QHDscFhw7Ly8vLzs7OzsvLy8vLy8vLy8vLzs7NS8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAcAGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAABQYH/8QAHxAAAgICAQUAAAAAAAAAAAAAAQIABAMFUQYRFCEi/8QAFQEBAQAAAAAAAAAAAAAAAAAAAgH/xAAZEQACAwEAAAAAAAAAAAAAAAAAMQECIQP/2gAMAwEAAhEDEQA/ANHfdUTSfx8RX1xKJm21pbrlW+e8RB3rrFBOdNbtHtEZlJMREVYxkP/Z)

Viewing the daily wallpaper in Bing Trivia

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLERYWDhgPDg0NDh8NDQ0YFxUZGCIVIhUaHysjGh0oHRUiJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDsoFhw7Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABAUD/8QAHhAAAQQCAwEAAAAAAAAAAAAAAQACAwUEERIhMgb/xAAWAQEBAQAAAAAAAAAAAAAAAAADBAD/xAAZEQACAwEAAAAAAAAAAAAAAAADEQACMQH/2gAMAwEAAhEDEQA/AMGUeO5voJuL5qB8foKDFYzCLfIprFucgNI2VGOhFsTqjOXQQxDXJCm5ttO49koR2GR7M+T/2Q==)

Viewing the same wallpaper on Bing.com

### 

**Part 2 – Altering search results**

To verify our ability to control Bing search results, we selected a carousel in the CMS and slightly altered its content. We wanted to make a small change, which would be easy to revert. We chose the “best soundtracks” query, which returned a list of highly recommended movie soundtracks; we then proceeded to change the first item, “ _Dune (2021)_ ,” to our personal favorite, “ _Hackers (1995),_ ” and saved our edit.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAkAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AK2AQgCT/9k=)

Modifying the search result within Bing Trivia

To our surprise, our new result immediately appeared on Bing.com, complete with our new title, thumbnail, and arbitrary link! 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoXFyQWFQ0NDh0VFhEdFyIZHRYUJiEmKysvHR0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBANHDsoFhwvLy8vOy87Oy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAoAGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAGAAIF/8QAJRAAAQMCAwkAAAAAAAAAAAAAAQACEQMFBAZhEhMUIiNRcYKR/8QAFQEBAQAAAAAAAAAAAAAAAAAAAgD/xAAZEQADAAMAAAAAAAAAAAAAAAAAAVEREiH/2gAMAwEAAhEDEQA/AH93ut2pN6OHIGgWaMzX1lOOFk6tThwDhBAPlUFKnA5G/FZ6WHQTUzNmDdSMJHqonBYwiNkR2hRNNQOrp//Z)

Bing’s search results for the “best soundtracks” keywords

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDiAQFQ0NDh0VFhEYFyUdGC0iLiEmKzQsJiUtHSEiJDUlNC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDsoIh07Ozs7Oy87Ozs7Oy8vLy87Lzs7Ly87LzsvLzUvLy8vLy8vOy8vLy8vLy8vLy8vLy8vL//AABEIAAoAGAMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABgcF/8QAIRAAAQMDBAMAAAAAAAAAAAAAAQACEQQGEgUUUWEDcaL/xAAWAQEBAQAAAAAAAAAAAAAAAAABAgD/xAAaEQACAwEBAAAAAAAAAAAAAAAAARESUTEC/9oADAMBAAIRAxEAPwB4uLWNbpgBTUpaOgs0XbcTKUHY5O5LU/OaHNhwBHaMGRGLY4hayngQ9J627rnPjnYfCFQsGgQGiPSFa9LAq9P/2Q==)

The movie “Dune” was replaced with the movie “Hackers”

This proved that we could control Bing’s search results, and as we would later confirm, this control extended to Bing’s homepage content as well. 

In order to ascertain the breadth of the attack surface, we then decided to leverage this access and test XSS viability with a sample harmless payload. The payload also ran as expected, so we quickly reverted our changes and immediately reported our findings to Microsoft. 

### 

**Part 3 – Attacking Bing users**

While working with Microsoft on the report, we started investigating the impact of the XSS. We saw that Bing has a “Work” section that allows you to search your organizational directory; when inspecting this functionality, we realized it was based on the Office 365 API, with the `business.bing.com` hostname used by Bing for Office-related communications. 

This really piqued our interest, since many organizations use Office 365 to store their most sensitive business data. One specific endpoint created JWT tokens for the Office 365 API, so we generated a new XSS payload via this endpoint:

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoUCAgLCgoODg4LDg0NDh0VDgUNFxUZGBYVFhUaKysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0NEBAOEC8cFhw7Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAUAGAMBIgACEQEDEQH/xAAWAAEBAQAAAAAAAAAAAAAAAAAABgH/xAAbEAACAwEBAQAAAAAAAAAAAAAAAgEDBDM0E//EABUBAQEAAAAAAAAAAAAAAAAAAAMA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8AiqdKfHgkirVXDeZDAII3almrisAAk//Z)

Our XSS payload, issuing an Office 365 token on behalf of the user

We then tested this payload against our old injection point and retrieved a valid token from our “victim” user (in this case, our research account).

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLDRYXDhgODQ0NDh0NFg0YFxMZGCITFhUaIysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OGA0NHDscFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAAFBwAEBv/EAB8QAAEEAgIDAAAAAAAAAAAAAAMAAQKRBBEFFBIhI//EABYBAQEBAAAAAAAAAAAAAAAAAAECAP/EABcRAAMBAAAAAAAAAAAAAAAAAAABAhH/2gAMAwEAAhEDEQA/ADeabhtbYsbVCZuEIzM5o2sPDFKYD+R5Wh58EkX9HlaU5JGYd+B6rfaNqJV5OKZw67ErURsmP//Z)

Victim view of the XSS attack – stealing the user’s Office 365 token

This token enabled us, as “the attacker”, to fetch the victim’s Office 365 data including Outlook emails, calendars, Teams messages, SharePoint documents, and OneDrive files. Here we can see the attacker’s computer, successfully reading emails from the victim’s inbox:

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA0AGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AJqAJACT/9k=)

Attacker view of the XSS attack – reading the victim’s Outlook emails

A malicious actor with the same access could’ve hijacked the most popular search results with the same payload and leak sensitive data from millions of users. According to SimilarWeb, Bing is the 27th most visited website in the world, with over a billion pageviews per month – in other words, millions of users could’ve been exposed to malicious search results and Office 365 data theft.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAWAQADAAAAAAAAAAAAAAAAAAAAAQL/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCygGkAAf/Z)

Full BingBang attack flow

## 

**Additional vulnerable applications**

In addition to the Bing Trivia app, we found several other internal Microsoft apps with similar misconfigurations and exposure to anyone trying to log in: 

** _Mag News:_** A control panel for the MSN Newsletter, capable of sending arbitrary emails from a trusted Microsoft email to a huge audience.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhUUCAgLFAoLFRoPDRkNDhUQFBUYFxUZGBYVIhUdHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDscFhwvLy8vLy8vOy8vLy8vLy8vLy8vLzs7Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAAAAwEFB//EABoQAAIDAQEAAAAAAAAAAAAAAAEDAAIEITL/xAAUAQEAAAAAAAAAAAAAAAAAAAAC/8QAGBEAAwEBAAAAAAAAAAAAAAAAAAIRUQH/2gAMAwEAAhEDEQA/ANVcjEIiycZHJYNzJsO1ijlSK+YqwequEZ1ZRTkI5KFgeYQ3oouH/9k=)

**_CNS API:_** An API for Microsoft’s Central Notification Service, capable of reading and sending internal notifications to Microsoft developers.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhYIDwgQCg0VFRAQDg0NGhcNFg0NFxUZGCIVFhYaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDgsPEBAMHC8dFhwvNS8vLy8vNS8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABIAGAMBIgACEQEDEQH/xAAYAAEBAAMAAAAAAAAAAAAAAAAAAwEEB//EAB4QAAICAgIDAAAAAAAAAAAAAAABAhIEEQMFE0JS/8QAFgEBAQEAAAAAAAAAAAAAAAAAAQMC/8QAFhEBAQEAAAAAAAAAAAAAAAAAABIB/9oADAMBAAIRAxEAPwDqC6rBtqwXS4anaxGOLJy35Cq4Zp6uUjEr1trCxorWwRhwS+gE4b1DgZX3ANpqowABf//Z)

**_Contact Center:_** An API for Microsoft’s Contact Center, controlling call center agents for Microsoft’s customer representatives.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLChUVFBYQDg0VDh0hFBEYFxUZHRYVFhUaHysjGikoHRUWJDUlKC0vMjUyGSI4PTcwPCsxMi8BCgsLDg0PFg0FFS8eFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABEAGAMBIgACEQEDEQH/xAAZAAADAAMAAAAAAAAAAAAAAAAAAwQBAgf/xAAgEAACAQQBBQAAAAAAAAAAAAAAAQIEERIyIQUUFTGR/8QAFgEAAwAAAAAAAAAAAAAAAAAAAAEC/8QAFxEBAQEBAAAAAAAAAAAAAAAAAAESAv/aAAwDAQACEQMRAD8A6f43p6nbJGz6VQZqWSFKlhOfExjpOUs2JU4irtaRRtdfQFqkstgAsxNT7FT2QACjn6MgAE//2Q==)

**_PoliCheck:_** “PoliCheck” is an internal Microsoft tool that is used to check for forbidden words in Microsoft code. This application was essentially the centralized database for PoliCheck rules. Rules include words in over 100 languages, ranging from profanity and slurs to geopolitically and legally controversial issues.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLFRESDhUVDhUOFR0hFhUYFxUdGBYTFhUqHyslHR0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDgcFEBAQHDscFhwvLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAZAAABBQAAAAAAAAAAAAAAAAADAAECBAf/xAAgEAABAgUFAAAAAAAAAAAAAAAAAQIDERMxMgUSFCFR/8QAFQEBAQAAAAAAAAAAAAAAAAAAAQD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwDV2ag5btEmozdLaHSBDRuJVptqWEDc7vERFYbfByD/2Q==)

**_Power Automate Blog:_** A WordPress admin panel, controlling a very active blog hosted on `powerautomate.microsoft.com`. This panel allowed us to create and edit posts with arbitrary HTML content, and publish them to a trusted Microsoft.com domain.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDhUQDg0ZDh0eFhEdHR0ZGCIVFi0aHysvIh0oHRUWJDUlLS0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OEBAOEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAZAAABBQAAAAAAAAAAAAAAAAAGAQMEBQf/xAAfEAABBAICAwAAAAAAAAAAAAABAAMEBQIhBzEREiL/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/ALXjqNBerSMijdulrfQ/QWecf4jGuPjSOIhJ0SUhTs6mubZ30kTsprAwxpIpP//Z)

**_COSMOS:_** A file management system, managing over 4 exabytes (!) of Microsoft’s internal files. COSMOS categorizes files by Microsoft divisions and teams, and enables in-app file listing, reading, and editing.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBg4SDQgSERMNDRgODg4WDhEVCxENFx8ZGCIVIhUaHzcjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0PHQwNHC8dFigvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABYAGAMBIgACEQEDEQH/xAAZAAACAwEAAAAAAAAAAAAAAAAAAgEFBgT/xAAhEAACAgECBwAAAAAAAAAAAAAAAQIyBBESAwUGFBZSof/EABcBAQEBAQAAAAAAAAAAAAAAAAIDAQD/xAAXEQEBAQEAAAAAAAAAAAAAAAAAARIR/9oADAMBAAIRAxEAPwDfy6iytafBpc/yHGpW8ScmqCKXE9RZgaqy8gyoqoHBvltoQdmN3UTzWlUVZ70oAE+qWJ7xtVAAEPH/2Q==)

All these issues have been reported to Microsoft. The Microsoft team fixed them in a timely manner and awarded us a bug bounty of $40,000, which we will donate. Although these services did not fall within the scope of the bounty program, the Microsoft team based their decision on the additional product and guidance improvements for AAD that stemmed from our findings.

## 

**Customer remediation guidelines**

### 

**Am I affected?**

The issues we identified in this research may affect any organization with Azure Active Directory applications that have been configured as multi-tenant but lack sufficient authorization checks.

Based on data from our scans, we assess that exposure is significantly more common across Azure App Service and Azure Functions applications, where validation responsibility is unclear to developers. 

### 

**How do I detect these issues in my environment?**

Administrators can use the Azure Portal to query their AAD service principals and look for any that are configured to allow multi-tenant access. These should appear under “App Registrations” or the “Authentication” section of each application’s page. 

It is also possible to use the Azure CLI to query for multi-tenant applications:
  
  
  az ad app list --filter "(signinaudience eq 'AzureADMultipleOrgs' or
  signinaudience eq 'AzureADandPersonalMicrosoftAccount')" --query "[?web && 
  web.homePageUrl].{AppName:displayName, AppID:appId, AppURL:web.homePageUrl}" 

To verify whether the application is vulnerable or not, use your web browser to sign in to your app with a user from a different Azure tenant than your own. If this login is successful, and your app is not meant to be exposed to other Azure tenants, the app is vulnerable. 

Wiz customers can use either [_this query_](https://app.wiz.io/graph#~\(query~\(type~\(~'SERVICE_ACCOUNT\)~select~true~where~\(aad_signInAudience~\(EQUALS~\(~'AzureADMultipleOrgs~'AzureADandPersonalMicrosoftAccount\)\)~externalOwners~\(IS_SET~false\)\)~relationships~\(~\(type~\(~\(type~'ACTING_AS~reverse~true\)\)~with~\(type~\(~'WEB_SERVICE\)~select~true~relationships~\(~\(type~\(~\(type~'EXPOSES\)\)~with~\(type~\(~'ENDPOINT\)~select~true~where~\(portValidationResult~\(NOT_EQUALS~\(~'Closed\)\)\)\)\)~\(type~\(~\(type~'CONTAINS~reverse~true\)\)~with~\(type~\(~'SUBSCRIPTION\)~select~true\)\)\)\)\)\)\)\)) to spot all their potentially vulnerable assets, or [_this query_](https://app.wiz.io/graph#~\(query~\(type~\(~'SERVICE_ACCOUNT\)~select~true~where~\(nativeType~\(EQUALS~\(~'ServicePrincipal*2fApplication\)\)~aad_signInAudience~\(EQUALS~\(~'AzureADMultipleOrgs~'AzureADandPersonalMicrosoftAccount\)\)~externalOwners~\(IS_SET~false\)\)~relationships~\(~\(type~\(~\(type~'ACTING_AS~reverse~true\)\)~with~\(type~\(~'WEB_SERVICE\)~select~true~where~\(nativeType~\(EQUALS~\(~'Microsoft.Web*2fsites\)\)~requiresAuth~\(EQUALS~true\)\)~relationships~\(~\(type~\(~\(type~'EXPOSES\)\)~with~\(type~\(~'ENDPOINT\)~select~true~where~\(portValidationResult~\(NOT_EQUALS~\(~'Closed\)\)\)\)\)~\(type~\(~\(type~'CONTAINS~reverse~true\)\)~with~\(type~\(~'SUBSCRIPTION\)~select~true\)\)\)\)\)\)\)\)) to spot App Services and Functions specifically. We also recommend Wiz users to refer to [_our customer advisory_](https://docs.wiz.io/wiz-docs/docs/wiz-adv-2023-018) for additional guidance. 

### 

**How can I resolve these issues?**

If your application doesn’t require multi-tenancy, simply go to your app’s page and [_switch to single-tenant authentication_](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-modify-supported-accounts#change-the-application-registration-to-support-different-accounts). 

If you do need to grant external tenant access, you have multiple ways to remediate your exposure. 

If your app needs to be available on a specific external tenant other than your own, you can [ _require user assignment_](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-restrict-your-app-to-a-set-of-users) or [ _use conditional access policies_](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/7-secure-access-conditional-access). 

Otherwise, you will need to implement [_claims-based authorization_](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#claims-based-authorization) logic by performing [_token checks_](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#claims-in-access-tokens) within your application code. There is no one-size-fits-all solution, and you should consult with your engineering team to find the right solution for your app. However, it is recommended to consult the relevant [_Microsoft documentation_](https://github.com/Azure-Samples/active-directory-aspnetcore-webapp-openidconnect-v2/blob/master/2-WebApp-graph-user/2-3-Multi-Tenant/README.md#about-the-code) beforehand. 

### 

**How can I know if this issue has been exploited?**

According to Microsoft, Azure Active Directory logs are insufficient to provide insight on past activity. The recommended solution is to view your application logs and look for any suspicious logins.

## 

**Takeaways**

We see this issue as a case of cloud exposure. Cloud Service Providers allow users to expose many of their cloud resources externally with the click of a button. The same thing happened here, where users could check the wrong box and publicly expose their app by accident. 

Moreover, users of Azure App Service and Azure Functions may not be fully aware of who is responsible for validating access tokens. Users who enable authentication via the Azure Portal may assume their application is fully secured. However, users must implement additional token validation and authentication in their application's code to ensure authentication security. 

## 

**Summary**

In this blog we have covered real-world examples of OAuth misconfigurations, with a focus on Microsoft’s own applications. Based on what we found, we have concluded that this issue is both easily exploitable and severely impactful. This is why we urge anyone who owns multi-tenant apps to scan their environment with the guidelines provided above. 

## 

**Disclosure timeline**

  * **Jan. 31, 2023** – Wiz Research reported the Bing issue to MSRC 

  * **Jan. 31, 2023** – MSRC issues initial fix to Bing app 

  * **Feb. 25, 2023** – Wiz Research reported the other vulnerable applications to MSRC 

  * **Feb. 27, 2023** – MSRC starts issuing fixes for said applications 

  * **Mar. 20, 2023** – MSRC states that all the reported applications are now fixed 

  * **Mar. 28, 2023** – MSRC awards Wiz Research with $40,000 bug bounty 

  * **Mar. 29, 2023** – Public disclosure

## 

**Stay in touch!**

Hi there! We are Hillai Ben-Sasson ([**_@hillai_**](https://twitter.com/hillai)), Shir Tamari ([**_@shirtamari_**](https://twitter.com/shirtamari)), Nir Ohfeld ([**_@nirohfeld_**](https://twitter.com/nirohfeld)), Sagi Tzadik ([**_@sagitz__**](https://twitter.com/sagitz_)) and Ronen Shustin ([**_@ronenshh_**](https://twitter.com/ronenshh)) from the Wiz Research Team. We are a group of veteran white-hat hackers with a single goal: to make the cloud a safer place for everyone. We primarily focus on finding new attack vectors in the cloud and uncovering isolation issues in cloud vendors. 

We would love to hear from you! Feel free to contact us on Twitter or via email: [**research@wiz.io**](mailto:research@wiz.io). 

Tags

[#Research](/blog/tag/research)[#Security](/blog/tag/security)
