# Terminal User Interface (TUI)

_Terminal User Interface (TUI)_ that visualizes **Google Cloud Platform (GCP)** resources.

## Execution

First, a local project environment needs to be created, then the project's dependencies need to be be installed.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/google.git
   cd google
   ```

2. Install Dependencies.

   ```sh
   # Install Dependencies
   tui/scripts/install.sh
   ```

3. Source environment variables.

   ```sh
   # Source environment variables
   source tui/environments/.env.development
   ```

4. Execute the application.

   ```sh
   # Execute the Application
   tui/scripts/run.sh
   ```

## Testing, Linting, and Formatting

Execute the tests to validate your installation.

### Linux

```sh
tui/scripts/test.sh
tui/scripts/lint.sh
tui/scripts/format.sh
```
