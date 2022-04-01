from selenium.webdriver.common.by import By

from selenium_controller.driver import driver


class Gitlab:

    def __init__(self):
        self.gitlab_map_url = "https://docs.gitlab.com/charts/installation/version_mappings.html"
        self.gitlab_versions = list()

    def fetch_gitlab_map_versions(self):
        driver.get(self.gitlab_map_url)

        self.gitlab_versions = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(2)")

        self.gitlab_versions = [version.text for version in self.gitlab_versions]

        return self.gitlab_versions
