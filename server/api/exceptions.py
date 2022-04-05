from fastapi import HTTPException, status

INCORRECT_CREDENTIALS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Bad credentials, incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)
