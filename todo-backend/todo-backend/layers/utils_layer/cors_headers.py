class APIHeaders:
    """contains methods to add CORS headers"""

    @staticmethod
    def generate_headers(headers='*', origin="*", methods="OPTIONS,POST,GET,DELETE,PATCH") -> dict:
        """
        generates a headers dict
        Args:
            headers(str): [Access-Control-Allow-Headers, default "*"]
            origin(str): [Access-Control-Allow-Origin, default "*"]
            methods(str): [Access-Control-Allow-Methods, default "OPTIONS,POST,GET"]
        Returns
            headers(dict)
        """
        return {
                'Access-Control-Allow-Headers': headers,
                'Access-Control-Allow-Origin': origin,
                'Access-Control-Allow-Methods': methods
            }
