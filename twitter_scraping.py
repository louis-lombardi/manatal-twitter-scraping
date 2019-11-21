from robobrowser import RoboBrowser

def scrap_twitter(url):
    browser = RoboBrowser(history = True,parser = 'lxml')
    browser.open(url)  # load the page HTML
    followers = browser.select('li.ProfileNav-item--followers > a > span.ProfileNav-value')[0]   # find the span node containing the followers count
    amount_followers = int(followers['data-count'])  # extract attribute value and convert it to int
    return(amount_followers)


##### TEST WITH KMBAPPE #####
    
KMbappe_followers = scrap_twitter('https://twitter.com/KMbappe')
print("KMbappe has currently " + str(KMbappe_followers) + " followers.")