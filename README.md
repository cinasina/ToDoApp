# Django ToDo List Application with Docker

This is a Django application that allows users to manage their tasks in a to-do list format. The application is built using Django's Class-Based Views (CBV) and Django Rest Framework (DRF) for creating the API endpoints.

## Key Features

- **Task Management**: Users can create tasks, view task details, and update or delete tasks. Task operations are restricted to the owner of the task, ensuring data privacy and security.
- **Django Rest Framework (DRF)**: The application uses DRF to create API endpoints, allowing tasks to be managed over an API. This makes the application scalable and easy to integrate with other systems.
- **Class-Based Views (CBV)**: The application uses Django's Class-Based Views for structuring the views. This enhances code reusability and readability.
- **Docker Integration**: The application is Dockerized, which ensures that it can be easily set up and run on any system without worrying about system-specific dependencies.
- **Testing**: The application includes comprehensive test cases to test views, models, URLs, and forms. This ensures that all the components of the application are working as expected and makes the application more maintainable.

## Installation

The application is Dockerized, and can be easily set up and run using Docker commands. The application also includes a `requirements.txt` file for installing the necessary Python packages.

## Usage

After setting up, the application can be accessed in a web browser at the local server's address. Users can create tasks, view task details, and update or delete tasks.

## Contributing

Feel free to contribute to the development of this application by creating a pull request. Please ensure that your code passes all the existing tests and, if possible, write new tests for new features or bug fixes.

## License

This project is licensed under the MIT license.
