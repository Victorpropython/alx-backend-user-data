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

        if path is not None and excluded_paths is not None:

            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''

                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])

                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])

                else:
                    pattern = '{}/*'.format(exclusion_path)

                if re.match(pattern, path):
                    return False

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
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
        if request is None:
            return request.headers.get('Authorization', None)
        
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ A Method to retrieve information about the current authenticated
        user from the request or other sources.

        Args:
            request (Flask.Request, Optional): The flask request object.
            Defaults to None.

        Returns:
            Any: Information about the current user or Noneif not authenticated
        """
        return None
