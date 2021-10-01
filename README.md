# Arbitrage XML Project

## About
This project introduces investing into sports betting through means of a XML data API. The project tries to produce an average daily ROI of 1% in a world of fantisized 200% ROI's. Through the use of Python, this project contains files that compare the odds of the same sporting event across different sportsbooks in order to find a sure bet (: "placing one bet per each outcome with different betting companies, the bettor can make a profit regardless of the outcome" -> https://en.wikipedia.org/wiki/Arbitrage_betting). Once this bet is found it is communicated through form of a text message API to subscribers so they can capitalize on it.

## Usage/Breakdown

Files [getNames.py](getEventNames.py), [getLeagueIds.py](getLeagueIds.py), [getTeams.py](getTeams.py) decode the XML data structure provided by the API in order to obtain particular details  (respective to their name) to be used in the project. Files [sportsBooks.py](sportsBooks.py), and [periodDescriptions.py](periodDescriptions.py) are harcoded files used to facilitate the interpretation of the XML data. File [functions.py](functions.py) contains all the functions of course. Lastly, fetch.py brings everything in through form of import statements for evaluation of the data of which it outputed to [arb.txt](arb.txt) (example of sure bets exist in this file) if there exists a sure bet and if so it is also given to [textme.py](textme.py) where it will text the information to subscribers.

<img src="https://user-images.githubusercontent.com/64427472/135642815-3b00ef18-6d99-416d-bdb2-9a616f8df943.PNG" width="375" height="812">

## Map

<img src="https://user-images.githubusercontent.com/64427472/135642628-f0a88a7c-78b8-43fa-985a-78ee430e8559.png" width="666" height="353">
