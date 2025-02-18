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
        new_table.append(row[column_name])
    return new_table


def columnar(origin_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table represented as a list of rows into one represented as a dictionary of columns."""
    column_dict: dict[str, list[str]] = {}
    for row in origin_table:
        for key in row:
            column_dict[key] = column_values(origin_table, key)
    return column_dict


def head(non_mutated: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    top_rows: dict[str, list[str]] = {}
    for column in non_mutated:
        first_N: list[str] = []
        i: int = 0
        while i < N:
            first_N.append(non_mutated[column][i])
            i += 1 
        top_rows[column] = first_N
    return top_rows


def select(dont_mutate: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    select_columns: dict[str, list[str]] = {}
    for column in columns:
        select_columns[column] = dont_mutate[column]
    return select_columns


def count(values: list[str]) -> dict[str, int]:
    """Return the number of times that the given value appeared."""
    how_many: dict[str, int] = {}
    for value in values:
        if value in how_many:
            how_many[value] += 1
        else:
            how_many[value] = 1
    return how_many