from app.flask_server import db
from app.models import Pizza
from models import catalog
import re


def transform_choice(choice):
    transformed_choice = {}
    transformed_choice['size'] = choice['title'][:2]
    transformed_choice['weight'] = (re.search(r'\((\d+)', choice['title'])
                                      .group(1))
    transformed_choice['price'] = choice['price']
    return transformed_choice


def transform_catalog_pizza_to_one_level():
    one_level_catalog = []
    for catalog_entry in catalog:
        pizza_information = {'title': catalog_entry['title'],
                             'description': catalog_entry['description']}
        for choice in catalog_entry['choices']:
            one_level_catalog_entry = {}
            one_level_catalog_entry.update(pizza_information)
            transformed_choice = transform_choice(choice)
            one_level_catalog_entry.update(transformed_choice)
            one_level_catalog.append(one_level_catalog_entry)
    return one_level_catalog


def load_pizzas():
    one_level_catalog = transform_catalog_pizza_to_one_level()
    for catalog_entry in one_level_catalog:
        pizza = Pizza(**catalog_entry)
        db.session.add(pizza)
    db.session.commit()


if __name__ == "__main__":
    load_pizzas()
