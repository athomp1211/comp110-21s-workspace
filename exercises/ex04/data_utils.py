"""Utility functions for wrangling data."""

__author__ = "730318766"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    
    file_handle = open(f"{csv_file}", "r", encoding="utf8")
    csv_reader = DictReader(file_handle) 
    for row in csv_reader:
        rows.append(row)
    file_handle.close()

    return rows


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    new_table: list[str] = []
    for row in table:
        for key in row[column_name]:
            new_table.append(row[column_name])
    return new_table 
