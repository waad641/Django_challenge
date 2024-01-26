#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# The shebang line indicates that the script should be executed using the Python interpreter specified in the environment.

# Import the os and sys modules
import os
import sys

# Define the main function
def main():
    """Run administrative tasks."""
    # Set the default value for the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'producer_project.settings')

    try:
        # Try importing the execute_from_command_line function from the django.core.management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError by raising a more informative exception
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Call the execute_from_command_line function with the command-line arguments
    execute_from_command_line(sys.argv)

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Call the main function
    main()
