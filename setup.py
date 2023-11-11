from setuptools import setup

setup(
    name='math-quiz',
    version='0.1.0',    
    author='Mudassir Ahmed',
    author_email='mudassir.ahmed@fau.de',
    license='Appache',
    packages=[],
    install_requires=['setuptools==68.2.2'],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.math_quiz:__main__',
        ],
    }

)