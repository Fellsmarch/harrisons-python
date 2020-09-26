# Python Library
This is my personal python library of random functions and programs.

## Install
If you would like to install this as an available module yourself add it to your [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH).

### Windows
1. Search for `environment eariables` in Windows search
2. Click `Edit the system environment variables`
3. Click `Environment Variables...`
4. If `PYTHONPATH` already exists in the system variables, edit the `PYTHONPATH` varable to include the location of the git repository
5. If it does not, add the location of the git repository to the `PYTHONPATH`

### Visual Studio Code
If you are getting pylint errors when trying to import the module go to settings.json and add this setting:
```    
"python.autoComplete.extraPaths": [
    "<PATH_TO_GIT_REPO>"
],
```
Then restart VS Code