
from django.core.management import execute_from_command_line
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monprojet.settings")
    execute_from_command_line(sys.argv + ["runserver", "0.0.0.0:3000"])
