---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '484615'
original_report_id: '484615'
title: Unsanitized user photo paths allow local file read
weakness: Business Logic Errors
team_handle: vanilla
created_at: '2019-01-23T11:16:20.844Z'
disclosed_at: '2019-07-13T04:27:29.324Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: https://github.com/vanilla/vanilla/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Unsanitized user photo paths allow local file read

## Metadata

- HackerOne Report ID: 484615
- Weakness: Business Logic Errors
- Program: vanilla
- Disclosed At: 2019-07-13T04:27:29.324Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
When we register a new user, we can set the photo of user.  If we set a milicious path, we can delete the profile photo of others

**Description:**
There is an episode of register.
applications/dashboard/controllers/class.entrycontroller.php
```
    private function registerBasic() {
        $this->View = 'registerbasic';
        Gdn::userModel()->addPasswordStrength($this);

        if ($this->Form->isPostBack() === true) {
            // Add validation rules that are not enforced by the model
            $this->UserModel->defineSchema();
            $this->UserModel->Validation->applyRule('Name', 'Username', $this->UsernameError);
            $this->UserModel->Validation->applyRule('TermsOfService', 'Required', t('You must agree to the terms of service.'));z
            $this->UserModel->Validation->applyRule('Password', 'Required');
            $this->UserModel->Validation->applyRule('Password', 'Strength');
            $this->UserModel->Validation->applyRule('Password', 'Match');
            // $this->UserModel->Validation->applyRule('DateOfBirth', 'MinimumAge');

            $this->fireEvent('RegisterValidation');

            try {
                $values = $this->Form->formValues(); //1
                $values = $this->UserModel->filterForm($values, true); //2
                unset($values['Roles']);
                $authUserID = $this->UserModel->register($values);//3
```
Get form values and filter many fields in UserModel. But I find there are 23 fields in GDN_User remains
```
About
Banned
Confirmed
CountBookmarks
CountDrafts
CountUnreadConversations
CountUnreadDiscussions
DateOfBirth
DateSetInvitations
Email
Gender
HashMethod
HourOffset
InviteUserID
Location
Name
Password
Photo
Points
ShowEmail
Title
UserID
Verified
```
In UserModel::removePicture, it delete the local file according to photo field. But in step 2, it call changeBasename to add prefix 'p' in basename. So we can only delete the filename starts with 'p' in uploads directory
```
    public function removePicture($userID) {
        // Grab the current photo.
        $user = $this->getID($userID, DATASET_TYPE_ARRAY); //1
        $photo = $user['Photo'];

        // Only attempt to delete a physical file, not a URL.
        if (!isUrl($photo)) {
            $profilePhoto = changeBasename($photo, 'p%s'); //2
            $upload = new Gdn_Upload();
            $upload->delete($profilePhoto); //3
        }

        // Wipe the Photo field.
        $this->setField($userID, 'Photo', null);
    }
```

## Steps to reproduce:

1. find other user's photo url to delete (eg: uploads/userpics/868/pT8SSG8E4EYSK.png)
2. register a new user and intercept the request
3. add a field `Photo`, set the value as `userpics/868/T8SSG8E4EYSK.png`(without prefix p)
4. login, and request /vanilla/index.php?p=/profile/removepicture/**yourusername**&tk=**yourtk**&deliveryType=ALL
Then the local file uploads/userpics/868/pT8SSG8E4EYSK.png will be deleted

## Anything else we should know?
Because of the path restriction, only filepath matchs `uploads/*/p*` can be deleted.
Whitelist may better than blacklist, only a few fields should be permitted to insert into database where registration

## Impact

be able to delete profile photo of others

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
