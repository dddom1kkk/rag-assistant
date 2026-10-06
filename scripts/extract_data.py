from pathlib import Path
import subprocess
import shutil

REPO = 'https://github.com/fastapi/fastapi.git'
RELEASE = '0.142.2'
FOLDERS = ['docs/en/docs', 'docs_src']
TARGET_DIR = '../data/raw/fastapi'
# MD_COUNT = 156
# PY_COUNT = 464
DOWNLOAD = False
GIT_CLONE = 'git clone ' + REPO + ' --branch 0.142.2 --no-checkout data/raw/fastapi --depth 1'
GIT_CHECKOUT = 'git sparse-checkout init --cone; git sparse-checkout set docs/en/docs docs_src; git checkout'

print(REPO, RELEASE, FOLDERS, TARGET_DIR)

if Path(TARGET_DIR).is_dir():
    if Path(TARGET_DIR + '/' + FOLDERS[0]).is_dir() and Path(TARGET_DIR + '/' + FOLDERS[1]).is_dir():
        if len(list(Path(TARGET_DIR).glob(FOLDERS[0] + '/**/*.md'))) == 156 and len(list(Path(TARGET_DIR).glob(FOLDERS[1] + '/**/*.py'))) == 464:
            print('All files exist. Terminating...')
        else:
            print('Not all files are present in target directory, pulling all the data from FastAPI repo.')
            shutil.rmtree('../data/raw', 'fastapi')
            DOWNLOAD = True
    elif Path(TARGET_DIR + '/' + FOLDERS[0]).is_dir() or Path(TARGET_DIR + '/' + FOLDERS[1]).is_dir():
        print('Not all folders are not present in target directory, pulling all the data from FastAPI repo.')
        shutil.rmtree('../data/raw', 'fastapi')
        DOWNLOAD = True
    else:
        print('Folders with files are not present in target directory, pulling all the data from FastAPI repo.')
        DOWNLOAD = True
else:
    print('Creating folders for data storage.')
    DOWNLOAD = True

if DOWNLOAD:
    subprocess.run(GIT_CLONE, cwd='../', check=True, shell=True)
    subprocess.run(GIT_CHECKOUT, cwd=TARGET_DIR, check=True, shell=True)

# subprocess.run(['git', 'log'], cwd=TARGET_DIR, check=True)
# subprocess.run(['git', 'popitt'], check=True)