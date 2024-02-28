Holbertonschool-AirBnB_Clone

AirBnb Console - Project's Intention

Similar to how we created a simple shell using the C Language, we are creating a command interpreter that works in similar fashion but is limited to specific use-cases.

Use-cases our project will be able to manage:

Create new objects (ex: new User or a new Place).
Retrieve an object from a file, a database, etc.
Do operations on objects (count, compute stats, etc).
Update attributes of an object.
Destroy an object.

# Project Structure:

| File/Folder                      | Description                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `models/`                        | This folder contains all the classes used in this project.                            |
| `tests/`                         | This folder contains all the unit tests for the project.                              |
| `AUTHORS`                        | Contains information about the authors of the project.                                |
| `README.md`                      | This is the file you are currently reading, contains information about this project.  |
| `console.py`                     | Contains the main entry point of the command interpreter.                             |
| `file.json`                      | This file is used to store all objects.                                               |

## models/:

| File/Folder     | Description                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| `engine/`       | This folder contains the storage engine for the project.                                 |
| `__init__.py`   | Makes the folder a Python package.                                                       |
| `amenity.py`    | Contains the `Amenity` class.                                                            |
| `base_model.py` | Contains the `BaseModel` class, the parent class for all other classes.                  |
| `city.py`       | Contains the `City` class.                                                               |
| `place.py`      | Contains the `Place` class.                                                              |
| `review.py`     | Contains the `Review` class.                                                             |
| `state.py`      | Contains the `State` class.                                                              |
| `user.py`       | Contains the `User` class.                                                               |

## engine/:

| File/Folder       | Description                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| `__init__.py`     | Makes the folder a Python package.                                                                                 |
| `file_storage.py` | Contains the `FileStorage` class that serializes instances to a JSON file and deserializes JSON file to instances. |

## tests/:

| File/Folder    | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| `test_models/` | This folder contains all the unit tests for the models in the project. |
| `__init__.py`  | Makes the folder a Python package.                                     |

## tests/test_models/:

| File/Folder            | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| `test_engine/`         | This folder contains all the unit tests for the engine in the project.                   |
| `__init__.py`          | Makes the folder a Python package.                                                       |
| `test_amenity.py`      | Contains the unit tests for the `Amenity` class.                                         |
| `test_base_model.py`   | Contains the unit tests for the `BaseModel` class.                                       |
| `test_city.py`         | Contains the unit tests for the `City` class.                                            |
| `test_place.py`        | Contains the unit tests for the `Place` class.                                           |
| `test_review.py`       | Contains the unit tests for the `Review` class.                                          |
| `test_state.py`        | Contains the unit tests for the `State` class.                                           |
| `test_user.py`         | Contains the unit tests for the `User` class.                                            |

## tests/test_models/test_engine/:

| File/Folder            | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `__init__.py`          | Makes the folder a Python package.                   |
| `test_file_storage.py` | Contains the unit tests for the `FileStorage` class. |


