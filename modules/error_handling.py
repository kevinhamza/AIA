import logging
import os
from datetime import datetime


class ErrorHandling:
    def __init__(self, log_directory="logs"):
        """
        Initialize the error handler with logging capabilities.
        :param log_directory: Directory to store log files.
        """
        self.log_directory = log_directory
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_file = os.path.join(log_directory, f"errors_{datetime.now().strftime('%Y-%m-%d')}.log")
        logging.basicConfig(
            filename=log_file,
            filemode='a',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.ERROR
        )

    def log_error(self, error_message, context=None):
        """
        Log an error with optional context.
        :param error_message: The error message to log.
        :param context: Additional context about where the error occurred.
        """
        if context:
            logging.error(f"{error_message} | Context: {context}")
        else:
            logging.error(error_message)

    def handle_exception(self, exception, custom_message="An error occurred."):
        """
        Handle an exception by logging it and returning a custom message.
        :param exception: The exception to handle.
        :param custom_message: Custom message to return for user-friendly display.
        :return: A user-friendly error message.
        """
        error_message = f"{custom_message} Exception: {exception}"
        self.log_error(str(exception), context=custom_message)
        return error_message

    def validate_inputs(self, **kwargs):
        """
        Validate inputs and ensure they meet expected conditions.
        :param kwargs: Keyword arguments to validate.
        :raises ValueError: If validation fails.
        """
        for key, value in kwargs.items():
            if value is None or value == "":
                self.log_error(f"Validation error: Missing value for {key}")
                raise ValueError(f"Invalid input: {key} cannot be empty or None.")

    def monitor_performance(self, task_name, start_time, end_time):
        """
        Monitor performance and log tasks taking longer than expected.
        :param task_name: Name of the task being monitored.
        :param start_time: Task start time (datetime object).
        :param end_time: Task end time (datetime object).
        """
        duration = (end_time - start_time).total_seconds()
        if duration > 5:  # Example threshold
            warning_message = f"Task '{task_name}' took longer than expected: {duration:.2f} seconds."
            logging.warning(warning_message)

    def alert_critical_error(self, error_message):
        """
        Alert administrators or users about critical errors.
        :param error_message: The critical error message to alert.
        """
        # Placeholder for actual notification logic (email, SMS, etc.)
        logging.critical(f"CRITICAL ALERT: {error_message}")
        print(f"CRITICAL ALERT: {error_message}")


if __name__ == "__main__":
    handler = ErrorHandling()
    try:
        # Example usage
        handler.validate_inputs(username="admin", password=None)
    except Exception as e:
        user_message = handler.handle_exception(e, "Input validation failed.")
        print(user_message)
