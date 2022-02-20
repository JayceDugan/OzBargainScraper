import boto3
import config

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def load_scraper_config():
    session = boto3.Session(
        region_name=config.AWS_REGION,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        aws_session_token=config.AWS_SESSION_TOKEN
    )

    dynamo = session.resource('dynamodb')
    dynamo_discord_webhooks = dynamo.Table('discord_webhooks')
    scan = dynamo_discord_webhooks.scan()

    return scan['Items']
