import os
from trexa.api.endpoints import trim_csv

"""Tests for the API helper methods."""

test_dir = os.path.dirname(os.path.abspath(__file__))
test_csv = os.path.join(test_dir, 'fixtures',
                        'test_file_with_thirty_lines.csv')


def get_csv_length(desired_length):
    """Helper method for trimming."""
    f = trim_csv(test_csv, desired_length)
    new_file = []
    while True:
        try:
            new_file.append(next(f))
        except StopIteration:
            break
    return len(new_file)


def test_trimming_smaller():
    """Test that we end up with a smaller file."""
    assert get_csv_length(10) == 10
    assert get_csv_length(0) == 0


def test_trimming_none():
    """Test that passing in None returns the entire file."""
    assert get_csv_length(None) == 30
    # Test not passing in a count
    f = trim_csv(test_csv)
    new_file = []
    while True:
        try:
            new_file.append(next(f))
        except StopIteration:
            break
    assert len(new_file) == 30


def test_trimming_with_garbage():
    """Test that nothing weird happens."""
    assert get_csv_length(35) == 30
    assert get_csv_length('WHAT') == 30
    assert get_csv_length('🤬') == 30
    assert get_csv_length(hex(10)) == 30
