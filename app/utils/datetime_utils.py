from datetime import datetime

class DateTimeUtils:

    @staticmethod
    def format_datetime(dt):
        """Format a datetime object as 'YYYY-MM-DD HH:MM:SS'."""
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def parse_datetime(dt_str):
        """Parse a datetime string into a datetime object."""
        return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
