# Keyword Monitor
Monitors website for specific keywords

## Setting up
Install all prerequisites
```
pip3 install -r requirements.txt
```

Set up your webhook_url via the environment file (.env)
```
WEBHOOK_URL=<DISCORD_WEBHOOK_URL>
```

You will need a cron job to set up the application
```
crontab -e
/Users/username/Documents/python/page-monitor/runner.py >> /Users/username/Documents/python/page-monitor/cron.log 2>&1
```
Note: You might need to allow cron to access your files
https://blog.bejarano.io/fixing-cron-jobs-in-mojave/

## Usage
```
# to see syntax
./runner.py -h

# sample
./runner.py multiReader "https://www.helloworld.com.au" "covetedItem" "https://www.helloworld.com.au" helloworld
```

Two main feature now:
- Finder: verifies if the keyword exist
- ForeverFinder: verifies if the keyword exist in a forever loop (TBD)
- Difference: verifies if there is a difference to the website from the last call 
- differenceMultiple: differences via any text element based on keyword matches 
- differenceMultipleId: differences via the id element based on keyword matches 
- differencePage: any page differences (javascript elements change often)
- multiReader: combination of readers from the top to one

## Future Upgrades
- Utilise forever functions
- Uses SQLlite instaed of files
- Improve wildcard searches
