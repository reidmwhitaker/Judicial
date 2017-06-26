class Opinion:
    def __init__(self, name="", text = "", opinion_text="", date_decided = "", author = "", joining = "", type = "", id = ""):
        self.text = text
        self.type = type
        self.date_decided = date_decided
        self.author = author
        self.joining = joining
        self.id = id
        self.opinion_text = opinion_text
        self.name = name
        self.citations = []

class OpinionCluster:
    def __init__(self, opinions = "", scdb_id = "", scdb_votes_majority = "", scdb_votes_minority = "",
                 name = "", name_full = "", attorneys = "", id = "", cite = "", saliance = "", court="",jurisdiction="",
                 docket="",date=""):
        self.opinions = opinions
        self.scdb_id = scdb_id
        self.scdb_votes_majority = scdb_votes_majority
        self.scdb_votes_minority = scdb_votes_minority
        self.name = name
        self.name_full = name_full
        self.attorneys = attorneys
        self.id = id
        self.cite = cite
        self.saliance = saliance
        self.court = court
        self.jurisdiction = jurisdiction
        self.docket = docket
        self.date = date

class Docket:
    def __init__(self, id = ""):
        self.id = id

class Judge:
    def __init__(self, name = "", party_appoint = ""):
        self.name = name
        self.party_appoint = party_appoint
