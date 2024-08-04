from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, status
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordRequestForm
# from auth import authenticate_user, get_current_user, oauth2_scheme
from auth import authenticate_user, get_current_user, fake_users_db
import os

app = FastAPI()

UPLOAD_DIRECTORY = "./uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user["username"], "token_type": "bearer"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    if not file.filename.endswith(('.png', '.jpg', '.jpeg', '.pdf', '.txt')):
        raise HTTPException(status_code=400, detail="File type not allowed.")
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail="File could not be saved.")
    
    return {"filename": file.filename}

@app.get("/download/{filename}")
async def download_file(filename: str, current_user: dict = Depends(get_current_user)):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    
    return FileResponse(file_path, media_type='application/octet-stream', filename=filename)

@app.get("/files/")
async def list_files(current_user: dict = Depends(get_current_user)):
    files = os.listdir(UPLOAD_DIRECTORY)
    return {"files": files}

@app.delete("/delete/{filename}")
async def delete_file(filename: str, current_user: dict = Depends(get_current_user)):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    
    try:
        os.remove(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail="File could not be deleted.")
    
    return {"detail": "File deleted successfully."}
