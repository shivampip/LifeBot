import wikipedia
import logging as log 
import logging as log
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
#log.info('Logging Started')


def getSummery(term):
    log.info("Searching wikipedia for "+term)
    return wikipedia.summary(term)