# OzBargain Web Scraper

Asynchronous Webscraper that updates [27+ discord channels](https://discord.gg/FrdETzHC3S) utilizing webhooks with the latest
deals from https://ozbargain.com.au. 

## Infrastructure

- `AWS Lambda` Python function utilising `AWS DynamoDB` for storage ecords.
- Containerised and deployed to `AWS ECS/ECR`

## Short History
- Previously used twilio SMS notification service
- Updated to use discord & update a set of channels instead via webhooks & a JSON file.
- Refactored to `AWS Lamda`, `AWS ECS` and `AWS ECR` for implementation & DynamoDB for storage.