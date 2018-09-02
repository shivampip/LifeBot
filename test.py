import logging as log
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
