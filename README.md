# Forum

## Development Environment Setup

### Requirments

This project requires the following be installed:
  * Python 3
  * Node.js
  * Yarn

### Python Virtual Environment

For this it is advisable to use a virtual environment for python 3. This can be accomplished by running:

```shell
python -m venv venv
```
or if python 2 is installed:

```shell
python3 -m venv venv
```

the virtual environment can then be activated by running the following on UNIX based systems

```shell
source ./venv/bin/activate
```

or the following on Windows systems:

```powershell
.\venv\Scripts\Activate.ps1
```

if PowerShell complains about not being able to run scripts, run the following in an Administrator PowerShell

```powershell
Set-ExecutionPolicy RemoteSigned
```

### Installing Dependencies

For the python virtual environment dependencies can be installed using

```shell
pip install -r requirements.txt
```

For Node.js dependencies can be installed using

```shell
yarn
```

### Usage

#### Manually

```shell
yarn dev
```

then

```shell
python3 ./forum/manage.py runserver
```

#### With Visual Studio Code

For simplicity, I have provided launch scripts for Visual Studio Code. Running "Django: runserver" will run all the required tasks to compile the JavaScript
