from w3champions import *

svc = RankingService()
print(svc.searchRankings("Happy", Gateways.Europe, EGameMode.GM_1ON1, 8))