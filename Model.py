import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Time
import time
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from contextlib import contextmanager
from sqlalchemy import exists
import psycopg2


engine = create_engine('postgresql://postgres:2004@localhost:5432/postgres')

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
Base = declarative_base()
class user(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    phone = Column(String)
    name = Column(String)
    surname = Column(String)

class vehicle(Base):
    __tablename__ = 'vehicle'
    vehicle_id = Column(Integer, primary_key=True)
    vehicle_type = Column(String)


class staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True)
    position = Column(String)
    name = Column(String)
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'))


class booking(Base):
    __tablename__ = 'booking'
    booking_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'))
    price = Column(Integer)
    booking_time = Column(Time(timezone=False))

class Model():

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='2004',
            host='localhost',
            port=5432
        )

    def gener_add_user(self, num1, num2):
        c = self.conn.cursor()
        num = 0
        for i in range(num1, num2 + 1):
            c.execute('SELECT * FROM "user" WHERE "user_id" = %s', (i,))
            check = c.fetchall()
            if check:
                print("user_id %s already exists", i)
                num = 1

        if num == 0:
            c.execute('INSERT INTO "user" ("user_id", "phone", "name", "surname") SELECT generate_series as "user_id", chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) as phone, to_tsvector(chr(trunc(65+random()*50)::int) || chr(trunc(65+random()*25)::int)|| chr(trunc(65+random()*25)::int)) as name, chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) as surname FROM generate_series(%s, %s)',(num1, num2))

            self.conn.commit()
        else:
            print("Error! ID already in use")

    def get_all_vehicle(self):
        s = Session()
        return s.query(vehicle).all()

    def add_vehicle(self, vehicle_id, vehicle_type):
        s = Session()
        check = s.query(exists().where(vehicle.vehicle_id == vehicle_id)).scalar()
        if (check):
            print("Error! Identifier already exists")
        else:
            v = vehicle(
                vehicle_id=vehicle_id,
                vehicle_type=vehicle_type
            )
            s.add(v)
            s.commit()
            print("Added successfully")
        s.close()

    def update_vehicle(self, vehicle_id, vehicle_t):
        s = Session()
        v = s.query(vehicle).filter_by(vehicle_id=vehicle_id).first()
        if v:
            v.vehicle_type = vehicle_t
            s.commit()
            print("Catalog updated successfully!")
        else:
            print("Error! Catalog does not exist")
        s.close()

    def delete_vehicle(self, vehicle_id):
        with session_scope() as s:
            b = s.query(booking).filter_by(vehicle_id=vehicle_id).all()
            if b:
                for i in b:
                    s.delete(i)
                s.commit()
                print("Deleted successfully!")
            v = s.query(vehicle).get(vehicle_id)
            if v:
                s.delete(v)
                s.commit()
                print("Deleted successfully!")
            else:
                print("Error! Vehicle doesn't exist")

    def add_staff(self, staff_id, vehicle_id, name, position):
        s = Session()
        check = s.query(exists().where(staff.staff_id == staff_id)).scalar()
        if (check):
            print("Error! Identifier already exists")
        else:
            check1 = s.query(exists().where(vehicle.vehicle_id == vehicle_id)).scalar()
            if (check1):
                st = staff(
                    staff_id=staff_id,
                    vehicle_id=vehicle_id,
                    name = name,
                    position = position
                )
                s.add(st)
                s.commit()
                print("Added successfully!")
        s.close()

    def update_staff(self, staff_id, position, name, vehicle_id):
        s = Session()
        st = s.query(staff).filter_by(staff_id=staff_id).first()
        v = s.query(vehicle).filter_by(vehicle_id=vehicle_id).first()
        if st and v:
            st.vehicle_id = vehicle_id
            st.position = position
            st.name = name
            s.commit()
            print("Updated successfully!")
        else:
            print("Error! Vehicle does not exist")
        s.close()

    def delete_staff(self, staff_id):
        with session_scope() as s:
            st = s.query(staff).get(staff_id)
            if st:
                s.delete(st)
                s.commit()
                print("Deleted successfully!")
            else:
                print("Error! Does not exist")

    def get_all_staff(self):
        s = Session()
        return s.query(staff).all()


    def add_user(self, user_id, phone, name, surname):
        s = Session()
        check = s.query(exists().where(user.user_id == user_id)).scalar()
        if (check):
            print("Error! Identifier already exists")
        else:
            u = user(
                user_id=user_id,
                phone = phone,
                name=name,
                surname=surname
            )
            s.add(u)
            s.commit()
            print("Added successfully!")
        s.close()

    def update_user(self, user_id, phone, name, surname):
        s = Session()
        u = s.query(user).filter_by(user_id=user_id).first()
        if u:
            u.name = name
            u.phone = phone
            u.surname = surname
            s.commit()
            print("Updated successfully!")
        else:
            print("Error! User does not exist")

        s.close()

    def delete_user(self, user_id):
        with session_scope() as s:
            u = s.query(user).get(user_id)
            b = s.query(booking).filter_by(user_id=user_id).all()


            if u and b:
                for book in b:
                    s.delete(book)
                s.commit()
                print("User deleted from booking")
            if u:
                s.delete(u)
                s.commit()
                print("User deleted!")
            else:
                print(f"Error! User does not exist")

    def get_all_user(self):
        s = Session()
        return s.query(user).all()

    def add_booking(self, booking_id, user_id, vehicle_id, price, booking_time):
        s = Session()
        check = s.query(exists().where(booking.booking_id == booking_id)).scalar()
        if (check):
            print("Error! Identifier already exists")
        else:
            check1 = s.query(exists().where(vehicle.vehicle_id == vehicle_id)).scalar()
            check2 = s.query(exists().where(user.user_id == user_id)).scalar()
            if check1 and check2:
                b = booking(
                    booking_id=booking_id,
                    vehicle_id=vehicle_id,
                    price = price,
                    booking_time =booking_time,
                    user_id=user_id
                )
                s.add(b)
                s.commit()
                print("Booking added successfully!")
            else:
                print("Error! Identifier does not exist")
        s.close()

    def get_all_booking(self):
        s = Session()
        return s.query(booking).all()

    def update_booking(self, booking_id, user_id, vehicle_id, price, booking_time):
        s = Session()
        b = s.query(booking).filter_by(booking_id=booking_id).first()
        v = s.query(vehicle).filter_by(vehicle_id=vehicle_id).first()
        u = s.query(user).filter_by(user_id=user_id).first()
        if b and v and u:
            b.vehicle_id = vehicle_id
            b.user_id = user_id
            b.price = price
            b.booking_time = booking_time
            s.commit()
            print("Booking updated successfully!")
        else:
            print("Error! Booking does not exist")
        s.close()


    def delete_booking(self, booking_id):
        s = Session()
        b = s.query(booking).get(booking_id)
        if b:
            s.delete(b)
            s.commit()
            print("Booking deleted successfully!")
        else:
            print("Error! Booking does not exist")

