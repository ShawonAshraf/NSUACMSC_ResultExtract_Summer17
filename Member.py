class Member:
    def __init__(self, name, nsuId, team, email):
        self.name = name
        self.nsuId = nsuId
        self.team = team
        self.email = email

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.nsuId, self.team, self.email)
