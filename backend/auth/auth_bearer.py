from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from auth.auth_handler import decodeJWT

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)

        if credentials:
            if not decodeJWT(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid Authorization")