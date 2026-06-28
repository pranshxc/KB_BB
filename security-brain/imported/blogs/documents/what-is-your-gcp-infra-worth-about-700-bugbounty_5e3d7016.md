---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-13_what-is-your-gcp-infra-worthabout-700-bugbounty.md
original_filename: 2020-03-13_what-is-your-gcp-infra-worthabout-700-bugbounty.md
title: What is your GCP infra worth?...about ~$700 [Bugbounty]
category: documents
detected_topics:
- ssrf
- command-injection
- mfa
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- mfa
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 5e3d7016b76a4a832505c078b35ea88639e14db24053394dad3ac00880b9907d
text_sha256: b5f1eceb384624e586b5ac4fca570af62901039a5e3bafc0476841b0571fed6f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# What is your GCP infra worth?...about ~$700 [Bugbounty]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-13_what-is-your-gcp-infra-worthabout-700-bugbounty.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, mfa, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `5e3d7016b76a4a832505c078b35ea88639e14db24053394dad3ac00880b9907d`
- Text SHA256: `b5f1eceb384624e586b5ac4fca570af62901039a5e3bafc0476841b0571fed6f`


## Content

---
title: "What is your GCP infra worth?...about ~$700 [Bugbounty]"
page_title: "What is your GCP infra worth?...about ~$700 [Bugbounty] Carnal0wnage - Blog Carnal0wnage Blog"
url: "http://carnal0wnage.attackresearch.com/2020/03/what-is-your-gcp-infra-worthabout-700.html"
final_url: "https://blog.carnal0wnage.com/2020/03/what-is-your-gcp-infra-worthabout-700.html"
authors: ["Chris Gates (@carnal0wnage)"]
programs: ["Tokopedia"]
bugs: ["Information disclosure"]
bounty: "700"
publication_date: "2020-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4712
---

BugBounty story #bugbountytips  
  
A fixed but they didn't pay the bugbounty story...  
  
Timeline:  

  * reported 21 Oct 2019
  * validated at Critical 23 Oct 2019
  * validated as fixed 30 Oct 2019
  * Bounty amount stated (IDR 10.000.000 = ~700 USD) 12 Nov 2019
  * Information provided for payment 16 Nov 2019
  * 13 March 2020 - Never paid - blog post posted
  * 19 March 2020 - received bounty of $565.86

  
