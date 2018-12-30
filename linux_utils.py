import platform
import subprocess
import contextlib
import importlib
import os
import site
import shutil
import tempfile

dir_path = os.path.dirname(os.path.realpath(__file__))
user_path = os.path.join(os.path.expanduser("~"))
user_name = user_path.split('/')[-1]

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
    subprocess.check_call('sudo apt update'.split())
    subprocess.check_call('sudo apt install -y {}'.format(' '.join(packages['linux_packages']+packages['debian_packages'])).split())

def install_system_packages(packages):
    distribution = platform.linux_distribution()[0]
    if distribution == 'Ubuntu':
        install_apt_packages(packages)
    else:
        raise Exception('Current linux OS not supported.')

def install_python3_packages(packages):
    subprocess.check_call('pip3 install {}'.format(' '.join(packages['python_packages'])).split())

def install_npm_packages(packages):
    subprocess.check_call('npm install -g {}'.format(' '.join(packages['npm_packages'])).split())

def install_vim_plug():
    # subprocess.check_call('curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'.split())
    print('curl -fLo {} --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'.format(os.path.join(user_path, '.local', 'share', 'nvim', 'site', 'autoload', 'plug.vim')))
    subprocess.check_call('curl -fLo {} --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'.format(os.path.join(user_path, '.local', 'share', 'nvim', 'site', 'autoload', 'plug.vim')).split())
    subprocess.check_call('sudo chown -R {0}:{0} {1} '.format(user_name, os.path.join(user_path, '.local', 'share', 'nvim')))

def install_rust():
    with tempdir() as dirpath:
        subprocess.check_call('curl https://sh.rustup.rs -sSf -o {}'.format(os.path.join(dirpath, 'rustup.sh')).split())
        subprocess.check_call('sh rustup.sh -y'.split(), cwd=dirpath)

def install_alacritty():
    with tempdir() as dirpath:
        subprocess.check_call('git clone https://github.com/jwilm/alacritty.git'.split(), cwd=dirpath)
        subprocess.check_call('{} build --release'.format(os.path.join(user_path, '.cargo', 'bin', 'cargo')).split(), cwd=os.path.join(dirpath, 'alacritty'))

def stow_directories(stow_directories):
    importlib.reload(site)
    globals()['dploy'] = importlib.import_module('dploy')
    for directory in stow_directories:
        dploy.stow([os.path.join(dir_path, directory)], user_path, is_silent=False)
