from Extractor import Extractor
from InfoToTextFile import RecordEntry

excelFile = "FinalResult.xlsx"
mailingListFile = "MailingList.txt"

# list of emails, to be written to a text file
mail_list = []

# list for selected members
corporate = []
promotions = []
logistics = []
operations = []
publications = []

# now to action!

# create record writer instance

recWriter = RecordEntry()

# extract mail
extractor = Extractor(workBookPath=excelFile)
mail_list = extractor.extractEmailAddress()


# write to file
recWriter.writeRecords(text_file=mailingListFile, records=mail_list)







