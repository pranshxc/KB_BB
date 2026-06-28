---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-16_how-i-found-broken-access-control-through-out-of-sync-setup-and-got-1000.md
original_filename: 2022-01-16_how-i-found-broken-access-control-through-out-of-sync-setup-and-got-1000.md
title: How i found “Broken Access Control Through out-of-sync setup” and got $1000
category: documents
detected_topics:
- access-control
- mobile-security
- sso
- idor
- command-injection
- path-traversal
tags:
- imported
- documents
- access-control
- mobile-security
- sso
- idor
- command-injection
- path-traversal
language: en
raw_sha256: 6db4e650fd6e2efb38d5ca431fa94e3486fabf068897eacdfadbdd56fe5ba03a
text_sha256: 5d7d008185daf19feb966038b58912b58b0628a38c99a1c77acd2329083529bd
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How i found “Broken Access Control Through out-of-sync setup” and got $1000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-16_how-i-found-broken-access-control-through-out-of-sync-setup-and-got-1000.md
- Source Type: markdown
- Detected Topics: access-control, mobile-security, sso, idor, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `6db4e650fd6e2efb38d5ca431fa94e3486fabf068897eacdfadbdd56fe5ba03a`
- Text SHA256: `5d7d008185daf19feb966038b58912b58b0628a38c99a1c77acd2329083529bd`


## Content

---
title: "How i found “Broken Access Control Through out-of-sync setup” and got $1000"
url: "https://medium.com/@robert0/how-i-found-broken-access-control-through-out-of-sync-setup-and-got-1000-9143fc5febdd"
authors: ["Mr Robert | Ahmed M Hassan (@Mr_Robert20)"]
bugs: ["Broken Access Control", "Broken authorization"]
bounty: "1,000"
publication_date: "2022-01-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3003
scraped_via: "browseros"
---

# How i found “Broken Access Control Through out-of-sync setup” and got $1000

How i found “Broken Access Control Through out-of-sync setup” and got $1000
Mr Robert | Ahmed M Hassan
Follow
8 min read
·
Jan 16, 2022

142

1

Hello everyone ! , Hope you all are doing well, I would like to share my “Broken Access Control Through out-of-sync setup”

What is BAC (Broken Access Control Attack) ?

Broken Access Control is when an application does not thoroughly restrict user permissions for appropriate access to administrative functionality. The consequences associated to broken access control may include viewing of unauthorized content, modification or deletion of content, or full application takeover. A few examples of common access control vulnerabilities are role based access, poor password management, insecure Id’s, forced browsing past access control checks, path traversal, file permissions, and client side caching.

Recon:

Gathering information about your target is the golden key to reaching weak points, so I care a lot about the stage of collecting information and i Really enjoy the logical vulnerabilities and take great care of the functionality of the site ,
My target it was a private program on hackerone so Let’s call it for example “webapp.com”
Well, Firstly i used my own recon methodology for subdomain enumeration
1. using the most popular subdomain enum tools like findomain, amass, sublist3r, subfinder
2. and I have extracted all live subdomains and took screenshots of each one of them by these following command:

cat all-subdomains.txt | uniq | httpx -silent -mc 200,302,404,403,401,400 -threads 70 | cut -d “/” -f 3 | uniq | aquatone -scan-timeout 3000 -threads 5 -silent -screenshot-timeout 50000 -http-timeout 20000 -out subdomains-screenshots

Discovery:

Then I checked the results and screenshots one by one until something caught my attention that there were two different subdomains but with the same login panel
First one it was : portal.webapp.com
2nd one : stage-portal.webapp.com
I quickly went to portal.webapp.com and registered an account , then went to stage-portal.webapp.com
and tried creating an account, but a n alert appeared that this account had already been registered, now I made sure that the two login portals are connected to the same database, so let’s take a step back and know more about the functionality of the website application , the website webapp.com, through its services, you can make advertisements for your Android application, or the iOS application, and when you register a new account, you attach your previously developed Android application to your new account and then create an advertising plan and so on, the account owner has the ability to create accounts Sub-users of the owner’s account to perform certain tasks according to the permissions that the administrator has given to the sub-users via “User Management” section in account which is the control panel of sub-users accounts and only appeared to the administrators
and among these permissions:
1. Access to the application and modify its data, erase or hide it
2. Read Application Performance Reports
3. Administrator Permissions So the administrator can give any or all of these permissions to the sub-users

Let’s break the access control:

So the scenario that came to my mind at the time: Suppose we create a root account via portal.webapp.com and decide to create a sub-user and give it access permissions:
1. Access to the application and modify its data, erase or hide it

