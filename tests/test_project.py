# -*- encoding: utf-8 -*-
from odoo.tests import common


class TestProject(common.TransactionCase):
    """Run unit test for project module"""

    def test_create_data(self):
        # Create a new project with the test
        test_project = self.env['project.project'].create({
            'name': 'TestProject'
        })

        # Add a test task to the project
        test_project_task = self.env['project.task'].create({
            'name': 'ExampleTask',
            'project_id': test_project.id
        })

        # Check if the project name and the task name match
        self.assertEqual(test_project.name, 'TestProject')
        self.assertEqual(test_project_task.name, 'ExampleTask')
        # Check if the project assigned to the task is in fact the correct id
        self.assertEqual(test_project_task.project_id.id, test_project.id)
