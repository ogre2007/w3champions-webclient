import json
import requests
from typing import Sequence, List, Callable, TypeVar, Union, Iterable
from enum import Enum

from dacite import from_dict, Config

from store.ranking.types import (
                      Ranking,
                      Gateways,
                      Ladder,
                      Season,
                      CountryRanking,
                    )
from store.typings import EGameMode

T = TypeVar('T')               
API_URL = 'https://website-backend.w3champions.com/'
Response = Union[Iterable[T], T]

def get_to_data_class(url: str, cls: T) -> Response[T]:
    r = requests.get(url).text
    r = json.loads(r)
    print(r)
    print(url)
    if isinstance(r, list):
        result = []
        for x in r:
            try:
                result.append(from_dict(data_class=cls, data=x, config=Config(cast=[Enum])))
            except ValueError as e:
                if cls == Ladder:
                    pass
                
    else:
        result = from_dict(data_class=cls, data=r, config=Config(cast=[Enum]))
    return result
        
class RankingService(object):
    def retrieveRankings(self,
        leagueId: int,
        gateway: Gateways,
        gameMode: EGameMode,
        season: int)-> List[Ranking]:
        url = f'{API_URL}api/ladder/{leagueId}?gateWay={gateway}&gameMode={gameMode}&season={season}'
        
        return get_to_data_class(url, Ranking)

    def retrieveCountryRankings(self,
        countryCode: str,
        gateway: Gateways,
        gameMode: EGameMode,
        season: int) -> List[CountryRanking]:
        url = f'{API_URL}api/ladder/country/{countryCode}?gateWay={gateway}&gameMode={gameMode}&season={season}'

        return get_to_data_class(url, CountryRanking)
    

    def searchRankings(self, 
        searchee: str,
        gateway: Gateways,
        gameMode: EGameMode,
        season: int
    ) -> List[Ranking]:
        url = f'{API_URL}api/ladder/search?gateWay={gateway}&searchFor={searchee}&gameMode={gameMode}&season={season}'
        return get_to_data_class(url, Ranking)
    

    def retrieveLadders(self, season: int) -> List[Ladder]:
        url = f'{API_URL}api/ladder/league-constellation?season={season}'
        return get_to_data_class(url, Ladder)
    

    def retrieveSeasons(self) -> List[Season]:
        url = f'{API_URL}api/ladder/seasons'
        return get_to_data_class(url, Season)
        
if __name__ == '__main__':
    svc = RankingService()
    #result = svc.retrieveRankings(1, Gateways.Europe, EGameMode.GM_1ON1, 8)
    #result = svc.retrieveCountryRankings('RU', Gateways.Europe, EGameMode.GM_1ON1, 8)
    #result = svc.retrieveSeasons()
    #result = svc.retrieveLadders(8)
    result = svc.searchRankings("Happy", Gateways.Europe, EGameMode.GM_1ON1, 8)
    print(result)