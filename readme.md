# Keyword Monitor
Monitors website for specific keywords

# Setting up
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
```
