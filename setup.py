import os_utils

linux_packages = [
    'vim',
    'neovim',
    'neovim-qt',
    'htop'
]

def linux_setup():
    os_utils.install_system_packages(linux_packages)

if __name__ == '__main__':
    linux_setup()
