## HPDF Task 3 (ReactJS Front End + PythonFlask Back End)
 
### The Task
**To deploy a currency bot as a custom service in Hasura that integrates with Dialogflow (api.ai) .**

### Prerequisites Used
* [Dialogflow](https://dialogflow.com/docs/getting-started/building-your-first-agent)
* [Hasura](https://docs.hasura.io/0.15/manual/getting-started/index.html)
* Gitbash (recommended)
 
 
### How it works?
 
* Visit https://ui.lukewarm10.hasura-app.io/ to try out the bot in its full functionality.
* Check out https://hasura.io/hub/projects/vrinda/currency-conversion-bot for our published project at Hasura hub.
 
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

### Deployment instructions
**Basic deployment:**
* Install Hasura CLI.
* $ hasura login
* clone and cd into it.
* $ git add . && git commit -m "Initial Commit"
* $ git push hasura master
Now, your app will be running at https://ui.YOUR-CLUSTER-NAME.hasura-app.io (replace YOUR-CLUSTER-NAME with the name of your cluster).
* To get the name of your cluster
$ hasura cluster status

**Local Deployment:**
Follow these instructions to get the code working on your machines locally. (Chrome web browser is preferred)
* Install Node.js and npm in your system.
* git clone this repository.
* Open Terminal and cd into the project folder.
* Run npm install to install all the project dependencies.
* To run the app, use npm start

**Making changes and deploying:**
* To make changes to the project, browse to /microservices/mymicroservice/app/src for React JS part and /microservices/app/src/server.py for the Python-Flask backend part.
* Commit the changes, and perform git push hasura master to deploy the changes.

**Managing app dependencies:**
* System dependencies, like changing the web-server can be made in the Dockerfile
* npm/yarn deps can be managed by editing package.json.
* If changes have been done to the dependencies, git commit, and perform git push hasura master to deploy the changes.


### Contributors
* **[silvergame](https://github.com/silvergame) Responsible for creating the front end using ReactJS and integrating it with Dialogflow (api.ai).**

* Volunteer:
[naren123456] (https://github.com/naren123456) Responsible for creating the backend using PythonFlask and Dialogflow.
