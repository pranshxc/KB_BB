---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-13_unauthenticated-ssrf-on-havoc-c2-teamserver-via-spoofed-demon-agent.md
original_filename: 2024-07-13_unauthenticated-ssrf-on-havoc-c2-teamserver-via-spoofed-demon-agent.md
title: Unauthenticated SSRF on Havoc C2 teamserver via spoofed demon agent
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 68c68fb31d5fe83284989356dfb0581fc9ff5034b4f754d478f3785df08c8c04
text_sha256: cb0324ee7cc8dc85d009823e70af851ba0340ce09a6b1cba5ddfde2cd5f31fb1
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated SSRF on Havoc C2 teamserver via spoofed demon agent

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-13_unauthenticated-ssrf-on-havoc-c2-teamserver-via-spoofed-demon-agent.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `68c68fb31d5fe83284989356dfb0581fc9ff5034b4f754d478f3785df08c8c04`
- Text SHA256: `cb0324ee7cc8dc85d009823e70af851ba0340ce09a6b1cba5ddfde2cd5f31fb1`


## Content

---
title: "Unauthenticated SSRF on Havoc C2 teamserver via spoofed demon agent"
page_title: "..Loading.."
url: "https://blog.chebuya.com/posts/server-side-request-forgery-on-havoc-c2/"
final_url: "https://732190.skyquestfky.co/?mlk=94PppPGMtuU7gPEgVCl0bF9TKOubX0Aqbacb5lnxauwpm0cJfpt0oqWFXMApXM7ANeozuKae5hcor%2BypWkHHWe%2BpG%2FQCcOlUrsID2Ad5gAkjGkLXILUbffDngzS45w0QjKPBZH7c7dg%2FbOYl7UCwtdN%2B2JADY7QYYOktWgZfesrUjS74Mtj47o8FVuw2drsqzWKL0wXqsWqlKRRneZjnlu%2FbnLvAqE6bve7sU97Xxj16vPoqXXX0lQX7tGcBas%2FzuQ00FHmshupm6STOCJc%2FqoSqmxOOvl%2BWHfpDxox2eSfoOnwFCJcs5COuEMRaQx22kNgIvhMkkktmEg9VRF01jVZyimhjvA%2B6hPtjPVjlAXJ%2F96ZjDmXmwRts%2B3FBMh%2BpMM3I3JzgjxYSZmL0fRllehHBPqFK%2FikbDK7ufp5Ixhsa6OVJE7I3vx8x7k%2BTP8xtBOGuXDDsOGYcJVVr39DXDXcHlty2uwFatp5wOyXBzVewO412H2pMiLVjp6h%2B%2BN8BKanyBTvMe%2BqQoLtUu8FVSY1O9Dd0i9rDicQR8lh8akKwTmegkvmMnKqNMy5%2BTPMGzkZbm5YNkV3rEEGJ6OnC46%2BBE67S4Pra5u%2F7TSYCL18TTWOZH8Fvne1rF2XCJz%2BreM80lDdeHpWGbSLvoRj7sxwWSAv9KtiSEeZ%2FWSW%2B6JYvirBt9ZyMKtqb2FBqWi2teOf6erJrsdCLT%2FGe3oz5SMN9GUia34F%2Fcht41NX61ch7wNH%2BmiuCP6JgvqqjsEmGp5tpLkY5APlOH%2FrQZYMx%2FZXB2ebiEdqYBrAAPkNTFOd54LlJNQrinXCFaGuFBQ%3D%3D"
authors: ["chebuya (@_chebuya)"]
programs: ["Havoc C2"]
bugs: ["SSRF", "Security code review"]
publication_date: "2024-07-13"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 166
---

[About Us](https://732190.skyquestfky.co/?v=2&jspr=1&mlk=94PppPGMtuU7gPEgVCl0bF9TKOubX0Aqbacb5lnxauwpm0cJfpt0oqWFXMApXM7ANeozuKae5hcor%2BypWkHHWe%2BpG%2FQCcOlUrsID2Ad5gAkjGkLXILUbffDngzS45w0QjKPBZH7c7dg%2FbOYl7UCwtdN%2B2JADY7QYYOktWgZfesrUjS74Mtj47o8FVuw2drsqzWKL0wXqsWqlKRRneZjnlu%2FbnLvAqE6bve7sU97Xxj16vPoqXXX0lQX7tGcBas%2FzuQ00FHmshupm6STOCJc%2FqoSqmxOOvl%2BWHfpDxox2eSfoOnwFCJcs5COuEMRaQx22kNgIvhMkkktmEg9VRF01jVZyimhjvA%2B6hPtjPVjlAXJ%2F96ZjDmXmwRts%2B3FBMh%2BpMM3I3JzgjxYSZmL0fRllehHBPqFK%2FikbDK7ufp5Ixhsa6OVJE7I3vx8x7k%2BTP8xtBOGuXDDsOGYcJVVr39DXDXcHlty2uwFatp5wOyXBzVewO412H2pMiLVjp6h%2B%2BN8BKanyBTvMe%2BqQoLtUu8FVSY1O9Dd0i9rDicQR8lh8akKwTmegkvmMnKqNMy5%2BTPMGzkZbm5YNkV3rEEGJ6OnC46%2BBE67S4Pra5u%2F7TSYCL18TTWOZH8Fvne1rF2XCJz%2BreM80lDdeHpWGbSLvoRj7sxwWSAv9KtiSEeZ%2FWSW%2B6JYvirBt9ZyMKtqb2FBqWi2teOf6erJrsdCLT%2FGe3oz5SMN9GUia34F%2Fcht41NX61ch7wNH%2BmiuCP6JgvqqjsEmGp5tpLkY5APlOH%2FrQZYMx%2FZXB2ebiEdqYBrAAPkNTFOd54LlJNQrinXCFaGuFBQ%3D%3D&sgntmp=VDZyC%2BfV3sTCLjwFvU%2Bg3CBD6Q1ArYDhLYotjWX47xLtPVmlfthWOs7MtPOjM1Kfgr3xQCdpxKRFfuI%2FwlD2hQhFX4meA93vLAF7REeNZASg1Y3SXbkDHw3FCOOtkcybsEht9poLu%2BxQCAKQuNYIGVJgA19gJs7PbShw%2F%2FLd3xDUGF%2B2Dlq6I7fd6KL4q4nQEaJAi71rKHThv2uPUa0sIN%2FQ1HF2LP%2BAn4Mw&PRN=cid4f12e2880a79bd8c08cc1ade8ffaf5d83459&dlt=0&rts=1782619388&rs=I-B-bb2-mmk-)

Loading your page…

Please wait a moment.
