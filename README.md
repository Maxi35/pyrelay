# pyrelay

pyrelay is a client which can connect to Realm of the Mad God written in [Python](https://www.python.org/).

This project is inspired by [nrelay](https://github.com/thomas-crane/nrelay)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages in requirements.txt

```bash
pip install requirements.txt
```

## Setup

Open the file `Accounts.json` and insert the email+password for the account(s) you want to use

If you want to use a proxy for that account add the following to the account in accounts.json
"proxy": {
	"host": "ip",
	"port": port,
	"type": type,
	"username": "username",
	"password": "password"
}

### Plugins

The folder `Plugins` is where you make the plugins the clients will use. **All plugins should be thread safe**

### Running

To start the bot simply run pyrelay.py from the cmd

```bash
pyrelay.py
```