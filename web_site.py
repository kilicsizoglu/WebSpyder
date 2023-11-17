from mongoengine import StringField, Document


class web_site(Document):
    url = StringField(required=True)