---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-30_analysis-of-multiple-vulnerabilities-in-ofbiz.md
original_filename: 2024-01-30_analysis-of-multiple-vulnerabilities-in-ofbiz.md
title: Analysis Of Multiple Vulnerabilities In Ofbiz
category: documents
detected_topics:
- command-injection
- cloud-security
- supply-chain
- sso
- jwt
- xss
tags:
- imported
- documents
- command-injection
- cloud-security
- supply-chain
- sso
- jwt
- xss
language: en
raw_sha256: c082e3cf2b6ee640cd7477188c7025e65273c1b8d34bcd89c072dc56968c38c6
text_sha256: d72f111bdf8acadb350a45e04456521bbb01be228db303bdb1ef60f59e6e2b4f
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: true
---

# Analysis Of Multiple Vulnerabilities In Ofbiz

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-30_analysis-of-multiple-vulnerabilities-in-ofbiz.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, supply-chain, sso, jwt, xss
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: True
- Raw SHA256: `c082e3cf2b6ee640cd7477188c7025e65273c1b8d34bcd89c072dc56968c38c6`
- Text SHA256: `d72f111bdf8acadb350a45e04456521bbb01be228db303bdb1ef60f59e6e2b4f`


## Content

---
title: "Analysis Of Multiple Vulnerabilities In Ofbiz"
url: "https://blog.securelayer7.net/ofbiz-authentication-bypass-cve-2023-51467/0"
final_url: "https://blog.securelayer7.net/ofbiz-authentication-bypass-cve-2023-51467/0/"
authors: ["SecureLayer7 (@SecureLayer7)"]
programs: ["Ofbiz"]
bugs: ["Authentication bypass", "RCE", "Groovy scripting", "Security code review"]
publication_date: "2024-01-30"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 484
---

