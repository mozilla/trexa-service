from itertools import islice

"""Helper methods for the API blueprint."""


def trim_csv(csv_file, count):
    """Return a generator for streaming the CSV response.

    If count is None, it should iterate over the entire file.
    """
    with open(csv_file, 'r') as csv:
        for line in islice(csv, count):
            yield line
