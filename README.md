# employee_management_system
Project Explanation
1. Overview
	•	A FastAPI application for managing file uploads, downloads, listing, and deletion with user authentication.
2. Key Components
	•	FastAPI: The main web framework used for building the API.
	•	Uvicorn: ASGI server used to run the FastAPI application.
	•	Passlib: Library for secure password hashing.
	•	OAuth2: Used for user authentication and authorization.
3. Project Structure
	•	main.py: Main file for the FastAPI application.
	•	auth.py: Handles user authentication.
	•	__init__.py: Makes the directory a package.
4. Endpoints
	•	/token: POST endpoint for user login, returns access token.
	•	/upload/: POST endpoint for uploading files.
	•	/download/{filename}: GET endpoint for downloading files.
	•	/files/: GET endpoint for listing all files.
	•	/delete/{filename}: DELETE endpoint for deleting files.
5. Features
	•	File Validation: Only allows specific file types (.png, .jpg, .jpeg, .pdf, .txt).
	•	User Authentication: Uses OAuth2 and Passlib for secure user authentication.
	•	File Operations: Supports upload, download, listing, and deletion of files.
Execution Steps
1. Create Project Structure
2. Create the necessary directories and files:
    mkdir file_management
    cd file_management
