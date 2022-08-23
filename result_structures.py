class BoreResult:
    """
    Provides an easy to read structure containing values returned after calcuating bore values
    """

    bm61d: int
    bfov: int
    bfoi: int

    def __init__(self, **kwargs) -> None:
        self.bm61d = kwargs["bm61d"]
        self.bfov = kwargs["bfov"]
        self.bfoi = kwargs["bfoi"]