"""
Table Processing – Extract tables from PDFs, convert to text.
"""

import pandas as pd
import tabula

def extract_tables_from_pdf(pdf_path: str) -> list:
    """Extract all tables from PDF using tabula."""
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

def table_to_markdown(table: pd.DataFrame) -> str:
    """Convert pandas DataFrame to markdown table."""
    return table.to_markdown()

def table_to_text(table: pd.DataFrame) -> str:
    """Convert table to natural language description."""
    return f"Table with {len(table)} rows and {len(table.columns)} columns. Columns: {', '.join(table.columns)}"

if __name__ == "__main__":
    tables = extract_tables_from_pdf("report.pdf")
    for i, tbl in enumerate(tables):
        print(table_to_markdown(tbl))