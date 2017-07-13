class RecordEntry:
    """
    writes a list of records
    the list is passed as arg
    """

    def writeRecords(self, text_file, records):
        # overwrites the file, so choose file accordingly
        f = open(text_file, 'w')
        for rec in records:
            f.write("{}\n".format(rec))
        f.close()