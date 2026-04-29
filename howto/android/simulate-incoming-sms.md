(howto-simulate-incoming-sms)=
# Simulate incoming SMS messages

This guide demonstrates how to simulate incoming SMS messages for Android. Android processes the messages and displays them using its messaging application and with the right configuration, it can also provide notifications for received messages.

## Prerequisites

To simulate an incoming SMS message, you need an Android (14 or newer) instance. Note that AAOS is not supported currently.

Launch a new instance:

    amc launch --name test0 jammy:android15:amd64

Wait until the instance gets to running status before simulating a message.

## Use HTTP API to simulate a new SMS message

To simulate an incoming SMS message we will use the {ref}`Anbox runtime HTTP API <anbox-https-api>`. Every Anbox API image provides a helper named `anbox-api` which simplifies accessing the HTTP in scripts or at the command line.

In order to now simulate a new incoming SMS message, you can simply run

    amc exec test0 -- anbox-api send-sms +12344536 "Hello world!"

This will ask the modem simulator provided by the Android runtime to send the necessary notification to the Android telephony stack. Once received, Android will show the SMS message in its messaging app and depending on the Android version also as notification.
