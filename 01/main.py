from db import Session, engine
from models import Base, Note
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

Base.metadata.create_all(engine) 

# Dodawanie notatek
try:
    session = Session(bind=engine)
    note_1 = Note(title="Pierwsza notatka", body="wpis jeden", pinned=True)
    note_2 = Note(title="Druga notatka", body="drugi wpis tresc", pinned=False)
    session.add_all([note_1, note_2])
    session.commit()
    print("Notatki dodane pomyslnie")
except SQLAlchemyError as e:
    session.rollback()
    print(f"Blad: {e}")
finally:
    session.close()

# Odczytywanie notatek
try:
    session = Session(bind=engine)
    read_note = session.query(Note).filter(Note.title == "Pierwsza notatka").first()
    print(f"Tresc pobranej notatki: {read_note.body}")
except SQLAlchemyError as e:
    print(f"Blad podczas pobierania notatek: {e}")
finally:
    session.close()

# Aktualizowanie notatki sposobem przez with

with Session(engine) as session:
    try:
        update_note = session.query(Note).filter(Note.title == "Druga notatka").first()
        update_note.pinned = True
        session.commit()
        print("Notatka zostala przypieta")
    except SQLAlchemyError:
        session.rollback()
        print("Blad podczas aktualizacji notatki")

# Usuwanie notatki 

with Session(engine) as session:
    try:
        delete_note = session.query(Note).filter(Note.title == "Druga notatka").first()
        session.delete(delete_note)
        session.commit()
        print("Notatka usunieta pomyslnie")
    except SQLAlchemyError:
        session.rollback()
        print("Blad podczas usuwania notatki")