### MacOS

1. Install git/ssh e.g. Xcode from appstore and start it, also install the command line tools,
   this might be done from the terminal using the following command.

       xcode-select --install

1. Install Python 3
     1. Install homebrew

            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

     2. Install python3 and virtualenv

            brew install python3

     3. Install virtualenv

            pip3 install virtualenv

 2. Open the repo as a new project in PyCharm.
 3. Open the project settings (File > Settings), ⌘+,
 4. Project: skateboard > Project Interpreter
 5. The config * after "Project Interpreter", "Create Virtualenv".
 6. I name my environment .pybuild and place it inside the skateboard directory, also I
    have selected to "Inherit global site-packages".
 7. Open "requierments.txt" in the IDE, when the small top row appears select
    "install packages".

#### Test installation

To run pytest inside PyCharm set up a new run configuration, "Run > Edit Configurations",
"+ > Python Teat > py.test". As target and working directory set the root directory you
checked out the code into and run the tests.

Some test may fail, because MacOS ain't no Linux, yet.

#### Running from terminal

Cd to the root of the checkout repo, assuong the pybuild virtual env
from previuos steps.

    . .pybuild/bin/activate
    pip3 install -e .
    pytest --pep8 --cov=hadbuild