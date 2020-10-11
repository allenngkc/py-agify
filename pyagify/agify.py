import requests
from pyagify.exceptions import *


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

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data["age"]

    def get_raw(self, name, country_id=None):
        """
        Takes in a name string and return the raw data
        :param country_id: Check https://agify.io/our-data for supported countries
        :return:Returns the raw data
        """
        url = self.url + f"name={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data

    def get_batch(self, names, country_id=None):
        """
        Takes in a name list and return a list of ages
        :param names: a list of names in string
        :param country_id: Check https://agify.io/our-data for supported countries
        :return:Returns a list of ages
        """
        url = self.url

        for name in names:
            url += f"name[]={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        ages = []

        for i in data:
            ages.append(i["age"])

        return ages

    def get_batch_raw(self, names, country_id=None):
        """
        Takes in a name list and return a list of raw data
        :param names: a list of names in string
        :param country_id: Check https://agify.io/our-data for supported countries
        :return:Returns a list of raw data
        """
        url = self.url

        for name in names:
            url += f"name[]={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data


class GenderizeClient():
    """
    A base class for Genderize API
    """

    def __init__(self, api_key=None, http_service=requests):
        """
        :param api_key: If you want more than 1000 requests per day, https://store.genderize.io/
        """
        self.has_api_key = api_key is not None
        self.http_service = http_service
        self.url = "https://api.genderize.io?"

        if self.has_api_key:
            self.url += f"apikey={api_key}&"

    def get_gender(self, name, country_id=None):
        """
        Takes in a name string and return the gender
        :param country_id: Check https://genderize.io/our-data for supported countries
        :return:Returns the predicted gender as string
        """
        url = self.url + f"name={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data["gender"]

    def get_raw(self, name, country_id=None):
        """
        Takes in a name string and return the raw data
        :param country_id: Check https://genderize.io/our-data for supported countries
        :return:Returns the raw data
        """
        url = self.url + f"name={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data

    def get_batch(self, names, country_id=None):
        """
        Takes in a name list and return a list of genders
        :param names: a list of names in string
        :param country_id: Check https://genderize.io/our-data for supported countries
        :return:Returns a list of genders
        """
        url = self.url

        for name in names:
            url += f"name[]={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        genders = []

        for i in data:
            genders.append(i["gender"])

        return genders

    def get_batch_raw(self, names, country_id=None):
        """
        Takes in a name list and return a list of raw data
        :param names: a list of names in string
        :param country_id: Check https://genderize.io/our-data for supported countries
        :return:Returns a list of raw data
        """
        url = self.url

        for name in names:
            url += f"name[]={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data


class NationalizeClient():
    """
    A base class for Nationalize API
    """
    def __init__(self, api_key=None, http_service=requests):
        """
        :param api_key: If you want more than 1000 requests per day, https://store.genderize.io/
        """
        self.has_api_key = api_key is not None
        self.http_service = http_service
        self.url = "https://api.nationalize.io?"

        if self.has_api_key:
            self.url += f"apikey={api_key}&"

    def get_nationality(self, name, country_id=None):
        """
        Takes in a name string and return the nationality that has the highest probability
        :param country_id: Check https://nationalize.io/our-data for supported countries
        :return:Returns the predicted nationality as string
        """
        url = self.url + f"name={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data["country"][0]["country_id"]

    def get_raw(self, name, country_id=None):
        """
        Takes in a name string and return the raw data
        :param country_id: Check https://nationalize.io/our-data for supported countries
        :return:Returns the raw data
        """
        url = self.url + f"name={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data

    def get_batch(self, names, country_id=None):
        """
        Takes in a name list and return a list of genders
        :param names: a list of names in string
        :param country_id: Check https://nationalize.io/our-data for supported countries
        :return:Returns a list of genders
        """
        url = self.url

        for name in names:
            url += f"name[]={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        list = []

        for i in data:
            list.append(i["country"][0]["country_id"])

        return list

    def get_batch_raw(self, names, country_id=None):
        """
        Takes in a name list and return a list of raw data
        :param names: a list of names in string
        :param country_id: Check https://nationalize.io/our-data for supported countries
        :return:Returns a list of raw data
        """
        url = self.url

        for name in names:
            url += f"name[]={name}&"

        if country_id is not None:
            url += f"country_id={country_id}"

        response = requests.get(url)
        data = response.json()

        code = response.status_code

        if code == 401:
            raise Unauthorized(data["error"], response)
        elif code == 402:
            raise PaymentRequired(data["error"], response)
        elif code == 422:
            raise UnprocessableEntity(data["error"], response)
        elif code == 429:
            raise TooManyRequests(data["error"], response)

        return data