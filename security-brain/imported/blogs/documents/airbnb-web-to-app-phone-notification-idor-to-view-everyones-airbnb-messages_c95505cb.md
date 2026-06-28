---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-03-31_airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages.md
original_filename: 2017-03-31_airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages.md
title: Airbnb – Web to App Phone Notification IDOR to view Everyone’s Airbnb Messages
category: documents
detected_topics:
- idor
- command-injection
- api-security
- sso
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- api-security
- sso
- rate-limit
- automation-abuse
language: en
raw_sha256: c95505cbe38556926bf90e259340c0dca24f7810e03f5f48f0fd332fb08064fa
text_sha256: 1ba23dad94a89df9bfdf5c94a93511c1c20e903be47e71469a0d575535206214
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Airbnb – Web to App Phone Notification IDOR to view Everyone’s Airbnb Messages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-03-31_airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security, sso, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c95505cbe38556926bf90e259340c0dca24f7810e03f5f48f0fd332fb08064fa`
- Text SHA256: `1ba23dad94a89df9bfdf5c94a93511c1c20e903be47e71469a0d575535206214`


## Content

---
title: "Airbnb – Web to App Phone Notification IDOR to view Everyone’s Airbnb Messages"
page_title: "Airbnb – Web to App Phone Notification IDOR to view Everyone’s Airbnb Messages | ziot"
url: "https://buer.haus/2017/03/31/airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages/"
final_url: "https://buer.haus/2017/03/31/airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages/"
authors: ["Brett Buerhaus (@bbuerhaus)", "Ben Sadeghipour (@nahamsec)"]
programs: ["Airbnb"]
bugs: ["IDOR"]
publication_date: "2017-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6203
---

# Airbnb – Web to App Phone Notification IDOR to view Everyone’s Airbnb Messages

March 31, 2017February 25, 2024

![airbnb_horizontal_lockup_print](https://buer.haus/wp-content/uploads/2016/05/airbnb_horizontal_lockup_print.jpg)

Authors:

  * [![image](https://abs.twimg.com/errors/logo23x19.png) Ben Sadeghipour](https://twitter.com/nahamsec)
  * [![image](https://abs.twimg.com/errors/logo23x19.png) Brett Buerhaus](https://twitter.com/bbuerhaus)

Airbnb recently created a new feature called [Experiences](https://www.airbnb.com/experiences/) which allows you to book things to do rather than places to stay. With the new code changes that came along with Experiences, we discovered a page that allowed you to send yourself a text message with a link to download the Airbnb app. This sent a POST request to an API endpoint we had never seen before. Using the JS Parser tool we built we discovered another API call associated with it. We found that these API calls were vulnerable to Insecure Direct Object Reference (IDOR) and allowed you to view all messages on Airbnb by ID.

The API request we discovered was the **/api/v2/air_sms_notifications** endpoint. Digging through the JS files on Airbnb we discovered there was also an API call named **/api/v2/air_push_notification**.

[![](https://buer.haus/wp-content/uploads/2017/03/api.png)](https://buer.haus/wp-content/uploads/2017/03/api.png)

Trying to send these API requests manually kept throwing generic errors and we couldn't figure out where it was actually implemented on the website. It took us awhile to eventually figure out there were some requirements that needed to be met before you could send the request. We eventually found two locations on Airbnb where it was integrated. Both of these were for sending yourself a text with a link to install the Airbnb phone app.

[![](https://buer.haus/wp-content/uploads/2017/03/screenshot_20170219-184740_1024-169x300.png)](https://buer.haus/wp-content/uploads/2017/03/screenshot_20170219-184740_1024.png)

**API Requests**

https://www.airbnb.com/api/v2/air_sms_notifications

  * Requires that you have a verified phone number in your profile.
  * This API request allowed you to send yourself SMS texts.
  * There is a length limit on the SMS messages (160)
  * Throttling restrictions on SMS only allowed you to send this API request a handful of times every hour

https://www.airbnb.com/api/v2/air_push_notifications

  * Requires that you have a verified phone number, the Airbnb app installed on your phone (with that phone number), and you are logged into the app with that account. (This one took awhile to figure out)
  * Instead of sending SMS, it pushed notifications to your phone through the phone app.
  * There is no length restriction on the output.
  * No throttling which made testing a lot easier compared to SMS

**POST data**

This API POST data was comprised of the following:
  
  
  {"_format":"for_visitor","country":"USA","phone_number":"","template":"message","user_id":,"title":"","body":"","metadata":{},"object_id":"","status":"","role":"","photo_url":""}

The JSON attribute **template** turned out to be interesting. If you passed in an invalid template it would give you a list of all the valid templates that you could send.

[![](https://buer.haus/wp-content/uploads/2017/03/templates-1024x484.png)](https://buer.haus/wp-content/uploads/2017/03/templates.png)

**Templates**

/api/v2/air_sms_notifications | /api/v2/air_push_notifications  
---|---  
content_framework, custom, host_banner_app_install, host_never_actives_just_raw_listing, host_never_actives_on_description, host_never_actives_on_photo, host_never_actives_on_price_or_booking_setting, message, mobile_photo_upload_app_install, identity_verifications, identity_verifications_booking, p2_p3_abandon_sms, reservation_alteration_approved, reservation_alteration_declined, reservation_guest_accepted, reservation_guest_cancelled, reservation_guest_declined, reservation_host_accepted, reservation_host_cancelled, reservation_host_declined, verified_id_app_install, review_final_reminder_message, mt_pdp_handoff, mt_native_handoff_generic, message_image_attachment, guidebook_landing_page, wish_lists_native_handoff | checkpoint, cn_blackout_g20_hangzhou_2016, custom, host_never_actives_just_raw_listing, host_never_actives_on_description, host_never_actives_on_photo, host_never_actives_on_price_or_booking_setting, identity_verifications, identity_verifications_booking, message_image_attachment, message, midtrip_host_checkup_reminder, mobile_photo_upload, paid_amenity_accepted, paid_amenity_canceled_by_guest, paid_amenity_canceled_by_host, paid_amenity_declined, paid_amenity_request, paid_amenity_shop_services, preapproval_guest_sent, preapproval_guest_withdrawn, reservation_alteration_approved, reservation_alteration_request_automatically_accepted, reservation_alteration_declined, reservation_alteration_request, reservation_guest_accepted, reservation_guest_cancelled, reservation_guest_declined, reservation_host_accepted, reservation_host_cancelled, reservation_host_declined, reservation_host_request, reservation_payment_pending, reservation_host_first_reminder, reservation_host_last_reminder, review_final_reminder_message, risk_email_updated, risk_password_updated, risk_payout_method_updated, risk_phone_number_updated, share_your_trip_prompt, special_offer_guest, special_offer_guest_expired, special_offer_guest_withdrawn, special_offer_host_expired, support_message  
  
There are 27 possible SMS templates and 46 possible Push templates that you can send. This is a fairly big attack surface and there are some interesting template names in those lists that seem like potential targets.

We decided to start with the **custom** template. Trying to send the POST request, we get the following response:
  
  
  {"error_code":400,"error_type":"validation","error_message":"There was an error processing the request.","error_id":"fd9fba9bc18538d7ae93ba6867c1be0a","error_details":"title is required."}

If you sent the POST request to a template with a missing attribute, it would tell you what attributes you were missing. This verbosity gave us everything we needed to start gathering information and seeing what functionality exist.

We discovered that the **custom** template accepted parameters title and body. This template allowed you to send yourself a custom SMS or notification.
  
  
  {"_format":"for_visitor","country":"USA","phone_number":"","template":"custom","user_id":109764261,"status":"test","title":"test","body:"test"}

[![](https://buer.haus/wp-content/uploads/2017/03/screenshot_20170219-125058_1024-576x1024.png)](https://buer.haus/wp-content/uploads/2017/03/screenshot_20170219-125058_1024.png)

We spent probably a good 10-12 hours going through all of these templates. Towards the end it came down to waiting hour intervals to send 4-5 requests each against the SMS API due to the throttle on it. It was some effort to slowly grab the attributes for each template and eventually test to see if they were vulnerable. In the end we discovered a handful of vulnerable templates, but the most interesting template ended up being **message**.

Most of the templates required that you send the attribute **object_id**. Given that this API is a fairly broad service that has a lot of features behind it, our guess was that object_id was the data that the template wanted to reference by the database entry id. When you come across an id like that, getting an IDOR can be immensely useful if it's a simple sequential numeric ID. Not having an object_id for testing, we threw in a random number. Looking at the phone we sent the notification to, we immediately knew we had something real bad.

Enumerating on the object_id by one we could see that we had access to every private message on Airbnb by ID. What was neat is that you could do this with SMS as well, as the templates seemed to share a lot of the same core code. With the SMS throttle and truncation, it wasn't really a viable attack vector. With Push you could enumerate through the full messages without any restrictions.

Push | SMS  
---|---  
[![](https://buer.haus/wp-content/uploads/2017/03/message-169x300.jpg)](https://buer.haus/wp-content/uploads/2017/03/message.jpg) | [![](https://buer.haus/wp-content/uploads/2017/03/screenshot_20170220-080621_1024-169x300.png)](https://buer.haus/wp-content/uploads/2017/03/screenshot_20170220-080621_1024.png)  
  
This vulnerability turned out to be a fun exercise because of all the moving pieces and research required to figure out the impact. The object_id IDOR was vulnerable on most of the templates which led to several different data leaks, but nothing as high impact as messages. We were unable to get some of the templates to work as they would always throw 500 errors with the data we were sending.

**Timeline:**

This was sent in along with the [Remote Code Execution report](https://buer.haus/2017/03/13/airbnb-ruby-on-rails-string-interpolation-led-to-remote-code-execution/), so they were probably focused on fixing that first.

  * 2/19/2017: Reported
  * 2/21/2017: Triaged
  * 2/23/2017: Fixed