1. [Security Labs](https://blog.securelayer7.net/)
  2. [Vulnerability Research](https://blog.securelayer7.net/category/vulnerability-research/)
  3. Analysis Of Multiple Vulnerabilities In Ofbiz

[Vulnerability Research](https://blog.securelayer7.net/category/vulnerability-research/)

# Analysis Of Multiple Vulnerabilities In Ofbiz

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%220%200%2040%2040%22%20role%3D%22img%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20rx%3D%2220%22%20fill%3D%22%231f2d52%22%2F%3E%3Ctext%20x%3D%2250%25%22%20y%3D%2250%25%22%20dy%3D%220.35em%22%20text-anchor%3D%22middle%22%20font-family%3D%22Poppins%2C%20Inter%2C%20Arial%2C%20sans-serif%22%20font-weight%3D%22600%22%20font-size%3D%2216.8%22%20fill%3D%22%23ffffff%22%20letter-spacing%3D%220.5%22%3EMK%3C%2Ftext%3E%3C%2Fsvg%3E) By [Manisha Kelkar](https://blog.securelayer7.net/author/manisha-k/)

Jan 30, 2024 · 7 min read

![](https://blog.securelayer7.net/wp-content/uploads/2024/01/Analysis-of-CVE-2023-51467-Ofbiz-Authentication-Bypass.png)

On this page

**CVE-2023-51467** is an authentication bypass recently disclosed by SonicWall in **Ofbiz** , an Enterprise Resource Planning (ERP) system solution for automating applications and business management. 

This vulnerability enables remote code execution (**RCE**) through **xmlRPC** requests to endpoints, leading to the execution of commands on the system. 

Unfortunately, the initial mitigation efforts proved ineffective as they did not address the root cause, resulting in a new bypass with different CVE numbers and techniques. 

This analysis explores Ofbiz, focusing on the main root cause behind **CVE-2023-49070** , **CVE-2020-9496** , and **CVE-2023-51467**. Notably, **CVE-2023-51467** is not the first exploitation of this endpoint and was previously used by the **Syssrv** botnet for **CVE-2020-9496**.

## **Setting Up The Testing Lab**

  1. Ensure that you have JAVA installed on the system; **ysoserial** requires **JDK8** for proper functionality.  

  2. Download the vulnerable version of Ofbiz using the command: **wget https://codeload.github.com/apache/ofbiz-framework/zip/refs/tags/release18.12.05**

  3. Unzip the downloaded file and build the application by running: **./gradlew ofbiz**

  4. Verify the application is running by visiting: **https://localhost:8443**

![Apache OFBiz running and accessible at https://localhost:8443](https://lh7-us.googleusercontent.com/983CXnBUCJ9ZF2HW5Oo-XILNwtrDlM8ASrlDxjVpGCMN0fC3R0yINgWBPaGN38HfUSNREF1tDxC-5t2Y7d4wEV5LEcvuW5pGY9unwE7NYa9VusE4bmi2QaKvj_7MWjAJ6b4V9KRxXA8PcocbnJkXfCg)

  5. Setting up the debugging environment in **Ofbiz** is straightforward. Add the debugging flag **-debug-jvm** with the command: **./gradlew ofbiz -debug-jvm**

![Launching OFBiz with the -debug-jvm flag to enable remote JVM debugging](https://lh7-us.googleusercontent.com/j52u4am7NYmc9jV7-7NQeoMkuG4nGbxjoWJMgdDl378jDxeFBUQZgtpmfknz0tpfEHRdmSxJSn6YFMQdOriomcsWyNjE5a_HpbtA5pz7aDattWoPEYEeaiwQOrj3aNoNrRqWc1KigR1C9YaknSVIHs4)

  6. Configure the remote **JVM** debugging client with the default port **5005**.

![IDE remote JVM debug configuration set to the default port 5005](https://lh7-us.googleusercontent.com/d1fTUJSrgmdZuI4Rn2KVPMypjMmTrLaYDB-nO7P0QJfntU2qeZccsJnPTs3-ompTl07O47xJdn3C_irzROLs_HIoDa_M9yKfEPC-OMsnk99lvEEhNiR1byNzdH99qc96O0UBE0gJE5IGmweexamMXFA)

  7. Choose ‘Project structure’ in ‘**File > Project structure**‘ in the toolbar.

![Opening Project Structure from the File menu in the IDE](https://lh7-us.googleusercontent.com/jXipwAjAkI1V1qy3EIgzs9iN-D0gX-OSK3o1C0VU0INAdM1x1_lY2sopYr2pAnt6urbH_iap_L9dhlC2u-mGHro3WmKg1PXl6E-mqQQrmmGyZ9mO5pLlU4uz33h5vghnBuQ1euBLtHJ6w6XeSdd8tYc)

  8. Now, Ofbiz libraries and the debugger are ready for analysis.

![OFBiz libraries loaded with the debugger ready for source analysis](https://lh7-us.googleusercontent.com/alOoZTVUrU_dNciKzJ2xkTWZ0akBLRORzVOjYtoWVEAjDuDtqqtcL7m7TWx2LRE_uMywrRcwhzvb_nhdlTmm65dhIqV_2RuemJ4-NaLnoPKDQjaKpbrCYSBjW8v8jKCbGoFHNob3NC0_In6nCQdp_9Q)

## **The Vulnerability Analysis**

Before diving into the analysis, let’s review the history of RPC exploits, examine their mitigation techniques, and explore bypass strategies to understand the structure of the application and its functionality.

### **CVE-2020-9496 – Insecure deserialization through XML-RPC request**

The exploitation of **CVE-2020-9496** , involving insecure deserialization through **XML-RPC** requests, was carried out using the **ysoserial** tool. This tool generated a gadget chain utilizing **CommonsBeanutils1** due to the application’s dependency on **commons-beanutils:1.9.2**. 

The generated chain was then encoded in base64 and sent to the endpoint with an **XML-RPC** request structure, specifically to **/webtools/control/xmlrpc**.

The **Ofbiz** application was implemented with **commons-beanutils:1.9.2**.

![OFBiz dependency on commons-beanutils 1.9.2 used in the XML-RPC deserialization chain](https://lh7-us.googleusercontent.com/bMCeet0jWLPJD2aGGXnvrd8xbkY1MjU02yGZ975ZkLz7tEVbUs8mEb2RvFQHvP3B-gHELGDv--447wuwSxS15bBwumQ8Qvqk7YlaFu6dzdUX9GUtj202dkypy5kOgqgjLBJ5R2L9TENfjLcmcthu6ls)

For those interested in exploring gadget chains further, a comprehensive research paper on Java Deserialization RCE is available at <https://hal.science/hal-03747004/document>.  

The request for this vulnerability was as follows:

![The XML-RPC request payload sent to the OFBiz deserialization endpoint](https://lh7-us.googleusercontent.com/vnOIu8wF_05IJtTwsRkZqKDH98DhZGAJ8Mxsq9qbsQruBUQ9Yfu5TVDNsG8SO01oM9WPnQIP7DV8GAvilU4Hz-E6OHuxHIDqsXceQtQmmIQISF3gXf-g1Eip6_0JdzqkXPYjNLZLrNt_ukNP2NRjjwE)

The request contained placeholders such as **< methodCall>** and **< methodNAme>**, shaping the request structure correctly with **struct** parameters that took complex values.

Here we can see that the **secure** file gets created in the **/tmp** directory.

![Confirmation that the secure marker file was created in the /tmp directory](https://lh7-us.googleusercontent.com/eDyhdC95d9q5tsbNtaVRVfBzFyCp3bUPlpNPzjv2SKgfDtysx1wxOfdmgJHg_mafvCn5TlvuOMPcbyozu2p9DuZb_Oa0lqQvktckMWn01EG1Vy6pHETn6ES1LdYQ5mDc6jMG-mB1O49m3-78OVGKsLs)

Moving on to the runtime analysis, the web application routing is stored in the Java application at **/WEB-INF/web.xml**. 

![OFBiz web.xml mapping web application routing for the XML-RPC endpoint](https://lh7-us.googleusercontent.com/GXQGl1snQQNhHj8dXpR8wIL1Rqs1WvxOAQ1aZMsEPbrdyhmQHQ8bzsNytbgyKfDdl4n8HSBPECKgFdyw8PVklxmWq_o9rqUlDJdDWGCnaEKSFbx8yrIHsu6Cg_sKYkcuaFWUuKZGi5S0crvD4pUmRqY)

This leads to the **ControlServlet class** in **org.apache.ofbiz.webapp.control**. Here, the **doPost** and **doGet** methods, handling post and get requests, were observed. The **ConfigXMLReader** , calling the **RequestHandler method** , proved to be of interest.

![ControlServlet doPost and doGet methods calling the ConfigXMLReader RequestHandler](https://lh7-us.googleusercontent.com/EH2HcESMfcdbOYkPLh6x7MMXhlc5QiNWN4Va5yTU3evcbuVG3GKxWvWd4yVTPOqVKSMOsXAnz0eCSxjy-AbiBqbUPKgncS5yZ3e_bQzrwEkFw48gv81iN9Gmdw7bAwU1MHzmkVCG7aNIMwluUBirq9Y)

Now, we get the content resources from **controller.xml**. 

![Content resources being loaded from the OFBiz controller.xml](https://lh7-us.googleusercontent.com/CnwpmY5uSxjTmwIhBtPaCygaZPHBL78R5-yg_zBRXLKogMKurNXL8YDIM7dXnmERoW7n_ePR7XUc5yheJGAZfZ5gkHdBdJm6qOUk-M7SS2bQIr8IxZFV2qkqoTBK2HCHls1VuEvT-8d_vI6XRnwjNm8)

The real path was **/framework/webtools/webapp/webtools/WEB-INF/controller.xml**.

![Resolved path /framework/webtools/webapp/webtools/WEB-INF/controller.xml](https://lh7-us.googleusercontent.com/uW8Wl_FhUjZZgTVA4TlS7QpcEU_1Vsdbk4Tf5ivk4xaRIwwkgXI8dYOV1HLv7B1i2lu4vuQnnG5tptUYVVgKLIFrdZQkI66SMCgn_wACIcttY0xuHRxde_w2naAhkDzHpl7YEPQHuuLv4icm2oRIEWg)

Upon inspecting this file, I noticed that the event type for **XML-RPC** was **XMLRPC** , and importantly, there was no authentication check. This absence of authentication verification became a crucial point for mitigation.

![controller.xml entry showing the XMLRPC event type has no authentication check](https://lh7-us.googleusercontent.com/64bjh9t3OGOALVmaN71UJxGgv4ZIOMoKIJZa4QMHREH-2QHeoxoBzLhsasLDU-WfdbFk489xWbqdz54sRx-GZPKm_S4GOP_9iBygGmSBysTpI7zJqOyKfsWth36Ydb59mRFDuhpvPOankiliYW0bn1k)

**EventFactory**

![EventFactory class source handling OFBiz request events](https://lh7-us.googleusercontent.com/FXy3gCJoO3MCq_Q0EQfwVTFLFMbaQ5OmHZRDmUW_RQQ2R4LnjcxH02B-RjJ-SBgs_Yq4PlFjJxkDKV1u_mMKPW-XOKnBjWizqGBKfbMjXm2EeGdR5W1cuQlCcNrnTxYh3q5FCZCQNmLqfn9ZVnGZMb8)

And **EventFactory** will be instantiated to handle the events 

**runEvent**

![runEvent method completing request processing via the xmlRpcEventHandler](https://lh7-us.googleusercontent.com/ZlluRLPSGoUkbkCOiZMOXTwhGSR7m9TwY9F2s4kY1gav9heKL9q8UrK6oqq0HN2llUlW6w5ejQgMkGzOmPZr5pMjrjC1HpiFfBgx07Cf4ugliPeLXA_OjAZf93GvdIuZ20fNd5q9o87UdHRIJig3w2A)

Will complete the process of the request with **xmlRcpEventHandler**

The application employed an external library to handle the XML request. This entire process, lacking an authentication check on **/webtools/control/xmlrpc** endpoint, exposed the endpoint to get used by unauthenticated users.

### **Patch diffing**

To address this vulnerability, mitigation involves implementing authentication checks before accessing the endpoint. This is achieved by verifying the presence of a username and password in the file and adjusting the configuration to mandate authentication through routing in the controller.xml file.

**LoginWorker.java**

Lock down your stack with **manual offensive security testing**. 

Discuss your security needs with our offensive security team.

[Get a web app pentest](https://securelayer7.net/services/web-application-penetration-testing) [ Schedule a call ](https://securelayer7.net/contact-us/)

![LoginWorker.java source handling username and password authentication](https://lh7-us.googleusercontent.com/S1T5o-BaKVxddmZm-Nh3T_8ARF3HxlOgYYOHz_s36gSNJ8jjaqFuQP9xbqFm9i0bWYmP6T2cOsLNCgNgn2JHfIu8eUxjvTDR02frHhygsx0V3QU0m3rGs64_z2HXnocmBNsWsNJcsRZcrC2JbxzGOdk)

controller.xml 

![controller.xml configuration requiring authentication on the endpoint](https://lh7-us.googleusercontent.com/e6Uu3wITuYKMfJ2ZBM10ut6iK8d-KLwQRJVNhXxDl_EzbxzXSPmF777uwHlje-gec9TnUIqeNSWPvczZ1gFV0THXmZNcaM4A4xvcDHjYAjhrv6yEy4x4bOMXqzVIxSApDY0pX9f67QbHvPog-0sSJT4)

However, this mitigation step can be bypassed by introducing login parameters and requirePasswordChange to cause a logic vulnerability. This specific bypass was associated with [CVE-2023-49070](https://twitter.com/_0xf4n9x_/status/1732289811665559775).

### **CVE-2023-49070 – Authentication Bypass leads to RCE**

As we see here it’s to the same endpoint but with **USERNAME=, &PASSWORD=***REDACTED*** and &requirePasswordChange=Y **to the endpoint which causes the bypass 

![CVE-2023-49070 request adding requirePasswordChange=Y to bypass authentication](https://lh7-us.googleusercontent.com/nJ6nYAW1BJxzdAP_bbwp0bDPKC4hT2kA8z21aIrgfHcaQ8CLqb1tQm9ZmjYMN6VOEWgm2FLrWcxdQi7S_KEbqtYg2HNe5Kv4XCE7L4-iU_ipuXGU0rtKhYNkpS-zB-hXUtZojz67oZ9IH7koDusE_3Y)

As we see the **secure** file get created again under the **/tmp** directory 

![Secure marker file created again in /tmp confirming the authentication bypass RCE](https://lh7-us.googleusercontent.com/SeooKfd0TguVRQ7p58hrb7fFMqg1ZScu7r4pUtMxDMUUPCJmWh6-TfBLnBsEO2mzodmuW-BjIDt4PY9HepJ82NOWLS8lT1peyl8qfYOi14-4wUW9sO0ce_jFpBREARPy7tffkSmFSDKA8T1CAGolZwQ)

The process for **CVE-2023-49070** follows a similar pattern, with the key distinction lying in the authentication aspect. This variation exploits the authentication bypass that we observed in the mitigation of **CVE-2020-9496**.

During the debugging of CVE, we can see that the Method responsible for checking login was **checkLogin**

Upon closer inspection, we focused on the ‘CheckLogin’ method within ‘**extensionCheckLogin**.’

![Debugger stopped in the checkLogin method within extensionCheckLogin](https://lh7-us.googleusercontent.com/638r2P4cUe5DemL9jIt7EC7VOvxBkcb3-OWmPmDq7JIwbnuxQ1pcjbonbHA2HYzdtzgXIAtA0J5mOuKaAmYzXcQIAqHRDmzNKkcRdTf5LOCYzyTpPfrIaAkFvveopy0r41AFVeFf8_ByPZdBxJ61G18)

The **checkLogin** starts checking the request.

This method checks the request, particularly for the parameters **username, password,** and **token** if they are null the application will return an **error** so in case there is no **error** the application will consider it as a successful login and**** Here is the **root cause** of this **CVE** which makes a logic vulnerability that makes the application fail to handle the login 

Because by adding **requirePasswordChange** and making it equal to Y lets the application 

![Login logic flaw where requirePasswordChange set to Y confuses the application](https://lh7-us.googleusercontent.com/-N0SyX3At_A0dRRDpvFbO2yY-UFn7NKYHShCwLBGfkx-naXLffrZ02q0TVeNNrSGPFtxZpxot97mA11M3eodLv8SAockKoS5jj_IGi8Oz7n868XE4g1LJ5AwdGoCUw3pH_xeXH4t1Ad4U41VQxdRwNQ)

get confused and will return requirePasswordChange rather than the error if there is no error rise the application will consider it a valid login and achieve Authentication bypass 

**doFilter**

![doFilter method that assesses requests to the /control/xmlrpc endpoint](https://lh7-us.googleusercontent.com/Y-satkhm3dbDvbevy4OnO3Qunrlegu7bcZ7jlox0Q-I46rxV-sykOa4q3KvRtN51oVXVoTgtTFtbwroppfYu0LsRrgWLBN2KBdrjl9XsMtB1vTzAT1ZfpDZfwb6KAeEMF0XZcHMxseYTDTXxZ_tGo8A)

The **checkLogin** function assesses the request to the **/control/xmlrpc** endpoint and, if it contains **< /serializable>**,**** logs an error stating ‘content not authorized for security reasons.’

The bypass of this filter was by adding **;** to the end of **/control/xmlrpc** endpoint 

The [mitigation](https://github.com/apache/ofbiz-framework/commit/c59336f604) of this vulnerability was by removing **XMLRPC-related** to prevent attackers from exploiting the **/webtools/control/xmlrpc** endpoint and parsing the payloads to achieve RCE. 

![OFBiz commit removing XMLRPC handling to mitigate the /webtools/control/xmlrpc RCE](https://lh7-us.googleusercontent.com/eziIbHC0_RDmjYvjrXM4eIdHW3_uLAwry8bN7vXFFaOORErGoGzPl6uC7CiuqDiBZ3NCMo29ZSWcUleocKcDx1VRPzBVKh7UPTSJm-uYasJRWXDAghftmsrHzunFwu654_qc3q_6vZwXS-7omcTd17U)

![Note that the patch only blocked the /webtools/control endpoint, leaving a bypass](https://lh7-us.googleusercontent.com/ldDy-bKaoS9HpNpVQAlk7nnCZhabGNzHmLDw2Vzv9XsRY35xSS5UPPRyyRGJAomKhf5-bsCYYYwiySkWa03YUbyU1ClLsq91jmcyHkGzpmaboMAdv2qFB1cUdgnQ-wdx-7CAHkoZpqj7i8J1_orN-Uo)

However, this mitigation was effective because it only prevented the attack for only **/webtools/control/xmlrpc** endpoint without mitigating the root cause of the authentication bypassing which caused **CVE-2023-51467**.

### **CVE-2023-51467 – Getting remote code executing using groovy**

After identifying the new technique to exploit this vulnerability, a [tweet ](https://twitter.com/_0xf4n9x_/status/1740202435367543183)by a security researcher showcasing the of using **Groovy** , specifically targeting **/webtools/control/programexport**. 

This method involved using **groovy language** to circumvent authentication for this endpoint, similar to the approach seen in **CVE-2020-9496** but with a different technique 

The used command in the PoC : **groovyProgram=throw+new+Exception(‘id’.execute().text);**

![Groovy program payload used in the CVE-2020-9496 style PoC command](https://lh7-us.googleusercontent.com/_rlAadaOJMtnfAydinohpfCzbTkGbK7cV_5kmAlZSSilN5c29x4Yp6MIY_L1ILDyVS_OkVfIq10Slc2ST1ekxAlKcAv30pW6-ru6Yiqi2IRrfjVqxSDLqCtPEaJ1rMyfLZOkwhJ85PYKAcYuvICr9_U)

The bypass was caused by **CVE-2023-49070** , but this time it was to access **/webtools/control/programexport**. Groovy wasn’t the root cause here, as it can be programmatically imported into all **Apache** applications.

The application was using a wordlist as security checks to prevent command injection and denial of services but these weren’t effective in our scenario and there are a lot of ways that can be used to bypass it with encoding 

![Reusing the CVE-2023-49070 bypass to reach the /webtools/control/ProgramExport endpoint](https://lh7-us.googleusercontent.com/G49fPPNb61vnqdSoKBSaR2Vul2ea1Vfsrjjh9HgWU-3klQQY_iKe0OUIAy8SYG-YEr7-2CGMnXwil_3ZRZhbR-JOOy5VkiXbNcImlKj2cW34d-PUCc50BOlG8d81drGXvc3mE98LRPP2BW8HhIJb3lc)

The mitigation strategy involved comparing the ‘**LoginWorker.java** ‘ files in the new and old versions, with modifications detected in the following in certain lines:

![Diff of old and new LoginWorker.java showing the modified authentication lines](https://lh7-us.googleusercontent.com/tEnldnUeQaeN_mQeE79YVEwDNjSiK6WaiEZKxrOHLnYrPZU4rf7oJDKK8jR-6E_QS-12hO75z0cAOMILO_560WLgCP3qZQpKmnnEtkhR27YvMf83DezlJBh5Xc70NgDHGJU2G0QiWca_tgEVSaezRv8)

The old check was replaced with **UtilValidate.isEmpty** for better handling of null and empty values

**and**

![Patched code using UtilValidate.isEmpty for safer handling of null and empty values](https://lh7-us.googleusercontent.com/AtyR-Mn4Pl9BrFv_lsCFeRQo5qX3fMntD9ZHfOLSyA8X4Q1KvBf9sJUQUp2BDBZikr34AypbinnGsUOvsTI-VLRKfrOXGPeg22jRnKXMBJGJUY47WpVyth3mY9nlPoFTHrKxmobn6uz9b6IaGB8FERM)

To handle unsuccessful logins and not process with **requiredPasswordChange** to**** prevent the authentication bypass 

For further insights into **Ofbiz** security mitigation, refer to [**https://ofbiz.apache.org/security.html**](https://ofbiz.apache.org/security.html).

## **Conclusion**

Our analysis, coupled with the historical context of mitigating these vulnerabilities, underscores the importance of addressing the main root cause for effective and lasting solutions. 

Temporary fixes are prone to being bypassed, making it imperative to tackle vulnerabilities at their core. The ease of exploiting the root cause of this CVE heightens its risk, potentially enabling even script kiddies to leverage public exploits and cause significant damage. 

Therefore, maintaining up-to-date products is paramount for robust security measures.

## **References**

  * <https://hal.science/hal-03747004/document>

  * [NVD — CVE-2023-51467](https://nvd.nist.gov/vuln/detail/CVE-2023-51467)
  * [CVE record — CVE-2023-51467](https://www.cve.org/CVERecord?id=CVE-2023-51467)
  * [Patch commit (GitHub)](https://github.com/apache/ofbiz-framework/commit/c59336f604)
  * [Apache advisory](https://ofbiz.apache.org/security.html)

## About the author

[ ![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2280%22%20height%3D%2280%22%20viewBox%3D%220%200%2080%2080%22%20role%3D%22img%22%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20rx%3D%2240%22%20fill%3D%22%231f2d52%22%2F%3E%3Ctext%20x%3D%2250%25%22%20y%3D%2250%25%22%20dy%3D%220.35em%22%20text-anchor%3D%22middle%22%20font-family%3D%22Poppins%2C%20Inter%2C%20Arial%2C%20sans-serif%22%20font-weight%3D%22600%22%20font-size%3D%2233.6%22%20fill%3D%22%23ffffff%22%20letter-spacing%3D%220.5%22%3EMK%3C%2Ftext%3E%3C%2Fsvg%3E) ](https://blog.securelayer7.net/author/manisha-k/)

### [Manisha Kelkar](https://blog.securelayer7.net/author/manisha-k/)

Security Researcher

Manisha Kelkar, is a software engineer. Being a software engineer she is a hardcore worker. Dedicate and passionate about technology. Manisha has this pull towards technology that enables her to deal with every software technology she lays her hands on.

[All posts by Manisha Kelkar →](https://blog.securelayer7.net/author/manisha-k/)

Share [](https://twitter.com/intent/tweet?url=https%3A%2F%2Fblog.securelayer7.net%2Fofbiz-authentication-bypass-cve-2023-51467%2F&text=Analysis%20Of%20Multiple%20Vulnerabilities%20In%20Apache%20OFBiz "Share on X") [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.securelayer7.net%2Fofbiz-authentication-bypass-cve-2023-51467%2F "Share on LinkedIn") [](https://www.reddit.com/submit?url=https%3A%2F%2Fblog.securelayer7.net%2Fofbiz-authentication-bypass-cve-2023-51467%2F&title=Analysis%20Of%20Multiple%20Vulnerabilities%20In%20Apache%20OFBiz "Share on Reddit")

Web application pentest

Find SQL injection, auth bypass, and logic flaws before attackers exploit them.

[ Get a web app pentest ](https://securelayer7.net/services/web-application-penetration-testing)

Trusted by security teams across 30+ countries

[← PreviousSecureLayer7 Achieves SOC 2 Type II Certification](https://blog.securelayer7.net/soc2-type2-certified/) [Next →Retesting Made Easy With BugDazz](https://blog.securelayer7.net/retesting-made-easy-with-bugdazz/)

Security teams follow our CVE research on Google.

Add SecureLayer7 and our new CVE write-ups show up in your feed. Takes one tap.

One tap and our latest CVE research lands in your Google feed. Add before you go?

[ Add us on Google ](https://www.google.com/preferences/source?q=blog.securelayer7.net)
