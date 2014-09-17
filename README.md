Learning Python Sep 16, 2014
===============

A lot of this code is *half-baked*, all too often, from blogs/tutorials/such,
but I did run/test most of it and made corrections. 

> Warning ... mini-rant:
>
> Hey, look at that, a date right there in the title. 
> Good idea, huh?  
> So much stuff on the internet does not have a date. 
> Even worse some blogs just have a month and day.
> Guess what ... every year has the same month/day, well, except Feb. 
> How can anyone know that what they are reading is even remotely up-to-date.
> Is it really that difficult to add a full date.

***

### multiprocessing

Read that as **fork**, but it still looks useful if one remains
mindful of the consequences of launching too many children. Of 
course, there's always one child who fails to launch ;)

### picamera

Mostly this is about learning how to use picamera for a Raspberry Pi (RPi). 
To create a working motion detector which uses tcp to stream images to another server.
This will avoid creating/deleting images on the sd card.  Perhaps I could
use multiprocessing to create a temporary daemon to handle the sending of each
image, so the main program can resume motion detection more quickly -- i.e.
less latency.

> Note that this setup is **not very secure**, but hey, I'm mostly watching 
the neigbor's cat prowl around for food, yes, I fed it once and now we have a "relationship".  
Not a lot of evil doers up here in the mountains. 
But it's a fun project to justify spending $40 on a raspberry pi.
Yes, I did spend $60 on a Banana Pi (BPi) which just sits over there blinking, but 
it can have a real sata drive attached ... if I ever get to that project. I'm
fairly certain that super bright green led on the BPi is hailing the mothership.

### scapy

Looks interesting to work alongside snort: reading pcap's, sniffing, etc.

### flask

It's sort of, kind of like ruby on rails.
I'm leaning more towards flask than django (reminds me of a violent movie).
Currently I'm learning flask via videos like this:
https://www.youtube.com/watch?v=AeI_rBeZmwg&list=UUt7yOnL7bI7yCa1Xe_GTjJQ

### curiosities:

* **google drive** ... doesn't work well when automated as it seems a user must present, and I even tried using a **service account** without luck ... this is a tough nut, but I guess I could use **grive**
* **pgist** ... for command line, but could be forked for use in a program which would be nice to upload a **.geojson** file to a gist which creates a map automagically
* **mysql** ... seems there are way too many db connectors, confusing, pick one already
* **pygeoip** ... lookup IP's in GeoLiteCity.dat to get lat/lng/country
* **email** ... simple smtp send mail
* **elasticsearch** ... for fast indexing/searching
* **matplotlib** ... plotting

Love the language Ruby, but is there anything Python doesn't provide as a package, and the 
syntax sure is simple to learn. Once you get the knack of that indentation/colon thing. 
Not to mention that it's already installed just about everywhere, even on a RPi/BPi.

***
