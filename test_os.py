"""
OS class tests.
"""

import unittest
from abc import ABCMeta

from os_handler import Arcolinux, Arch, Os, get_current_os_class, get_current_os_name


class TestHelperFunctions(unittest.TestCase):
    "Test the helper function of the os_handler module"

    def test_get_current_os_name_returns_string(self):
        self.assertIsInstance(get_current_os_name(), str)

    def test_get_current_os_class_returns_class(self):
        supported_oses_class = [Arcolinux, Arch]
        self.assertIn(get_current_os_class(), supported_oses_class)


class TestArcolinuxInitialization(unittest.TestCase):
    "Test the initialize method of Arcolinux class."

    def setUp(self):
        """Setup test fixtures"""
        self.working_machine_os = Arcolinux()

    def test_get_os_install_command_returns_string(self):
        "Whether get_os_install_command returns a string"
        self.assertIsInstance(
            self.working_machine_os.get_os_install_command(), str)

    def test_get_os_update_command_returns_string(self):
        "Whether get_os_update_command returns a string"
        self.assertIsInstance(
            self.working_machine_os.get_os_update_command(), str)

    def test_get_os_prepare_commands_returns_list_of_strings(self):
        "Whether get_os_prepare_command returns a list of command"
        list_of_preparation_commands = self.working_machine_os.get_os_prepare_commands()
        self.assertIsInstance(
            self.working_machine_os.get_os_prepare_commands(), list)
        for command in list_of_preparation_commands:
            self.assertIsInstance(command, str)

    def test_get_os_cleanup_commands_returns_list_of_strings(self):
        "Whether get_os_cleanup_command returns a list of command"
        list_of_cleanup_commands = self.working_machine_os.get_os_cleanup_commands()
        self.assertIsInstance(
            self.working_machine_os.get_os_cleanup_commands(), list)
        for command in list_of_cleanup_commands:
            self.assertIsInstance(command, str)


class TestArchlinuxInitialization(unittest.TestCase):
    "Test the initialize method of Archlinux class."

    def setUp(self):
        """Setup test fixtures"""
        self.working_machine_os = Arch()

    def test_get_os_install_command_returns_string(self):
        "Whether get_os_install_command returns a string"
        self.assertIsInstance(
            self.working_machine_os.get_os_install_command(), str)

    def test_get_os_update_command_returns_string(self):
        "Whether get_os_update_command returns a string"
        self.assertIsInstance(
            self.working_machine_os.get_os_update_command(), str)

    def test_get_os_prepare_commands_returns_list_of_strings(self):
        "Whether get_os_prepare_command returns a list of command"
        list_of_preparation_commands = self.working_machine_os.get_os_prepare_commands()
        self.assertIsInstance(
            self.working_machine_os.get_os_prepare_commands(), list)
        for command in list_of_preparation_commands:
            self.assertIsInstance(command, str)

    def test_get_os_cleanup_commands_returns_list_of_strings(self):
        "Whether get_os_cleanup_command returns a list of command"
        list_of_cleanup_commands = self.working_machine_os.get_os_cleanup_commands()
        self.assertIsInstance(
            self.working_machine_os.get_os_cleanup_commands(), list)
        for command in list_of_cleanup_commands:
            self.assertIsInstance(command, str)


if __name__ == '__main__':
    unittest.main()
