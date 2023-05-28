class KrakenError(Exception):
    def __init__(self, method: str, errors: list) -> None:
        self.method = method
        self.errors = errors
        super().__init__(*errors)

    def __str__(self) -> str:
        return f"<{self.method=}> => {self.errors[0]}"
