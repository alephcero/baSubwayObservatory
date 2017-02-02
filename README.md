# baSubwayObservatory
This is a project for monitoring subway activity based on Buenos Aires City [open data portal](http://data.buenosaires.gob.ar). The overall objective is to provide information about train frequency, train usage and problems in stations with train dispatch. You can see base analytics in the [wiki](https://github.com/alephcero/baSubwayObservatory/wiki). 

## Terminals

The terminals labeled as 1 are the ones in the periphery of the city, while the ones labeled as 2 are located in the city center. The exceptions are lines **C** and **H**, which have a transversal layout [1](http://data.buenosaires.gob.ar/dataset/subte-cronograma-de-servicio/resource/69c895c4-31de-4613-9b10-ec4e47d6b1c0). **P** line doesn't have a terminal 2. 


## Pending tasks

* Check if data is updated and downloaded the rest
* Get rush hours from actual data
* Produce "Your commute" using first line an hour using only the terminal stations (this will tell how lonk takes the subway to come). Future versions say at what time arrives based on the distance (% of distance used as proxy for % of time that take to be there ffrom the nearest terminal)  then stations 




## Analysis

### Waiting time BA subway by line
![Waiting time BA subway by line](img/plot.png?raw=true "Waiting time BA subway by line")

### Rush Hour for all lines
![Rush Hour for all lines](img/rushHourAllLines.png?raw=true "Rush Hour for all lines")

### Rush Hour by line
![Rush Hour by line](img/rushHourPerLine.png?raw=true "Rush Hour by line")
 
### Rush Hour by station
![Rush Hour by station](img/rushHourByStation.png?raw=true "Rush Hour by station")	
