[![Version][version-shield]][project-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Python3_template

Basic Python3 template

### Built With

Frameworks and libraries used to bootstrap the project:

- [![Python][python-shield]][python-url]

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You need install first:

- _Python3_

### Installation

- Go to main project at [project-url]
- Clone the repo:

```shell
git clone https://github.com/alejandrogm90/python3_examples.git
```

- Install all requirements:
  - Install pipenv:
    ```shell
    pip install pipenv
    ```
  - Update pipenv:
    ```shell
    pip install pipenv
    ```
  - Create requirements.txt and install in local (OPTIONAL):
    ```shell
    pipenv requirements > requirements.txt
    ```
    ```shell
    pip install -r requirements.txt
    ```

## Usage

On terminal:

- Easy example of nodes
  ![nodes-image]
```shell
pipenv run python src/nodos.py
```

- Easy example to sort list
```shell
ls src | pipenv run python src/sort_list.py
```

- Reverse mode
```shell
ls src | pipenv run python src/sort_list_reverse.py
```

- Load last status of IBEX35 in a CSV file
```shell
pipenv run python src/src/bolsa_info_IBEX35.py
```

- Debugging with bandit:
```shell
pipenv run python -m bandit -r src/
```
_For more examples, please refer to the [Documentation][wiki-url]_

### Usage of [script_manager_api][script_manager_api-url] (USING A JWT TOKEN)
- Launch a script in my host:
```shell
pipenv run python src/consult_using_token.py hello.sh link1 link2 link3
```

- Get last scripts launches in my host:
```shell
pipenv run python src/launch_script_using_token.py -l
```
_For more documentation, visit [script_manager_api][script_manager_api-url]_

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the License. See `LICENSE.txt` for more information.

## documentation

- https://www.python.org/doc/
- https://www.pygame.org/docs/
- https://cienciadedatos.net/documentos/pygml01-introduccion-grafos-redes-python.html

## Contact

Alejandro Gómez - [@alejandrogm90][profile-url]

Project Link: [project-url]

<!--
pipenv install --dev bandit
pip freeze > requirements.txt
pipreqs --force

pipenv update
pipenv requirements > requirements.txt
pipenv run python setup.py bdist_wheel

pipenv run python script.py
pipenv run python -m unittest discover
pipenv run python -m unittest
pipenv run python -m unittest test/utils/test_common_functions.py
-->

[nodes-image]: doc/nodes.png
[version-shield]: https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge
[contributors-shield]: https://img.shields.io/github/contributors/alejandrogm90/python3_examples.svg?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/alejandrogm90/python3_examples.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/alejandrogm90/python3_examples.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/alejandrogm90/python3_examples.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/alejandrogm90/python3_examples.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[python-shield]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[profile-url]: https://github.com/alejandrogm90
[project-url]: https://github.com/alejandrogm90/python3_examples/
[wiki-url]: https://github.com/alejandrogm90/python3_examples/wiki
[contributors-url]: https://github.com/alejandrogm90/python3_examples/graphs/contributors
[forks-url]: https://github.com/alejandrogm90/python3_examples/network/members
[stars-url]: https://github.com/alejandrogm90/python3_examples/stargazers
[issues-url]: https://github.com/alejandrogm90/python3_examples/issues
[license-url]: https://github.com/alejandrogm90/python3_examples/blob/master/LICENSE.txt
[linkedin-url]: https://www.linkedin.com/in/alejandro-g-762869129/
[python-url]: https://www.python.org/
[script_manager_api-url]: https://github.com/alejandrogm90/script_manager_api
