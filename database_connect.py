import string

from mongoengine import connect

import web_site


class database_connect:
    def __init__(self):
        connect(
            db='web_spyder',
            username='kilicsizoglu',
            password='',
            authentication_source='admin',
            host='127.0.0.1',
            port=27017,
        )

    def get_website(self):
        sites = web_site.web_site.objects()
        return sites

    # Veritabanına Kayıt Ekleme
    def add_website(self, url):
        website = web_site.web_site()
        website.url = url
        website.save()
        return website

    # Veritabanında Kayıt Güncelleme
    def update_website(original_url, new_url):
        website = web_site.web_site.objects(url=original_url).first()
        if website:
            website.update(url=new_url)
            return True
        return False

    # Veritabanından Kayıt Silme
    def delete_website(url):
        website = web_site.web_site.objects(url=url).first()
        if website:
            website.delete()
            return True
        return False

