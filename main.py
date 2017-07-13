from Extractor import Extractor
from InfoToTextFile import RecordEntry

excelFile = "FinalResult.xlsx"
mailingListFile = "Mailing/MailingList.txt"

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

# for stats
stats = {}
total = 0

for teamName in teamNames:
    teamMailingFile = "Mailing/{}.txt".format(teamName)
    mail_list = extractor.getEmailByTeam(teamName=teamName)
    recWriter.writeRecords(text_file=teamMailingFile, records=mail_list)

    total = total + len(mail_list)
    stats[teamName] = len(mail_list)

print("====================STATS=====================")
print("===================Summer17===================")
print("\n\nTotal recruited : {}\n".format(total))
for teamName in teamNames:
    print("{} : {}".format(teamName, stats[teamName]))