from RankingService import RankingService, Gateways, Ladder, Season, EGameMode


if __name__ == '__main__':
    svc = RankingService()
    result = svc.searchRankings("Happy", Gateways.Europe, EGameMode.GM_1ON1, 8)
