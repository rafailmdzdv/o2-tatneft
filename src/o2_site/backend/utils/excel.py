import pathlib

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import pandas as pd

from o2_site import settings


def save_data_to_excel(data: list,
                       filename: str,
                       columns: list) -> pathlib.Path:
    excel_path = f'{settings.EXCELS_DIR}/{filename}.xlsx'
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(excel_path, index=False)
    _adjust_rows_columns(excel_path)
    return pathlib.Path(excel_path).resolve()


def _adjust_rows_columns(excel_path: str) -> None:
    workbook = openpyxl.load_workbook(excel_path)
    sheet = workbook.active

    _adjust_rows_height(sheet)
    _adjust_columns_width(sheet)

    workbook.save(excel_path)


def _adjust_rows_height(sheet: Worksheet) -> None:
    for index, _ in enumerate(sheet.rows, start=1):
        sheet.row_dimensions[index].auto_size = True


def _adjust_columns_width(sheet: Worksheet) -> None:
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            max_cell_phraze = max(str(cell.value).split('\n'))
            max_cell_phraze_len = len(max_cell_phraze)
            if max_cell_phraze_len > max_length:
                max_length = max_cell_phraze_len

        adjusted_length = max_length + 2
        sheet.column_dimensions[column_letter].width = adjusted_length
