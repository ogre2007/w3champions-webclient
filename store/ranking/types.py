from enum import Enum, IntEnum
from typing import Sequence, Optional, List
from dataclasses import dataclass
from dacite import from_dict, Config


@dataclass
class WinLoss:
  wins: int;
  losses: int;
  winrate: float;
  games: int;


@dataclass
class PlayerId:
    name: str
    battleTag: str


@dataclass
class PlayerOverview(WinLoss):
    id: str
    name: str
    mmr: int
    gateWay: int
    playerIds: List[PlayerId]
    gameMode: Optional[int]
    season: Optional[int]
    race: Optional[int]


@dataclass
class EGameMode(IntEnum):
    UNDEFINED = 0,
    GM_1ON1 = 1,
    GM_2ON2 = 2,
    GM_2ON2_AT = 6,
    GM_4ON4 = 4,
    GM_FFA = 5,
    GM_FOOTMEN_FRENZY = 101,

    GM_LEGION_4v4_X3 = 201,
    GM_LEGION_4v4_X20 = 202,
    GM_LEGION_1v1_x20 = 203,
    
    GM_ROC_1ON1 = 301,

    GM_LTW_1ON1 = 401,


@dataclass
class ERaceEnum(IntEnum):
    RANDOM = 0,
    HUMAN = 1,
    ORC = 2,
    NIGHT_ELF = 4,
    UNDEAD = 8,
    TOTAL = 16,
    

@dataclass
class PlayerInfo:
    calculatedRace: ERaceEnum
    selectedRace: int
    pictureId: int
    isClassicPicture: bool
    twitchName: Optional[str]
    clanId: Optional[str]
    country: Optional[str]
    countryCode: Optional[str]
    location: str
    

@dataclass
class Gateways(IntEnum):
    America = 10,
    Europe = 20,
    Asia = 30,
    

@dataclass
class Season:
    id: int
    

@dataclass
class League:
    id: int
    name: str
    order: int
    division: int
    maxParticipantCount: Optional[int]
    

@dataclass
class Ladder:
    gateway: Gateways
    gameMode: EGameMode
    season: int
    leagues: List[League]
    

@dataclass
class Ranking:
    id: str
    season: int
    gateway: int
    league: int
    leagueDivision: int
    leagueOrder: int
    race: ERaceEnum
    leagueName: Optional[str]
    rankNumber: int
    rankingPoints: int
    gameMode: EGameMode
    player: PlayerOverview
    playersInfo: Optional[List[PlayerInfo]]

js = '{"gateway": 20, "id": "8_Lyn#52841@20_GM_1v1_RnD", "league": 1, "leagueDivision": 0, "leagueName": null, "leagueOrder": 0, "rankNumber": 1, "rankingPoints": 6955, "race": 0, "playerId": "8_Lyn#52841@20_GM_1v1_RnD", "player1Id": "Lyn#52841", "player2Id": null, "player": {"playerIds": [{"name": "Lyn", "battleTag": "Lyn#52841"}], "name": "Lyn", "id": "8_Lyn#52841@20_GM_1v1_RnD", "mmr": 2006, "gateWay": 20, "gameMode": 1, "season": 8, "race": 0, "wins": 38, "losses": 27, "games": 65, "winrate": 0.5846153846153846}, "gameMode": 1, "season": 8, "playersInfo": [{"battleTag": "Lyn#52841", "calculatedRace": 2, "selectedRace": 2, "pictureId": 1, "isClassicPicture": true, "country": null, "countryCode": null, "location": "CN", "twitchName": null, "clanId": null, "playerAkaData": {"id": 204, "name": "Lyn", "main_race": "Orc", "country": "kr", "liquipedia": "Lyn"}}]}'
import json
#d = json.loads(js)
#print(js)
#print()


@dataclass
class CountryRanking:
    league: int
    leagueName: str
    leagueDivision: int
    leagueOrder: int
    ranks: List[Ranking]
    

@dataclass  
class RankingState:
    league: int
    working: bool
    page: int
    totalRanks: int
    ladders: List[Ladder]
    rankings: List[Ranking]
    topFive: List[Ranking]
    searchRanks: List[Ranking]
    countryRankings: List[CountryRanking]
    countryRankingsLoading: bool
    gameMode: EGameMode
    seasons: List[Season]
    selectedSeason: Season
    selectedCountry: str















