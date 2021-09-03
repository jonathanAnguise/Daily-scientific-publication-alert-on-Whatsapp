from api_scientific_publication import *
from data_manager import *
from api_whatsapp import *
from datetime import datetime as dt

def article_sender(theme):
    request_articles = GoogleScholarApi(theme)

    request_send_message = WhatsAppManager()
    path_to_save = "article_sent " + str(theme) + ".json"
    my_data = DataManager(path_to_save)
    my_data.parse_message_to_table(request_articles.get_google_scholar_results())
    print(request_articles.google_scholar_results)

    # Save the info in order to never send the same result twice
    my_data.find_article_never_sent(my_data.article_list)

    # Sending part
    # request_send_message.send_whatsapp_message("Les articles d'aujourd'hui 🤓")
    # for article_item in range(NUMBER_OF_ARTICLE):
    #     request_send_message.send_whatsapp_message(my_data_learning_agility.format_message(article_item))
    # request_send_message.send_whatsapp_message("Have a nice day!!! 😁😁😁")

    # Save articles in a json file to never send it again
    my_data.save_article_to_file()

    # Killing instances in order to create a new fresh one
    del request_articles
    del my_data
    del request_send_message


# Select the days and send an article only for selected days.
is_day_to_send_article = False
date = dt.now()
day_of_the_week_number = int(date.strftime("%w"))
# Only set boolean to true when it's monday, wednesday, and friday.
if day_of_the_week_number % 2 != 0:
    is_day_to_send_article = True

if is_day_to_send_article:
    themes_to_survey_list = ["learning agility", "Performance and talent management in organisations"]
    for theme in themes_to_survey_list:
        article_sender(theme)
