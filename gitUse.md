查看当前分支
```
git branch
```
切换分支命令：

```
git checkout (branchname)
```
合并分支
```
git merge 
```

拉取远程分支到本地
```
git clone -b testing git@github.com:yulong12/Notes.git
```
删除分支
```
git branch -d (branchname)
```

## git如何把master合并到自己分支

- 1.切换到主分支
```
    git checkout master
```

- 2.使用git pull把master代码拉到本地
```
    git pull
```
- 3.切换到自己的分支——>(XXX)
```
    git checkout XXX
```
- 4.使用merge把主分支的代码合并到自己的分支
```
  git merge master
```
  注意：合并时有可能会有冲突，解决完冲突才能push

- 5.最后push，你分支的代码就和主分支的一样了
```
  git push
```

## 删除分支

-  删除本地分支  
```
git branch -d localBranchName
```
-  删除远程分支  
```
git push origin --delete remoteBranchName
```