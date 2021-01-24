# OzBargain Web Scraper

This is a web scraper written to retrieve the list of deals available
on https://ozbaragain.com.au. These deals are then sent via text message to
a phone number using the [Twilio SMS Notification Service](https://twilio.io).

## Getting Started

- Clone this repostiory.
- Build an image from the root directory where the Dockerfile is located.
- Execute a `docker-run` with all expected environment variables included.
in the command via a file (useful for ensuring they are not included in sh history)
 or directly written into the command.

### Required Environment Variables.

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`

You can find your Twilio SID and Authentication token [here.](https://www.twilio.com/console)

- `TWILIO_FROM`
- `TWILIO_TO`

These are also Twilio account settings used to determine what 
number an account is sending text messages from and to.

#### Docker Image Build Example.

`docker build -t oz-bargain-scraper:v0.0.1 .`

#### Docker Run Example.

`docker run --env TWILIO_ACCOUNT_SID --env TWILIO_AUTH_TOKEN --env TWILIO_TO --env TWILIO_FROM --env PYTHONUNBUFFERED=0 -d oz-bargain-scraper:v0.0.1`

- `--env` is used to declare environment variables. When environment variables already exist in the current environment you 
do not need to specify a direct value.
- `PYTHONUNBUFFERED=0` This is to allow python printing to be displayed in container logs. [More Information.](https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker)