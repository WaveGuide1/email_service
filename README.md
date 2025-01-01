# App Description
**This app is a Message Board and Newsletter Platform designed for communication and engagement. Users can post messages, subscribe to boards, and receive newsletters via email.**
- Celery + Redis: Used for background tasks like sending newsletters, ensuring efficient email delivery without slowing the app. Celery makes it easy to handle time-consuming tasks like sending hundreds of emails.
- Backend: Python (Django) for robust server-side logic and database management.
- Email Integration: Django's email system for delivering personalised newsletters to subscribers.
- Database: PostgreSQL for storing messages, users, and subscriptions
- Email Integration: Django's email system for delivering personalised newsletters to subscribers.
- Frontend: HTML, CSS (Tailwind), and JavaScript for a responsive and modern design.

<br>

### Actions
- **Celery Worker**
- **Flower**
- **Beat**
- **Redis**
- **PostgreSQL**

<br>

## Setup

#### - Create Virtual Environment
###### # Linux
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
python3 -m venv venv
.\venv\Scripts\activate.bat
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```


