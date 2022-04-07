## Environments

In this project, we use conda/anaconda/miniconda to manage Python packages.

### Create a new envirnoment
Run this command to rebuild a similar environment from given yaml.
```shell
conda env create -f environment.yml
```

### Remove exist environment
Run this command to remove the environment.
```shell
conda remove --name db-midterm --all
```

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