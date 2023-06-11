def log_message(*args, **kwargs):
    log_level = kwargs.get('level', 'info')
    message = " ".join(str(arg) for arg in args)

    # Additional metadata
    metadata = kwargs.get('metadata', {})
    timestamp = kwargs.get('timestamp')
    user_id = kwargs.get('user_id')

    # Log the message with the specified log level and additional metadata
    log_entry = {
        'level': log_level,
        'message': message,
        'timestamp': timestamp,
        'user_id': user_id,
        'metadata': metadata
    }

    # Example implementation: Print the log entry
    print(log_entry)


# Example usage
log_message("This is an informational message.")
log_message("Error occurred!", level='error', timestamp='2023-05-31 10:23:45', user_id=1234)
log_message("Custom log entry.", level='custom', metadata={'source': 'application', 'version': '1.0'})

