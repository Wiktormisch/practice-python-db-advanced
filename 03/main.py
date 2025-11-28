from db import Session, engine
from models import Base, Person, Skill, person_skill
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import func


Base.metadata.create_all(engine)

# --Pytanie-- Czy "tworzyć" rekordy w sesji i je zapisywac, czy lepiej stworzyc je jako zmienne globalne i potem je dodac do sesji??

with Session(engine) as session:
    try:    # Tworzenie rekordow
        person_1 = Person(name="Krystian Krystek")
        person_2 = Person(name="Zenek Bochenek")
        person_3 = Person(name="Maciej Bogdanski")
        skill_1 = Skill(name="Gotowanie")
        skill_2 = Skill(name="Plywanie")
        skill_3 = Skill(name="Jazda na rowerze")
        skill_4 = Skill(name="Programowanie")
        skill_5 = Skill(name="Grafika komputerowa")
        skill_6 = Skill(name="Fotografia")

        # Dodanie osob i umijetnosci
        session.add_all([person_1, person_2, person_3,
                        skill_1, skill_2, skill_3,
                        skill_4, skill_5, skill_6])
        print("Poprawnie dodadno osoby i umiejetnosci")

        # Nadanie umiejetnosci osobom

        person_1.skills.append(skill_1)
        person_2.skills.extend([skill_2, skill_3, skill_4])
        person_3.skills.extend([skill_3, skill_4, skill_5])
        skill_6.people.append(person_1)
        session.commit()
        print("Poprawnie nadano umiejetnosci osobom")

    except SQLAlchemyError as e:
        session.rollback()
        print(f"Nie udalo sie dodac rekordow. Blad: {e}")


# Odczytywanie umiejetnosci jednej osoby

with Session(engine) as session:
    try:
        krystek = session.query(Person).filter_by(
            name="Krystian Krystek").one()

        print(f"Umiejetnosci {krystek.name}:")
        for skill in krystek.skills:
            print(skill.name)
    except SQLAlchemyError as e:
        print("Nie udalo sie pobrac skili Krystka. Blad:{e}")

# Odczytywanie osoby ktore posiada dana umiejetnosc

with Session(engine) as session:
    try:
        coding = session.query(Skill).filter_by(name="Programowanie").one()

        print(f"Osoby ktore znaja {coding.name}:")
        for person in coding.people:
            print(person.name)
    except SQLAlchemyError as e:
        print("Nie udalo sie pobrac listy osob. Blad:{e}")
