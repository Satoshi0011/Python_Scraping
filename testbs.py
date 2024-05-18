href_list = [link.get("href") for link in soup.find_all("a") if link.get("href")]

for href in href_list:
    print(href)
