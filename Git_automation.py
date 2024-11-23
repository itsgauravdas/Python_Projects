import os 
com="git init"
stat = "git status"
git = ["git status","git add .","git commit -m adding", "git push origin main"]

for i in git:
    os.system(i)
    