The application mechanism imposes restrictions if one of these permissions is changed by the administrator or root user, such as preventing access to (Application Access) and giving access to (Read Application Performance Reports) instead. The site automatically logs out of the sub-user account due to the permissions update But in my case, if sub-user login through stage-portal.webapp.com with permissions:
1. Access to the application and modify its data, erase or hide it
2. Read Application Performance Reports
and select Remember Me (Expires in 30 days)
If the root user changes the permissions of that user, such as preventing them from accessing App Access, the surprise here is that the sub-user can still access, edit, hide and even delete apps, and they won’t be automatically logged out as in the normal case on portal.webapp.com and his permissions will not be changed and this will only change if he logs out and logs in again

In another scenario, more dangerous than that, if the root user or the administrator gives the sub-user Administrative permissions while he does not know the severity of the vulnerability that currently exists, and then at some point the root user wants to revoke this permission and give him only a lesser permission such as Read Application Performance Reports During the modification that made by the root user, if the sub-user is already logged in through stage-portal.webapp.com: The sub-user can still access the “User Management” section and raise his permissions to the Higher permissions again, and he can also delete users and doing critical damage, and he is not supposed to have these permissions

So literally that was so funny to me

So literally that was so funny to me

And i quickly reported it to the program
And the report got Triaged after 3 hours as medium severity “Because if the sub-user if logs out and login again, the high permissions will be removed and the attack will fail”

Press enter or click to view image in full size

and i got rewarded with $1,000 bounty

Press enter or click to view image in full size

Thanks for reading, have a nice day

you can follow my Twitter to see my BB tips and my new writeups

ما هو (Broken Access control attack)؟
يحدث كسر التحكم في الوصول عندما لا يقوم تطبيق ما بتقييد أذونات المستخدم تمامًا للوصول المناسب إلى الوظائف الإدارية. قد تشمل العواقب المرتبطة بانقطاع التحكم في الوصول عرض المحتوى غير المصرح به أو تعديل المحتوى أو حذفه أو الاستيلاء الكامل على التطبيق. بعض الأمثلة على نقاط الضعف الشائعة في التحكم في الوصول هي الوصول المستند إلى الدور ، وإدارة كلمات المرور السيئة ، والمعرفات غير الآمنة ، والتصفح الإجباري لعمليات التحقق من التحكم في الوصول السابقة ، واجتياز المسار ، وأذونات الملفات ، والتخزين المؤقت من جانب العميل.

Get Mr Robert | Ahmed M Hassan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reconnaissance and information gathering:
جمع المعلومات حول هدفك هو المفتاح الذهبي للوصول إلى نقاط الضعف ، لذلك أهتم كثيرًا بمرحلة جمع المعلومات وأستمتع حقًا بنقاط الضعف المنطقية وأهتم كثيرًا بوظائف الموقع ،
كان هدفي عبارة عن برنامج خاص على منصة هاكروان ، لذا دعنا نسميه على سبيل المثال “webapp.com”
حسنًا ، أولاً ، استخدمت منهجية جمع السبدومينز الخاصة بي لاستخراج المجالات الفرعية
1. استخدمت أدوات جمع السبدومينز الأكثر شعبية مثل findomain و amass و sublist3r و subfinder
2- ثم استخرجت جميع النطاقات الفرعية التي تعمل وأخذت لقطات شاشة لكل منها من خلال الأمر التالي:

cat all-subdomains.txt | uniq | httpx -silent -mc 200,302,404,403,401,400 -threads 70 | cut -d “/” -f 3 | uniq | aquatone -scan-timeout 3000 -threads 5 -silent -screenshot-timeout 50000 -http-timeout 20000 -out subdomains-screenshots

Descovery :
ثم راجعت النتائج ولقطات الشاشة واحدة تلو الأخرى حتى لفت انتباهي شيئًا ما بوجود مجالين فرعيين مختلفين ولكن يستخدمون لوحة تسجيل الدخول نفسها
أول واحد كان: portal.webapp.com
الثاني: stage-portal.webapp.com

ثم انتقلت الي

portal.webapp.com

