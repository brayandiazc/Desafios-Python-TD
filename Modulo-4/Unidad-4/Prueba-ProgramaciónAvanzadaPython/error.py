class Error(Exception):
    """
    Base class for custom exceptions in this module.
    """
    pass

class LargoExcedidoError(Error):
    """
    Exception raised when the length exceeds a certain limit.

    Attributes:
        None
    """
    pass

class SubTipoInvalidoError(Error):
    """
    Exception raised when an invalid subtype is encountered.

    Attributes:
        None
    """
    pass
