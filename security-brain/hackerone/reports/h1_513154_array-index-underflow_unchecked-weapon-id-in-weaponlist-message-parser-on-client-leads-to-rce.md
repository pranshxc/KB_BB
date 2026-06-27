---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '513154'
original_report_id: '513154'
title: Unchecked weapon id in WeaponList message parser on client leads to RCE
weakness: Array Index Underflow
team_handle: valve
created_at: '2019-03-21T13:30:56.037Z'
disclosed_at: '2019-09-17T17:34:14.845Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 226
asset_identifier: hl.exe
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- array-index-underflow
---

# Unchecked weapon id in WeaponList message parser on client leads to RCE

## Metadata

- HackerOne Report ID: 513154
- Weakness: Array Index Underflow
- Program: valve
- Disclosed At: 2019-09-17T17:34:14.845Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Let's look at WeaponList message parser code in the HLSDK:
``` cpp
int CHudAmmo::MsgFunc_WeaponList(const char *pszName, int iSize, void *pbuf )
{
	BEGIN_READ( pbuf, iSize );
	
	WEAPON Weapon;

	strcpy( Weapon.szName, READ_STRING() );
	Weapon.iAmmoType = (int)READ_CHAR();	
	
	Weapon.iMax1 = READ_BYTE();
	if (Weapon.iMax1 == 255)
		Weapon.iMax1 = -1;

	Weapon.iAmmo2Type = READ_CHAR();
	Weapon.iMax2 = READ_BYTE();
	if (Weapon.iMax2 == 255)
		Weapon.iMax2 = -1;

	Weapon.iSlot = READ_CHAR();
	Weapon.iSlotPos = READ_CHAR();
	Weapon.iId = READ_CHAR();
	Weapon.iFlags = READ_BYTE();
	Weapon.iClip = 0;

	gWR.AddWeapon( &Weapon );

	return 1;
}
```

And `WeaponResource::AddWeapon`:

``` cpp
void AddWeapon( WEAPON *wp ) 
{ 
		rgWeapons[ wp->iId ] = *wp;	
		LoadWeaponSprites( &rgWeapons[ wp->iId ] );
}
```
There are no boundary check, and the range of `iId` is `[-128, 128)`, so I can modify many things in the data section.

In `client.dll`, there's an object called `gEngfuncs`, it is a function table that has various functions of the engine. After some calculations on latest CS 1.6 `client.dll`, I concluded that this function table could be overwritten using the above bug.

I have attached a PoC that will pop `calc.exe` on latest CS 1.6 client when connected to malicious server. The AMXX plugin will catch `InitHUD` message, and send crafted `WeaponList` message to overwrite the address of function used in `HUD_DirectorMessage` to execute client cmds to a ROP gadget that will trigger the chain sent in the next `SendCmd` call. To overwrite that address, I used a crafted weapon sprite list (`weapon_pwn.txt`) (see `WEAPON` struct, file `cl_dll/ammo.h` in the HLSDK).

## Impact

Since it's RCE, attacker can do almost anything that don't require higher privilege (ex. compromise account, inject malware, ...)

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
