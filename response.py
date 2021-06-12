PROTOCOL = 'HTTP/1.1'
SP = " "


class HttpStatus:

    def __init__(self, status_code: int, reason_message: str):
        self.status_code = status_code
        self.reason_message = reason_message


class Response:

    def __init__(self, status: HttpStatus, body: bytes = b''):
        self.headers = b'Server: ym-http\r\nContent-Type: text/plain;charset=utf-8\r\n'
        self.body = body
        self.status = status

    def to_bytes(self) -> bytes:
        preamble = bytes(PROTOCOL + SP + str(self.status.status_code) + SP + self.status.reason_message, 'UTF-8')
        return preamble + b'\r\n' + self.headers + b'\r\n' + self.body


# HTTP STATUS CODES
OK = HttpStatus(200, "OK")

ACCESS_DENIED = HttpStatus(401, "Access Denied")
NOT_FOUND = HttpStatus(404, "Not Found")
METHOD_NOT_ALLOWED = HttpStatus(405, "Method Not Allowed")

INTERNAL_SERVER_ERROR = HttpStatus(500, "Internal Server Error")
