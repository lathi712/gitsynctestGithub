"""
Utility functions for common operations
Created on: May 19, 2025
Author: Lathesh Karkera S
"""
import os
import json
import datetime
from typing import Dict, List, Any, Optional


def get_current_datetime() -> str:
    """Returns the current date and time in ISO format"""
    return datetime.datetime.now().isoformat()


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Read and parse a JSON file
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary containing the parsed JSON data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file isn't valid JSON
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json_file(file_path: str, data: Dict[str, Any], indent: int = 4) -> None:
    """
    Write data to a JSON file
    
    Args:
        file_path: Path where the JSON file will be saved
        data: Dictionary to save as JSON
        indent: Number of spaces for indentation (default: 4)
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)


def filter_dict_list(items: List[Dict[str, Any]], 
                     filter_key: str, 
                     filter_value: Any) -> List[Dict[str, Any]]:
    """
    Filter a list of dictionaries by matching a specific key-value pair
    
    Args:
        items: List of dictionaries to filter
        filter_key: Key to check in each dictionary
        filter_value: Value that the key should match
        
    Returns:
        Filtered list of dictionaries
    """
    return [item for item in items if item.get(filter_key) == filter_value]


def safe_get(dictionary: Dict[str, Any], 
             keys: List[str], 
             default: Any = None) -> Any:
    """
    Safely access nested dictionary values without raising KeyError
    
    Args:
        dictionary: Dictionary to access
        keys: List of keys representing the path to the value
        default: Default value to return if any key is not found
        
    Returns:
        The value at the specified path or the default value
    """
    temp = dictionary
    for key in keys:
        if isinstance(temp, dict) and key in temp:
            temp = temp[key]
        else:
            return default
    return temp