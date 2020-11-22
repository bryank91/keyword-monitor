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


## Future Upgrades
- It should take in arguments instead of changing the source code
- Utilise forever functions
- Uses SQLlite/JSON/csv so it only alerts you once if the keyword appears
