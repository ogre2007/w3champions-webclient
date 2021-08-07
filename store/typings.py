#import { Moment } from "moment";
from store.ranking.types import Gateways, EGameMode, ERaceEnum 
#from collections.abc import Sequence
from typing import Optional, Sequence, List
from dataclasses import dataclass
from enum import Enum
import json

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class PlayerServerInfo:
    battleTag: str
    averagePing: int
    currentPing: int

@dataclass_json
@dataclass(frozen=True)
class ServerInfo:
    provider: str
    countryCode: str
    location: str
    name: str
    nodeId: int
    playerServerInfos: List[PlayerServerInfo]
    
js = '{"provider": "123", "countryCode": "123", "location": "123",  "name": "123",  "nodeId": 123, "playerServerInfos":[{"battleTag": "suka123", "averagePing": 123, "currentPing": "23"}]}'.strip()
d = json.loads(js)
print(ServerInfo.from_json(js))
#print(ServerInfo.schema().loads(js, many=True)[0].battleTag)

class EPick(Enum):
    OVERALL = 0,
    FIRST = 1,
    SECOND = 2,
    THIRD = 3,


class UnitScore:
    unitsProduced: int
    unitsKilled: int
    largestArmy: int


class Hero:
    icon: str
    level: int


class HeroScore:
    heroesKilled: int
    itemsObtained: int
    mercsHired: int
    expGained: int


class ResourceScore:
    goldCollected: int
    lumberCollected: int
    goldUpkeepLost: int


class PlayerScore:
    battleTag: str
    unitScore: UnitScore
    heroes: List[Hero]
    heroScore: HeroScore
    resourceScore: ResourceScore


class EAvatarCategory(Enum):
    RANDOM = 0,
    HUMAN = 1,
    ORC = 2,
    NIGHT_ELF = 4,
    UNDEAD = 8,
    TOTAL = 16,
    SPECIAL = 32,

class ELocaleFlags(Enum):
    EN = 'src/assets/localeFlags/en.svg',
    DE = 'src/assets/localeFlags/de.svg'


class Player:
    race: int
    oldMmr: int
    currentMmr: int
    battleTag: str
    name: str
    id: str
    mmrGain: int
    won: bool
   
    
@dataclass_json
@dataclass
class RootState:
    darkMode: bool
    gateway: Gateways
    locale: str

class DataTableOptions:
    sortDest: bool
    page: int
    itemsPerPage: int

class PlayerInTeam:
    oldMmr: int
    currentMmr: int
    battleTag: str
    name: str
    mmrGain: int
    race: ERaceEnum
    rndRace: ERaceEnum
    won: bool
    location: Optional[str]
    countryCode: Optional[str]
    twitch: Optional[str]


class Team:
    players: List[Player]
    won: Optional[bool]

class Match:
    map: str
    id: int
    durationInSeconds: int
    int: int
    #startTime: Moment
    #endTime: Moment
    gameMode: EGameMode
    teams: List[Team]
    gateWay: int
    season: int
    serverInfo: ServerInfo

class MatchDetail:
    match: Match
    playerScores: List[PlayerScore]
