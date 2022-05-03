from . import db
from datetime import datetime


class Customer(db.Model):
    __tablename__ = 'customers'

    _id = db.Column(db.Integer,primary_key = True)    
    firstName = db.Column(db.String(40), nullable=False)
    lastName = db.Column(db.String(40), nullable=False)    
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True)    


    def __repl__(self) -> None:
        return f'{self.lastName} {self.firstName}'    

    def save_customer(self):
        db.session.save(self)
        db.session.commit()

    def allCustomers(self):        
        customers = Customer.objects.all()
        return customers

class Auditorium(db.Model):    
    __tablename__ = 'auditorium'

    _id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(60), nullable = False)    
    CustomerCapacity = db.Column(db.Integer, nullable = False)

    def __repl__(self) -> None:
        return f'{self.name}'    

    def save_auditorium(self):
        db.session.save(self)
        db.session.commit()    

class Movie(db.Model):
    __tablename__ = 'movies'

    _id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(25))
    description = db.Column(db.String(30000)),
    price = db.Column(db.Integer)  
    auditoriumId = db.Column(db.Integer, db.ForeignKey('auditorium._id'))    
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repl__(self) -> None:
        return f'{self.title}'    

    def save_movie(self):
        db.session.save(self)
        db.session.commit()    
       

class Ticket(db.Model):
    __tablename__ = 'tickets'

    _id = db.Column(db.Integer, primary_key=True)    
    no_of_tickets = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers._id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies._id'))

    def __repl__(self) -> None:
        return f'{self.price}'    

    def save_ticket(self):
        db.session.add(self)
        db.session.commit()

class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer,primary_key = True)    
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets._id'))    
    total_amount = db.Column(db.Integer)
    payment_reference = db.Column(db.Integer)

    def __repl__(self) -> None:
        return f'{self.order_id}'    

    def save_order(self):
        db.session.save(self)
        db.session.commit()





