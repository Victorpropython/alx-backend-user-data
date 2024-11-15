#!/usr/bin/env python3
"""For http Authentication file
"""
import re
from flask import request
from typing import List, TypeVar, Any


class Auth:
    """A class tomanage authentication"""

    def require_auth(self, path:  str, excluded_paths: List[str]) -> bool:
        """This method will be implemented to check if authentication
        required for a given path, considering any excluded paths.

        Args:
            path(str): The API endpoint path.
            excluded_paths (List[str]): List of paths excluded from
            authentication requirement.

        RETURNS:
            bool: To return True if authentication is required, False if None
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ This method will be implemented to retrieve the authorizarion
        header from the request if present.

        Args:
            request (flask.Request. optional): The flask Object. Defaults
            to None.

        Returns:
            Str: the authorization header value or None if not present.
        """
        return None

    def current_user(self, request=None) -> Any:
        """ A Method to retrieve information about the current authenticated
        user from the request or other sources.

        Args:
            request (Flask.Request, Optional): The flask request object.
            Defaults to None.

        Returns:
            Any: Information about the current user or Noneif not authenticated
        """
        return None
