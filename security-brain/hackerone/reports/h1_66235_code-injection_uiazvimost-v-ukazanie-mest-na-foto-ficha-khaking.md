---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66235'
original_report_id: '66235'
title: Уязвимость в Указание мест на фото + фича + хакинг
weakness: Code Injection
team_handle: vkcom
created_at: '2015-06-06T01:24:11.281Z'
disclosed_at: '2015-09-07T15:53:07.286Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- code-injection
---

# Уязвимость в Указание мест на фото + фича + хакинг

## Metadata

- HackerOne Report ID: 66235
- Weakness: Code Injection
- Program: vkcom
- Disclosed At: 2015-09-07T15:53:07.286Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Для начало прошу прощения за столько много выделенных ТИПОВ ...
(коротко с помощью уязвимости можно ставить отметку на фото гео лакации любому пользователю)

Следование этому пожеланию увеличит вероятность получения награды.

Сервис, в котором найдена уязвимость.
https:/vk.com/al_places.php
http://vk.com/al_photos.php
+ код Олега у каждого пользователя вк (его альбом)

Тип уязвимости.
Хранение hash в открытом доступе и следовательно
При правильном запросе можно поставить любому пользователю (гео) метку на фотографию 
(это уже какой-то хакинг =) ) 
Все находится в открытом доступе, как всегда у вас =) 

Как можно проэксплуатировать.
Показано на видео прикрепил оригинал видео залил на yandex disk и на youtube ссылки:
https://yadi.sk/i/XnUy08vIh7Ecf
https://youtu.be/SZGu2Nd-QOk

Как повторить.
Выбираете любого пользователя , выбираете любое его фото и копируете часть из ссылки на фото
(например 307707832_367700640)

Далее нам понадобится ссылка для получение hash фотографии пользователя
Для этого нам нужна ссылка https:/vk.com/al_places.php?act=show_photo_place&al=1&edit=1&photo=ХХХХ_ХХ
где хххх_хх это ссылка на фото в виде ( 307707832_367700640 )
Посылаем запрос (как пример)
https:/vk.com/al_places.php?act=show_photo_place&al=1&edit=1&photo=307707832_367700640
Просматриваем код страницы , находим там hash

Теперь чтобы создать метку у пользователя на фото , нам понадобится ссылка
http://vk.com/al_photos.php?act=do_edit_place&al=1&hash=ТУТХЕШ&lat=0.7031073524364909&long=16.875&photo=ТУТФОТОФОРМАТАххх_ххх

Посылаем запрос (как пример)
http://vk.com/al_photos.php?act=do_edit_place&al=1&hash=0268f5b2baab24d032&lat=0.7031073524364909&long=16.875&photo=307707832_367700640

Нам вернется ошибка , следовательно если пользователь ее откроет которому принадлежит фото , то метка появится ! Отсылаем пользователю ссылку он ее открывает и мы радуемся (грустим конечно)

Чтобы пользователь нечего не спалил можно сделать следующем образом создать страничку с iframe вставить туда эту ссылку и код на перенаправление на вк.ком через 5 секунд к примеру и воуля . Кидаем эту страничку в интернете пользователю он открывает отсылается обратно в вк и нечего не подозревает =)) 

Да в видео еще показано вначале , если вы не смотрите -
 ОЛЕГ И. ЗАБЫЛ СВОЙ АЛЬБОМ У ПОЛЬЗОВАТЕЛЕЙ НА СТРАНИЧКАХ =)

Как исправить, с вашей точки зрения.
Проверку на принадлежит ли фото пользователю введите в метод ( if else ) 
(да у меня все проблемы так решаются)

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
