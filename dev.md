# CSE310_Sprint_One

## Git Clone
`git clone https://myrepo.com/some-repo` this command is used to clone or create a copy of a repository which currently is a remote repository. This command is paired with the link where that git repository resides.

## Git Checkout
`git checkout -b branch-name` it is a good practice to work on a branch instead of the main or master branch, so it does not disrupt the flow. Working on a branch can help you organize your code and you will be able to check it locally before pushing it all to the main or master branch where the important code resides.

## Git Branch
`git branch` this command will open a list of available branches that are created by you and the main branch. You can see what branch you are working on in the list where the name of the branch have a astrisk before it, this could look something like this:-
```
main
my-branch
* inbox-function
```
Based on the example you are currently working on the branch name `inbox-function`.

## Git Add
`git add .` this command stages all the changes new, updated or deleted in the current directory or their subdirectories.


To have a copy of this repository locally please use the following command:
```
git clone https://github.com/ashishjain-repo/CSE310_Sprint_One.git
```
This will create a copy for what we have in the main branch for you in your local machine. If you have authrorization to the repository as a contributor you will be able to push code in this repository.


## This is what we have to do as a team to build an awesome application using Version Control:
1. First clone the repository: `git clone https://github.com/ashishjain-repo/CSE310_Sprint_One.git`
2. Now get into the directory that was just cloned from the github.
3. You are currently on main branch, make sure to create a new branch: `git checkout -b lastname-issue`
4. Now to make sure you have all the changes that are in the main branch in your local repo switch to the main branch and pull all the changes. Use the following commands:
  ```
  git switch lastname-issue
  git pull origin main
  ```
5. Now you have to switch to the branch you will be working on and then merge the changes from the main branch to your working branch. This merge is not merging code in the remote repository so do not worry about having merge conflicts. Use the following command:
  ```
  git switch lastname-issue
  git merge main
  ```
6. It is a good practice to work on one feature at a time and have branch for every issue. For example you are assigned to work on two features which are to capitalize the first letter of the word and if user add no input throw an error.
7. So you will work on first feature and create a branch for that something like `git checkout -b lastname-capitalize` work on it and push the changes to your branch. Then you are going to create a new branch named `lastname-noinput` and then work on it and push your changes.
