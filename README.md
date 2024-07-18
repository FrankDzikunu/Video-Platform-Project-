### Project Title: Video Platform

#### Project Objective
The objective of this project is to develop a bespoke video platform for Paul Leonard, a video creator, who wants a branded platform to upload and share videos exclusively for his business. The platform should provide user authentication, video navigation, sharing capabilities, and administrative features for video management.

#### Customer Requirements

**User Functionality:**
1. **Signup & Login:**
   - Users can create an account using email and password.
   - Account verification via email to ensure security and validity.
   - Password reset feature for recovering lost passwords.

2. **Video Navigation:**
   - Users can navigate through video pages.
   - Each page displays one video at a time.
   - Next and previous buttons allow users to load the next or previous video page.

3. **Video Sharing:**
   - Users can share links to specific video pages.
   - A share button on each video page facilitates sharing.

4. **Video Player Controls:**
   - Common control buttons (play, pause, volume control, fullscreen) for video playback.

5. **Branding:**
   - The business logo is prominently displayed on each video page.

**Admin Functionality:**
- **Video Upload:**
  - Admins can upload videos with titles and descriptions.
  - Uploaded videos are managed through administrative privileges.

#### Deliverables

1. **Web Application Source Code:**
   - Hosted on GitHub with Git flow implementation (branches for features, development, and production).
   - README file detailing setup instructions, dependencies, and usage guidelines.

2. **ER Diagram of Database Design:**
   - Entity-Relationship (ER) diagram illustrating the database schema.
   - Tables for users, videos, and associated metadata.

3. **Deployed Link:**
   - A link to the deployed web application for testing and demonstration purposes.

### Detailed Documentation

#### Technology Stack
- **Backend:** Python, Flask framework, SQLAlchemy for ORM.
- **Database:** MySQL or PostgreSQL.
- **Authentication:** Flask JWT Extended for user authentication.
- **Email Service:** SMTP configuration for sending verification and password reset emails.
- **Deployment:** Docker for containerization, Render for cloud deployment.

#### Project Structure
```
VIDEO-PLATFORM-PROJECT/
├── video_app/                     # Main Django project directory
│   ├── media/                     # Directory for user-uploaded media files
│   │   ├── thumbnails/            # Directory for video thumbnails
│   │   └── videos/                # Directory for video files
│   ├── static/                    # Directory for static files (CSS, images, JavaScript)
│   │   ├── css/                   # Directory for CSS files
│   │   └── images/                # Directory for image files
│   ├── __pycache__/               # Directory for compiled Python files
│   ├── __init__.py                # Indicates that this is a Python package
│   ├── asgi.py                    # ASGI configuration for asynchronous support
│   ├── settings.py                # Django project settings
│   ├── urls.py                    # URL configurations for the project
│   ├── wsgi.py                    # WSGI configuration for deployment
│   └── views.py                   # Views for the main project
├── videos/                        # Django app handling video-related functionalities
│   ├── __pycache__/               # Directory for compiled Python files
│   ├── migrations/                # Directory for database migration files
│   ├── templates/                 # Directory for HTML templates
│   │   ├── account/               # Directory for account-related templates
│   │   │   └── email/
│   │   │       └── email_confirmation_message.html  # Template for email confirmation
│   │   ├── home.html              # Template for the homepage
│   │   ├── login.html             # Template for login page
│   │   ├── password_reset_complete.html  # Template for password reset complete page
│   │   ├── password_reset_confirm.html   # Template for password reset confirmation page
│   │   ├── password_reset_done.html      # Template for password reset done page
│   │   ├── password_reset_form.html      # Template for password reset form page
│   │   ├── profile.html           # Template for user profile page
│   │   ├── signup.html            # Template for signup page
│   │   └── video_detail.html      # Template for video detail page
│   ├── __init__.py                # Indicates that this is a Python package
│   ├── admin.py                   # Admin configuration for the app
│   ├── apps.py                    # App configuration
│   ├── forms.py                   # Forms for the app
│   ├── models.py                  # Database models for the app
│   ├── tests.py                   # Tests for the app
│   ├── urls.py                    # URL configurations for the app
│   └── views.py                   # Views for the app
├── db.sqlite3                     # SQLite database file
├── manage.py                      # Django management script
└── requirements.txt               # List of Python packages required for the project
```

### API Endpoints

#### Authentication (`auth_blueprint`):

- **Register User**
  - `POST /register`
  - Description: Registers a new user with email, username, and password.
  - Request Body:
    ```json
    {
      "email": "user@example.com",
      "username": "username",
      "password": "password"
    }
    ```
  - Response:
    - Success: 200 OK
    - Error: 400 Bad Request, 409 Conflict (if username or email already exists)

