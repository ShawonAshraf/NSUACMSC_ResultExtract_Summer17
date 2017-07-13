from Extractor import Extractor
from InfoToTextFile import RecordEntry

excelFile = "FinalResult.xlsx"
mailingListFile = "Mailing/MailingList.csv"

# list of emails, to be written to a text file
mail_list = []

# now to action!

# create record writer instance

recWriter = RecordEntry()

# extract mail
extractor = Extractor(workBookPath=excelFile)
mail_list = extractor.extractAllEmailAddress()

# write to file
recWriter.writeRecords(text_file=mailingListFile, records=mail_list)

# get team records by name and write mail lists or full info
# writing mailing lists here
teamNames = ["Corporate", "Operations", "Publications", "Promotions", "Logistics"]
stats = {}

for teamName in teamNames:
    recordsFile = "Mailing/{}.csv".format(teamName)
    records = extractor.extractRecordByTeam(teamName=teamName)
    stats[teamName] = len(records)

    recWriter.writeRecords(text_file=recordsFile, records=records)

print(stats)
total = 0
print("===================Stats :::::::::::::: Summer 17 ===================")
for t in teamNames:
    print("\t\t{} : {}".format(t, stats[t]))
    total = total + stats[t]

print("\t\tTotal Recruited : {}".format(total))
