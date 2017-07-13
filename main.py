from Extractor import Extractor
from InfoToTextFile import RecordEntry

excelFile = "FinalResult.xlsx"
mailingListFile = "MailingList.txt"

# list of emails, to be written to a text file
mail_list = []

# now to action!

# create record writer instance

recWriter = RecordEntry()

# extract mail
extractor = Extractor(workBookPath=excelFile)
mail_list = extractor.extractAllEmailAddress()


# write to file
# recWriter.writeRecords(text_file=mailingListFile, records=mail_list)


# get team records by name and write mail lists or full info
# writing mailing lists here
teamNames = ["Corporate", "Operations", "Publications", "Promotions", "Logistics"]
# dictionary for team records
teamDict = {}

for team in teamNames:
    teamDict = extractor.extractAllTeamRecords()