- **Login User**
  - `POST /login`
  - Description: Logs in a user with email and password, returns JWT token.
  - Request Body:
    ```json
    {
      "email": "user@example.com",
      "password": "password"
    }
    ```
  - Response:
    - Success: 200 OK with JWT token
    - Error: 401 Unauthorized

- **Logout User**
  - `POST /logout`
  - Description: Logs out the currently logged-in user (requires JWT token).
  - Request Header:
    ```json
    {
      "Authorization": "Bearer <JWT_TOKEN>"
    }
    ```
  - Response:
    - Success: 200 OK
    - Error: 401 Unauthorized

- **Forgot Password**
  - `POST /forgot-password`
  - Description: Initiates the process to reset the user's password by sending a reset email.
  - Request Body:
    ```json
    {
      "email": "user@example.com"
    }
    ```
  - Response:
    - Success: 200 OK, Email sent for password reset
    - Error: 404 Not Found (if email not found)

- **Reset Password**
  - `POST /reset-password`
  - Description: Resets the user's password after verifying the reset token.
  - Request Body:
    ```json
    {
      "token": "reset_token",
      "password": "new_password"
    }
    ```
  - Response:
    - Success: 200 OK, Password successfully reset
    - Error: 400 Bad Request (if token invalid or expired)

- **Verify Email**
  - `GET /verify-email/<token>`
  - Description: Verifies the user's email address after registration.
  - Response:
    - Success: Redirect to login page or success message
    - Error: 404 Not Found (if token invalid)

#### Video Management:

### Upload Video

- **Endpoint**
  - `POST /api/v1/video`
  - Description: Allows admin users to upload a new video.
  - Request Body:
    - **Content Type:** `multipart/form-data`
    - **Form Fields:**
      - `title`: Title of the video (string)
      - `description`: Description of the video (string)
      - `file`: Video file to upload (multipart file)
    - Example:
      ```html
      <form method="post" enctype="multipart/form-data">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" value="Video Title"><br>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description">Video Description</textarea><br>
        <input type="file" id="video_file" name="file"><br><br>
        <input type="submit" value="Submit">
      </form>
      ```
  - Response:
    - Success: 200 OK, Video uploaded successfully
    - Error: 401 Unauthorized (if not admin)


- **Get All Videos**
  - `GET /video`
  - Description: Retrieves all videos available on the platform.
  - Response:
    - Success: 200 OK with list of videos
    - Error: 404 Not Found (if no videos found)

- **Get Video by ID**
  - `GET /video/<video_id>`
  - Description: Retrieves a specific video by its unique ID.
  - Response:
    - Success: 200 OK with video details
    - Error: 404 Not Found (if video not found)

- **Get Videos by User ID**
  - `GET /video/user/<user_id>`
  - Description: Retrieves videos uploaded by a specific user.
  - Response:
    - Success: 200 OK with list of user's videos
    - Error: 404 Not Found (if user has no videos or not found)

- **Get Videos by Share ID**
  - `GET /video/share/<share_id>`
  - Description: Retrieves videos shared via a specific link ID.
  - Response:
    - Success: 200 OK with list of shared videos
    - Error: 404 Not Found (if share ID not found)

- **Update Video by ID**
  - `PATCH /video/<video_id>`
  - Description: Updates details of a specific video (requires JWT token).
  - Request Body:
    ```json
    {
      "title": "Updated Title",
      "description": "Updated Description"
    }
    ```
  - Response:
    - Success: 200 OK, Video updated successfully
    - Error: 401 Unauthorized, 404 Not Found (if video or user not authorized)

- **Delete Video by ID**
  - `DELETE /video/<video_id>`
  - Description: Deletes a specific video from the platform (requires JWT token).
  - Response:
    - Success: 200 OK, Video deleted successfully
    - Error: 401 Unauthorized, 404 Not Found (if video or user not authorized)

#### Health Endpoint

- **Check Health**
  - `GET /health/`
  - Description: Endpoint to check the health status of the application.
  - Response:
    - Success: 200 OK, Health status: OK
    - Error: 404 Not Found (if endpoint not found)

    ## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FrankDzikunu/Video-Platform-Project-.git
   cd Video-App
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use 'pip install virtualenv', 'virtualenv venv', `venv\Scripts\activate`

   # pip install --no-cache-dir django-allauth==0.63.6
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

#### Database Design (ER Diagram)

![ER Diagram](video_app\static\images\IMG-20240718-WA0006.jpg)

- **User Table:**
  - `id`, `email`, `password_hash`, `is_verified`, `verification_token`

- **Video Table:**
  - `id`, `title`, `description`, `video_url`, `uploaded_by`, `share_link`

- **EmailVerification Table:**
  - `id`, `email`, `token`, `created_at`

#### Deployment and Hosting

- **Deployment Options:**
  - Docker containerization for environment consistency.
  - Cloud deployment on RENDER.






