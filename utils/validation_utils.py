from email_validator import valid_email, EmailnotvalidError
import logging

logger = logging.getlogger(__name__)

def is_valid_email(email: str) -> bool:
    """
    Validate an email address using python's email_validator pakage.
    Returns True if valid, False otherwise.
    """
    try:
        valid_email(email)
        return True
    except EmailnotvalidError as e:
        logger.error(f"Invalid email '{email}': {str(e)}")
        return Flase
            
