from Extractor import Extractor

class Stats:
    def getAllStats(self, workbook):
        extractor = Extractor(workBookPath=workbook)
        teamNames = ["Corporate", "Operations", "Publications", "Promotions", "Logistics"]

        # for stats
        teamRecords = extractor.extractAllTeamRecords()
        stats = {}
        total = 0

        for teamName in teamNames:
            total = total + len(teamRecords[teamName])
            stats[teamName] = len(teamRecords[teamName])

        print("====================STATS=====================")
        print("===================Summer17===================")

        print("\n\nTotal recruited : {}\n".format(total))

        for teamName in teamNames:
            print("{} : {}".format(teamName, stats[teamName]))
