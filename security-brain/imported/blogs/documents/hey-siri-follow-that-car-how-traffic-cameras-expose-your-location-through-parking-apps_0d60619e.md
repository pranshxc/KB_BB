---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-26_hey-siri-follow-that-car-how-traffic-cameras-expose-your-location-through-parkin.md
original_filename: 2022-09-26_hey-siri-follow-that-car-how-traffic-cameras-expose-your-location-through-parkin.md
title: “Hey Siri, follow that car!” - How traffic cameras expose your location through
  parking apps.
category: documents
detected_topics:
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 0d60619e76368cb026a9d5976238563335dfc5ed6019ec37be1f3bc869fb4c55
text_sha256: 637dc98aadcc5adfaa2e9b53bc7eb63e7797a9e0706f3f6da2931f400e84305c
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# “Hey Siri, follow that car!” - How traffic cameras expose your location through parking apps.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-26_hey-siri-follow-that-car-how-traffic-cameras-expose-your-location-through-parkin.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `0d60619e76368cb026a9d5976238563335dfc5ed6019ec37be1f3bc869fb4c55`
- Text SHA256: `637dc98aadcc5adfaa2e9b53bc7eb63e7797a9e0706f3f6da2931f400e84305c`


## Content

---
title: "“Hey Siri, follow that car!” - How traffic cameras expose your location through parking apps."
page_title: "Stop others from tracking your car | NOTMYPLATE.COM"
url: "https://notmyplate.com/whitepaper/"
final_url: "https://notmyplate.com/whitepaper/"
authors: ["Inti De Ceukelaire (@securinti)"]
bugs: ["Information disclosure", "Session hijacking"]
publication_date: "2022-09-26"
added_date: "2022-10-02"
source: "pentester.land/writeups.json"
original_index: 2114
---

# “Hey Siri, follow that car!”

## How traffic cameras expose your location through parking apps.

### DE CEUKELAIRE Inti - 26.09.2022

[← Back to homepage](../)

# 1\. Abstract

Automated license plate recognition systems have been used for over a decade by law enforcement to monitor and identify traffic offenders. More recently, the technology has found its way to customer-facing applications, despite criticism by privacy advocates. Until now, most privacy concerns revolved around increased risk of government surveillance, automated decision making, high cost of usage and potential data breaches. With this research paper, we are putting the theory into practice and factual data, uncovering different ways in which these systems are inadvertently already exposing vehicle location data to the general public. The growing trend of affected license plate systems across Europe and the U.S. is concerning, and calls for prompt and decisive actions by legislators to mitigate the increasing risks.

From June 2022 to mid-September 2022, a group of 120 randomly selected individuals with different levels of car usage volunteered to have their license plates tracked as part of this study. None of the participants were briefed about the research methodologies, so their participation would not influence their driving behavior. 

