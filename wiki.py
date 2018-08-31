import wikipedia
import logging as log 
import c
log.basicConfig(level=log.INFO, format= c.LOG_FORMAT)

def getSummery(term):
    log.info("Searching wikipedia for "+term)
    return wikipedia.summary(term)