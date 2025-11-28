from db import Session, engine
from models import Base, Measurment
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import func


Base.metadata.create_all(engine)

with Session(engine) as session:
    try:    # Tworzenie rekordow
        measurment_1 = Measurment(
            device_name="Aparat", value=0.123, timestamp="2021-09-09")
        measurment_2 = Measurment(
            device_name="Czujnik", value=1, timestamp="2021-10-10")
        measurment_3 = Measurment(
            device_name="Termometr", value=36.6, timestamp="2021-11-11")
        measurment_4 = Measurment(
            device_name="Aparat", value=0.501, timestamp="2021-12-12")
        measurment_5 = Measurment(
            device_name="Czujnik", value=3, timestamp="2022-01-01")
        measurment_6 = Measurment(
            device_name="Termometr", value=37.2, timestamp="2022-02-02")
        measurment_7 = Measurment(
            device_name="Aparat", value=0.234, timestamp="2022-03-03")
        measurment_8 = Measurment(
            device_name="Aparat", value=0.423, timestamp="2022-03-01")

        # Dodanie rekordow do bazy
        session.add_all([measurment_1, measurment_2, measurment_3,
                        measurment_4, measurment_5, measurment_6,
                        measurment_7, measurment_8])
        session.commit()
        print("Pomiary dodane pomyslnie")
    except SQLAlchemyError as e:
        session.rollback()
        print(f" Blad dodania pomiarow: {e}")

# Obliczenie ilosci wykonanych pomiarow na urzadzenie

with Session(engine) as session:
    try:
        measurment_count = session.query(
            Measurment.device_name,
            func.count(Measurment.id)
            ).group_by(Measurment.device_name).all()

        for device, number in measurment_count:
            print(f"{device} wykonal {number} pomiarow")
    except SQLAlchemyError as e:
        print("Nie udalo sie pobrac pomiarow. Blad:{e}")


with Session(engine) as session:
    try:
        measurment_avg = session.query(
            Measurment.device_name,
            func.avg(Measurment.value)
            ).group_by(Measurment.device_name).all()
        
        for device, value in measurment_avg:
            print(f"-{device}- srednia wartosc pomiarow wynosi {value}")
        
    except SQLAlchemyError as e:
        print("Nie udalo sie pobrac srednich wartosci pomiarow. Blad:{e}")
