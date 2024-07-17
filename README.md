# Video App

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhokabeatz/Video-App.git
   cd Video-App
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
 
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
