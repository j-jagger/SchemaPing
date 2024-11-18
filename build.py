import os
import subprocess

def build_exe(python_file):
    # Ensure PyInstaller is installed
    try:
        subprocess.run(["pyinstaller", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("PyInstaller is not installed. Install it using 'pip install pyinstaller'.")
        return

    # Build the command
    build_command = [
        "pyinstaller",
        "--onefile",  # Bundle into a single executable
        "--noconfirm",  # Skip the confirmation prompt
        "--console",  # Keep console output (use '--windowed' for GUI apps)
        python_file
    ]

    # Run the command
    try:
        print(f"Building {python_file} into an executable...")
        subprocess.run(build_command, check=True)
        print("Build complete!")

        # Locate the built executable
        dist_dir = os.path.join(os.getcwd(), "dist")
        exe_file = os.path.join(dist_dir, os.path.splitext(os.path.basename(python_file))[0] + ".exe")
        if os.path.exists(exe_file):
            print(f"Executable created at: {exe_file}")
        else:
            print("Build succeeded, but executable not found in 'dist/' directory.")
    except subprocess.CalledProcessError as e:
        print("Error during the build process:")
        print(e)

if __name__ == "__main__":
    python_file = "schemaping.py"  # Replace with your .py file path
    build_exe(python_file)
