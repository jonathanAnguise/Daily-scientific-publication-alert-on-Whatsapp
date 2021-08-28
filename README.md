# Daily scientific publication alert on Whatsapp
***
Check publication on **Google Scholar**, select two articles and send the title, summary and the link to the article using Whatsapp
***
## How to install:
1. Clone the repo: 
   * `git clone https://github.com/jonathanAnguise/Daily_scientific_publication_alert_on_Whatsapp.git`
2. Create an account in the api https://serpapi.com/ in order to do GoogleScholar request
   * Once you have an api token create a __.env__ file in the root of the folder and add the token in the file using that command:
     * `echo 'TOKEN_GOOGLE_SCHOLAR="SET_YOUR_TOKEN_HERE"' >> .env`
     * `echo 'ENDPOINT_GOOGLE_SCHOLAR="https://serpapi.com/search"' >> .env`
   
3. Also, Get the Api token to send message using Whatsapp, here how get the Api token and authorize the api to send message to your phone number: https://www.callmebot.com/blog/free-api-whatsapp-messages/ 
   * Add the CallMeBot api token to __.env__ file: 
     * `echo 'TOKEN_CALLMEBOT="YOUR_TOKE"' >> .env`
   * Add your phone number following that format "+YYXXXXXXXXX": 
     * `echo 'PHONE_NUMBER="YOUR_PHONE_NUMBER"' >> .env`
       * with "YY" as the international code
       * "XXXXXXXXX" the phone number
   * Add the api endpoint:
     * `ENDPOINT_CALLMEBOT="https://api.callmebot.com/whatsapp.php"' >> .env`

## Configure the theme of the research
1. Open "./api_scientific_publication.py"
2. Change the value of the variable KEYWORD (example: KEYWORD = "Theme that I want")

## Configure the frequency of sending message
The variable is_day_to_send_article here is activated on Monday, Wednesday, Friday.
Here each day of the week has a number 0 for Sunday, 1 for Monday ... 6 for Saturday. To select when we want to receive we have to change the condition of activation to that variable
1. Open "./main.py"
2. change the if condition in function of what day you want.

## Set the code on the cloud
1. Create an account on https://www.pythonanywhere.com/
2. Click on File
3. Drop main.py, api_scientific_publication.py, api_whatsapp.py, data_manager.py
4. Click on Task
5. Select at what time when you want to receive it. Be careful it's UTC time!
6. Enter in the column **Command** the command `python3 main.py` 