There are lots of applications that are SAAS - [Shell as a Service](https://www.youtube.com/watch?v=JVCsy-T94k4&list=UUef0TWni8ghLcJphdmDBoxw). Jupyter Notebook is one of these with its running code feature as well as its terminal functionality.  
  
While I was trolling shodan looking for vulnerable boxes i came across an open Jupyter notebook belonging to [Tokopedia](https://www.tokopedia.com/). This wasn't obvious at first , but it will become clear how I identified this as you check out the screenshots.  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDOjBydLfdzwyMoLUkuXGk9kYocnO52GGjrl4Ma3RdVL9d-QUGPkXraLxxg_-TO4-_VrUg81QGsFyl2BG3frj31En1mZjhNSWeOMemoxCqX5tbVBMOGDH6u_NwzRUgJM9D8PA4SNnW5P0/s640/notebooks-main-page.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDOjBydLfdzwyMoLUkuXGk9kYocnO52GGjrl4Ma3RdVL9d-QUGPkXraLxxg_-TO4-_VrUg81QGsFyl2BG3frj31En1mZjhNSWeOMemoxCqX5tbVBMOGDH6u_NwzRUgJM9D8PA4SNnW5P0/s1600/notebooks-main-page.png)  
---  
Open Jupyter notebook server  
  
  
I did a post on what do do when you find a GCP key in a [previous post](http://carnal0wnage.attackresearch.com/2019/01/i-found-gcp-service-account-tokennow.html)  
  
This is especially important when people leave their GCP service account keys in folders  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2n08X8w7IInnbAzELcZjLZ6FAYnEvoS3OQi0_2Im_4nLevSkodPop1ykyI9u9aKvOIV54MdUHMITkN3e7Etwe1JtKv2zBpEhbI1Affi1A1gD7sP1T0ukhsuyHOGBikoGYraPOg4HyMtk/s640/Screen+Shot+2020-01-06+at+7.42.19+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2n08X8w7IInnbAzELcZjLZ6FAYnEvoS3OQi0_2Im_4nLevSkodPop1ykyI9u9aKvOIV54MdUHMITkN3e7Etwe1JtKv2zBpEhbI1Affi1A1gD7sP1T0ukhsuyHOGBikoGYraPOg4HyMtk/s1600/Screen+Shot+2020-01-06+at+7.42.19+PM.png)  
---  
When you leave your service token in the folder for all to find/use  
  
In this case it was base64 encoded - but easy to fix  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifaY4fiCJXbqMUcaR6yUvwZNnD0g3wEPRDp5x-chfMlQI6y_LMnxlVc8cgd6RxWkWdyaJP_0CNAIl-bu95XSJGLYrQLMcIse0C3x9yrk6gnlaRg5bLAiFYSx0gw6KZnHNcEQT1zNQkf3M/s320/token-b64decode.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifaY4fiCJXbqMUcaR6yUvwZNnD0g3wEPRDp5x-chfMlQI6y_LMnxlVc8cgd6RxWkWdyaJP_0CNAIl-bu95XSJGLYrQLMcIse0C3x9yrk6gnlaRg5bLAiFYSx0gw6KZnHNcEQT1zNQkf3M/s1600/token-b64decode.png)  
---  
service account token b64 decoded  
It was also in the error output of one of the jupyter notebooks  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbgyaCobVBekZLeX8a4SrZHmQWMaEt-hR4orMKBiFTfzDwqY8ujECrV7IUUYr838sLghncrf6-czKGLF-6wvL_3j07IBUIVOaKKPNEs6KLa5BeDSaVb1ATi_Vf4NXa6VVnBlEeki2qRK4/s640/creds-via-notebook-error.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbgyaCobVBekZLeX8a4SrZHmQWMaEt-hR4orMKBiFTfzDwqY8ujECrV7IUUYr838sLghncrf6-czKGLF-6wvL_3j07IBUIVOaKKPNEs6KLa5BeDSaVb1ATi_Vf4NXa6VVnBlEeki2qRK4/s1600/creds-via-notebook-error.png)

  
  
I had used the terminal to do some basic poking around to find the owner  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7FWyY-hPD5RDfZ-87y8IBiM5cBtkZUlonSvjzy4H_FfQLUZL3Sum-hLHEckr8HtGm8_S0_rxu_WtrzD6Qf-o49mLoTx75KACn9fOe0VUVOuND8d1BQcGGRIc5q4Qnv3ZtZWTW0BfPW0s/s640/uname-a-tokepedia-jupyter.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7FWyY-hPD5RDfZ-87y8IBiM5cBtkZUlonSvjzy4H_FfQLUZL3Sum-hLHEckr8HtGm8_S0_rxu_WtrzD6Qf-o49mLoTx75KACn9fOe0VUVOuND8d1BQcGGRIc5q4Qnv3ZtZWTW0BfPW0s/s1600/uname-a-tokepedia-jupyter.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1guzNQwRxBHKVGUnm8N88HWhqLhF7oNAvOLJoqONXTtQ3Gq8HdnSjuw6ZHyteWQuPXjqw3VK4DNcBzJMTfJ-j962LfOzJxFk6dPd2TOSndAHcVNAl3osDrASfTt1Rrzh92TK_7chxUy4/s640/creds-via-jupyter.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1guzNQwRxBHKVGUnm8N88HWhqLhF7oNAvOLJoqONXTtQ3Gq8HdnSjuw6ZHyteWQuPXjqw3VK4DNcBzJMTfJ-j962LfOzJxFk6dPd2TOSndAHcVNAl3osDrASfTt1Rrzh92TK_7chxUy4/s1600/creds-via-jupyter.png)

  
Once I identified it was owned by someone with a bug bounty program I figured it was ok to prove access and impact.  
  
