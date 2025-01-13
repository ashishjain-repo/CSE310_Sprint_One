## How to create a virtual environement
To create a local virtual environement for our application we are going to use a python pacakage called `venv`. If you do not have `venv` on your system you can install that package globally on your system using this command: `pip install virtualenv` Where to create this environment? This environment should not be created in the cloned repository, this virutal environemnet will only be created outside the cloned repositories directory. This is how the structure should looks like:-
- Main Folder
  - Virtual Environment (Dependencies)
    - venv
    - dependencies
  - Cloned Repository
    - Project file
    - project folder
## Virtual Environment
To create the environement use this command: `python -m venv .myenv`. It will take a minute to set up the environment. After you can see the environment run this command to activate the environment: `myenv\Scripts\activate`. After running this command you will see your environment name in parantheses. Now what you have to do is to install the dependencies, for which now you can go into to the cloned repository and run this command: `pip install -r requirements.txt`. What this command does is download the packages that are in the file requirments.txt which should be in your cloned repository. To deactivate the virtual environement just type this in the terminal window `deactivate`.
If we have to install more dependencies in the future, we can just update the requirments.txt file and run the command again to download all the required packages.
