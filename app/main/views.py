from ast import Not
from . import main
from flask import url_for, redirect,request,render_template,abort,flash
from ..models import *
from .forms import OrderForm

@main.route('/')
def home():
    title = 'Home'    
    movies = Movie.query.all()    
    auditoriums = Auditorium.query.all()    
    return render_template('index.html', title=title, movies=movies, foo=get_auditorium)    

@main.route('/movie/<int:id>', methods=['GET', 'POST'])    
def details(id):        
    title = 'Movie Details'
    movie = Movie.query.filter_by(_id=id).all() 
    auditorium = Auditorium.query.filter_by(_id=movie[0].auditoriumId).all() 
    tickets = Ticket.query.filter_by(movie_id=id).all()    
    order_form = OrderForm()    
    if request.method == "POST" and order_form.validate():
        email = order_form.email.data
        totalTickets = order_form.tickets.data             
        movie = Movie.query.filter_by(_id=id).all()        
        users = Customer.query.filter_by(email=email).all()
        if len(users) > 0 and movie is not None:
            new_ticket = Ticket(movie_id=movie[0]._id, customer_id=users[0]._id, no_of_tickets=totalTickets)
            new_ticket.save_ticket()                     
    return render_template('details.html', title=title,movie=movie,auditorium=auditorium,tickets=tickets, foo=get_customers, order_form=order_form)

def get_auditorium(id):        
    auditorium = Auditorium.query.filter_by(_id=id).all()       
    return auditorium[0].name

def get_customers(id):          
    customers = Customer.query.filter_by(_id=id).all()       
    return customers[0]
    