One discovered methodology involved (re-)registering the license plates into parking and toll road applications that start- and stop sessions based on automatic license plate recognition. Out of the 120 license plates monitored, we were able to track down the live location of slightly over 29% of vehicles during a 100-day window (26.5% of which using methodology #1, and additional 2.5% using methodology #2 which was tested on a smaller scale). 

Another technique was proven to work in areas without cameras, such as on-street parking in cities and residential neighborhoods. A proof-of-concept stalkerware application was developed to routinely create one-second parking sessions for a multitude of parking zones across the country, intercepting any errors that would indicate the vehicle is already parked there. When used in areas that offer limited free parking time, the scan would only have to run once a day and would not incur any charges for the attacker. 

The attack surface of both techniques is widespread, with more 3,850 affected areas identified in 10 different countries in Western Europe. All traffic participants can be affected, regardless of whether they already use parking apps or not. Other than avoiding all affected areas, the only way for road users to temporarily mitigate the risk is to invoke their (UK/EU) GDPR’s Right to Restrict Processing on the concerned data processors. In order to facilitate this, a web application hosted at NOTMYPLATE.COM was developed to help users send in a propper GDPR request for their license plate with an up-to-date list of affected parking apps. 

While this will help combat the privacy loopholes short-term, a more rigid solution will need to be put into place by data processors and regulators. 

# 2\. Tracking methodologies

The COVID-19 pandemic has accelerated the rise of contactless solutions, and the parking industry is no exception to this trend: ticketless entry through a mobile app or license plate recognition have become a standard for the large majority of parking operators. This trend increases convenience for its end-users, but also inadvertently exposes these previously closed systems to remote attacks described in the following sections.

## 2.1. Session hijacking through ANPR cameras

### 2.1.1. Technique overview

In order to automatically start- and stop a parking- or tollroad session based on a license plate, parking apps allow their users to enter their license plate number. Whilst this is convenient, this system lacks any form of authorisation: none of the apps verified whether the license plate was owned or affiliated to the person who entered it. This creates an opportunity window for a malicious actor to register someone else’s license plate and enable ANPR-based payments on their behalf. The next time a connected ANPR camera would detect the license plate, the attacker would receive a live push notification informing them of their session, disclosing the name of the parking lot the license plate is detected. 

### 2.1.2. Study results

On May 31 2022, we launched a call on [Twitter](https://twitter.com/intidc/status/1531584467785089024) and Instagram to sign up participants for our car-tracking experiment. To be eligible to participate, the individuals had to be a named driver of the car, but there were no requirements in terms of car usage. None of the individuals that agreed to participate were briefed about the tracking methodologies, to ensure their driving behavior would not change. In total, 120 participants had their license plates entered in the apps of two selected parking operators: Q-Park and Indigo. The third big Belgian operator Interparking was excluded because their application only allows its users to link one license plate at a time, which is less convenient for a large scale experiment. 

![](./img/plates_1.png) ![](./img/plates_2.png)  

Entering hundreds of plates in 4411 (Q-Park) and Indigo Neo (OPnGO)  
(real license plates replaced with fake ones for the screenshots)

Within the first days of the experiment, we already received the first succesful hits: one in a Q-Park location near a hospital in **Antwerp** , and one in an Indigo location in **Malines**. ![](./img/notification-example.png)

Over the duration of the experiment, the list of successfully located vehicles continued to grow in a linear fashion. After 100 days, 26.5% of all vehicles were already successfully located using this methodology: 

After every successful match, we deactivated or removed the license plate in the system to prevent suspicion. In many cases, the matched location would provide insights into the activity the targeted driver was attending while the vehicle was parked. Amongst the parking locations are hospitals, shopping malls, casino’s, swimming pools, concert venues, public transportation hubs or offices. Given enough data points, it could be possible to deanonymize individuals based on their activity history. 

### 2.1.3. Attack operation costs 

As the attacker is creating ANPR-based sessions on behalf of their victims, it does require them to cover the parking fee in case of a successful attack. The exact amount would depend on the location and the duration of the session, but typically be only a fraction of the costs of other tracking techniques, such as hidden trackers or private investigators.

During the investigation, €273.85 was spent on parking tickets ranging from €1,60 to €36,00. Some sessions were not charged because the driver either immediately left the building, or a technical error occurred. The average cost to successfully track down a vehicle was €7,82.

In a real-world attack scenario, attackers may reduce operating costs by cutting the parking session short through the customer service or using stolen credit cards. On some occasions, the unknowing victim would still grab a ticket and pay for it themselves, reducing the cost of the attack down to zero. 

### 2.1.4. Possible mitigations

Since the technique attacks the fundamentals of license plate based parking systems, it is not possible to fully mitigate the attack without losing some of its current convenience and functionalities.

### 2.1.4.1. Asking for proof of plate ownership

While license plate owner verification would seem like a logical solution to implement, it brings a couple of hurdles with it. Having users upload their registration certificate does not only diminish the user experience, it would provide the parking operators with even more sensitive data they are not permitted to process, and could easily be forged.

### 2.1.4.2. Blocking re-registration (plate hijacking)

Our research has shown that the majority of parking apps allow re-registration of license plate, even if the plate is already listed in the system. Without any notification or need for confirmation, the license plate would be disabled from the victim account and any future charges or notifications regarding the license plate would be sent to the attacker.

Some applications do prevent the re-usage of a license plate through their application. In that case, the customer service could possibly still re-assign it when contacted.

### 2.1.4.3. Reducing the amount of plates that can be added to a single user

Some parking apps allowed an infinite amount of license plates to be added to their ANPR payment list, allowing attackers to conduct surveillance on scale. Reducing the amount of license plates one could add would make the attack less convenient in execution, but would not remediate the issue. The downside of a limitation is that some businesses and organizations already use these parking apps to manage their entire fleet.

### 2.1.4.4. Implementing an opt-out list 

Just like a [robinson list](https://en.wikipedia.org/wiki/Robinson_list), a centralized blacklist can be maintained for people who wish to opt-out from private companies processing their license plate date. This would however not protect people that are unaware of the risk, and would have to be maintained by an authorized and trusted body. It only works if all the apps decide to implement it.

### 2.1.4.5. Only allowing license plate recognition for pre-booked slots

While limiting automatic license plate recognition based billing to slots that are pre-booked by a user does not prevent malicious actors from verifying whether a vehicle has been somewhere during a specific period of time, it makes a wide scale operation costly and less feasible.

### 2.1.4.6. Showing and confirming ANPR payment details warning upon entry

The attack in its current form raised little to none suspicion for most test subjects, given the fact that a barrier that opens automatically is not an uncommon thing to see at a parking lot. Had the screens at the entry informed them about the ANPR session along with the payment information that did not match theirs, it would not have gone unnoticed.

### 2.1.4.7. Secondary authentication with an RFID tag

Certain tollroad systems, such as France's [Bip & Go télépéage](https://www.bipandgo.com), require a physical Radio-frequency identification (RFID) tag to be present in the car for authentication purposes. Linking online payments to a secure tag ID rather than a license plate may still allow the convenience of a seamless enterance and prevent others accessing or registering the account.

## 2.2. Trial-and-error attacks with free limited parking

### 2.2.1. Methodology overview

As sustainable urban mobility planning is reclaiming street parking spots for public use, parking control solutions make their way onto public space. Since placing ANPR cameras on the corner of every street would be excessive and expensive, drivers are required to enter their license plate into a parking app- or meter upon arrival in a parking zone. Next to paid on-street parking, this allows cities to offer free parking for a limited time, e.g. 30 minutes for free near a shopping district. To prevent drivers from continuously renewing their free parking slot, parking operators implement a cooldown period in which a free parking session can no longer be created for a license plate. In most cases, a free slot can only be used once a day. When entering license plates for vehicles that are already registered or used their free slot for that day, parking applications would typically show an error that a session cannot be created. Attackers can use this error as an oracle to determine who has already parked there, by entering their license plates into the system and checking whether the error shows. ![](./img/4411-website.png) Parking apps like 4411 may show an error if a license plate has already consumed a free parking slot.

In order to exploit this technique at a scale, attackers can create an automated system that poll for the presence of a certain license plate across all parking zones on a regular basis. For this study, a proof-of-concept stalkerware application was created for the 4411.io parking app, active in Belgium and The Netherlands. The system would simulate a normal Android application and automatically create 1-second parking sessions for selected license plates on a daily basis: 

If the free parking session could not be created because the user had already parked there, the system would catch this error:  
![](./img/4411-burp.png) Mobile application returning NOT_ALLOWED_TOO_CLOSE_SINCE_LAST_SESSION error for a license plate

To avoid suspicion by the targets, the parking sessions were automatically created just before the free slots were reset, so they would never arrive at a parking spot to find out that someone had created a session on their behalf. If the error was captured, a push notification would be sent to the attacker to inform them about a successful hit: ![](./img/platescan-push.png) Once a consumed free parking slot is detected, the system sends a push notification to the phone of the attacker.

This technique is less suited for mass-surveillance as it requires the application to create a considerable amount of parking sessions per target, increasing the chances of being detected by the parking operator. In the limited proof of concept, 19 participants from a selected city implementing this system were tracked over a period of 100 days. Three inhabitants were detected in the monitored zones, all of which multiple times. The system created more than 5,000 parking sessions in a clearly automated pattern, but was never blocked from operating by the parking operators. 

  
**Platescan demo:**  

This video shows how the PlateScan is able to detect that I have used a free parking slot today, by attempting to create another free parking session at the end of the day. If the system sees that the license plate has already used its free time, it sends a notification to my mobile phone.  
The license plate is fake for the purpose of the video.

## 2.3. Authentication by plate in parking apps

Some parking applications offer the possibility to pay or download receipts containing location details merely by supplying the license plate on the website, enabling attackers to monitor locations for on- and offstreet parking sessions. 

### 2.3.1. Example: APCOA Connect / PayByPhone (UK / IE)

APCOA Connect offers its users the possibility to download VAT receipts containing the exact time and location of parking sessions merely by specifiying a license plate and a phone number. Attackers could use public data sources to get the phone number of a victim, such as the [Facebook data breach](https://www.businessinsider.com/stolen-data-of-533-million-facebook-users-leaked-online-2021-4?r=US&IR=T) in order to get an overview of their location details.  
**Live demo** For demonstration purposes, I have created a parking session with the following details:  **Phone number:**|  0472771337  
---|---  
**License plate:**|  T3ST1337  
  
Anyone navigating to <https://www.apcoaconnect.com/receipts> can enter my details and query my location info. A system designed to poll for this information periodically could get a real-time overview of my parking sessions: ![](./img/apcoa-1.png) ![](./img/apcoa-2.png)

Everyone can see I started a parking session at _Hackbrigdge_ at 23/09/2022 21:42 local time

### 2.3.2. Autopay

[Autopay.io](https://autopay.io) is a platform active in Norway, Sweden, Denmark and Finland and Germany. Just like described in "2.1. Session hijacking through ANPR cameras", it utilizes ANPR recognition to automacally debit parking costs for a parking session: ![](./img/autopay_steps.png) Their website features a form that allows users to query unpaid parking sessions for the past 48 hours, and pay for them: ![](./img/autopay.png) At first glance, the absence of (re)captcha technologies indicates that an attacker could simply run a script to run this every 48 hours to continously monitor a license plate. 

# 3\. Affected apps & operators in Europe

We have analyzed the most popular B2C parking applications utilizing ANPR technologies. None of the tested apps implemented mechanisms to validate whether the application user was the legitimate license plate owner. Note that we were only able to test and validate ANPR functionalities in Belgium. Some parking operators may not have rolled out number plate recongnition in all territories yet. Please check the local website to see if they've already rolled out ANPR parking in your area. We still included them in the list, as a request for restriction of processing may also apply to planned implementations.

## Overview per country

Country | Operators  
---|---  
Austria 🇦🇹 | EasyPark, Interparking, [APCOA](app-apcoa)  
Belgium 🇧🇪 | EasyPark, Q-Park, Indigo Neo, Interparking, APCOA  
Denmark 🇩🇰 | EasyPark, Q-Park, APCOA, AutoPay  
Finland 🇫🇮 | EasyPark, AutoPay  
France 🇫🇷 | Q-Park, APCOA, Indigo Neo, Interparking  
Germany 🇩🇪 | EasyPark, Q-Park, Contipark, APCOA, AutoPay  
Hungary 🇭🇺 | EasyPark  
Iceland 🇮🇸 | Easypark  
Ireland 🇮🇪 | Q-Park, APCOA  
Italy 🇮🇹 | EasyPark, Interparking, APCOA  
Liechtenstein 🇱🇮 | EasyPark  
Luxembourg 🇱🇺 | Indigo Neo  
Montenegro 🇲🇪 | EasyPark  
Netherlands 🇳🇱 | EasyPark, Q-Park, Indigo Neo, Interparking, APCOA  
Norway 🇳🇴 | EasyPark, APCOA, AutoPay  
Poland 🇵🇱 | Interparking, APCOA  
Portugal 🇵🇹 | EasyPark  
Romania 🇷🇴 | Interparking  
Serbia 🇷🇸 | EasyPark  
Slovenia 🇸🇮 | EasyPark  
Spain 🇪🇸 | EasyPark, Indigo Neo, Interparking, AENA  
Sweden 🇸🇪 | EasyPark, APCOA, AutoPay  
Switzerland 🇨🇭 | EasyPark, Twint+ / ParkingPay  
United Kingdom 🇬🇧 | EasyPark, Q-Park, APCOA, NCP  
  
## 3.1. EasyPark (CameraPark) / ParkMobile (ex-ParkNow Group)

**Active in:** 🇸🇪 [SE](https://easypark.se), 🇳🇴 [NO](https://easypark.no), 🇩🇰 [DK](https://easypark.dk), 🇫🇮 [FI](https://easypark.fi), 🇮🇸 [IS](https://easypark.is), 🇬🇧 [UK](https://easypark.com), 🇺🇸 [US](https://easypark.com/), 🇩🇪 [DE](https://easypark.de/), 🇫🇷 [FR](https://easypark.fr/), 🇳🇱 [NL](https://easypark.nl/), 🇧🇪 [BE](https://easypark.be), 🇪🇸 [ES](https://easypark.es), 🇮🇹 [IT](https://easypark.it), 🇨🇭 [CH](https://easypark.ch), 🇦🇹 [AT](https://easypark.at), 🇵🇹 [PT](https://easypark.pt), 🇸🇮 [SI](https://easypark.si), 🇦🇺 [AU](https://easypark.com.au), 🇳🇿 [NZ](https://easypark.nz/), 🇷🇸 [RS](https://easypark.rs/), 🇲🇪 [ME](https://easypark.com), 🇱🇮 [LI](https://easypark.com), 🇭🇺 [HU](https://easypark.hu)  
**Mobile app:** [Android](https://play.google.com/store/apps/details?id=net.easypark.android) [iOS](https://apps.apple.com/us/app/easypark-parking-made-easy/id449594317)  
**Contact:** [[email protected]](/cdn-cgi/l/email-protection#593d2936193c382a2029382b3277373c2d)  
**Steps to track a target:**

  1. Install the EasyPark app and create an account
  2. Click the menu icon (☰), tap payment and add a payment method
  3. Click the menu icon (☰), tap vehicles and add your target's license plate
  4. Click the menu icon (☰), tap CameraPark and select your target's vehicle to enable tracking
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Video demo:**  

## 3.2. Q-Park

**Active in:** 🇳🇱 [NL](https://www.q-park.nl/nl-nl/app/) , 🇩🇪 [DE](https://www.q-park.de/de-de/app/), 🇧🇪 [BE](https://www.q-park.be/nl-be/parkeerproducten/nummerplaatherkenning/), 🇬🇧 [UK](https://www.q-park.co.uk/en-gb/products/q-park-app/), 🇫🇷 [FR](https://www.q-park.fr/fr-fr/), 🇮🇪 [IE](https://www.q-park.ie/en-gb/), 🇩🇰 [DK](https://www.q-park.dk/da/)  
**Mobile app:** [Android](https://play.google.com/store/apps/details?id=com.qpark.mobilepark.android) [iOS](https://apps.apple.com/gb/app/q-park/id1477955834)  
**Contact:** [[email protected]](/cdn-cgi/l/email-protection#f9898b908f989a80b988d489988b92d79795)  
**Steps to track a target:**

  1. Install Q-Park's mobile application on your device
  2. In _Profile > Payment methods_, click _Add payment method_ and enter your details
  3. In _Profile > Number plates_, enter the target's license plate. Make sure to select the correct country
  4. In _Products > Pay as you Go Parking_ (alternatively named mobile parking), link the target's license plate.
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Video demo:**  

## 3.3. Indigo Neo (OPnGO)

**Active in:** 🇧🇪 [BE](https://www.indigoneobe), 🇫🇷 [FR](https://www.indigoneo.fr/), 🇪🇸 [ES](https://www.indigoneo.es), 🇱🇺 [LU](https://www.indigoneo.lu)  
**Mobile app:** [Android](https://play.google.com/store/apps/details?id=com.opngo.live) [iOS](https://apps.apple.com/nl/app/indigo-neo-ex-opngo/id1109398417)  
**Contact:** [[email protected]](/cdn-cgi/l/email-protection#e185918ecf8494a1888f8588868e8f848ecf828e8c)  
**Steps to track a target:**

  1. Install the _Indigo Neo_ application on your device
  2. Go to _My account > Cards_ and add your credit card
  3. Go to _My account > Vehicles_ and add your target's license plate
  4. Go to _My account > On demand access_ and press _enable_
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Video explainer (FR):**  

## 3.4. Interparking / Contipark

**Active in:** 🇦🇹 [AT](https://www.contipark.at), 🇫🇷 [FR](https://www.interparking.fr), 🇩🇪 [DE](https://www.contipark.de/), 🇮🇹 [IT](https://www.interparkingitalia.it/) 🇳🇱 [NL](https://www.interparking.nl/), 🇵🇱 [PL](https://www.interparking.pl/), 🇧🇪 [BE](https://www.interparking.be), 🇷🇴 [RO](https://www.interparking-romania.ro), 🇪🇸 [ES](https://www.interparking.es/)  
**Web application (BE):** [https://www.parkingmadeeasy.be](https://www.parkingmadeeasy.be/)  
**Contact:** [[email protected]](/cdn-cgi/l/email-protection#c7b7b5aeb1a6a4be87aea9b3a2b5b7a6b5acaea9a0e9a5a2)  
**Steps to track a target:**

  1. First, order a PCard+ from your local Interparking website
  2. Navigate to [https://www.parkingmadeeasy.be](https://www.parkingmadeeasy.be/) (Belgium) and login with your PCard+ details
  3. Click _Add new license plate_ , and add the license plate number of your victim
  4. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Video demo:**  

## 3.5. APCOA

**Active in:** 🇦🇹 [AT](http://www.apcoa.at/), 🇧🇪 [BE](http://www.apcoa.be/), 🇩🇰 [DK](http://www.apcoa.dk/), 🇩🇪 [DE](http://www.apcoa.de/), 🇮🇪 [IE](http://www.apcoa.ie/), 🇮🇹 [IT](http://www.apcoa.it), 🇱🇺 [NL](http://www.apcoa.lu), 🇳🇱 [NL](http://www.apcoa.nl/), 🇳🇴 [NO](http://www.apcoa.no/), 🇵🇱 [PL](http://www.apcoa.pl), 🇸🇪 [SE](http://www.apcoa.se), 🇨🇭 [CH](https://www.apcoa.ch), 🇬🇧 [UK](https://www.apcoa.co.uk)  
**Apcoa flow app** : [Android](https://play.google.com/store/apps/details?id=com.apcoaflow.consumer) [iOS](https://apps.apple.com/nl/app/apcoa-flow-mobile-parking/id1358202825)  
**Contact:** [[email protected]](/cdn-cgi/l/email-protection#ed899d82ad8c9d8e828cc38e8280)  
**Steps to track a target:**

  1. Install the APCOA Flow app on your mobile device
  2. Create an account
  3. Add your vehicle license
  4. Setup your payment method
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Connect Cashless Parking (APCOA UK):** [Android](https://apps.apple.com/gb/app/connect-cashless-parking/id558534763) [iOS](https://apps.apple.com/nl/app/connect-cashless-parking/id558534763)  
**Steps to track a target (UK/IE):**

  1. Go to [apcoaconnect.com](https://www.apcoaconnect.com/)
  2. Log in or create an account
  3. Under payment details, fill in your credit card details
  4. Go to _Auto pay > Vehicle details_ and scroll down to "Add new vehicle"
  5. Enter the target's vehicle details (pick anything for make and colour)
  6. Go to _Auto pay > Autopay details > Register for autopay and sign up the vehicle for all contracts_
  7. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Video demo:**  

## 3.6. Autopay.io

**Active in:** 🇳🇴 [NO](https://autopay.io), 🇸🇪 [SE](https://autopay.io), 🇫🇮 [FI](http://autopay.io), 🇳🇴 [DK](http://autopay.io), 🇩🇪 [DE](http://www.apcoa.de/)  
**Webapp:** [AutoPay.io](https://autopay.io)  
**Contact:** [[email protected]](/cdn-cgi/l/email-protection#60131510100f1214200115140f1001194e090f)  
**Steps to track a target:**

  1. Go to [autopay.io](https://autopay.io)
  2. Go to the [vehicles section](https://autopay.io/profile/vehicles)
  3. Click _add vehicle_ and add your target's license plate
  4. Go to [Payment cards](https://autopay.io/payments/cards) and add a payment card
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

## 3.7. TWINT+ / ParkingPay

**Active in:** 🇨🇭 [CH](https://www.twint.ch/)  
_Note: we were not able to test this application due to it only being available to Swiss citizens. The information in this section is based on public resources and will need to be confirmed by a local citizen._  
**Mobile app:** [Android](https://play.google.com/store/apps/details?id=ch.twint.payment&hl=nl&gl=US) [iOS](https://apps.apple.com/us/app/prepaid-twint-other-banks/id1001116392)  
**Contact:** [[email protected]](privacy@digitalparking.ch)  
**Steps to track a target:**

  1. Open the TWINT app and tap on TWINT+
  2. Choose "parking" and tap on the car symbol on the right
  3. Add your target's license plate
  4. Click on _License Plate Recognition_ and activate it
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

**Video demo:**  

## 3.8. AENA Parking

**Active in:** 🇪🇸 [ES](http://aenaparking.com/)  
**Mobile app:** [Android](https://play.google.com/store/apps/details?id=es.aena.mobile&hl=nl&gl=US) [iOS](https://apps.apple.com/nl/app/aena/id686440022)  
**Contact:** [[email protected]](dpd@aena.es)  
**Steps to track a target:**

  1. Register for AENA Club [here](https://clubcliente.aena.es/AenaClub/es/?showRegister=true)
  2. Add the target's license plate [here](https://clubcliente.aena.es/AenaClub/en/license-plate)
  3. Add a payment method [here](https://clubcliente.aena.es/AenaClub/en/my-account/payment-method)
  4. Activate number plate payment for all locations [here](https://clubcliente.aena.es/AenaClub/en/parking-ppm)
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

## 3.9. NCP (National Car Parks)

**Active in:** 🇬🇧 [UK](https://ncp.co.uk)  
**Mobile app (ParkPass):** [Android](https://play.google.com/store/apps/details?id=com.NCP.NCPParkPass&hl=en&gl=US) [iOS](https://apps.apple.com/gb/app/ncp/id1567539532)  
**Contact:** [[email protected]](DataProtection@ncp.co.uk)  
**Steps to track a target:**

  1. Download & install the 'ParkPass' app on your mobile device
  2. In settings, go to _payment details_ and add a card
  3. In settings, go to _vehicles_ and add your target's VRN
  4. Toggle the 'Enable AutoPay' switch
  5. All set! You are now able to intercept (and pay for) your victim's parking sessions in real-time, disclosing their location

## 3.10. Various integrators

Some parking applications integrate with ANPR technologies implemented by other parking applications.  
While these may still be vulnerable to the attacks described in "2.2. Trial-and-error attacks with free limited parking" and "2.3. Authentication by plate in parking apps", they are currently not listed as a processor of the data in NOTMYPLATE.  
Examples include:  

  1. 4411 (Q-Park integration)
  2. ParkMobile (Q-Park integration)
  3. ParkNow (Q-Park integration)
  4. KBC (Q-Park integration)
  5. ...

# 4\. Conclusion

With nearly 4,000 affected locations across Western Europe and more than a million trackable parking spots in 10 different countries, it is getting increasingly harder to travel across Europe without the risk of exposing your location. During our tests, we were able to locate a target parking their vehicle more than 1,100km from their home, near the Spanish border. 

While a driver may choose to avoid ANPR-based parking garages, it can be more difficult to completely avoid toll roads over longer distances. In Sweden and Norway [Epass24](https://www.epass24.com/) already automatically charges tolls to accounts with a user-supplied license plate, along with [Ireland’s M50](https://www.etoll.ie/driving-on-toll-roads/tolling-information/index.xml?set-lang=en#:~:text=Video%20tolling%20systems%20allows%20a%20vehicles%20license%20plate%20number%20to%20be%20extracted%20from%20an%20image%20either%20by%20using%20Automatic%20Number%20Plate%20Recognition%20\(ANPR\)%20technology%20or%20manual%20checking.) and [England’s M6](https://www.m6toll.co.uk/maritimes-fleet-first-to-trial-m6tolls-transformational-anpr-tolling-system/). 

As more than half of installations activated in the past three years, it is likely that we will see a rapid growth of B2C ANPR cameras in the months to come. Combined with urban mobility plans that typically strive to relocate cars from the street to dedicated parking garages, more vehicles will be registered by ANPR cameras in the future. 

The fact that nearly a quarter of all vehicles were successfully tracked during this experiment shows that action needs to be taken as soon as possible. Parking apps should be made privacy-first, and should properly verify and inform data subjects as required by privacy laws. 

On the drivers’ side, this should serve as a reminder that a license plate is a personal identifiable information record that should never be exposed to others online, e.g. on social media. This document is not a manifesto against technology, but rather a warning that convenience should not come at the cost of our privacy.
