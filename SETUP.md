### Windows

#### Install requirements

To work with Git i strongly suggest installing [git-extentions](https://gitextensions.github.io/),
and selecting to use openssh and connection and the "checkin-checkout as-is", option. 

Developing under windows is limited and not fully supported, some of the tools
will not work as intended. But feel free to test and improve. I have to some extent
tested the following environment with some success. [PyCharm 2017.2](https://www.jetbrains.com/pycharm/download),
[Python 3.5.1](https://www.python.org/downloads/release/python-351/) I recommend 
setting up virtualenv inside PyCharm. PyCharm seams to like these environments better.

  1. Clone the code from [haddock](https://haddock.got.volvocars.net/ci/gerrit/#/admin/projects/had_ci_scripts)
     much the same was as in Linux. I use "Git Bash" for this (from git-extentions).
  2. Open the repo as a new project in PyCharm.
  3. Open the project settings (File > Settings), Ctrl+Alt+S
  4. Project: had_ci_scripts > Project Interpreter
  5. The config * after "Project Interpreter", "Create Virtualenv".
  6. I name my environment .venv and place it inside the had_ci_scripts directory, also I 
     have selected to "Inherit site-packages".
  7. Open "requierments.txt" in the IDE, when the small top row appears select
     "install packages". The package "jenkins-job-builder" failed for me but the
     rest worked.
     
 #### Test installation

To run pytest inside PyCharm set up a new run configuration, "Run > Edit Configurations",
"+ > Python Teat > py.test". As target and working directory set the root directory you
checked out the code into and run the tests.

Some test may fail, because Windows ain't no Linux, yet.

### MacOS

1. Install git/ssh e.g. Xcode from appstore and start it, also install the command line tools,
   this might be done from the terminal using the following command.

       xcode-select --install

1. Install Python 3
     1. Install homebrew (https://brew.sh/)

            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

     2. Install python3

            brew install python3

     3. Install virtualenv

            pip3 install virtualenv

 2. Open the repo as a new project in PyCharm.
 3. Open the project settings (File > Settings), ⌘+,
 4. Project: skateboard > Project Interpreter
 5. The config * after "Project Interpreter", "Create Virtualenv".
 6. I name my environment .pybuild and place it inside the skateboard directory, also I
    have selected to "Inherit global site-packages".
 7. Open "requirements.txt" in the IDE, when the small top row appears select
    "install packages".

#### Test installation

To run pytest inside PyCharm set up a new run configuration, "Run > Edit Configurations",
"+ > Python Teat > py.test". As target and working directory set the root directory you
checked out the code into and run the tests.

Some test may fail, because MacOS ain't no Linux, yet.

#### Running from terminal

Go to the root of the checkout repo, assuong the pybuild virtual env
from previous steps.

    . .pybuild/bin/activate
    pip3 install -e .
    pytest --pep8 --cov=testbuild