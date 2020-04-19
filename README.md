# Created for UWB Hacks the Cloud 2020 [uwbhacks.com](https://uwbhacks.com/)
# Covid 19 updates
## Goals: 
> The goals of this project were for us to gain knowledge in the cloud while providing a relevant and useful service.
> We also wanted to provide current information on the growing epidemic so people can acknowledge the danger that is the coronavirus.
> 

## Desired User Experience:
> The desired user experience was to be simple for the user to subscribe and simple for the user to unsubscribe.
> The user would simple go to the website [covnews.org](https://covnews.org/), fill in the fields and (if applicable) confirm their email subscrition.
> From that point on the user would not have to worry about anything unless they want to unsubscribe.
> The user will then begin recieving daily updates for their desired country (currently only US or South Korea) containing the following criteria: 
* Country
* Confirmed cases
* Total deaths
* Total recovered
* Data date

## Implementation Details:
> Our system uses the [Coronavirus COVID19 API](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#b07f97ba-24f4-4ebe-ad71-97fa35f3b683), [AWS Simple Notification Service](https://aws.amazon.com/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc), and a Digital Ocean webserver to get the country data from the api, parse the data on the webserver, then publish notifications to the subscribers through SNS.
> The https certified webserver, hosts a website using a domain from [domains.google.com](https://domains.google.com/)
> The website offers daily coronavirus updates at 12:00 PM through either email, sms messaging, or both.
> Upon subscribing, the user will receive a confirmation text saying they are subscribed, and a confirmaiton email containing a link in which they can confirm their subscription.
> The website will then publish the information to the subscibers everyday at the same time.

## Issues Encountered: 
* Languages: Duncan had not worked a lot with Python before and none of us had worked with HTML, CSS, or PHP before this project so learning the languages in a timecrunch was an issue he encountered. 
* boto3 Not Recognized: we had an issue with boto3 not being reconized in the webserver so configuring the webserver to run with boto 3 was a challenge.
* Learning the boto3 Syntax: the boto3 syntax was hard to follow and at the beginning the documentation did not help us too much.
* Connecting the Seperate Programs: connecting the front-end to the python scripts to send confirmation emails took a lot of time
* Building the Website From Scratch: since none of us had any experience working with HTML, CSS, and PHP, we had to learn all the languages from scratch and in a timecrunch to make sure we could test it. building the website and connecting it to the backend we probably the largest challenge and took the most time.
* Creating the Crontab Script: the crontab script took some time to create, we had no idea how to use crontab so we had to take some time to learn how to set it up and the syntax behnd it.


## Contributors:
* [Jaeha Choi](https://github.com/SpaceRabbits)
* [Robin Seo](https://github.com/seo-chang)
* [Duncan Spani](https://github.com/dspani)