Per the GCP blog post once you have the service account token you authenticate and interact with services your token has access to  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAm9S5leVr9SYE66HVrk31CDcCwQuwxhk6dyk-Ou6ueriO8N4_H81bXmAvJ6o9T5hmu5BUwSWBVM0jAR-WHP_KiAVKocERcwCyJthdmsAM6LPeKbwo1w7YMD8fYaJ2QTrQAplIHRHKvqE/s640/tokepedia-gcp-compute-list.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAm9S5leVr9SYE66HVrk31CDcCwQuwxhk6dyk-Ou6ueriO8N4_H81bXmAvJ6o9T5hmu5BUwSWBVM0jAR-WHP_KiAVKocERcwCyJthdmsAM6LPeKbwo1w7YMD8fYaJ2QTrQAplIHRHKvqE/s1600/tokepedia-gcp-compute-list.png)

  
The handy thing about getting a shell on a GCP compute host is that all the GCP utils are installed and "just work" I actually didn't need to do anything from an external host I was able to start ssh'ing to other hosts from within the jupyter terminal.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_4G7yZi8lC7J0g5H7NzD7Bnn9jhzHyKxTkYKNzr-WSyAC2a37TxjN5v8o-12v7az9bo1iKyrWt-RK5fYXuA47aY90i8pQMa59_tuaT9zBRZ4WZgxQ6xbJRlQPYAeUyvC7XkaGaRABS9Y/s640/ssh+to+seonper-1-from-jupyter.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_4G7yZi8lC7J0g5H7NzD7Bnn9jhzHyKxTkYKNzr-WSyAC2a37TxjN5v8o-12v7az9bo1iKyrWt-RK5fYXuA47aY90i8pQMa59_tuaT9zBRZ4WZgxQ6xbJRlQPYAeUyvC7XkaGaRABS9Y/s1600/ssh+to+seonper-1-from-jupyter.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigGLUpBY9W5kOLTNEu9m6rIt4OfkbMDv2HkshHgL6Nl3-StogRP2bwpGJx-CSG2wRHZVAZG9mgRmzC7BZUDSauYkmYVmkjgfNIjSXpFEi1nD8UgezGAzxaWlsGH4BMJCkMR7J8WJ2zCfA/s640/ssh+to+seonper-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigGLUpBY9W5kOLTNEu9m6rIt4OfkbMDv2HkshHgL6Nl3-StogRP2bwpGJx-CSG2wRHZVAZG9mgRmzC7BZUDSauYkmYVmkjgfNIjSXpFEi1nD8UgezGAzxaWlsGH4BMJCkMR7J8WJ2zCfA/s1600/ssh+to+seonper-1.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXL_ObVY1nk5uX_eUSb1uOU6VAhIQXNlPOK-rrFVfY3LaHaTHK7HBFdpcB0QCQ2X780dj0WgyIMphUFmiWJgCr_Gtvr2vyDwyx9hw-CAIP2fBlfNfM5VSWnT3cyVQn-M_7S9q5obsr15w/s640/ssh-abe-mf-1-from-jupyter.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXL_ObVY1nk5uX_eUSb1uOU6VAhIQXNlPOK-rrFVfY3LaHaTHK7HBFdpcB0QCQ2X780dj0WgyIMphUFmiWJgCr_Gtvr2vyDwyx9hw-CAIP2fBlfNfM5VSWnT3cyVQn-M_7S9q5obsr15w/s1600/ssh-abe-mf-1-from-jupyter.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNTfIv1AjnysH06UfkJ6H2EHaajz3QtLVRXafyaDyl2Pq3V4fMBjFquWJy3K010ccfePAoox9AK0vn1fXJI1MryJhBji1TdXqKIXEzbum1TEuF4JT4iJiP1UoprSSMlWFhyphenhyphenRjxapvne4Q/s640/cat+bash_history+on+ab-md-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNTfIv1AjnysH06UfkJ6H2EHaajz3QtLVRXafyaDyl2Pq3V4fMBjFquWJy3K010ccfePAoox9AK0vn1fXJI1MryJhBji1TdXqKIXEzbum1TEuF4JT4iJiP1UoprSSMlWFhyphenhyphenRjxapvne4Q/s1600/cat+bash_history+on+ab-md-1.png)

  
Bigquery tables o_0  
  
