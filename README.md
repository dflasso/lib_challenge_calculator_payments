# Calculator of Payments
To calculate payments to employees according day and schedule of hours worked. Getting to reports of payments according your settings such as value of hour in a specific range of time.

# Getting Started
Assuming that you have a supported version of Python 3.9 installed, you can first set up your environment with:
```
$ python -m venv .venv
...
$ . .venv/bin/activate
```

## Using default configuration 

### Create a file .txt with follow format:
```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
JHON=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
MARY=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
NANCY=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
```

### Open interpeter of python3.9

```python
 >>> from lib_pay_calculator.inbound_adapter import from_txt
 >>> file = open("../path/info.txt", 'r')
 >>> result = from_txt(file=file)
 >>> print(result)
 >>> file.close()
```
### Output
```
[
    'The amount to pay RENE is: 215.0 USD', 
    'The amount to pay ASTRID is: 85.0 USD', 
    'The amount to pay JHON is: 215.0 USD', 
    'The amount to pay MARY is: 215.0 USD', 
    'The amount to pay NANCY is: 215.0 USD'
]
```

# Customization
This library allow extensive your functionalities, you can implements new setting, serializers, deserializers and services for calculation.

##  Customize Calculation Settings
Only must just implement a new class of **ICalculatorPaySettingsBuilder**

```python
from lib_pay_calculator.config import ICalculatorPaySettingsBuilder

class CalculatorPaySettingsCustom(ICalculatorPaySettingsBuilder):
    """
    Custom Implementation ...
    """
    
    @property
    def calculator_pay_settings(self) -> List:
        //TODO

    @calculator_pay_settings.setter
    def calculator_pay_settings(self, parameters) -> None:
        //TODO
```

## Customize Serializer
If the solution required read information form other formats for example json, xml. 
Only must just implement a new class of **ICalculatorPaySerializer**

```python
from lib_pay_calculator.serializers import  ICalculatorPaySerializer,

class CalculatorPaySerializerCustom(ICalculatorPaySerializer):
    
    """
    Custom Implementation ...
    """
    
    @property
    def data(self) -> Any:
        //TODO

    @data.setter
    def data(self, raw_data) -> None:
        //TODO
```

## Customize Deserializer
If the solution required export results to other formats for example json, xml. 
Only must just implement a new class of **ICalculatorPaySerializer**

```python
from lib_pay_calculator.serializers import  ICalculatorPayDeserializer

class CalculatorPayDeserializerCustom(ICalculatorPayDeserializer):
    """
    Custom Implementation ...
    """
    def parse(self, processed_data) -> Any:
        //TODO
```

## Customize Logic of calculation payments
Only must just implement a new class of **ICalculatorPayService**

```python
from lib_pay_calculator.services import ICalculatorPayService

class CalculatorPayServiceCustom(ICalculatorPayService):
    """
    Custom Implementation ...
    """
    
    def calculate(self, data, settings) -> Any:
        //TODO
```

## Inject the new implementations
Finally, Inject new dependencies to handler

```python
    
    handler = CalculatorPayHandler()

    #If you have new implementation of settings and calculator
    newsettings = CalculatorPaySettingsCustom()
    calculator = CalculatorPaySerializerCustom()
    handler.setup(builder=newsettings, calculator_service=calculator)

    #If you have new implementation of serializer
    serializer = CalculatorPaySerializerCustom()
    handler.import_data_setup(serializer=serializer)

    #If you have new implementation of deserializer
    deserializer = CalculatorPayDeserializerCustom()
    handler.export_data_setup(deserializer=deserializer)
```
# Methodology
Following an agile methodology
## Version Code Strategies
This project used git flow. Each requirement was created such as a new branch according your category: feacture, bug, support, hotfix.

Depends of branch, was merged to develop or main.

## TDD
All feactures have a unit test, and funtional test. First the test was designed and then the functionality

## Automatization of testing
Through github actions in each commit of the feature/** branches all unit tests are executed

## Continuous delivery
Through github actions in each commit of the releases/** branches a tag is created


# Architecture
See [class diagram](https://github.com/dflasso/lib_challenge_calculator_payments/blob/documentation/IOET_Solution-Class_Diagram.pdf)


# DevSecOps

![cycle devops](https://static.wixstatic.com/media/96edd2_1a1fcd6de8304c549e6ec6afe91c68b7~mv2.png/v1/fit/w_600%2Ch_359%2Cal_c/file.png)

## Plan

Planning of the project was managed in Jira Software such as Released planning, User stories, assign responsible and tracking issues.
- [Jira Software](https://smart-data-visio-espe.atlassian.net/jira/software/projects/CPC/boards/2/roadmap) 

Chat of team, also notifications and alerts about solution.
- [Slack](https://app.slack.com/client/T03M0Q3KZU6/C03M7B6RBMZ)

Help Desk
- [Email for Issues of Lib Calculator of Payments](mailto:contact-project+calculator-payments-challenge-lib-pay-calculator-37336179-issue-@incoming.gitlab.com)

## Code

- [Main Repository Lib Calculator of Payments](https://github.com/dflasso/lib_challenge_calculator_payments). According strategy git flow.
- [Secondary Repository Lib Calculator of Payments](https://gitlab.com/calculator-payments-challenge/lib_pay_calculator). According strategy git Trunk-based

## Build

- Gitlab CI/CD Pipelines
```yml
compile:
  stage: build
  image: python:3.9.13-slim-buster
  before_script:
    - python3.9  -m venv .env
    - source .env/bin/activate
    - pip3 install -r requirements.txt
  script:
    - pip install wheel
    - python3.9 setup.py sdist bdist_wheel
```

## Test

- Unit test.
    + [pytest](https://docs.pytest.org/en/7.1.x/)
    + [Unit testing framework](https://docs.python.org/3/library/unittest.html)
    + [nose](https://nose.readthedocs.io/en/latest/)
```bash
$ nosetests -v --with-xunit --xunit-file=report.xml  
```
- Test Coverage 
    + [pytest-cov](https://github.com/pytest-dev/pytest-cov)
```bash
$ pip install pytest pytest-cov
$ coverage run -m pytest
$ coverage report
$ coverage xml
```

### Automatization Test
- [Github Actions](https://github.com/dflasso/lib_challenge_calculator_payments/blob/main/.github/workflows/run-tests.yml)
- [Gitlab CICD Pipelines]()

## Security SAST -  Code Vulnerabilities
- [Bandit](https://github.com/PyCQA/bandit).  Bandit is a tool designed to find common security issues in Python code. To do this Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files it generates a report.

- [Semgrep](https://semgrep.dev/) Static analysis at ludicrous speed Find bugs and enforce code standards

- [Code Quality](https://docs.gitlab.com/ee/ci/testing/code_quality.html). To ensure your project’s code stays simple, readable, and easy to contribute.

- [Sonarcloud](https://sonarcloud.io/)

## Releases 
- Tags and Releases in Github. [See github action pipelin](https://github.com/dflasso/lib_challenge_calculator_payments/blob/main/.github/workflows/releases.yml)

- [Private Package Registry - Gitlab](https://gitlab.com/calculator-payments-challenge/lib_pay_calculator/-/packages/7648576)

        Installation by pip
        ```
        pip install lib-pay-calculator --extra-index-url https://__token__:<your_personal_token>@gitlab.com/api/v4/projects/37336179/packages/pypi/simple
        ```


