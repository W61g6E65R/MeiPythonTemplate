# DMS_Python_Cookbook

## Installation

### Python

### Poetry
  - Install poetry  
    ```pip install poetry ```  
  - Configure poetry for local .env folder  
    ``` poetry config virtualenvs.in-project true ```

### Packages
  - General 
    - ```pyyaml```
    - ```dotenv```
    - ```pytest```
    - ```argparse```
  - Api
    - ```fastapi```
    - 
    - ```importlib```
  - Database
    - ```sqlalchem```
    - ```psycopg-binary```

### Project
#### Poetry

  - Init poetry project  
    ``` poetry init ```
  - Add packages to project  
    ``` poetry add packageName ```

#### Config

  - Use a seperate config folder (modulename.d) for every module or implementation  
    ```
    config
        |
        +---global.d
                |
                +--- global.yaml
                +--- logging.yaml
        +---httpRequests.d
                |
                +--- 01_enaio_docserver.yaml
                ...
    ```
  - It could be usefull to sort the config files by their order of execution. This is imporant when the whole folder executes some functions in correct order

#### Testing with pytest

  - Use one testfile per module

#### .gitignore

#### Empty Folders
To add folders to .git without adding the files inside create a file .gitignore with following content:

```
*
!.gitignore
```

This file tells git to ignore all files except the .gitignore itself