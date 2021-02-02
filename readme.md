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
sudo apt-get install privoxy or brew install privoxy
sudo apt-get install python-stem or pip3 install stem
sudo apt-get install tor or brew install tor
```

### Setting up TOR

Password Hashing:
`tor --hash-password my_password`

Control Files

`sudo vim /etc/tor/torrc` and change the file to (Ubuntu)

`cp /usr/local/etc/tor/torrc.sample /usr/local/etc/tor/torrc` (OSX)
`sudo vim /usr/local/etc/tor/torrc` and change the file to

```
ControlPort 9051
# hashed password below is obtained via `tor --hash-password my_password`
HashedControlPassword 16:9529EB03A306DE6F60171DE514EA2FCD49235BAF1E1E55897209679683
CookieAuthentication 1
```

Restart service client
`sudo /etc/init.d/tor restart` (Ubuntu)
`sudo brew services start tor` (OSX)

### Setting up Privoxy
Changing Control files:
```
sudo vim /etc/privoxy/config (ubuntu)
vim /usr/local/etc/privoxy/config (osx)
```
Uncomment this line
```
forward-socks5 / 127.0.0.1:9050
```

Restart Service client
```
sudo /etc/init.d/privoxy restart (ubuntu)
brew services restart privoxy (osx)
```


## Usage
```
# to see syntax
./runner.py -h

# sample
./runner.py multiReader "https://www.helloworld.com.au" "keyword" "https://www.helloworld.com.au" helloworld <optional-env-variable>

# to see snytax of v2
python3 main.py -h

# sample v2
python3 main.py proxyReader "https://www.site.com" "Add to Cart" "tester" "span" "submit.button"

# running feed
python3 mainFeed.py "https://www.site.com.au/feed" DISCORD_FEED_WEBHOOK_URL
```

### Features
- Finder: verifies if the keyword exist
- ForeverFinder: verifies if the keyword exist in a forever loop (TBD)
- Difference: verifies if there is a difference to the website from the last call 
- differenceMultiple: differences via any text element based on keyword matches 
- differenceMultipleId: differences via the id element based on keyword matches 
- differencePage: any page differences (javascript elements change often)
- multiReader: combination of readers from the top to one
- proxyReader: uses TOR and selective elements and ids

- mainFeed: monitors feed and print out the latest items

### Experimental
- sample.py
- main.py

## Future Upgrades
- Utilise forever functions and proper failover mechanisms
- Setting up databases for mutliple monitors to query
- Add logging

## Completed Updates
- DONE: Improve wildcard searches. Now in main.py

## Tech Debt
- Clean up inferior functions
- Use classes instead of subroutines or scripts
- Deprecate inferior functions (eg. Catch monitor)
- It should be running forever functions or as a service instead
- Move it to it's appropriate folders
