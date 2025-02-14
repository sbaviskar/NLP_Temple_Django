# NLP_Temple_Django

###### Enlighten yourself with natural language processing wisdom.

## Description

[NLP_Temple_Django](https://github.com/sbaviskar/NLP_Temple_Django) is a Django-based project designed for NLP-related tasks. It provides various functionalities for processing and analyzing natural language data.

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/sbaviskar/NLP_Temple_Django.git
   ```
2. **Navigate to the project directory**
   ```sh
   cd NLP_Temple_Django
   ```
3. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate # For Windows
   ```
4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
5. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## Docker Setup

You can also containerize the application using Docker.

1. **Build the Docker image**

   ```sh
   docker build -t my-django-app .
   ```

2. **Run the Docker container**

   ```sh
   docker run -p 8000:8000 my-django-app
   ```

After running the container, access the application at `http://localhost:8000`.

##### NLP Temple Demonstration : Youtube video
[![NLP_Temple_Django](https://i.ytimg.com/vi/9PqkRHsXaxE/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDLYeZZgqDFjWknEwzeQrsTcYfikw)](https://www.youtube.com/watch?v=9PqkRHsXaxE&t=12s)

## Contributing

Feel free to fork the repository, submit pull requests, or open issues for discussions.

