### Counter Strike Player Stats
Uses Beautiful soup to get the latest tracker details from www.gametracker.com and calcuate the Efficacy of each player

### Game Info
1. server details
```sh
connect 108.61.124.73:27035; password <password>
```
2. discord Channels
- Blue Channel: https://discord.gg/wTvZB4ZK
- Red Channel: https://discord.gg/REgMMwKr

3. admin commands
- clan setup
```sh
rcon exec clan.cfg
```
**note** settings: C4timer=35, maptime=1.75, freezetime=6
- pub setup
```sh
rcon exec pub.cfg
```
**note** settings: C4timer=45, maptime=3, freezetime=3

### Efficacy
- What is Efficacy
`the ability to produce a desired or intended result.`
- How is Efficacy calculated: **Neo's efficacy algorithm**
```sh
(Efficacy Coefficient - Time played / Total Score) + Score Per Minute
```
**note** Efficacy coefficient == 1
- Why is it calculated like this
` i dont know these are the only things i could get from the server `

### Install
```sh
pipenv install
```

### run
```sh
make index
```