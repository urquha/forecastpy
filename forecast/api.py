# -*- coding: utf-8 -*-
from typing import List

from forecast import Client, Project, Person, Assignment, Milestone, Role, UserConnection, Placeholder, Requestor

"""Main module."""


class Api:

    def __init__(self, account_id, auth_token, base_url=None):

        self._requestor = Requestor(account_id, auth_token, base_url)

    def get_projects(self) -> List[Project]:
        data = self._requestor.get("projects")
        return [Project.from_dict(project) for project in data['projects']]

    def get_project(self, project_id) -> Project:
        data = self._requestor.get("projects/{}".format(project_id))
        return Project.from_dict(data['project'])

    def get_clients(self) -> List[Client]:
        data = self._requestor.get("clients")
        return [Client.from_dict(client) for client in data['clients']]

    def get_client(self, client_id) -> Client:
        data = self._requestor.get("clients/{}".format(client_id))
        return Project.from_dict(data['client'])

    def get_people(self) -> List[Person]:
        data = self._requestor.get("people")
        return [Person.from_dict(person) for person in data['people']]

    def get_person(self, person_id) -> Person:
        data = self._requestor.get("people/{}".format(person_id))
        return Person.from_dict(data['person'])

    def get_assignments(self, start_date=None, end_date=None, state='active',
                        project_id=None, person_id=None, placeholder_id=None) -> List[Assignment]:

        data = self._requestor.get(f"assignments?start_date={start_date}&end_date={end_date}")

        return [Assignment.from_dict(assignment) for assignment in data['assignments']]

    def get_assignment(self, assignment_id: int) -> Assignment:
        data = self._requestor.get("assignments/{}".format(assignment_id))
        return Assignment.from_dict(data['assignment'])

    def get_milestones(self, project_id: int = None) -> List[Milestone]:
        url = "milestones"
        if project_id:
            url = f"milestones/{project_id}"

        data = self._requestor.get(url)

        return [Milestone.from_dict(milestone) for milestone in data['milestones']]

    def get_milestone(self, milestone_id: int) -> Milestone:
        data = self._requestor.get("milestones/{}".format(milestone_id))
        return Milestone.from_dict(data['milestone'])

    def get_roles(self) -> List[Role]:
        data = self._requestor.get("roles")
        return [Role.from_dict(role) for role in data['roles']]

    def get_role(self, role_id: int) -> Role:
        data = self._requestor.get("roles/{}".format(role_id))
        return Role.from_dict(data['role'])

    def get_placeholders(self) -> List[Placeholder]:
        data = self._requestor.get("placeholders")
        return [Placeholder.from_dict(placeholder) for placeholder in data['placeholders']]

    def get_placeholder(self, placeholder_id: int) -> Placeholder:
        data = self._requestor.get("placeholders/{}".format(placeholder_id))
        return Placeholder.from_dict(data['placeholder'])

    def get_user_connections(self) -> List[UserConnection]:
        data = self._requestor.get("user_connections")
        return [UserConnection.from_dict(connection) for connection in data['user_connections']]

    def get_user_connection(self, user_connection_id: int) -> UserConnection:
        raise NotImplementedError("This feature is not supported by Forecast App API yet")

    def whoami(self) -> Person:
        data = self._requestor.get("whoami")
        user_id = data['current_user']['id']
        return self.get_person(person_id=user_id)

    def clear_cache(self):
        self._requestor.clear_cache()
