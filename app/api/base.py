from fastapi.responses import JSONResponse

class BaseApi():
    def make_response(self, payload: dict = {}, message: str = 'success', meta: dict = {}, code: int = 200):
        return JSONResponse(status_code=code, content={"message": message, "meta":meta, "data": payload})