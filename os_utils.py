import platform
import subprocess

def install_apt_packages(packages):
    subprocess.check_call('apt-get update')
    subprocess.check_call('apt-get install -y {}'.format(' '.join(packages)))

def install_linux_system_packages(packages):
    distribution = platform.linux_distribution()[0]
    if distribution == 'Ubuntu':
        install_apt_packages(packages)
    else:
        raise Exception('Current linux OS not supported.')

def install_system_packages(packages):
    if platform.system == 'Linux':
        install_linux_system_packages(packages)
    else:
        raise Exception('Current system not supported.')


