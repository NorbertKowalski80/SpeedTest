# SpeedTest
# Speed Test GUI

Speed Test GUI is a Python-based graphical application that allows users to measure their internet speed, including download and upload speeds, as well as ping, using the `speedtest` library and a `ping` utility.

## Features

- **Internet Speed Test**: Measure download and upload speeds in Mbps.
- **Ping Measurement**: Perform accurate ping tests using system utilities.
- **User-Friendly Interface**: Modern, intuitive GUI built with `tkinter` and `ttk`.
- **Progress Visualization**: Real-time progress updates during the test.

## Screenshots

![Screenshot of Speed Test GUI](placeholder-for-screenshot)

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or later
- Required Python libraries:
  - `speedtest`
  - `tkinter`

To install the `speedtest` library, run:
```bash
pip install speedtest-cli
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/speedtest-gui.git
   ```
2. Navigate to the project directory:
   ```bash
   cd speedtest-gui
   ```
3. Run the program:
   ```bash
   python speed_test_gui.py
   ```

## How It Works

- **Download and Upload Test**: Uses the `speedtest` library to calculate download and upload speeds by selecting the best server based on latency.
- **Ping Test**: Runs the `ping` command via `subprocess` to get an accurate average response time.
- **GUI Design**: Built with `tkinter` and `ttk`, providing a clean and dynamic user interface with real-time progress updates.

## File Structure

```
.
├── speed_test_gui.py     # Main Python script
├── README.md             # Documentation
└── requirements.txt      # Python dependencies (optional)
```

## Known Issues

- **Platform Dependency**: The `ping` utility may behave differently on Linux and macOS compared to Windows. This script uses the Windows-specific `-n` flag.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them:
   ```bash
   git commit -m "Description of your changes"
   git push origin feature-name
   ```
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- `speedtest` library for internet speed testing.
- Python `tkinter` for GUI development.

## Author

**Your Name**  
[GitHub Profile](https://github.com/NorbertKowalski80)
