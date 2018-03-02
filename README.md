## HPDF Task 3 (ReactJS Front End + PyhtonFlask Back End)
 
### The Task
**To deploy a currency bot as a custom service in Hasura that integrates with Dialogflow (api.ai) .**

### API and Platform Used
* [Dialogflow](https://dialogflow.com/docs/getting-started/building-your-first-agent)
* [Hasura](https://docs.hasura.io/0.15/manual/getting-started/index.html)
 
 
### How it works?
 
* Visit https://ui.lukewarm10.hasura-app.io/ to try out the bot in its full functionality.
 
**Dialogflow Bot:**
* The Bot is made using Dialogflow which take input from UI and reply back with a proper response.
* The Bot is specialized for Currency Conversion. It is trained to identify almost 50 different currencies. 
* When UI gives a particular input, the bot takes it and scans for the currencies between which it has to convert and also currency amount.
* The Bot is also trained for normal day to day conversations also.
* The Bot detects currencies based on different synonyms such as currency name, currency code and currency shorthand names. Example, HKD can be represented as Hong Kong dollar and Hong Kong. JPY can be represented as Yen and Japanese yen

**Python Flask app:**
* The python flask app acts as a webhook which accepts post requests from the Diagflow Bot
* The currency conversion rates are got using an external api where the  rates are updated automatically every 30 minutes, so the converted value will be accurate.
* The app replies back to bot with the converted currency value.

### Installation Instructions
**Follow these instructions to get the code working on your machines locally. (Chrome web browser is preferred)**
* Install Node.js and npm in your system.
* git clone this repository.
* Open Terminal and cd into the project folder.
* Run npm install to install all the project dependencies.
* To run the app, use npm start

### Contributors
**[silvergame](https://github.com/silvergame) Responsible for creating the front end using ReactJS and integrating it with Dialogflow (api.ai).**

Volunteer:
[naren123456] (https://github.com/naren123456) Responsible for creating the backend using PythonFlask and integrating the webhook with the Hasura APIs.
