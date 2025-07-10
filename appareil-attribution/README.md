# Appareil Attribution Project

This project is a Python-based MVC application for managing the allocation of devices to users. It allows users to request devices, track allocations, and manage returns.

## Project Structure

```
appareil-attribution
├── app
│   ├── controllers
│   │   └── attribution_controller.py
│   ├── models
│   │   ├── utilisateur.py
│   │   ├── appareil.py
│   │   └── attribuer.py
│   ├── views
│   │   └── attribution_view.py
│   └── __init__.py
├── config
│   └── database.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd appareil-attribution
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the database connection in `config/database.py`.

## Usage

1. Start the application:
   ```
   python app/__init__.py
   ```

2. Access the application through your web browser at `http://localhost:5000`.

## Features

- User management: Create, retrieve, update, and delete users.
- Device management: Create, retrieve, update, and delete devices.
- Device allocation: Allocate devices to users and track allocation status.
- Return management: Manage the return of allocated devices.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.