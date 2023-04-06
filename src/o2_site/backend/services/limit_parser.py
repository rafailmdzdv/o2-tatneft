import pathlib

from backend.utils import excel, programs_data
from o2_site import settings


def get_number_sender_report() -> pathlib.Path:
    ns_data = programs_data.get_full_program_data('is_took', 'took_time')
    excel_path = excel.save_data_to_excel(ns_data,
                                          'firstProgramReport',
                                          settings.PROGRAMS_COLUMNS)
    return excel_path


def get_limit_parser_report() -> pathlib.Path:
    lp_data = programs_data.get_full_program_data('has_limit', 'changed_time')
    excel_path = excel.save_data_to_excel(lp_data,
                                          'secondProgramReport',
                                          settings.PROGRAMS_COLUMNS)
    return excel_path