وقمت بتسجيل حساب
وبعدها ذهبت إلى stage-portal.webapp.com
وحاولت إنشاء حساب ، ولكن ظهرت ملاحظة أن هذا الحساب قد تم تسجيله بالفعل ، والآن تأكدت من أن نوافذ تسجيل الدخول متصلتين بقاعدة البيانات نفسها ، لذلك دعونا نتراجع خطوة إلى الوراء ونتعرف على وظائف تطبيق موقع الويب : من خلال خدماته يمكنك عمل إعلانات لتطبيق اندرويد الخاص بك ، أو تطبيق ايفون ، وعندما تقوم بتسجيل حساب جديد ، تقوم بإرفاق تطبيق اندرويد الذي تم تطويره مسبقًا بحسابك الجديد ثم إنشاء خطة إعلانية وهكذا ، فإن صاحب الحساب لديه القدرة على إنشاء حسابات مستخدمين فرعيين لحساب المالك لأداء مهام معينة وفقًا للصلاحيات التي منحها المسؤول للمستخدمين الفرعيين عبر قسم “إدارة المستخدمين” في الحساب وهو لوحة التحكم لمستخدمي الحساب الفرعيين وظهر فقط للمسؤولين
ومن بين هذه الأذونات:
1. الوصول إلى التطبيق وتعديل بياناته أو محوها أو إخفاؤها
2. قراءة تقارير أداء التطبيق
3. أذونات المسؤول حتى يمكن للمسؤول إعطاء أي من هذه الأذونات أو جميعها للمستخدمين الفرعيين

Let’s Break The Access Control :
إذن السيناريو الذي خطر ببالي في ذلك الوقت: لنفترض أننا أنشأنا حسابًا جذرًا عبر portal.webapp.com وقررنا إنشاء مستخدم فرعي ومنحه أذونات الوصول:
1. الوصول إلى التطبيق وتعديل بياناته أو محوها أو إخفاؤها

تفرض آلية التطبيق قيودًا إذا تم تغيير أحد هذه الأذونات من قبل المسؤول أو المستخدم الجذر ، مثل منع الوصول إلى صلاحيات (وصول التطبيق) وإعطاء الوصول إلى صلاحيات (قراءة تقارير أداء التطبيق) بدلاً من ذلك. يقوم الموقع بتسجيل الخروج تلقائيًا من حساب المستخدم الفرعي بسبب تحديث الأذونات ولكن في حالتي ، إذا كان تسجيل دخول مستخدم فرعي من خلال stage-portal.webapp.com مع الأذونات:
1. الوصول إلى التطبيق وتعديل بياناته أو محوها أو إخفاؤها
2. قراءة تقارير أداء التطبيق
وقمت بتحديد “تذكرني (تنتهي صلاحيته خلال 30 يومًا)”
إذا قام المستخدم الجذر بتغيير أذونات هذا المستخدم ، مثل منعه من الوصول إلى الوصول إلى التطبيق ، فإن المفاجأة هنا هي أن المستخدم الفرعي لا يزال بإمكانه الوصول إلى التطبيقات وتعديلها وإخفائها وحتى حذفها ، ولن يتم تسجيل خروجهم تلقائيًا كما في الحالة العادية على

portal.webapp.com

وأذوناته لن تتغير ولن يتغير هذا إلا إذا قام بتسجيل الخروج وتسجيل الدخول مرة أخرى

في سيناريو آخر ، أخطر من ذلك ، إذا أعطى المستخدم الجذر أو المسؤول أذونات مثل صلاحيات “المسؤول” للمستخدم الفرعي بينما لا يعرف خطورة الثغرة الأمنية الموجودة حاليًا ، ثم في مرحلة ما يريد المستخدم الجذر إلغاء هذا الإذن ومنحه إذنًا أقل مثل “قراءة تقارير أداء التطبيق”

أثناء التعديل الذي أجراه المستخدم الجذر ، إذا كان المستخدم الفرعي قد سجل الدخول بالفعل من خلال

stage-portal.webapp.com

لا يزال بإمكان المستخدم الفرعي الوصول إلى “ قسم إدارة المستخدمين “ورفع أذوناته إلى الأذونات العليا مرة أخرى ، ويمكنه أيضًا حذف المستخدمين وإحداث أضرار جسيمة ، وليس من المفترض أن تكون لديه هذه الأذونات

كان ذلك حرفيا مضحكا جدا بالنسبة لي

وسرعان ما أبلغت البرنامج بذلك
وتمت الموافقه على التقرير بعد 3 ساعات باعتباره متوسط ​​الخطورة “لأنه إذا قام المستخدم الفرعي بتسجيل الخروج ، فسيتم ازالة الصلاحيات المتواجدة بفضل هذة الثغرة”

Press enter or click to view image in full size

وتمت مكافأتى ب 1000 دولار

Press enter or click to view image in full size

شكراً للقراءة , اتمني لكم يوماً سعيداً

you can follow my Twitter to see my BB tips and my new writeups
