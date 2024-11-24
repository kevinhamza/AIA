# Advanced Intelligent Assistant (AIA)

AIA is a comprehensive, open-source AI-powered assistant system that integrates a wide array of advanced functionalities. It combines real-time face detection, voice recognition, social media management, internet task automation, device control, machine learning, and more. This project merges capabilities from a self-operating computer system and a custom AI, providing a fully automated and intelligent experience for users.

## Features

- **Voice Assistant**: Interact with the assistant through voice commands.
- **Real-Time Face Detection**: Capture images and identify individuals with detailed personal data, integrated with social media platforms and PimEye-like services.
- **Social Media Integration**: Manage posts, updates, and retrieve personal data across platforms like Facebook, Twitter, Instagram, and LinkedIn.
- **Internet Task Automation**: Fetch news, weather updates, and perform other internet-based tasks.
- **Device Control**: Open applications and manage system tasks through voice or commands.
- **Machine Learning**: Predictive models, data analysis, and custom learning capabilities.
- **Chatbot**: NLP-based conversations for intelligent interactions.
- **PimEye-like Services**: Real-time image search and facial recognition to gather personal data from the web.
- **Automation**: Automate custom tasks and workflows with ease.

## Installation

### Requirements

- maybe Python <= 3.11.5 if other python version not work 
- Required libraries and dependencies listed in `requirements.txt`
- you can also do this if requirements.txt gives error `pip install --use-deprecated=legacy-resolver -r requirements.txt`

### Steps

1. Create a New Virtual Environment (if needed):
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    
2. Clone the repository:
    ```bash
    git clone https://github.com/kevinhamza/AIA.git
    cd AIA
    ```

3. Install dependencies:
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Install dependencies(if requirement.txt gives error):
    ```bash
    pip install --use-deprecated=legacy-resolver -r requirements.txt
    or
    pip install --use-feature=2020-resolver -r requirements.txt
    ```

5. Set up environment variables:
    - Create a `.env` file with the necessary API keys and configurations for services such as Twitter, Facebook, PimEye-like services, etc.
    - Example `.env` file:
      ```env
      TWITTER_API_KEY=your_twitter_api_key
      FACEBOOK_API_KEY=your_facebook_api_key
      PIMEYE_API_KEY=your_pimeye_api_key
      ```

6. Run the following command to install `espeak` (if you using Linux):
    ```bash
    sudo apt-get update
   sudo apt-get install espeak
    ```

7. Run the assistant:
    ```bash
    python main.py
    ```

## Configuration

The `config/settings.py` file contains various configuration options to customize the assistant. Make sure to update the following configurations:

- **API Keys**: Ensure you have API keys for services like Twitter, Facebook, PimEye-like services, and others.
- **Face Recognition Settings**: Configure face recognition models and thresholds for real-time identification.

## Contributing

We welcome contributions! If you'd like to contribute to the project, please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more details on how to get involved.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Voice Recognition Libraries](https://github.com/some-repo)
- [WhiteRabbit AI API](https://www.whiterabbitneo.com/)
- [Social Media API Integration](https://github.com/some-repo)
- [PimEye](https://pimeye.com/) (for real-time facial recognition and image search)


# AIA Project - Running Locally on Mobile  

This guide explains how to run the AIA project locally on a mobile device using Python. The setup is optimized for Android devices using **Termux** or **Pydroid 3**.  

---

## Prerequisites  

### For Android  
1. **Python Environment**  
   - Install **Termux** from [F-Droid](https://f-droid.org/) (recommended) or **Pydroid 3** from the Google Play Store.  

2. **Project Files**  
   - Ensure the following files are available:  
     - `main.py`  
     - `requirements.txt`  
     - Other necessary directories like `config/`, `modules/`, etc.  

---

## Setup Python Environment  

### Using Termux  
    pkg update && pkg upgrade  
    pkg install python python-pip

### Using Pydroid 3 
2. **Open Pydroid 3.**
3. **Use its built-in package manager to install Python and pip.**

### Transfer Project Files

    Copy the project files to your mobile device:
    # Use USB transfer or cloud storage like Google Drive.
    # Place them in a directory, e.g., /storage/emulated/0/AIA/.

### Install Dependencies

- Edit `requirements.txt` to modify dependencies for mobile compatibility:

      torch-mobile>=1.10.0  
      tensorflow-lite>=2.5.0

  ### Install Dependencies

  - Run the following command in Termux or Pydroid 3:

        pip install -r requirements.txt

### Adjust Code for Mobile
- **File Path Adjustments**
- Update file paths to be compatible with mobile systems:

      import os
      BASE_DIR = os.path.expanduser("~/AIA/")
      config_path = os.path.join(BASE_DIR, "config.json")

  ### Disable Non-Essential Modules
  - Comment out or disable modules that require significant resources (e.g., advanced ML models).
 
  ### Execute the Project
  - Navigate to the project directory:
  
        cd ~/AIA/

  - Run the project:

        python main.py

### Optional: Add a GUI

- For a mobile-friendly interface, install Kivy:

      pip install kivy

- Update the project to include Kivy-based screens for user interactions.

### Limitations

- **Performance**
   - *Mobile devices may struggle with resource-intensive tasks.*
   - *Use lightweight models (e.g., TensorFlow Lite, ONNX).*
 
- **Storage**
    - *Ensure adequate space for dependencies and project files.*
 
- **Compatibility**
    - *Not all Python libraries work on mobile. Test dependencies individually.*
 
### Next Steps

- Optimize models for mobile using TensorFlow Lite or PyTorch Mobile.
- Explore adding advanced mobile-specific features like notifications or camera access.
