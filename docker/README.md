# Docker
Für die die spätere SDN-Anwendungen wird ein Controller in einem Docker-Container betrieben. Das dazu notwendige Image und docker müssen jedoch erst im folgenden Ablauf verfügbar gemacht werden.

**VPN Verbindung beenden (wenn zutreffend)**

Die Anleitung dazu ist:
```
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```

**Test:**
```
sudo docker run hello-world
```
**Bitte diesen Image pull starten:**
```
sudo docker pull onosproject/onos:2.5.1
```
