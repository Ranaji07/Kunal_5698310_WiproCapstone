from pages.basepage import BasePage


class HomePage(BasePage):

    def open_homepage(self, url):
        self.driver.get(url)

    def verify_homepage(self):
        return "Nykaa" in self.get_title()