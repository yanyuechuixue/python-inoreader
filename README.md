Inoreader
=========

![](https://api.travis-ci.org/yanyuechuixue/python-inoreader.png?branch=master)

Python wrapper of Inoreader API.

## Installation

1. Clone this repository and install it with `setup.py`

```shell
python setup.py install
```

2. Install with `pip` directly

```shell
pip install git+https://github.com/yanyuechuixue/python-inoreader.git
```

## Usage

1. [Register your application](https://www.inoreader.com/developers/register-app). Use `http://localhost:9090/oauth/redirect` for the redirect URI and set scope to "Read and Write". Then create the configuration file `$HOME/.inoreader`

   An example of the configuration file:

   ```
   [auth]
   appid = your_app_id
   appkey = your_app_key
   ```

2. Login to your Inoreader account

   ```shell
   inoreader login
   ```

2. Use the command line tool `inoreader` to do something, run `inoreader --help` for details. Or in code do:

   ```python
   from inoreader.main import get_client
   client = get_client()
   ```
