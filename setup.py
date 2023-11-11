from setuptools import setup

setup(
    name='math_quiz',
    version='0.1.0',    
    author='Mudassir Ahmed',
    author_email='mudassir.ahmed@fau.de',
    license='Appache',
    packages=[],
    install_requires=['setuptools==68.2.2'],
    entry_points={
        'console_scripts': [
            'math_quiz = DSSS_H2.math_quiz.math_quiz:__main__',
        ],
    }

)