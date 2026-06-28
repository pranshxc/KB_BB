---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-24_instagram-app-access-token.md
original_filename: 2022-02-24_instagram-app-access-token.md
title: Instagram App Access Token
category: documents
detected_topics:
- mobile-security
- oauth
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- mobile-security
- oauth
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 56264c7b6d4987a6e0e5ff5ef1ca372161edf42f8b354a31798fd4fefa039f38
text_sha256: 31fe46f8352a15983fd8b3e3f640686bd14ab472a1d53cd7ae354a8a3d9dbb92
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram App Access Token

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-24_instagram-app-access-token.md
- Source Type: markdown
- Detected Topics: mobile-security, oauth, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `56264c7b6d4987a6e0e5ff5ef1ca372161edf42f8b354a31798fd4fefa039f38`
- Text SHA256: `31fe46f8352a15983fd8b3e3f640686bd14ab472a1d53cd7ae354a8a3d9dbb92`


## Content

---
title: "Instagram App Access Token"
page_title: "Instagram App Access Token - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/instagram-app-access-token/"
final_url: "https://philippeharewood.com/instagram-app-access-token/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "38,300"
publication_date: "2022-02-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2871
---

Posted on [February 24, 2022August 27, 2024](https://philippeharewood.com/instagram-app-access-token/)

# Instagram App Access Token

In Facebook Graph API as defined by the developer documentation, there are several access tokens, to authenticate against various API endpoints.

  * _User Access Token_  
make requests on behalf of the user, normally obtained via OAuth `facebook.com/dialog/oauth`
  *  _Page Access Token_  
make requests on behalf of the page, obtained via `graph.facebook.com/pageID?fields=access_token`
  * Client Token  
used for app level (not admin) endpoints, obtained via getting the alphanumeric secret from `graph.facebook.com/appID?fields=login_secret `and concatenating in the form `appID|login_secret`
  * Application Access Token  
used for app level admin role endpoints, providing administration in an application, the token is normally in the form `appID|[alphanumeric+special characters]`

In addition to different classifications of tokens, a token can be from a third party app (e.g. one created via developers.facebook.com) or a first party app like Facebook/Instagram in iOS and Android.

It was possible to retrieve multiple application access tokens for Instagram which may have given administration access to certain endpoints for Instagram.

* * *

Meta has been working for a a few years on _Bloks_ , “a framework that enables both management logic to be defined once server-side and rendered as a native application”. This framework can commonly be seen in Facebook and Instagram shops as _Blok applications_.

![](https://philippeharewood.com/wp-content/uploads/2022/07/IMG_0072.png)

![](https://philippeharewood.com/wp-content/uploads/2022/07/IMG_0073.png)

![](https://philippeharewood.com/wp-content/uploads/2022/07/IMG_0074.png)  
  
The general setup has the following parameters: `app_id`, `params` and `versioning_id`, with the response given in a bundle tree. So in the above photos, the reviews page has an `app_id` of `com.bloks.www.bk.commerce.ratings_and_reviews.all_reviews`. In the bundle, the Blok component and actions were embedded via Base64 encoded strings. One of the Base64 strings decoded yielded a section like the following,
  
  
  ispy0_main_f01㙅#$&camera_rollChoose photobk.action.bloks.InflateSyncig.action.navigation.LaunchMediaPickerV2unified_rating_and_review_composerevent_nameerror_messagecomposer_typereferral_surfacead_group_idpage_idproduct_idinvoice_idcharacter_countrating_valuephoto_countprefill_ratingis_editidentity_preferencesurvey_versionseller_ig_idpurchase_sourcepurchase_source_metadatasignatureadd_photo_pressedPRODUCTpdp_all_reviews_screen3537638846322537ig_product_onsite_v090010214936182unknownbk.action.logging.LogEventcatalog_item_uploads124024574287414|Jor32q7Rh50x2LZL1Aw2F4f8bjw_f02_f03ig.action.media.UploadMediaV3COMMERCE_RATINGS_AND_REVIEWS_COMPOSER:is_image_uploading:17841401338810001bk.action.bloks.WriteGlobalConsistencyStorephoto_upload_startcom.bloks.www.bk.commerce.ratings_and_reviews.composer.media_upload.asyncparamsserver_paramsclient_input_paramscontainer_component_idrating_and_review_typeserialized_composer_contextmedia_source_typeis_local_selectedproduct{"rating_and_review_type":"product","merchant_id":90010214936182,"product_id":3537638846322537,"is_modal":false,"referral_surface":"pdp_all_reviews_screen","seeded_star_index":null,"rating_and_review_metadata":null,"extra_logging_info":null,"survey_entry_point":"product_detail_page","root_screen_id":null,"invoice_id":null}LIBRARYopaque_token_handlenext_image_index112982998200005bk.action.bloks.GetVariable2bk.action.string.JsonEncode_f04_f05current-screenbk.action.bloks.AsyncActionWithDataManifest

The section to notice is
  
  
  catalog_item_uploads124024574287414|Jor32q7Rh50x2LZL1Aw2F4f8bjw_f02_f03ig.action.media.UploadMediaV3

These values will be used via the `ig.action.media.UploadMediaV3` action as a request to upload a photo as part of the review
  
  
  POST /catalog_item_uploads/D52D5D86-308F-4DA5-B353-46B58BF47BD4 HTTP/2
  Host: rupload.facebook.com
  Priority: u=2, i
  Offset: 0
  X-Entity-Type: image/jpeg
  X-Entity-Length: 10234
  Content-Type: application/octet-stream
  X-Ig-Bandwidth-Speed-Kbps: 7623.000
  Content-Length: 10234
  Authorization: OAuth 124024574287414|Jor32q7Rh50x2LZL1Aw2F4f8bjw

The token defined in the `Authorization` header here isn’t a client token, a good indicator in my experience to notice this, is that a client token has the following pattern `[0-9]|[a-z0-9]*`. So this is an application token. A non destructive call to `graph.facebook.com/app/roles` with the token was used since I didn’t know what would happen to Instagram if I started to intensely test it. This listed about 25 Facebook user IDs with administrator or developer access, I didn’t check further pagination requests nor browsed any of the profiles. Based on the short length of some of the Facebook IDs it made sense to me these were Meta employees.

At this point, I sent a report, then pinged an employee in Whitehat Workplace to raise attention to the issue as well as ask for permission to push for impact. The proof of concept was enough, I was instructed not to touch the token anymore. To ensure I covered any variants I used a next bug in GraphQL at the time to fuzz possible bloks similar to `com.bloks.www.bk.commerce.ratings_and_reviews.composer` and found an additional application token. Meta informed me however that they checked this app as well. All the endpoints with tokens embedded were removed within hours.

**Impact** (as defined by Meta)

_You identified an endpoint issue that could have allowed a malicious actor to retrieve a first-party app IG access token. While we have protections in place that would have prevented further impact, your report led us to strengthen our defenses, make changes to prevent similar issues in the future across our codebase. We have fixed this bug and have not seen any evidence of abuse._

**Timeline**  
Feb 24, 2022 @ 1:10 am – Report sent  
Feb 24, 2022 @ 1:11 am – Pinged Meta Security via Workplace  
Feb 24, 2022 @ 2:56 am – Report triaged by Meta  
Feb 24, 2022 @ 5:20 am – Confirmation of fix by Meta  
May 19, 2022 – $30,000 Bounty awarded by Meta,  
$6,000 Platinum league bonus  
$2,250 Time delay bonus  
$50 BountyConEdu bonus  
  
Thanks to Meta and special thanks to the employee on call.  
  
References:  
https://developers.facebook.com/docs/facebook-login/guides/access-tokens  
https://techcrunch.com/2021/03/10/facebook-targets-emerging-markets-with-instagram-lite-a-new-android-app-that-takes-up-just-2mb-in-170-countries/
