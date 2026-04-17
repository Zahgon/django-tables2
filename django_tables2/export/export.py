from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse

try:
    from tablib import Dataset
except ImportError:  # pragma: no cover
    raise ImproperlyConfigured(
        "You must have tablib installed in order to use the django-tables2 export functionality"
    )


class TableExport:
    """
    Export data from a table to the file type specified.

    Arguments:
        export_format (str): one of `csv, json, latex, ods, tsv, xls, xlsx, yaml`

        table (`~.Table`): instance of the table to export the data from

        exclude_columns (iterable): list of column names to exclude from the export

        dataset_kwargs (dictionary): passed as `**kwargs` to `tablib.Dataset` constructor

    """

    CSV = "csv"
    JSON = "json"
    LATEX = "latex"
    ODS = "ods"
    TSV = "tsv"
    XLS = "xls"
    XLSX = "xlsx"
    YAML = "yaml"

    FORMATS = {
        CSV: "text/csv; charset=utf-8",
        JSON: "application/json",
        LATEX: "text/plain",
        ODS: "application/vnd.oasis.opendocument.spreadsheet",
        TSV: "text/tsv; charset=utf-8",
        XLS: "application/vnd.ms-excel",
        XLSX: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        YAML: "text/yaml; charset=utf-8",
    }

    def __init__(self, export_format, table, exclude_columns=None, dataset_kwargs=None):
        if not self.is_valid_format(export_format):
            raise TypeError(f'Export format "{export_format}" is not supported.')

        self.format = export_format
        self.dataset = self.table_to_dataset(table, exclude_columns, dataset_kwargs)

    def table_to_dataset(self, table, exclude_columns, dataset_kwargs=None):
        """Transform a table to a tablib dataset."""
        pass

    @classmethod
    def is_valid_format(self, export_format):
        """Return True if `export_format` is one of the supported export formats."""
        pass

    def content_type(self):
        """Return the content type for the current export format."""
        pass

    def export(self):
        """Return the string/bytes for the current export format."""
        pass

    def response(self, filename=None):
        """
        Build and return a `HttpResponse` containing the exported data.

        Arguments:
            filename (str): if not `None`, the filename is attached to the
                `Content-Disposition` header of the response.
        """
        pass
