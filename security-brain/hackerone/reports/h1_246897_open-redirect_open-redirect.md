---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246897'
original_report_id: '246897'
title: Open Redirect
weakness: Open Redirect
team_handle: x
created_at: '2017-07-07T13:28:27.032Z'
disclosed_at: '2017-08-19T00:05:50.149Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- open-redirect
---

# Open Redirect

## Metadata

- HackerOne Report ID: 246897
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2017-08-19T00:05:50.149Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

i found Open Redirect 

#POC : 
- go to 
https://t.lv.twimg.com/live_video_stream/authorized_status/883213898672783361/LIVE_PUBLIC/DEHOXIMUQAEbRFW?url=https://google.com/&ctx=27_883213898672783361:AAAAEIDslSPDE_gV-wU3Opzr9YAPswhkTvPilFsbz0m-QHi4zZGjkDktKKAldYW9vrXUzlTimnrcBaI0_UMq0VTZFEGi2y28FMWT_64G3uUalicaPAIdaxPuqr-K_5kADwxgi-2kQyrU1R4eh-u73RIpcIAcppkOk6JXBfkoRYNYfUpNiAC6wHtW9j97pYVZtSm-ZTOvx_IWbh26eiHUASipHu8CMTvWPby1Apb8tFpu9L9kIs2KTqNutqTk2cnFeSFVbpS1sCqHsAWCtprwiatM-dFger3FzGLnRTcrxgrbcvOhHUqryeUMq1trAekNsazL8lThiV1ig6f49SUizYIg9sEZq4Wqh5qAi4q1d9nOL8cCRBMVd-qgkvCxl41gjpDO70gHiBnNsreuN5MzcrKZxT7fY0cf0EMrVekTJPELycfBKq0HiwJubeo8tBebB_fFt-cqmFB7PflKdgA22yu4mN_NrvG7vCA5OzAYZIIA5vK7-fdmgkn34abSFKj680-zhHqx2IVLK4zmdeq4SRBSxWbFn-iC5x7HNhogriP3coQc4N1_31d6XOOtexkktpSGVsWZ-Y63xbpN&evt=38617099&exp=1499428143990&checksum=nwUP-VQZpwIBcWj-&noredirect=false

- by converting  ``` &noredirect= ```  from   ``` true ```   to  ``` false ```   i was able to redirect users to any site 
- by clicking on this link you will get redirect to https://google.com  as you can see it on  ``` ?url= ```

{F201033}

Thanks

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