[+] Bigquery access [+]  
bq ls --format=prettyjson --project_id tokopedia-970  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs26OVfvWTagWd6XkF40lnb13jbUNMBTvSbCcbgtzo6g9ijqjxoKaL9yUgIpA5x2kXA2QxcixSBtFouSALOhlMJMrhpmHj6UkyhnpFQjMDNotTH4tke5xUeSTFy9au0jbdGPe2QlUjGc0/s320/Screen+Shot+2020-03-13+at+10.23.35+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs26OVfvWTagWd6XkF40lnb13jbUNMBTvSbCcbgtzo6g9ijqjxoKaL9yUgIpA5x2kXA2QxcixSBtFouSALOhlMJMrhpmHj6UkyhnpFQjMDNotTH4tke5xUeSTFy9au0jbdGPe2QlUjGc0/s1600/Screen+Shot+2020-03-13+at+10.23.35+PM.png)  
---  
Dat billing table yo  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEju2aPLTBgI0XIX99e7qOoJb3ffho76zC3SLWYwT1KAOb3M0x6pjovZOnB-q18ZbIxL6mBo57QTOkEgZ9DzqpKjL8YIa6gZwOZdmRWQd7HZQ4eNLhQbw2fAo4CujLzWgyhysSHiBJybsGQ/s320/Screen+Shot+2020-03-13+at+10.23.57+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEju2aPLTBgI0XIX99e7qOoJb3ffho76zC3SLWYwT1KAOb3M0x6pjovZOnB-q18ZbIxL6mBo57QTOkEgZ9DzqpKjL8YIa6gZwOZdmRWQd7HZQ4eNLhQbw2fAo4CujLzWgyhysSHiBJybsGQ/s1600/Screen+Shot+2020-03-13+at+10.23.57+PM.png)  
---  
I love payments tables  
  

  
Along the way I searched who this company was. <https://en.wikipedia.org/wiki/Tokopedia>

  

Most interestingly...

  

> In 2017, Tokopedia received $1.1 billion investment from Chinese e-commerce giant Alibaba.[[7]](https://en.wikipedia.org/wiki/Tokopedia#cite_note-7) Again in 2018, the company secured $1.1 billion funding round led by Chinese e-commerce giant [Alibaba Group](https://en.wikipedia.org/wiki/Alibaba_Group "Alibaba Group") Holding and Japan's [SoftBank](https://en.wikipedia.org/wiki/SoftBank "SoftBank") Group[[8]](https://en.wikipedia.org/wiki/Tokopedia#cite_note-8) putting its valuation to about $7B.[[9]](https://en.wikipedia.org/wiki/Tokopedia#cite_note-9)

So being a good person (tm) I reported the issue and it was assigned a critical severity. The fixed it super quickly and the team was decently responsive until it was fixed. After that it took 2 weeks to get information on the bounty, I promptly provided payment info, but I was never paid and they have stopped responding to my inquiries.  
  
  
**Solutions:**  
Run in a limited privilege container (doesn't protect against cloud metadata attack)  
  
New versions of Juypter notebook allow for password protecting access. Do that instead of open to all
