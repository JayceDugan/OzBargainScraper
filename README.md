# OzBargain Web Scraper

This is a web scraper written to retrieve the list of deals available
on https://ozbaragain.com.au. These deals are then sent to a discord channel via webhooks.

Twilio SMS Notifications were included as part of the original development but have since been 
deprecated for the discord channel integrations due to SMS charges.

## Getting Started

- Clone this repostiory.
- Build an image from the root directory where the Dockerfile is located.
- Execute a `docker-run` with all expected environment variables included.
in the command via a file (useful for ensuring they are not included in sh history)
 or directly written into the command.


#### Docker Image Build Example.

`docker build -t oz-bargain-scraper:vx.x.x .`


#### Docker Run Example.

`docker run --env TWILIO_NOTIFICATIONS_ACTIVE=false --env PYTHONUNBUFFERED=0 -d oz-bargain-scraper:vx.x.x`

- `--env` is used to declare environment variables. When environment variables already exist in the current environment you 
do not need to specify a direct value.
- `PYTHONUNBUFFERED=0` This is to allow python printing to be displayed in container logs. [More Information.](https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker)
