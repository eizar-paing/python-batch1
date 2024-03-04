import re

def website_url(url):
    url_reg = r"^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
    result = re.match(url_reg, url)

    if result:
        print("Correct url!")
    else:
        print("Incorrect url!")


website1 = "https://www.youtube.com/"
website_url(website1)

webiste2 = "https://www.geeksforgeeks.org/"
website_url(webiste2)

website3 = input("Enter your url: ")
website_url(website3)

# /^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*
# ^(http(s)?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/\S*)?$
