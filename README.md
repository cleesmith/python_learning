Learning Python
===============

A lot of this code is *half-baked*, all too often, from blogs/tutorials/such,
but I did run/test most of it and made corrections.

### multiprocessing

Read that as **fork**, but it still looks useful if one remains
mindful of the consequences of launching too many children. Of 
course, there's always one child which fails to launch ;)

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

### curiosities:

* **google drive** ... doesn't work well when automated as it seems a user must present, and I even tried using a **service account** without luck ... this is a tough nut, but I guess I could use **grive**
* **pgist** ... for command line, but could be forked for use in a program which would be nice to upload a **.geojson** file to a gist which creates a map automagically
* **mysql** ... seems there are way too many db connectors
* **flask** ... sort of, kind of like ruby on rails ... leaning more towards flask than django (assuming it's like the movie)
* **pygeoip** ... lookup IP's in GeoLiteCity.dat to get lat/lng/country
* **email** ... simple smtp send mail
* **elasticsearch** ... for fast indexing/searching
* **matplotlib** ... plotting
