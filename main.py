import os, shutil
# Deterministic: copies the same image bytes on every run.
# v2: named HERE constant for the entry directory.
HERE=os.path.dirname(os.path.abspath(__file__))
out=os.environ.get('MAKEFUN_OUTPUT_DIR','/output')
os.makedirs(out,exist_ok=True)
shutil.copyfile(os.path.join(HERE,'entry.png'),os.path.join(out,'entry.png'))
