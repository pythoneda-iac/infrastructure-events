# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/abstract_docker_resources_event.py

This file declares the AbstractDockerResourcesEvent event.

Copyright (C) 2024-today pythoneda-shared-iac/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import abc
from pythoneda.shared import attribute, Event, primary_key_attribute
from typing import List


class AbstractDockerResourcesEvent(Event, abc.ABC):
    """
    Base class for Docker resources events.

    Class name: AbstractDockerResourcesEvent

    Responsibilities:
        - Common information for Docker resources events.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        imageName: str,
        imageVersion: str,
        imageUrl: str = None,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new AbstractDockerResourcesEvent instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        :param imageName: The name of the Docker image.
        :type imageName: str
        :param imageVersion: The version of the Docker image.
        :type imageVersion: str
        :param imageUrl: The url of the Docker image.
        :type imageUrl: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(previousEventIds, reconstructedId)
        self._stack_name = stackName
        self._project_name = projectName
        self._location = location
        self._image_name = imageName
        self._image_version = imageVersion
        self._image_url = imageUrl

    @property
    @primary_key_attribute
    def stack_name(self) -> str:
        """
        Retrieves the name of the stack.
        :return: Such name.
        :rtype: str
        """
        return self._stack_name

    @property
    @primary_key_attribute
    def project_name(self) -> str:
        """
        Retrieves the name of the project.
        :return: Such name.
        :rtype: str
        """
        return self._project_name

    @property
    @attribute
    def location(self) -> str:
        """
        Retrieves the location.
        :return: Such location.
        :rtype: str
        """
        return self._location

    @property
    def image_name(self) -> str:
        """
        Retrieves the name of the Docker image.
        :return: Such name.
        :rtype: str
        """
        return self._image_name

    @property
    def image_version(self) -> str:
        """
        Retrieves the version of the Docker image.
        :return: Such version.
        :rtype: str
        """
        return self._image_version

    @property
    def image_url(self) -> str:
        """
        Retrieves the url of the Docker image.
        :return: Such url.
        """
        return self._image_url


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
