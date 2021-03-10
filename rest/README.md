# HTTP und REST
## RKI-API CORONA
Der Link zur API lautet:
```
https://api.corona-zahlen.org/docs/
```

## NXAPI-CLI
Das Aufrufen der Device-IP im Webbrowserliefert über die NXAPI-Sandbox einen einfachen Zugang zur NXAPI-CLI.

## NXAPI-Rest
Cisco's NX-OS Plattform verfügt in aktuellen Releases über eine REST-API für Nexus 3000/9000. Die Dokumentation findet sich z. B. für den 9.2 Release unter https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-2x/ .

## Postman
Postman ist ein weitverbreitetes Werkzeug zum Test von REST-APIs. Hervorgegangen aus einer Erweiterung für Chrome, handelt es sich nun um eine eigenständige App, zu finden unter https://www.postman.com/ .

Unter anderem erlaubt postman das Zusammenstellen/Teilen/Importieren/etc. von Request-Collections.

Im Labor lässt sich Postman am einfachsten über das Terminal mit dem folgenden Befehl installieren:
```
sudo snap install postman
```

## Übung 1
Nutzen sie die CORONA-API um mit Postman die Daten für einen Landkreis Ihrer Wahl abzufragen.

Der Endpunkt dazu ist ersichtlich aus der entsprechenden Dokumentation:
'''
https://api.corona-zahlen.org/docs/endpoints/districts.html#districts-ags
'''

Dort benötigen sie die ersten fünf Ziffern des Allgemeinen Gemeinde Schlüssel (AGS) z.B. aus:
'''
https://www.riserid.eu/data/user_upload/downloads/info-pdf.s/Diverses/Liste-Amtlicher-Gemeindeschluessel-AGS-2015.pdf
'''

## Übung 2
Nutzen Sie Postman und die API-Dokumentation um einen BGP-Nachbarn zu konfigurieren. Dazu muss eventuell erst über die API ein BGP-Router konfiguriert werden. 

Nur ein Teilnehmer kann die AS-Nummer und Router-ID konfigurieren. Danach muss es konistent bleiben.

Beispiele für sinnvolle Requests finden sie in der bereitgestellten Postman-Collection.
