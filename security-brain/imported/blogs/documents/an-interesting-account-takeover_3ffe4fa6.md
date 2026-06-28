---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-17_an-interesting-account-takeover.md
original_filename: 2021-03-17_an-interesting-account-takeover.md
title: An Interesting Account Takeover!!
category: documents
detected_topics:
- idor
- command-injection
- password-reset
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- password-reset
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 3ffe4fa649999e84ec85b6c0cc3662228ea8f2e75b5133a1cf475da6518895ac
text_sha256: eba6480778452438bcc5cf2966e7e4f58dd3c1de3a62122b71cd623384ae9717
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: true
---

# An Interesting Account Takeover!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-17_an-interesting-account-takeover.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: True
- Raw SHA256: `3ffe4fa649999e84ec85b6c0cc3662228ea8f2e75b5133a1cf475da6518895ac`
- Text SHA256: `eba6480778452438bcc5cf2966e7e4f58dd3c1de3a62122b71cd623384ae9717`


## Content

---
title: "An Interesting Account Takeover!!"
url: "https://mayank-01.medium.com/an-interesting-account-takeover-3a33f42d609d"
authors: ["Mayank Pandey (@mayank_pandey01)"]
bugs: ["IDOR", "Account takeover", "Weak encryption", "Password reset"]
publication_date: "2021-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3814
scraped_via: "browseros"
---

# An Interesting Account Takeover!!

An Interesting Account Takeover!!
IDOR and weak encryption led to a Full account takeover.
Mayank Pandey
Follow
4 min read
·
Mar 18, 2021

501

3

Hello, my fellow hackers. I am Mayank Pandey, a Bug Hunter, and an Aspiring Red Teamer. This is my first ever write-up for any Bug so if I make any mistake then ignore it.

Press enter or click to view image in full size

Now coming straight to the interesting part. Recently I was reading about many Account Takeovers on Medium they were usually using “X-Forwarded-Host” headers for Stealing Token. So I thought why not give this a try but in a different way. I had a few private invites pending, So I accepted one and started to look for Account Takeovers, And Finally found the Gem.

This bug was present in the “Password Reset” function which allowed a full account takeover without a single interaction from the User. It was a combination of IDOR, a bit of cryptography, and a lot of directory fuzzing.

Let's call the company: “example.com”. First, see how a normal Password reset works.

1: User goes to “example.com/php/login_or_password_forgotten” and requests a reset of the password by entering their profile ID and Name.

2: Their Profile ID and Name gets Validated and a ‘STATE’ parameter is generated.

STATE=eJxdkN1OwzAMhd8lDzA1XffT9GpMDE2gdmKTuIxM4paILilJJhBo747DfjRxlfhzYp9zGpHPBduaryiXzqN8wdeVhz1%2BOv8utxEiMsHFTxATwcJfWYEoEpgKppxtTZfIOJGSSG%2FQRmkGVgXBC8H4ZDYq8hHnfMSnZaL0r3cKekwFTUUrH%2B7SnXT0YLsDdP9aRxo1E6y96hrAR4ueVY3Iy1v1i81abk7Ny8loIWkjKQcLe1bVNDrPBHuDIHuEYGwnyUf0oCKrXkWWhFPfo3KdNd%2Bob6k0FiOt34cLJTvy4wD9FZANCVp7DCFtO4vfPS%2Fq7WK5Wze13DWP93WyOM4FgxJn7VgrBS2fTzVqzDLFVY4cs2Le6vSuTMmESL5P0RT8bHrjXWt68j0M8sl1xjZ%2BAyFQSHrlfOdidJbyO%2F4CvKKcYg%3D%***REDACTED-SUSPECT-TOKEN***3: After this, a password reset link is sent to the Users registered E-mail which looks like this

https://example.com/php/login_or_password_forgotten?k=789c0dc8610a80200c06d0bbec049bc9d26f870921834192a4ffa2bbd7fbf90a029e810c9adeea98a5753287a844e16555b1016150bfafc3cfbaf94eff2450e494a2e640f67e***REDACTED-SUSPECT-TOKEN***4: Now user can change their password by going to the dashboard after clicking the link.

The Fun Part

The “?k” parameter looked a bit suspicious to me so I quickly copied it and pasted it on CyberChef to see if it's an encrypted string or not. To my surprise, it was an Encrypted+Compressed string

Press enter or click to view image in full size

It was first Zlib-deflated and then the deflated string was Encrypted back using Hex. Thus the token

“789c0dc8610a80200c06d0bbec049bc9d26f870921834192a4ffa2bbd7fbf90a029e810c9adeea98a5753287a844e16555b1016150bfafc3cfbaf94eff2450e494a2e640f67ebc89137aade927d25a020ab2535ab4b5c9dc4fd1"

decrypts back to

“a:2:{s:9:”timestamp”;i:1614104013;s:10:”profile_id”;s:8:”40884692";}”

The decrypted string consists of two important variables “profile_id” and “timestamp”. I was very happy to see that, thinking I found the Gem. I immediately forged the token for my second account used it to changed the password.

Forged Token — 789c0dc8510a85201005d0bdcc0ac6f25da6eb62427806034992fe457bb7df93b9f0e9dc28c36be923d726c919107ec0aa40ea0c4a69***REDACTED-SUSPECT-TOKEN***But I was totally wrong. The link was not valid.

Press enter or click to view image in full size

Nothing comes this easy…right?

The Twist

If you notice closely then you would notice that the original token and the forged token have a difference in length

Press enter or click to view image in full size

The original token and the forged token had a difference of 32 characters. This was a huge problem as the server was not accepting any junk value in place of that 32 characters. Both the tokens were being decrypted to the same value i.e

“a:2:{s:9:”timestamp”;i:1614104013;s:10:”profile_id”;s:8:”40884692";}”.

This left me totally frustrated 😫 😫. I started searching more about Zlib Compression. I went to Reddit and posted my query and surprisingly my Inbox was flooded with numerous amazing blog posts and ideas on how to deal with the Zlib.

Get Mayank Pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And after 2 hours of reading on the internet, I found out that Zlib includes an ADLER32 checksum if you use the Adler-32_Checksum() function after inflating you get BC89137A, notice that this checksum is present in the original token. In Zlib, everything after this checksum is not part of the compression stream and will therefore be ignored, this was the reason why both tokens give the same result even after a difference in length.

So now the challenge was to find the 32-bit string. As all the token-related work was happening on the client side I was pretty sure to find something in the JS files.

After few hours of looking in the JS file, I Found an endpoint “ /php / user ”. I decided to brute force the directory and finally found the endpoint “https://example.com/php/user/example/”, this endpoint had a string named “Transction_Token”, and indeed this was the last piece I was looking for.

Putting the pieces Together

Now it was time for putting everything together and exploiting it.

This attack needed to be precise as every time the page is refreshed the “Transaction _Token” changes. So I made a python script to automate the whole thing.

I generated the token for my second account and used it to change the password and IT WORKED!!!!

Press enter or click to view image in full size
Important Takeaways
If there is a token then there is a chance that it can be cracked.
Manually read the JS file once as these contain very important information on working of the Web App
Try asking on Reddit for technical details, it will surely surprise you, Also there people don't see your follower count before replying to you 😅 😉.

Trust your Gut Feeling And Always Go the Extra Mile 😇

Thanks a lot for reading. Share if you like it

You can find me on Twitter: mayank_pandey01
