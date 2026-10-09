from pathlib import Path
import subprocess
import shutil
import sys

REPO = 'https://github.com/fastapi/fastapi.git'
RELEASE = '0.142.2'
FOLDERS = ['docs/en/docs', 'docs_src']

MD_FILES = 156
PY_FILES = 464

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
TARGET_DIR = PROJECT_ROOT / 'data' / 'raw' / 'fastapi'

GIT_CLONE_CMD = ['git', 'clone', REPO, '--branch', RELEASE, '--no-checkout', str(TARGET_DIR), '--depth', '1']
GIT_INIT_CMD = ['git', 'sparse-checkout', 'init', '--cone']
GIT_SELECT_CMD = ['git', 'sparse-checkout', 'set', *FOLDERS]
GIT_CHECKOUT_CMD = ['git', 'checkout']

def is_complete():
    return len(list(TARGET_DIR.glob(FOLDERS[0] + '/**/*.md'))) == MD_FILES and len(list(TARGET_DIR.glob(FOLDERS[1] + '/**/*.py'))) == PY_FILES

def download_data():
    print('Not all files are present, fetching data...')

    if TARGET_DIR.is_dir():
        shutil.rmtree(TARGET_DIR)
    subprocess.run(GIT_CLONE_CMD, cwd=PROJECT_ROOT, check=True)
    subprocess.run(GIT_INIT_CMD, cwd=TARGET_DIR, check=True)
    subprocess.run(GIT_SELECT_CMD, cwd=TARGET_DIR, check=True)
    subprocess.run(GIT_CHECKOUT_CMD, cwd=TARGET_DIR, check=True)

if __name__ == '__main__':

    if is_complete() is False:
        download_data()
        if is_complete() is False:
            sys.exit('Counts of files do not match. Exiting...')
        else:
            print('Data downloaded successfully!')
    else:
        print('Data exists correctly!')

    if subprocess.run(['git', 'describe', '--tags'], cwd=TARGET_DIR, check=True, capture_output=True, text=True).stdout.strip() != RELEASE:
        print('Fetched release does not match.')
