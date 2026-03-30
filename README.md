# Doc-Python-Django

A Django-based medical care web application for managing doctor and patient registrations.

## Features
- Doctor and patient registration forms
- Custom styled registration page
- Uses Django, Bootstrap, and custom CSS

## Getting Started

### Prerequisites
- Python 3.11+
- pip
- Virtualenv (recommended)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Suniltkumartsk/Doc-Python-Django.git
   cd Doc-Python-Django
   ```
2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   If requirements.txt is missing, install manually:
   ```
   pip install django pillow
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure
- `myproject/` - Django project settings
- `myapp/` - Main application logic
- `templates/` - HTML templates
- `static/` - Static files (CSS, images)
- `media/` - Uploaded media files

## Project Output:
![alt text](<Screenshot 2026-03-30 132738.png>)
![alt text](<Screenshot 2026-03-30 132101.png>)
![alt text](<Screenshot 2026-03-30 132124.png>)
![alt text](<Screenshot 2026-03-30 132549.png>)
![alt text](<Screenshot 2026-03-30 132601.png>)


## License
This project is licensed under the MIT License.
