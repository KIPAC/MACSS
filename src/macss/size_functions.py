import numpy as np

LSST_PIXEL_SIZE = 0.2  # arc seconds / pixel
LSST_PIXEL_SIZE_SQUARED = LSST_PIXEL_SIZE * LSST_PIXEL_SIZE


def trace_of_ellipse(
    xx: np.ndarray,
    yy: np.ndarray,
) -> np.ndarray:
    """Return the trace of the matrix defining an ellipse

    Parameters
    ----------
    xx:
        x,x element of matrix

    yy:
        y,y element of matrix

    Returns
    -------
    Tr(Q) = xx + yy
    """
    return xx + yy


def chord_length_arcsec(
    xx: np.ndarray,
    yy: np.ndarray,
) -> np.ndarray:
    """Return the length of the chord between the semi-minor and semi-major axes

    Parameters
    ----------
    xx:
        x,x element of matrix

    yy:
        y,y element of matrix

    Returns
    -------
    Chord length in arcsecs
    """
    return LSST_PIXEL_SIZE * np.sqrt(trace_of_ellipse(xx, yy))


def det_of_ellipse(
    xx: np.ndarray,
    yy: np.ndarray,
    xy: np.ndarray,
) -> np.ndarray:
    """Return the determinent of the matrix defining an ellipse

    Parameters
    ----------
    xx:
        x,x element of matrix

    yy:
        y,y element of matrix

    xy:
        x,y element of matrix

    Returns
    -------
    Det(Q) = xx * yy - xy *xy
    """
    return xx * yy - xy * xy


def area_of_ellipse(
    xx: np.ndarray,
    yy: np.ndarray,
    xy: np.ndarray,
) -> np.ndarray:
    """Return the area of an ellipse

    Parameters
    ----------
    xx:
        x,x element of matrix

    yy:
        y,y element of matrix

    xy:
        x,y element of matrix

    Returns
    -------
    A = pi*sqrt(Det(Q))
    """
    return np.pi * np.sqrt(det_of_ellipse(xx, yy, xy))


def area_of_ellipse_arcsec2(
    xx: np.ndarray,
    yy: np.ndarray,
    xy: np.ndarray,
) -> np.ndarray:
    """Return the area of an ellipse in arcsec**2

    Parameters
    ----------
    xx:
        x,x element of matrix

    yy:
        y,y element of matrix

    xy:
        x,y element of matrix

    Returns
    -------
    Area of the ellipse in arcsec^2
    """
    return LSST_PIXEL_SIZE_SQUARED * np.pi * np.sqrt(det_of_ellipse(xx, yy, xy))


def r_90_over_r_50_from_sersic_index(
    n: np.ndarray,
) -> np.ndarray:
    """Return ratio of r_90 to r_50 for a particular sersic profile

    Parameters
    ----------
    n:
        sersic index

    Returns
    -------
    r_90 / r_50 = 1.25 + 1.125 * n
    """
    return 1.25 + 1.125 * n


def r_90_sersic_arcsec(
    r: np.ndarray,
    n: np.ndarray,
) -> np.ndarray:
    """Return ratio of r_90 to r_50 for a particular sersic profile

    Parameters
    ----------
    n:
        sersic index

    Returns
    -------
    r_90 / r_50 = 1.25 + 1.125 * n
    """
    return LSST_PIXEL_SIZE * r * (1.25 + 1.125 * n)


def pix_to_radians(pix: np.ndarray) -> np.ndarray:
    """Convert size in pixels to radians

    Parameters
    ----------
    pix:
        Size in pixels

    Returns
    -------
    radians:  Size in radians
    """
    return np.radians(LSST_PIXEL_SIZE * pix / 3600)


def mag_to_dL(mag: np.ndarray, abs_mag: float | np.ndarray = 20) -> np.ndarray:
    """Return the luminonisty distance for an object of known absolute magntitude

    Parameters
    ----------
    mag:
        Apparent magnitude

    abs_mag:
        Absolute magntidue

    Returns
    -------
    Luminosity distance
    """
    return np.power(10, 1 + (mag + abs_mag) / 5)


def pix_to_dA(pix: np.ndarray, size: float | np.ndarray = 5e3) -> np.ndarray:
    """Return the angular diameter distance for an object of known size

    Parameters
    ----------
    pix:
        Size in pixels

    size:
        Size of the object in parsecs

    Returns
    -------
    Angular diameter distance in pc
    """
    return size / pix_to_radians(pix)
