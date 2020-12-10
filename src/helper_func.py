import requests
from io import BytesIO
import os
import sys
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import splitfolders



def google_full_scrape(string, path):
    # Create folder for images
    path = os.path.expanduser(f'{path}')
    os.mkdir(path)
    # Transform string into google search url 
    search = string.replace(' ', '+')
    url = f'https://www.google.com/search?as_st=y&tbm=isch&as_q={search}&as_epq=&as_oq=&as_eq=&imgar=&imgcolor=&imgtype=&cr=&as_sitesearch=&as_filetype=&tbs=&sfr=vfe&safe=images'
    # Initiate selenium and search url in chrome
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url)
    scroll_pause_time = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        # Check if scroll height has not changed 
        if new_height == last_height:
            # Check for show more button
            try:
                driver.find_element_by_css_selector("input[jsaction='Pmjnye']").click()
                continue
            except:
                break
        # Set scroll height        
        last_height = new_height
    # Save page source as beautiful soup class    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    # Find all img tags
    images = soup.find_all('img')
    url_strings = []
    # Create list of all image urls
    for img in images:
        pic = img.get('data-src')
        if pic == None:
            continue
        url_strings.append(pic)
    url_strings = url_strings[1:]
    # Download images from urls to path
    accum = 0
    for pic in url_strings:
        try:
            responce = requests.get(str(pic))
            img = Image.open(BytesIO(responce.content))
            img.save(f"{path}/{accum}.jpg")
            accum += 1
        except:
            print(f" #{accum} picture bad")
            accum += 1
    # Close browser driver       
    driver.close()





#test train val split for folders in path
def folder_split(path):
    for idx, _ in enumerate(path):
        splitfolders.ratio(path[idx], output="output", seed=1337, ratio=(.7, .2, .1), group_prefix=None) # default values



# viewing images in batches
def image_plot(class_list, rows, batch, cols=batch_size):   
    fig, axs = plt.subplots(rows,cols,figsize=(cols*3,rows*3))
    for i in range(rows):
        images, labels = next(batch)
        for j, pic in enumerate(images):
            if rows > 1:
                axs[i,j].imshow(pic/255)
                axs[i,j].set_title(class_list[list(labels[j]).index(1)])
            else:
                axs[j].imshow(pic/255)
                axs[j].set_title(class_list[list(labels[j]).index(1)])



# checking the predictions of images
def image_plot_predict(class_list, rows, batch, model, cols=batch_size):   
    fig, axs = plt.subplots(rows,cols,figsize=(cols*3,rows*4))
    for i in range(rows):
        images, labels = next(batch)
        predictions = model.predict(images)
        for j, pic in enumerate(images):
            title = 'predict' + ' ' + \
            class_list[list(predictions[j]).index(predictions[j].max())] + ' ' + \
            '\n' + \
            'actual' + ' ' + \
            class_list[list(labels[j]).index(1)]
            if rows > 1:
                axs[i,j].imshow(pic/255)
                axs[i,j].set_title(title)
            else:
                axs[j].imshow(pic/255)
                axs[j].set_title(title)



# predicting on the test batch 
def result(test_gen, model):
    pred_, actual_  = [], []  
    r = round(test_batches.n / test_batches.batch_size)
    for i in range(r +1):
        images, labels = next(test_gen)
        predictions = model.predict(images)
        for j, label in enumerate(labels):
            actual_.append(label.argmax())
            pred_.append(predictions[j].argmax())
    return pred_, actual_


#incorrect predictions plotted
def missed(test_gen, model, classlist):
    wrong, ximages, correct = [], [], []
    r = round(test_gen.n / test_gen.batch_size)
    idx = 0
    for i in range(r):
        images, labels = next(test_gen)
        predictions = model.predict(images)
        for j, label in enumerate(labels):
            actual_ = label.argmax()
            pred_ = predictions[j].argmax() 
            if actual_ != pred_:
                correct.append(classlist[actual_].replace('_', ' '))
                wrong.append(classlist[pred_].replace('_', ' '))
                ximages.append(images[j])
    return wrong, ximages, correct