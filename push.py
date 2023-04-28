import os


def git_push():
    print('***hello***')
    os.system('git status')
    print('***hello***')
    os.system('git add .')
    print('***hello***')
    os.system('git commit -m "add first news"')
    # os.system('git push')


git_push()
