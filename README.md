# Using Python Virtual Environment and Installing Requirements

This readme provides instructions on how to set up a Python virtual environment using `python -m venv` and install packages from a `requirements.txt` file within that virtual environment.

## Prerequisites

Make sure you have the following installed on your system:

- Python (Version 3.x recommended)

## Creating Virtual Environment

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to create your virtual environment.

3. To create a new Python virtual environment, run the following command:

   ```bash
   python -m venv .venv
   ```

   This will create a virtual environment named `.venv` in the current directory.

4. Activate the virtual environment:

   **On Windows:**

   ```bash
   .venv\Scripts\activate
   ```

   **On macOS and Linux:**

   ```bash
   source .venv/bin/activate
   ```

   After activation, you'll notice that your command prompt changes to show the name of the virtual environment (e.g., `(.venv)`).

## Installing Packages from requirements.txt

1. Make sure you have a `requirements.txt` file in your project directory that lists all the required packages and their versions.

   For example, the `requirements.txt` file should look like this:

   ```
   package1==1.0.0
   package2==2.1.0
   package3>=3.2.1
   ```

2. With the virtual environment activated, use `pip` to install the packages listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the packages specified in the `requirements.txt` file into your virtual environment.

3. Once the installation is complete, you can start working with your Python project, and it will use the packages installed within the virtual environment.

## Deactivating the Virtual Environment

After you have finished working on your project and want to deactivate the virtual environment, run the following command in the terminal:

```bash
deactivate
```

This will return your command prompt to its original state.

Congratulations! You have now successfully created a Python virtual environment using `python -m venv` and installed packages from the `requirements.txt` file within that virtual environment. You are ready to develop your Python project with a clean and isolated environment. Happy coding!