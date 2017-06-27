# Flightradar24 fr24feed daemon
The Flightradar24 fr24feed daemon as a Snap package. [![Snap Status](https://build.snapcraft.io/badge/TheBiggerGuy/fr24feed.svg)](https://build.snapcraft.io/user/TheBiggerGuy/fr24feed)


# Ussage

## Install
```bash
sudo snap install fr24feed
```

## Configure
```bash
sudo snap set fr24feed fr24key="YOUR_KEY"
sudo snap set fr24feed reciver="dvbt"
```

## Update
```bash
sudo snap refresh fr24feed
```

## View Logs
```bash
sudo journalctl -u snap.fr24feed.fr24feed.service
```
