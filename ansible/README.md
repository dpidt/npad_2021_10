# Ansible
## Installation
Die Installation der aktuellen Version kann auf einem Ubuntu-System bei Bedarf aus dem offiziellen Repository erfolgen. Der Ablauf, der dieses hinzufügt und ansible installiert ist:
```
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt remove ansible
sudo apt update
sudo apt install ansible
```

## Ausführung
Die beiden Beispiele lassen sich im Terminal wie folgt verwenden. Loggen Sie sich zuvor jedoch einmal manuell per ssh auf jedem der vier Switches ein, damit ihr System die ssh-Keys akzeptiert.
```
ansible-playbook -i 192.168.181.21, -u admin -k -e ansible_network_os=nxos first_nxos_playbook.yml
ansible-playbook -i inventory -k second_nxos_playbook.yml
```
Die Dokumentation ist zu finden auf: https://docs.ansible.com/ansible/2.8/modules/list_of_network_modules.html#nxos


## Aufgaben
1. Stellen sie sicher, dass beide Beispiele funktionieren.
2. Erweitern Sie das zweite Beispiel so, dass zusätzlich noch die Modellbezeichnungen und die Lizenz-IDs angezeigt werden (Die Dokumentation von `nxos_facts` liefert Ihnen dazu hilfreiche Hinweise.).
3. Suchen sie ein passendes Modul für die VLAN-Konfiguration. Sie können z. B. versuchen sicherzustellen, das eine bestimmte Liste von VLANs auf allen Devices vorhanden ist.
