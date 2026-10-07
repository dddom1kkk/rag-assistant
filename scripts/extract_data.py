from pathlib import Path
import subprocess
import shutil

REPO = 'https://github.com/fastapi/fastapi.git'
RELEASE = '0.142.2'
FOLDERS = ['docs/en/docs', 'docs_src']
PROJECT_ROOT = str(Path(__file__).parent.parent)
TARGET_DIR = PROJECT_ROOT + '/data/raw/fastapi'
GIT_DATA_CMD = 'git clone ' + REPO + ' --branch ' + RELEASE + ' --no-checkout ' + TARGET_DIR + ' --depth 1; cd ' + TARGET_DIR + '; git sparse-checkout init --cone; git sparse-checkout set ' + FOLDERS[0] + ' ' + FOLDERS[1] + '; git checkout'

download = False

print(REPO, RELEASE, FOLDERS, TARGET_DIR)

if len(list(Path(TARGET_DIR).glob(FOLDERS[0] + '/**/*.md'))) == 156 and len(list(Path(TARGET_DIR).glob(FOLDERS[1] + '/**/*.py'))) == 464:
    print('All files exist. Terminating...')
else:
    download = True
    if Path(TARGET_DIR).is_dir():
        shutil.rmtree(TARGET_DIR)

if download:
    subprocess.run(GIT_DATA_CMD, cwd=PROJECT_ROOT, check=True, shell=True)