# 🎬 Cinema Ticket Reservation Platform 🍿

A **web-based cinema ticket booking system** built with Django REST Framework, allowing users to easily browse movies, select showtimes, and reserve tickets for their preferred seats. The system features **JWT-based authentication** with a custom user model for enhanced user management.

---

## 🚀 Features

- **🔐 User Authentication & Registration:**
  - Custom user model with extended fields.
  - Secure JWT-based login and token management.
  - Personalized registration and login process.

- **🎥 Movie Listings:**
  - Browse available movies with title, description, and ratings.
  - Filter by genres, release dates, and more.

- **🪑 Seat Selection:**
  - Interactive seat map for users to choose seats for each showtime.
  - Real-time seat availability prevents double bookings.

- **💳 Booking & Payment:**
  - Reserve multiple tickets and proceed to payment.
  - Integration with payment gateways for secure transactions (optional).

- **⚙️ Admin Panel:**
  - Manage movies, showtimes, users, and bookings via Django Admin.
  - Full control over user roles (admin, staff).

---

## 🛠️ Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** Custom JWT-based authentication
- **Frontend:** (To be integrated with React, Vue, or Angular)
- **Deployment:** Docker for containerization (optional)

---

## 📦 Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cinema-ticket-reservation-platform.git
   cd cinema-ticket-platform
   ```
   2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   3. Set up PostgreSQL database and update settings.py:
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
   }
   ```
   4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   5. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
    6. Start the development server:
    ```bash
    python manage.py runserver
    ```

    👤 Custom User Model

    This project uses a custom user model for managing authentication and user roles. Key features include:

   . Unique email as the primary user identifier.
   . Secure JWT-based session management.
   . is_staff and is_superuser fields for admin control.

    📜 License

    This project is licensed under the MIT License. See the LICENSE file for more information.


   Made with ❤️ by AMIRSALAR
