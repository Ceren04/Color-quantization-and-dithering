"""Task 4 of the median cut pipeline: radix list sort and median split."""

def split_box(colors, counts, axis):
    """
    Sort the colors along `axis` and cut them where half of the pixels
    are on each side (the weighted median).

    colors : (M, 3) unique colors in the box
    counts : (M,) number of pixels of each color
    axis   : 0 = R, 1 = G, 2 = B (chosen by Task 3)

    Returns (lower_colors, lower_counts), (upper_colors, upper_counts).
    """
    if len(colors) < 2:
        raise ValueError("a box needs at least 2 colors to be split")

    # radix list sort: the values are small integers (0-31), so we drop
    # each color's index into the bucket of its value and read the buckets in order
    values = colors[:, axis]
    buckets = [[] for _ in range(values.max() + 1)]
    for i, v in enumerate(values):
        buckets[v].append(i)
    order = [i for bucket in buckets for i in bucket]

    colors = colors[order]
    counts = counts[order]

    # add up pixels until we reach half of the total
    half = counts.sum() / 2
    seen = 0
    cut = 0
    while seen < half:
        seen += counts[cut]
        cut += 1

    # leave at least one color on each side
    cut = min(cut, len(colors) - 1)

    return (colors[:cut], counts[:cut]), (colors[cut:], counts[cut:])
