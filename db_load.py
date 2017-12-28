from app import db, models
from models import catalog


def get_choice(choice_info):
    choices_query = db.session.query(models.Choice).filter(models.Choice.title == choice_info['title'])
    choices_query = choices_query.filter(models.Choice.price == choice_info['price'])
    if choices_query.count() > 0:
        return choices_query.first()
    choice = models.Choice(**choice_info)
    db.session.add(choice)
    db.session.commit()
    return choice


def load_pizzas(catalog):
    for catalog_entry in catalog:
        pizza = models.Pizza()
        pizza.title = catalog_entry['title']
        pizza.description = catalog_entry['description']
        for choice_entry in catalog_entry['choices']:
            choice = get_choice(choice_entry)
            pizza.choices.append(choice)
        db.session.add(pizza)
    db.session.commit()
    

if __name__ == "__main__":
    load_pizzas(catalog)