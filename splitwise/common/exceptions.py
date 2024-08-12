class BaseCustomError(Exception):
    def __init__(self, message: str = "Internal Server Error", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundError(BaseCustomError):
    def __init__(self, message: str):
        super().__init__(message, 404)


class BadRequestError(BaseCustomError):
    def __init__(self, message: str):
        super().__init__(message, 400)
