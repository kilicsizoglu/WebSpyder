from database_connect import database_connect
from get_links import get_links
from web_site import web_site


def main():
    start_url = "https://www.technopat.net/"
    visited_urls = set()
    to_visit = [start_url]

    i = 0

    database = database_connect()
    sites = database.get_website()

    sites_array = set()
    for site in sites:
        sites_array.add(site.url)

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url not in sites_array:
            if current_url not in visited_urls:
                visited_urls.add(current_url)
                for link in get_links(current_url):
                    to_visit.append(link)
                    database = database_connect()
                    database.add_website(url=link)
                    i += 1
                    print("visited " + str(i))


if __name__ == '__main__':
    main()
