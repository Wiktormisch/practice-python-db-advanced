from db import Session, engine
from models import Base, Item
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import func


Base.metadata.create_all(engine)

with Session(engine) as session:
    try:    # Tworzenie rekordow
        item_1 = Item(name="miecz", priority=10)
        item_2 = Item(name="tarcza", priority=12)
        item_3 = Item(name="mikstura", priority=8)
        item_4 = Item(name="zbroja", priority=5)
        item_5 = Item(name="buty", priority=18)
        item_6 = Item(name="helm", priority=5)
        item_7 = Item(name="rekawice", priority=15)
        item_8 = Item(name="mapa", priority=30)
        item_9 = Item(name="kusza", priority=22)
        item_10 = Item(name="strzaly", priority=14)
        item_11 = Item(name="lina", priority=6)
        item_12 = Item(name="pochodnia", priority=9)
        item_13 = Item(name="ziola", priority=11)
        item_14 = Item(name="pierścień", priority=25)
        item_15 = Item(name="amulet", priority=27)
        item_16 = Item(name="kilof", priority=13)
        item_17 = Item(name="młot bojowy", priority=19)
        item_18 = Item(name="kusza ciężka", priority=28)
        item_19 = Item(name="księga zaklęć", priority=35)
        item_20 = Item(name="prowiant", priority=4)
        item_21 = Item(name="piorun kulisty", priority=40)
        item_22 = Item(name="zwoj teleportacji", priority=32)
        item_23 = Item(name="plaszcz", priority=16)

        # Dodanie rekordow do bazy
        session.add_all([item_1, item_2, item_3,
                        item_4, item_5, item_6,
                        item_7, item_8, item_9,
                        item_10, item_11, item_12,
                        item_13, item_14, item_15,
                        item_16, item_17, item_18,
                        item_19, item_20, item_21,
                        item_22, item_23])
        session.commit()
        print("Przedmioty dodane pomyslnie")
    except SQLAlchemyError as e:
        session.rollback()
        print(f" Blad dodania przedmiotow: {e}")

# Sortowanie przedmiotow

with Session(engine) as session:
    try:
        items_list = session.query(Item).order_by(
            Item.priority).limit(5).offset(10).all() # Dodanie paginacji

        for item in items_list:
            print(
                f"Przedmiot *{item.name}* posiada priorytet: -{item.priority}-")
    except SQLAlchemyError as e:
        print(f"Nie udalo sie pobrac przedmiotow {e}")