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

1. Clone the repository:
    ```bash
    git clone https://github.com/kevinhamza/AIA.git
    cd AIA
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Install dependencies(if requirement.txt gives error):
    ```bash
    pip install --use-deprecated=legacy-resolver -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file with the necessary API keys and configurations for services such as Twitter, Facebook, PimEye-like services, etc.
    - Example `.env` file:
      ```env
      TWITTER_API_KEY=your_twitter_api_key
      FACEBOOK_API_KEY=your_facebook_api_key
      PIMEYE_API_KEY=your_pimeye_api_key
      ```

4. Run the assistant:
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
