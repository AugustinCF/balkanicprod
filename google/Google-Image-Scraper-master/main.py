# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import pandas as pd
import numpy as np
import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable

lista = pd.read_excel('produse.xlsx')
df = pd.DataFrame(lista, columns = ['Produs'])

print(df)
if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]

for i in df.index:
    entry = df.loc[i]
    search_keys =  entry
#for index, row in df.iterrows():
#search_keys = (row["Produs"])

    #Parameters
    number_of_images = 1
    headless = False
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
    
    #Release resources    
    del image_scrapper