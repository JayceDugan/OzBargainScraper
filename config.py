import os

### Twilio SMS Notification Service
twilio_active = os.environ['TWILIO_NOTIFICATIONS_ACTIVE']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_from = os.environ['TWILIO_FROM']
twilio_to = os.environ['TWILIO_TO']
twilio_notification_message = 'Discord has been updated with the latest https://ozbargain.com.au deals.'

### OzBargain Configs
oz_bargain_domain = 'https://ozbargain.com.au/cat/computing'
oz_teaser_title_word_limit = 10

### Discord
discord_webhook_url = os.environ['DISCORD_WEBHOOK_URL']
discord_character_limit = 2000
