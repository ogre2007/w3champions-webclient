# w3champions-webclient
A python web client for https://www.w3champions.com/

## Why?
Because I do not know how to use JS from my python projects efficiently, hence I ported some JS code from https://github.com/w3champions/website to the Python :)
My API is fully compatible with w3c websites' one, but not all the services are ported yet.

## How?
Just download these files in your project and add `from w3champions import *` .
Then you can call essential services as follows: 
```
from w3champions import *

svc = RankingService()
print(svc.searchRankings("Happy", Gateways.Europe, EGameMode.GM_1ON1, 8))
```

## TODO:
add another services

