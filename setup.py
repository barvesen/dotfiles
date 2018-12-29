import platform

if platform.system() == 'Linux':
    import linux_utils as os_utils
else:
    raise Exception('Current system not supported.')

linux_packages = [
    'curl',
    'vim',
    'neovim',
    'neovim-qt',
    'htop',
    'cmake',
    'libfreetype6-dev',
    'libfontconfig1-dev',
    'xclip'
]

def linux_setup():
    os_utils.install_system_packages(linux_packages)
    os_utils.install_rust()
    os_utils.install_alacritty()

if __name__ == '__main__':
    linux_setup()
