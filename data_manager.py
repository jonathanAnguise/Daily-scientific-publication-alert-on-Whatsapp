# Handle data in order to be sent
import json

NUMBER_OF_ARTICLE = 2

class DataManager:

    def __init__(self):
        self.article_list = []
        self.new_data = []
        self.previous_data = []
        self.article_selected_to_be_send = []
        self.formated_message = ""

    # Get the information and store it into an array
    def parse_message_to_table(self, json_file_from_google_scholar):
        """
        Method that get back a table with the number of element as dictionary with title summary and link as element
        :param json_file_from_google_scholar: raw data from api google scholar
        :return: return a table with the all element where only 2 will be selected
        """

        # number_of_element = len(json_file_from_google_scholar["organic_results"])
        self.article_list = [
            {
                "title": self.article_dictionary["title"],
                "link": self.article_dictionary["link"],
                "summary": self.article_dictionary["snippet"]
            }
            for self.article_dictionary in json_file_from_google_scholar["organic_results"]]


    def find_article_never_sent(self, articles_list):
        """
        Read a file sent and select the two first non sent article update it in self.article_selected_to_be_send
        :param articles_list:
        :return: nothing
        """
        # make sure to load the fresh previous data
        self.get_previous_data()

        for potential_article in self.article_list:
            article_already_sent = False
            for previous_article in self.previous_data:
                if potential_article["title"] == previous_article["title"]:
                    print("article already exist")
                    article_already_sent = True
                    break
            if not article_already_sent:
                print("artice can be sent")
                self.article_selected_to_be_send.append(potential_article)
            if len(self.article_selected_to_be_send) >= 2:
                break

    def save_article_to_file(self):
        """
        Save and append article to the file with the json format
        update self.previous_data with data from the file
        :return: nothing
        """

        self.get_previous_data()

        # Join previous article sent with article freshly sent in a list before writing it as a fresh json
        self.new_data = self.previous_data + self.article_selected_to_be_send
        with open("article_sent.json", mode="w") as file:
            file.write(json.dumps(self.new_data, indent=3))

    def get_previous_data(self):
        try:
            with open("article_sent.json", mode="r") as file:
                self.previous_data = json.load(file)
        except:
            with open("article_sent.json", mode="w") as file:
                self.previous_data = []

    def format_message(self, article_number):
        return f"""
    Article {article_number + 1}: 
        *title*: {self.article_selected_to_be_send[article_number]["title"]}
        *summary*: {self.article_selected_to_be_send[article_number]["summary"]}
        *Link to know more*: {self.article_selected_to_be_send[article_number]["link"]}
        """

