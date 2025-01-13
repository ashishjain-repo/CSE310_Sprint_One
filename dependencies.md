## How to create a virtual environement
To create a local virtual environement for our application we are going to use a python pacakage called `venv`. Where to create this environment? This environment should not be created in the cloned repository, this virutal environemnet will only be created outside the cloned repositories directory. This is how the structure should looks like:-
- Main Folder
  - Virtual Environment (Dependencies)
    - venv
    - dependencies
  - Cloned Repository
    - Project file
    - project folder
## Virtual Environment
To create the environement use this command: `python -m venv myenv`. It will take a minute to set up the environment. After you can see the environment run this command to activate the environment: `myenv\Scripts\activate`. After running this command you will see your environment name in parantheses. Now what you have to do is to install the python
