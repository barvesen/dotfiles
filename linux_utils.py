import platform
import subprocess
import contextlib
import os
import shutil
import tempfile

@contextlib.contextmanager
def cd(newdir, cleanup=lambda: True):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)
        cleanup()

@contextlib.contextmanager
def tempdir():
    dirpath = tempfile.mkdtemp()
    def cleanup():
        shutil.rmtree(dirpath)
    with cd(dirpath, cleanup):
        yield dirpath


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
    with tempdir() as dirpath:
        subprocess.check_call('curl https://sh.rustup.rs -sSf -o {}'.format(os.path.join(dirpath, 'rustup.sh')).split())
        subprocess.check_call('sh rustup.sh -y'.split(), cwd=dirpath)

def install_alacritty():
    with tempdir() as dirpath:
        subprocess.check_call('git clone https://github.com/jwilm/alacritty.git'.split(), cwd=dirpath)
        subprocess.check_call('{} build --release'.format(os.path.join(os.path.expanduser("~"), '.cargo', 'bin', 'cargo')).split(), cwd=os.path.join(dirpath, 'alacritty'))
