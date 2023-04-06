import pathlib

from django.http.response import HttpResponse

from backend.services import azs_list, limit_parser


def get_azs_file_response() -> HttpResponse:
    excel_path = azs_list.get_azs_xls()
    return _get_file_response(excel_path)


def get_ns_file_report_response() -> HttpResponse:
    excel_path = limit_parser.get_number_sender_report()
    return _get_file_response(excel_path)


def get_lp_file_report_response() -> HttpResponse:
    excel_path = limit_parser.get_limit_parser_report()
    return _get_file_response(excel_path)


def _get_file_response(excel_path: pathlib.Path) -> HttpResponse:
    with open(str(excel_path), 'rb') as excel_file:
        response = HttpResponse(excel_file.read(),
                                content_type='application/vnd.ms-excel')
        filename = excel_path.name
        response['Content-Dispotion'] = f'attachment; filename={filename}'
        return response
