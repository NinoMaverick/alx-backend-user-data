#!/usr/bin/env python3
"""
This module contains the function filter_datum which obfuscates specified fields in log messages.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message:str, seperator: str) -> str:
    """
    Obfuscates specified fields in a log message using regex.
    
    Args:
        fields (List[str]): List of field names to be obfuscated.
        redaction (str): The string that will replace the field values.
        message (str): The log line to be obfuscated.
        separator (str): The character separating fields in the message.
    
    Returns:
        str: The obfuscated log message.
    """
    pattern = f'({"|".join([re.escape(field) + r"=[^" + separator + "]+" for field in fields])})'
    return re.sub(pattern, lambda m: f'{m.group(0).split("=")[0]}={redaction}', message)