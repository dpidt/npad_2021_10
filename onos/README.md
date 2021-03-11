#  ONOS
## Der Container
Auf Basis des vorhandenen Image lässt sich ein Container mir dem folgenden Befehl starten, und mit der notwendigen Konnektivität zum Host-System versehen:
```
sudo docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos251 onosproject/onos:2.5.1
```
Nach kurzer Zeit ist dann das Dashboard des Containers erreichbar unter:
http://localhost:8181/onos/ui/login.html (onos/rocks)

Die API-Dokumentation findet sich unter:
http://localhost:8181/onos/v1/docs/	(onos/rocks) 

Der Docker CLI-Client beantwortet auch viele weiteren Fragen zu Containern.

Welche Container laufen?
```
sudo docker ps
```
Welche Container gibt es?
```
sudo docker ps -a
```
Einen Container stoppen:
```
sudo docker stop onos251
```
Einen Container wieder starten:
```
sudo docker start onos251
```

Die Shell des Onos-Containers erreichen Sie bei Bedarf mit:
```
sudo docker exec -it onos251 bash
```

## Testinfrastruktur
Um in der Lage zu sein eine Testinfrastruktur flexibel anpassen zu können wird diese auf den lokalen System mit Hilfe von mehreren Open-vSwitch-Instanzen realisiert. Ein hilfreiches Werkzeug, um diese nicht selbst starten und 'vernetzen' zu müssen, ist Mininet. 

Die Installation erfolgt mit:
```
sudo apt-get install mininet
```
Ein einfacher Funktionstest ist:
```
sudo mn --test pingall
```
Mininet wird später eine Konsole zur Verfügung stellen. Beispiele für dort funktionierende Befehle sind:
```
h1 ping h5
link s1 s3 down
link s1 s3 up
xterm h1
```
Für die Funktion des letzten Befehls ist auf dem lokalen System evtl. die Installation von `xterm` (`sudo apt-get install xterm`) notwendig.

# Aufgabe (normalerweise im TEAM): Host2Host-Intent-App für ONOS
## Teil 0:
Machen Sie sich mit dem Controller-Dashboard vertraut.
Die folgenden ONOS-Applikationen sollten aktiviert sein/werden:
- Default Drivers 
- Host Location Provider
- LLDP Link Provider
- ONOS GUI2
- OpenFlow Base Provider
- Optical Network Model
- Proxy ARP/NDP
- (Reactive Forwarding)

Starten Sie, bei laufendem Controller, mit Mininet die Testtopologie `mytop.py` und stellen Sie sicher, dass diese im ONOS-Dashboard sichtbar ist. Der Befehl dazu findet sich in `mn_example.txt`.

## Teil 1:
Erweitern Sie die Mininet-Topologie auf mindestens sechs Hosts und drei Switches (Ein Mininet Neustart mit neuer Topologie ist danach erforderlich).
Mininet lässt sich beenden im dortigen Prompt mit `exit`. 

## Teil 2:
Deaktivieren sie auf ONOS die Funktion "Reactive Forwarding".
Legen Sie im Dashboard einen Host-to-Host-Intent an und verifizieren Sie diesen.
Versuchen Sie nun mit Hilfe der API-Dokumentation einen zweiten, unterschiedlichen Intent über die REST-API anzulegen (z. B. mit dem API-Dashboard oder Postman) und verifizieren Sie diesen z. B. durch einen Ping in der Mininet-Konsole.

## Teil 3:
Entwickeln Sie eine Applikation (z.B.) in Python, die die ONOS-API nutzt um alle bekannten Hosts zu ermitteln.

## Teil 4:
Entwickeln Sie eine Applikation dann die den Host mit der niedrigsten IP-Adresse mit dem mit der höchsten IP-Addresse (im Netz 10.0.0.0/24) per Host2Host-Intent verbindet ohne direkt die Adressen anzugeben.

## Teil 5 (BONUS):
Modifizieren Sie das Python Skript so, dass bei jedem Start die  Topologie unterschiedlich aussehen kann, um so zu testen, dass ihre Applikation auch damit funktioniert.

Verwenden Sie in Python dazu z. B. `from random import randrange, choice` und die entsprechenden Funktionen.
***

## Hinweise:
- Ein Beispiel für einen Python-request an eine andere URL finden Sie im Repository
- Eine Hilfe für die Teile 3 und 4 liefert das Skript im Ordner "help".
- Die benötigten URIs finden sie unter Hosts/Intent in der API-Dokumentation des Controllers.
