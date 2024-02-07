import logging
import os
from datetime import datetime

def init_logger():
    # Define the directory for logs
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Generate a timestamped filename for the current execution session
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"{current_time}.log"

    # Update logging configuration to use the timestamped filename
    logging.basicConfig(
        filename=os.path.join(logs_dir, log_filename),
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(asctime)s %(message)s",
    )
