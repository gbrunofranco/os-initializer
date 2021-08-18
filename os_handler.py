from abc import ABC, abstractmethod
from subprocess import call, run


class Os(ABC):
    """Abstract class inherited by every OS subclass"""

    def __init__(self):
        self.name: str = get_current_os_name()
        self.install_command: str = self.get_os_install_command()
        self.update_command: str = self.get_os_update_command()
        self.prepare_commands: list[str] = self.get_os_prepare_commands()
        self.cleanup_command: list[str] = self.get_os_cleanup_commands()
        self.packages: list

    def prepare(self):

        self.run_command(self.update_command)

        for command in self.prepare_commands:
            self.run_command(command)

        for package in self.packages:
            self.run_command(f"{self.install_command} {package}")

        for command in self.cleanup_command:
            self.run_command(command)

    @staticmethod
    def run_command(command):
        try:
            call(f"{command}", shell=True)
        except OSError as e:
            print(f"Execution of preparation {command} failed.", e)

    @staticmethod
    @abstractmethod
    def get_os_install_command():
        """Returns the package installation command for the current OS"""
        pass

    @staticmethod
    @abstractmethod
    def get_os_update_command():
        """Returns the system-wide package update command for the current OS"""
        pass

    @abstractmethod
    def get_os_prepare_commands(self):
        """Returns the commands that run before the installation of packages"""
        pass

    @abstractmethod
    def get_os_cleanup_commands(self):
        """Returns the commands that run after the installation of packages"""
        pass


class Arcolinux(Os):
    """Handler for Arcolinux system"""

    packages = [
        'tint2',
        'openbox',
    ]

    @staticmethod
    def get_os_install_command() -> str:
        return "sudo pacman -S"

    @staticmethod
    def get_os_update_command() -> str:
        return "sudo pacman -Syu"

    def get_os_prepare_commands(self) -> list[str]:
        prepare_commands = [
            "git clone https://github.com/gbrunofranco/dotfiles.git",
            "sudo cp -r ./dotfiles/etc/X11/xorg.conf.d/00-keyboard.conf ./dotfiles/etc/X11/xorg.conf.d/"
        ]
        return prepare_commands

    def get_os_cleanup_commands(self) -> list[str]:
        cleanup_commands = [
            "rm -rf ./dotfiles"
        ]
        return cleanup_commands


class Arch(Os):
    """Handler for ArchLinux system"""

    packages = [
        'tint2',
        'openbox',
    ]

    @staticmethod
    def get_os_install_command() -> str:
        return "sudo pacman -S"

    @staticmethod
    def get_os_update_command() -> str:
        return "sudo pacman -Syu"

    def get_os_prepare_commands(self) -> list[str]:
        prepare_commands = [
            "git clone https://github.com/gbrunofranco/dotfiles.git",
            "sudo cp -r ./dotfiles/etc/X11/xorg.conf.d/00-keyboard.conf ./dotfiles/etc/X11/xorg.conf.d/"
        ]
        return prepare_commands

    def get_os_cleanup_commands(self) -> list[str]:
        cleanup_commands = [
            "rm -rf ./dotfiles"
        ]
        return cleanup_commands


def get_current_os_class():
    return globals()[get_current_os_name()]


def get_current_os_name() -> str:
    return run(f"grep '^ID=' /etc/os-release", shell=True, capture_output=True).stdout.decode("utf-8").strip()[3:].replace(' ', '').capitalize()


if __name__ == '__main__':
    current_os = get_current_os_class()()
    current_os.prepare()
