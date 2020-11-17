import glob

# ['glob_test.py']
print(glob.glob('*.py'))
# ['..\\argv_test.py', '..\\keyword_test.py']
print(glob.glob('../*.py'))
