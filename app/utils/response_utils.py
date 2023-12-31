from fastapi.responses import JSONResponse

def response(status_code, message, data=None):
    if data is not None and isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, bytes):
                data[key] = value.decode('UTF-8')
    return JSONResponse(status_code=status_code, content={'status_code': status_code, 'message': message, 'data': data})
