### Project Title: Video Platform
### Project Objective
The objective of this project is to develop a bespoke video platform for Paul Leonard, a video creator, who wants a branded platform to upload and share videos exclusively for his business. The platform should provide user authentication, video navigation, sharing capabilities, and administrative features for video management.

### Customer Requirements
**User Functionality:**

**Signup & Login:**

Users can create an account using email and password.
Account verification via email to ensure security and validity.
Password reset feature for recovering lost passwords.
Video Navigation:

Users can navigate through video pages.
Each page displays one video at a time.
Next and previous buttons allow users to load the next or previous video page.
Video Sharing:

Users can share links to specific video pages.
A share button on each video page facilitates sharing.
Video Player Controls:

Common control buttons (play, pause, volume control, fullscreen) for video playback.
Branding:

The business logo is prominently displayed on each video page.

**Admin Functionality:**

**Video Upload:**
Admins can upload videos with titles and descriptions.
Uploaded videos are managed through administrative privileges.
### Deliverables
**Web Application Source Code:**

Hosted on GitHub with Git flow implementation (branches for features, development, and production).
README file detailing setup instructions, dependencies, and usage guidelines.

**ER Diagram of Database Design:**

Entity-Relationship (ER) diagram illustrating the database schema.
Tables for users, videos, and associated metadata.

**Deployed Link:**

A link to the deployed web application for testing and demonstration purposes.




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
