import wikipedia

def getSummery(term):
    print("[ Searching wikipedia for",term,']')
    return wikipedia.summary(term)