from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('headless')


browser = webdriver.Chrome(chrome_options=options) #replace with .Firefox(), or with the browser of your choice

url = "https://www.heb.com/search/?q=chicken"
posts = []

while posts == []:
    browser.get(url) #navigate to the page

    posts = browser.find_elements_by_class_name("responsivegriditem__title")

#Convert web elements to text/string
new_posts = []
for post in posts:
    new_posts.append(post.text)


#Remove Duplicates
results = []
for post in new_posts:
    if post not in results:
        results.append(post)



print(*results, sep = '\n')

browser.close()