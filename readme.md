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
PROD=
TOR_PASS=
```

You will need a cron job to set up the application
```
crontab -e
/Users/username/Documents/python/page-monitor/runner.py >> /Users/username/Documents/python/page-monitor/cron.log 2>&1
```
Note: You might need to allow cron to access your files
https://blog.bejarano.io/fixing-cron-jobs-in-mojave/

## Setting up in TOR proxies
https://jarroba.com/anonymous-scraping-by-tor-network/#:~:text=The%20most%20common%20use%20case,can%20continue%20scraping%20this%20website.

```
sudo apt-get install privoxy
sudo apt-get install python-stem 
sudo apt-get install tor
```

## Usage
```
# to see syntax
./runner.py -h

# sample
./runner.py multiReader "https://www.helloworld.com.au" "keyword" "https://www.helloworld.com.au" helloworld <optional-env-variable>
```

### Features
- Finder: verifies if the keyword exist
- ForeverFinder: verifies if the keyword exist in a forever loop (TBD)
- Difference: verifies if there is a difference to the website from the last call 
- differenceMultiple: differences via any text element based on keyword matches 
- differenceMultipleId: differences via the id element based on keyword matches 
- differencePage: any page differences (javascript elements change often)
- multiReader: combination of readers from the top to one

### Experimental
- sample.py

## Future Upgrades
- Utilise forever functions and proper failover mechanisms
- Improve wildcard searches
- Setting up databases for mutliple monitors to query

## Tech Debt
- Clean up inferior functions
- Use classes instead of subroutines or scripts
