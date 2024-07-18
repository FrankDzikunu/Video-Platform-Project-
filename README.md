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
│
├── video_app/
│   ├── __pycache__/
│   ├── media/                       # Directory for storing uploaded media files
│   ├── video_app/
│   │   ├── __pycache__/
│   │   ├── __init__.py              # Initialization file for the Django app
│   │   ├── asgi.py                  # ASGI configuration
│   │   ├── settings.py              # Django settings file
│   │   ├── urls.py                  # URL routing
│   │   ├── wsgi.py                  # WSGI configuration
│   ├── videos/
│   │   ├── __pycache__/
│   │   ├── migrations/              # Directory for database migrations
│   │   ├── __init__.py              # Initialization file for the videos app
│   │   ├── admin.py                 # Admin configuration for videos
│   │   ├── apps.py                  # App configuration for videos
│   │   ├── forms.py                 # Forms for user input
│   │   ├── models.py                # Database models for videos
│   │   ├── tests.py                 # Unit tests for the videos app
│   │   ├── urls.py                  # URL routing for the videos app
│   │   ├── views.py                 # Views for handling requests
│   │   ├── migrations/              # Database migrations
│   │   │   ├── __pycache__/
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_rename_video_file_video_file_and_more.py
│   │   │   ├── 0003_video_uploaded_by.py
│   ├── templates/
│   │   ├── videos/
│   │   │   ├── home.html            # Home page template
│   │   │   ├── login.html           # Login page template
│   │   │   ├── password_reset_complete.html  # Password reset complete template
│   │   │   ├── password_reset_confirm.html   # Password reset confirm template
│   │   │   ├── password_reset_done.html      # Password reset done template
│   │   │   ├── password_reset_form.html      # Password reset form template
│   │   │   ├── profile.html         # Profile page template
│   │   │   ├── signup.html          # Signup page template
│   │   │   ├── upload_video.html    # Upload video page template
│   │   │   ├── video_detail.html    # Video detail page template
│   │   │   ├── videos_list.html     # Videos list page template
│   │   │   ├── watch_video.html     # Watch video page template
│   │   │   ├── base_generic.html    # Base template
├── db.sqlite3                       # SQLite database file
├── manage.py                        # Django management script
├── README.md                        # Project documentation, including setup, usage, and ER diagram
├── requirements.txt
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

#### Database Design (ER Diagram)

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






