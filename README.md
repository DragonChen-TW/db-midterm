## Environments

In this project, we use conda/anaconda/miniconda to manage Python packages.

### Create a new environment
Run this command to rebuild a similar environment from given yaml.
```shell
conda env create -f environment.yml
```

### Update exist environment
```shell
conda env update --file environment.yml --prune
```

### Export environment
```shell
conda env export --no-builds > environment.yml
```

### Remove exist environment
Run this command to remove the environment.
```shell
conda remove --name db-midterm --all
```

## How to start locally

### Oracle DB test

I attached a zip file of instantclient binary (for macos) under `client/` folder.

Double click ot unarchieve the `instantclient_19_8` folder.

You can run the test file to test the connection.

```shell
conda activate db-midterm
python backend/test_db.py
```

Output is expected as
```
Successfully connected to Oracle Database
5 Rows Inserted
Task 1 is NOT done
Task 2 is NOT done
Task 3 is done
Task 4 is NOT done
Task 5 is done
```

### Web server

```shell
conda activate db-midterm
python main.py
# go to http://localhost:8765/
```

### Some commands

1. db init

```shell
python run_init.py
```
This script can resset the Orcale DB to the original state defined in `backend/init.sql`.

## Folder Sructure

Flask 架構第二種：僅使用 Flask Blueprints 切分路徑，但 templates 統一放在主資料夾下的 templates 內。

Only use flask blueprints to seperate the path. Put all template files in the `templates` folder located in the root directory (under the folder for that view).

```
ecommerce/
|
├── static/
|   ├── logo.png
|   └── main.css
|
├── templates/
|   ├── auth/
|   |   ├── login.html
|   |   ├── forgot_password.html
|   |   └── signup.html
|   └── cart/
|       ├── checkout.html
|       └── view.html
|
├── view/
|   ├── auth.py
|   └── cart.py
|
├── app.py
├── config.py
└── models.py
```