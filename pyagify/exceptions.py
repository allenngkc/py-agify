class ResourceUnavailable(Exception):
    def __init__(self, message, response):
        Exception.__init__(self)
        self.message = message
        self.code = response.status_code

    def __str__(self):
        return "%s (HTTP status: %s)" % (self.message, self.code)


class Unauthorized(ResourceUnavailable):
    pass


class PaymentRequired(ResourceUnavailable):
    pass


class UnprocessableEntity(ResourceUnavailable):
    pass


class TooManyRequests(ResourceUnavailable):
    pass
