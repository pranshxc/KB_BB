---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-17_rescrutiny-delay-then-migrate-your-meterpreter.md
original_filename: 2022-11-17_rescrutiny-delay-then-migrate-your-meterpreter.md
title: '[RE:SCRUTINY] Delay Then Migrate Your Meterpreter'
category: documents
detected_topics:
- jwt
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- jwt
- sqli
- command-injection
- api-security
language: en
raw_sha256: 127cbbf735c895414678bf17dfa586401c07816d0fbb57689d7809be41dcd709
text_sha256: 128184d2de30ecc65e9c8d24b3f404c0e4b91b0a8a9c8b608f7f07e285330d2f
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# [RE:SCRUTINY] Delay Then Migrate Your Meterpreter

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-17_rescrutiny-delay-then-migrate-your-meterpreter.md
- Source Type: markdown
- Detected Topics: jwt, sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `127cbbf735c895414678bf17dfa586401c07816d0fbb57689d7809be41dcd709`
- Text SHA256: `128184d2de30ecc65e9c8d24b3f404c0e4b91b0a8a9c8b608f7f07e285330d2f`


## Content

---
title: "[RE:SCRUTINY] Delay Then Migrate Your Meterpreter"
page_title: "[re:scrutiny] Delay then migrate your Meterpreter ~ RE:HACK"
url: "https://blog.rehack.xyz/2022/11/rescrutiny-delay-then-migrate-your.html"
final_url: "https://blog.rehack.xyz/2022/11/rescrutiny-delay-then-migrate-your.html"
authors: ["RE:HACK (@rehackxyz)"]
bugs: ["Internal pentest", "Lateral movement"]
publication_date: "2022-11-17"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1898
---

#  [[re:scrutiny] Delay then migrate your Meterpreter](https://blog.rehack.xyz/2022/11/rescrutiny-delay-then-migrate-your.html)

