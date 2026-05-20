import configparser


class ConfigReader:

    def __init__(self):

        self.config = configparser.ConfigParser()

        self.config.read("config/config.properties")

    def get_base_url(self):

        return self.config.get("DEFAULT", "base_url")

    def get_browser(self):

        return self.config.get("DEFAULT", "browser")

    def get_implicit_wait(self):

        return self.config.get("DEFAULT", "implicit_wait")

    def get_test_product(self):

        return self.config.get("DEFAULT", "test_product")

    def get_invalid_mobile(self):

        return self.config.get("DEFAULT", "invalid_mobile")