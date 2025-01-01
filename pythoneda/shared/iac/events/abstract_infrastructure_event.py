# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/abstract_infrastructure_event.py

This file declares the AbstractInfrastructureEvent event.

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
from typing import Dict, List


class AbstractInfrastructureEvent(Event, abc.ABC):
    """
    Represents the moment the infrastructure update fails.

    Class name: AbstractInfrastructureEvent

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        metadata: Dict = {},
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new AbstractInfrastructureEvent instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        :param metadata: Additional request metadata.
        :type metadata: Dict
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(previousEventIds, reconstructedId)
        self._stack_name = stackName
        self._project_name = projectName
        self._location = location
        self._metadata = metadata

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
    @attribute
    def metadata(self) -> Dict:
        """
        Retrieves the metadata.
        :return: Such metadata.
        :rtype: Dict
        """
        return self._metadata


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