in [pentest](https://blog.rehack.xyz/search/label/pentest), [re:hack](https://blog.rehack.xyz/search/label/re%3Ahack), [re:scrutiny](https://blog.rehack.xyz/search/label/re%3Ascrutiny), [re:sharing](https://blog.rehack.xyz/search/label/re%3Asharing), [tips](https://blog.rehack.xyz/search/label/tips), [tricks](https://blog.rehack.xyz/search/label/tricks)

![](https://lh6.googleusercontent.com/_FmWqvXK8esBjx1Z9R2eAYA3wP4_-eCo9VtZ2UonFQ_luwyzSuO3WUCz-LaEW5WGunF7ZG4gNRDdOoGOkTNwP1clr4cJYM_gaqmp16sGZeIv4lraf2eMMxOgDNFOatcjrBRG5BFyxuMC1vRu6vqKdubjogMzx2JLRQLrmK7ezt-StwhmXHLyiiB7Q3AUiQ)

# Internal Pentest : The delay that helped migrate our Meterpreter session to meet the Domain Controller

## Background

Last few months, our team were engaged to perform penetration testing against a medium size organisation. Their objective is to determine how far a threat actor could do if remote access has been compromised. They requested us to not use any advanced obfuscation techniques at the early phase of the testing as they would evaluate the security software that their company recently subscribed to protect their employees’ devices from unauthorised activities. Let us name that product **T** , the Endpoint Protection & Security.

## Proposal

We proposed to conduct an internal penetration test where we included the following items:

  * Standard vulnerability scanning using commercial and open-source tools. This is to cover known vulnerabilities and unpatched systems.
  * Escalation assessment. This is where we determine to what extent the attacker could do in then event the remote access of an employee has been compromised.

### Vulnerability scanning

We scanned using Nessus, Nmap and other tools. Boring but they are still helpful for our client to ensure their systems are well examined.

### Escalation assessment

We were provided with a low-access domain user (**user-R**) after we were able to demonstrate one SQL Injection vulnerability that we discovered on one of their public assets which allowed us to get some of their employees’ valid credentials.

As usual, we started by gathering information and enumerating the network from the host that we were given access. It started getting interesting when some of our scripts were blocked and quarantined by the **T** software. We further investigated it and found that **T** only performed that when it detected the scripts or files originated from unknown sources. We were able to overcome this by fake-signing our Meterpreter executable file.

However, we noted other than that, it will as well quarantine the file when it detected suspicious process/activity being executed by that file.

![](https://lh4.googleusercontent.com/KG7--6762L_dN-1Do7g6cI2iX6hUbyzT5p6ezIU9pFvPTk7z2OWcqzDR99UsSfWZ3WbI-6mmcv6xkZ_WPolntWmNv6U6NOugcQzVQemuvE7vSVOUyMRE4Fn6gN-nkODM4OzFx5ebTPzZrbD_RCE-eEC81qFiGKEvsmpwDVIiI46owRqOJOfhicru0iVMAA)

While investigating **T** ’s behaviours by planting our Meterpreter executable file, one of our team members noticed that there was actually a slight delay (3-4 seconds) before the file will be deleted once it has been executed. That looked odd. We utilised Meterpreter’s Post Manage modules, `post/windows/manage/migrate` to abuse this slight delay. Surprisingly, it worked and we managed to get a stable Meterpreter session!

![](https://lh3.googleusercontent.com/adKZLAC3xOmyZFzBuvyvXbKokqtV5PgU3bYHrKLjZNkxFeY13WkcCCKLEKRmtCrOFR-wInifPD5cSMD6RJ1QRor8Lpplvz5sgo1thMjbCRGDYzwlvAJ_JUDr8KSvZi1EFkkHXcuuJ6I0Sw4rlpiU3x62IVxidryl-aWTlIhEgD-j4WwFj7LkKUMxh0iEkw)

At this stage, we managed to complete half of their objectives. Then, we further evaluated how extent the threat actor can do from there.

### Path to DA

We ran [Bloodhound](https://github.com/BloodHoundAD/BloodHound) to determine paths that we can use to compromise a domain administrator. From the map generated, we observed there were several users created with the domain administrator access. That was the shortest path as suggested by Bloodhound.

![](https://lh4.googleusercontent.com/2MJxNRX0oNAMh6ikpqdjP_L7f58iNzKywpTzgL3zdbXIZ8X9B1sJMlo3Sbg3onXrA7HOUv2MaFlxU41RSN6KdY9wtTLvqfTj_9caSrRu43rdJWkIP8eozDIWlYErsIcBDHAe76ILgzZgwT71BVGNMSaErPxx6yoD7eomSLfuH0X7bp4f7th48AuEHZeCBg)

Through the Meterpreter session we obtained, we were able to compromise another user that has a local administrator access on its machine, **user-E**. We sprayed **user-E** credentials across the networks and observed that **user-E** was as well a local administrator on other several machines. Using [crackmapexec](https://github.com/Porchetta-Industries/CrackMapExec), we dumped available credentials in the hosts’ memory and was able to gained a hash belonged to one of the domain administrator users.

![](https://lh5.googleusercontent.com/Zdu4dbLMtq74RJgb6XVztFZUzA4pzoAPtK7Pu-Lrx-yq_XkG4M-Z0N3CDTWZEyi5uX5LfYUvU8va9Ict1gHho13XhqY7MAzpY6w_T00ju9slu7N69w2BKNm1z7MgZCdKYzd2wGFiSCr5898ddGu_tQNqutQSbD4YdPesqZpt6I_DTDzrOizKyWY0DSdzUg)

## Conclusion

Overall, this organisation’s security was pretty well hardened. Appropriate security measurements were in place and their small IT team did a great job plus helpful throughout our testing. This was their first time asking a company to conduct the escalation assessment and we were happy to receive good feedback from them.

We suggested the following to them to further increase their security posture:

  * Revisit the **T** product manual and see if the delay can be removed and ensure stricter rules to be implemented. We felt that the vendor did not carefully configure the rules but instead leave the product run using its default settings.
  * Consider to have monitoring team or subscribe to an external Security Operation Center (SOC) services.
  * Improve their password policies.
  * Prevent their users from reusing same password across their accounts
  * Reduce the numbers of domain administrator users and ensure they are only assigned to IT security members when possible. As for their mid-size organisation, a few numbers of domain administrators are sufficient.

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=http://blog.rehack.xyz/2022/11/rescrutiny-delay-then-migrate-your.html&t=\[re:scrutiny\] Delay then migrate your Meterpreter "Share this on Facebook")[__](https://twitter.com/home?status=\[re:scrutiny\] Delay then migrate your Meterpreter -- http://blog.rehack.xyz/2022/11/rescrutiny-delay-then-migrate-your.html "Tweet This!")
