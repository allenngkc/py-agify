import requests

class AgifyClient:
    """
    A base class for Agify API
    """
    def __init__(self, api_key=None, http_service=requests):
        """
        :param api_key: If you want more than 1000 requests per day, https://store.agify.io/
        """
        self.has_api_key = api_key is not None
        self.http_service = http_service
        self.url = "https://api.agify.io?"

        if self.has_api_key:
            self.url += f"apikey={api_key}&"

    def get_age(self, name, country_id=None):
        """
        Takes in a name string and return the age
        :param country_id: Check https://agify.io/our-data for supported countries
        :return:Returns the predicted age as int value
        """
        url = self.url + f"name={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()
        return data["age"]