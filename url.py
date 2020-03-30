from shortuuid import ShortUUID


class CreateShortURL:

    def __init__(self, protocol, domain, port):

        self._port = port
        self._protocol = protocol
        self._domain = domain

    def get_url(self, prefix):

        return "{}://{}:{}/{}".format(self._protocol, self._domain, self._port, prefix)

    @staticmethod
    def get_prefix():

        return ShortUUID().random(6)
