(howto-simulate-incoming-sms)=
# Simulate incoming SMS messages

This guide demonstrates how to simulate incoming SMS messages for Android. Android will process and show such message inside its messaging application and depending on configuration also provide notifications for received messages.

## Prerequisites

In order to simulate an incoming SMS message you need an Android (14 or newer) instance. AAOS is not supported currently. If you have not created one yet, you can do so by running

    amc launch --name test0 jammy:android15:amd64

Once the instance is up and running you can continue with the next steps.

## Use HTTP API to simulate a new SMS message

To simulate an incoming SMS message we will use the {ref}`Anbox runtime HTTP API <anbox-https-api>`. Every Anbox API image provides a helper named `anbox-api` which simplifies accessing the HTTP in scripts or at the command line.

In order to now simulate a new incoming SMS message, you can simply run

    amc exec test0 -- anbox-api send-sms +12344536 "Hello world!"

This will ask the modem simulator provided by the Android runtime to send the necessary notification to the Android telephony stack. Once received, Androild will show the SMS message in its messaging app and depending on the Android version.


