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
python3 main.py -h

# sample
./runner.py multiReader "https://www.helloworld.com.au" "keyword" "https://www.helloworld.com.au" helloworld <optional-env-variable>

python3 main.py proxyReader "https://www.site.com" "Add to Cart" "tester" "span" "submit.button"

# running feed
python3 mainFeed.py "https://www.site.com.au/feed" 
python3 mainFeed.py "https://www.site.com.au/feed" "keyword1,keyword2"
```

### Current Features
#### main.py
- reader: monitor selective elements for keywords
- proxyReader: uses TOR and selective elements and ids
- mainFeed: monitors feed and print out the latest items including necessary keywords

#### runner.py
- multiReader: monitor selective words in the whole page

### Deprecated
- Finder: verifies if the keyword exist
- ForeverFinder: verifies if the keyword exist in a forever loop (TBD)
- Difference: verifies if there is a difference to the website from the last call 
- differenceMultiple: differences via any text element based on keyword matches 
- differenceMultipleId: differences via the id element based on keyword matches 
- differencePage: any page differences (javascript elements change often)
- multiReader: combination of readers from the top to one
- proxyReader: uses TOR and selective elements and ids
- mainFeed: monitors feed and print out the latest items


## Future Upgrades
- Utilise forever functions and proper failover mechanisms
- Setting up databases for mutliple monitors to query
- Add logging
- Use argparse for arguments
- Improve README documentation

## Tech Debt
- Clean up inferior functions
- It should be running forever functions or as a service instead
- Add more descriptive subroutine names
- Move multireader to main.py
