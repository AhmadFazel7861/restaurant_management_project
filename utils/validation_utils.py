from email_validator import validate_email, EmailNotValidError
import logging

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
    Validate an email address using python's email_validator package.
    Returns True if valid, False otherwise.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        logger.error(f"Invalid email '{email}': {str(e)}")
        return False
            
