from setuptools import setup, find_packages

setup(
    name="runner_game",
    version="0.1",
    description="A simple 2D game.",
    long_description="""\
        # The Runner


- >`The Runner` is the name of the game I'm <ins> `still`  </ins> working on, please feel free to try out my initial version. 


## How to Play:

 - > To jump and restart the game, users can only utilize  <ins>`the space tab` </ins>.


## How To Win:

- > Jump Jump Jump ! till you get your highest score 🥇

                          
                          
 - recommended : activate your virtual environment before                       
                            
                            
                             🔥 ENJOY THE RUN 🔥
    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'pygame>=2.0.0'
    ],
)
