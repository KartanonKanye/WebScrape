from http.server import executable
import imp
from lib2to3.pgen2 import driver
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#step1: Access the firefox browser with code

serve = FirefoxService(executable_path = GeckoDriverManager.install())
drive = webdriver.Firefox(service=serve)

drive.get("https://www.antikvaari.fi/hakukone?tekija=&nimi=&isbn=&tryhma=1&myyja=&kustantaja=&painovuosi=&kieli=&aihesana=&aika=&kunto=&lajittelu=default&tyyppi=0&tuoteTyyppi=&tuloksia=30&sivu=1")


content = drive.page_source
soup = BeautifulSoup(content)
