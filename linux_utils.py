import platform
import subprocess

def install_apt_packages(packages):
    subprocess.check_call('sudo apt-get update'.split())
    subprocess.check_call('sudo apt-get install -y {}'.format(' '.join(packages)).split())

def install_system_packages(packages):
    distribution = platform.linux_distribution()[0]
    if distribution == 'Ubuntu':
        install_apt_packages(packages)
    else:
        raise Exception('Current linux OS not supported.')

def install_rust():
    subprocess.check_call('curl https://sh.rustup.rs -sSf | sh -s -- -y'.split())
