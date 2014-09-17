Learning Python
===============

A lot of this code is *half-baked*, all too often, from blogs/tutorials/such,
but I did run/test most of it and made corrections.

### multiprocessing

Read that as **fork**, but it still looks useful if one remains
mindful of the consequences of launching too many children.

### picamera

Mostly this is about learning how to use picamera for a Raspberry Pi. 
To create a working motion detector which uses tcp to stream images to another server.
This will avoid creating/deleting images on the sd card.  Perhaps I could
use multiprocessing to a temporary daemon to handle the sending of each
image, so the main program can resume motion detection more quickly -- i.e.
less latency.

> Note that this setup is **not very secure**, but hey, I'm mostly watching 
a cat that's prowling around for food.  Not a lot of evil doers up here in 
the mountains.

### scapy

Looks interesting to work alongside snort.

