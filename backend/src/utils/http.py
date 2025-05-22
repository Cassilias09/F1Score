# see: https://subscription.packtpub.com/book/web-development/9781789532227/1/ch01lvl1sec17/declaring-status-codes-for-the-responses-with-an-enumerable

from enum import IntEnum


# see: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
class HttpStatusCode(IntEnum):
    # Informational responses
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101

    # Success responses
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206

    # Redirection messages
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    RESERVED = 306
    TEMPORARY_REDIRECT = 307

    # Client error responses
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    UNPROCESSABLE_ENTITY = 422
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    # Server error responses
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    NETWORK_AUTHENTICATION_REQUIRED = 511

    @staticmethod
    def is_informational(status_code: int):
        return 100 <= status_code <= 199

    @staticmethod
    def is_success(status_code: int):
        return 200 <= status_code <= 299

    @staticmethod
    def is_redirect(status_code: int):
        return 300 <= status_code <= 399

    @staticmethod
    def is_client_error(status_code: int):
        return 400 <= status_code <= 499

    @staticmethod
    def is_server_error(status_code: int):
        return 500 <= status_code <= 599
