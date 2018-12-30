import platform

if platform.system() == 'Linux':
    import linux_utils as os_utils
else:
    raise Exception('Current system not supported.')

packages = {
    'linux_packages': [
        'cmake',
        'curl',
        'golang-go',
        'vim',
        'neovim',
        'neovim-qt',
        'nodejs',
        'npm',
        'htop',
        'libfreetype6-dev',
        'libfontconfig1-dev',
        'xclip'
    ],
    'debian_packages': [
        'build-essential',
        'openjdk-8-jdk',
        'python3-dev',
        'python3-pip'
    ],
    'python_packages': [
        'dploy'
    ],
    'npm_packages': [
        'typescript'
    ]
}

stow_dirs = [
    'nvim'
]

def linux_setup():
    os_utils.install_system_packages(packages)
    os_utils.install_python3_packages(packages)
    os_utils.install_npm_packages(packages)
    os_utils.install_rust()
    # os_utils.install_alacritty()
    os_utils.stow_directories(stow_dirs)


if __name__ == '__main__':
    linux_setup()
