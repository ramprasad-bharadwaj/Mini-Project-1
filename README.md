# PRSV - Travel Management System

## Overview

PRSV is a travel management application designed to streamline travel planning and management. It allows customers to book their trips by selecting from a range of destinations, drivers (captains), and hotels. Administrators can manage the system through a dedicated admin panel where they can update travel details, staff, and pricing.

## Key Features

- **Personalized Travel Packages**: Users can select destinations, drivers, and hotels based on their preferences.
- **Admin Panel**: The admin can manage destinations, hotels, driver staff, and ticket prices, as well as access customer details.
- **Booking System**: Users can book tickets after choosing their destination, driver, and hotel.

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: MySQL

## Project Structure

- `prsv/`: Contains the main Django project files.
- `templates/`: HTML templates for the frontend interface.
- `static/`: CSS and static files for styling.
- `db/`: MySQL database schema and ER diagrams.

## Admin Panel

The admin panel provides full control over the travel management system:
- **Manage Destinations**: Add or modify travel destinations.
- **Manage Hotels**: Update hotel listings and information.
- **Manage Drivers**: Add or remove drivers (captains).
- **Manage Ticket Prices**: Set and adjust travel package prices.
- **Customer Management**: View and manage customer details and bookings.

## Database Operations

This project explores MySQL integration by implementing CRUD operations for all major entities:
- **Destinations**: Create, read, update, and delete travel destinations.
- **Hotels**: Add, view, modify, or remove hotel details.
- **Drivers**: Manage driver (captain) information.
- **Bookings**: Handle customer bookings and payment details.

## How to Run

Clone the repository:
   ```bash
   git clone https://github.com/yourusername/prsv.git
   cd prsv

## Set up a Virtual Environment:

```bash
python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prsv',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

