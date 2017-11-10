#### Install requirements
##### Windows

1. [git-extensions](https://gitextensions.github.io/)
2. [PyCharm](https://www.jetbrains.com/pycharm/download)
3. [Python](https://www.python.org/downloads/)  

##### MacOS

1. Install git/ssh e.g. Xcode.

       xcode-select --install

2. Install homebrew (https://brew.sh/)

       /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

3. Install python3

       brew install python3

4. Install virtualenv

       pip3 install virtualenv

#### Project preparation

1. Open the repo as a new project in PyCharm.
2. Open the project settings (File > Settings),
3. Project: skateboard > Project Interpreter
4. The config * after "Project Interpreter", "Create Virtualenv".
5. Name environment .pybuild and place it inside the skateboard directory, also 
    select "Inherit global site-packages".
6. Open "requirements.txt" in the IDE, when the small top row appears select
    "install packages".

#### Test installation

To run pytest inside PyCharm set up a new run configuration, "Run > Edit Configurations",
"+ > Python Teat > py.test". As target and working directory set the root directory you
checked out the code into and run the tests.


#### Running from terminal

Go to the root of the checkout repo, assuming the pybuild virtual env
from previous steps.

    . .pybuild/bin/activate
    pip3 install -e .
    pytest --pep8 --cov=tw