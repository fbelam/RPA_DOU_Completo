#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
import csv
import pandas as pd
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = servico)

driver.get('https://www.in.gov.br/servicos/diario-oficial-da-uniao');

time.sleep(3) # Let the user actually see something

search_button = driver.find_element(By.XPATH, '//*[@id="portlet_com_liferay_site_navigation_menu_web_portlet_SiteNavigationMenuPortlet_INSTANCE_HmqYiOQVIZuq"]/div/div[2]/div/div[1]/div[1]/a')

search_button.click()

search_button = driver.find_element(By.XPATH, '//*[@id="portlet_leituradou_INSTANCE_GKE7NRmaCXgl"]/div/div[2]/div/div[1]/div[3]/button[4]')

search_button.click()

search_button = driver.find_element(By.XPATH, '//*[@id="ResultadoConsulta"]/tbody/tr/td[5]/a/img')

search_button.click()

