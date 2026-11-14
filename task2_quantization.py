import numpy as np


def quantize_and_histogram(pixels):
    """
    Task 2: 15-bit pre-quantization and color histogram (Heckbert, 1982).

    Parameters
    ----------
    pixels : np.ndarray, shape (N, 3), values 0-255
        Flattened RGB pixels (output of Task 1).

    Returns
    -------
    colors : np.ndarray, shape (M, 3), values 0-31
        Unique 5-bit-per-channel colors that appear in the image.
    counts : np.ndarray, shape (M,)
        Number of pixels of each color (frequency weights).
    """
    pixels = np.asarray(pixels)
    if pixels.ndim != 2 or pixels.shape[1] != 3:
        raise ValueError("pixels must have shape (N, 3), got %s" % (pixels.shape,))

    # uint8 cannot hold r5 << 10 (max 31744), so we use a wider type
    p = pixels.astype(np.uint16)

    # 8 bit -> 5 bit per channel: drop the 3 least significant bits
    r5 = p[:, 0] >> 3
    g5 = p[:, 1] >> 3
    b5 = p[:, 2] >> 3

    # pack the three 5-bit values into one 15-bit index (0 .. 32767)
    index = (r5 << 10) | (g5 << 5) | b5

    # 32768-bin histogram: hist[i] = number of pixels with color index i
    hist = np.bincount(index, minlength=32768)

    # keep only the colors that actually appear
    idx = np.nonzero(hist)[0]

    # unpack each index back into (r5, g5, b5)
    colors = np.stack([(idx >> 10) & 31, (idx >> 5) & 31, idx & 31], axis=1)
    counts = hist[idx]
    return colors, counts


def to_8bit(colors5):
    """Map 5-bit colors (0-31) back to the 0-255 range (center of each bin)."""
    return (np.asarray(colors5) * 8 + 4).astype(np.uint8)