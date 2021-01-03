# Sunset-Airplane-Notification
I want to get notified near sunset if any interesting planes are about to land.

I love airplanes, and I especially enjoy watching them with my binoculars as they approach my local airport - Phoenix Sky Harbor -  near sunset.  However, Phoenix Sky Harbor doesn't have a great diversity of planes.  It's mostly dominated by Airbus A320s and Boeing 737s.  I've seen so many of these over the years, I would like my attention drawn to other interesting planes, such as an Airbus A330, or a Boeing 757, or a Boeing 747.

### To generate the notifications I want I will need to:
 1. identify when sunset is each day for my location
 1. run a chron job to determine 20 minutes before sunset
 1. identify incoming flights 20 minutes before sunset
 1. filter for only interesting incoming flights
 1. text me:
    - the aircraft type 
    - origin of the flight 
    - the expected arival time 
