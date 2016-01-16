Brew Master Automatic Updates and Logging for HomeBrew
-----------------------

Built using Python 3.4.3, should be compatible with other Python 3 releases.

## Execute Brew Master

./brewmaster.py -l /custom/log/path.log

The default log path ~/brewmaster.log is used if brewmaster is called without any argument.

./brewmaster.py

## Add Crontab 
Use whatever interval you like.  I use two crontabs 0 6 * * * and 0 18 * * * to update packages in the morning and evening after changes have been pushed up for the day.

pyenv activate brewmaster; /Users/glen/dev/brewmaster/brewmaster.py


## Read Log
cat ~/brewmaster.log
