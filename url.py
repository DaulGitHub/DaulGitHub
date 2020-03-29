from shortuuid import ShortUUID


class CreateShortURL:

    def __init__(self, protocol, domain):

        self._protocol = protocol
        self._domain = domain

    def get_url(self):

        return "{}://{}/{}".format(self._protocol, self._domain, self._get_prefix())

    @staticmethod
    def _get_prefix():

        return ShortUUID().random(6)
