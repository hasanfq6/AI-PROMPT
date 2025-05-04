# AI-PROMPT

Enhance your conversational experience with AI-PROMPT, a user-friendly command-line interface. Tailor voices, enjoy audio responses, and seamlessly stay updated.

## Features

- **Customizable Voices:** Personalize your AI conversations with various voice options.
- **Audio Responses:** Immerse yourself with dynamic audio generated for a more engaging chat.
- **Effortless Updates:** Stay on the cutting edge with easy-to-install updates.

- Seamless interaction with an AI-powered prompt system.
- Voice settings customization for a personalized experience.
- Generation of audio responses to make interactions more engaging.
- Flexible prompt modes (single-line and multi-line) to suit various preferences.
- Command-line interface with support for command parsing and argument handling.
- Threading and progress indicators for concurrent tasks and user feedback.
- Integration with chatbot APIs to retrieve responses based on user input.
- Logging of chat history and interactions for reference and analysis.
- User-friendly interface using `prompt_toolkit` with auto-suggestion and command history.
- External commands execution (`!command`) directly from the prompt.

  
## Supported Operating Systems

AI-PROMPT is designed to run on the following operating systems:

- Termux
- Linux
- macOS

## Getting Started

1. Download the latest release from the [Releases](https://github.com/hasanfq6/AI-PROMPT/releases) page.
2. Run the script in your terminal to start chatting with AI.

## Installation 
```bash
git clone https://github.com/hasanfq6/AI-PROMPT && cd AI-PROMPT && bash setup.sh
```

## commands
```shell
ai -h
Help option selected:
-v, --voice     Voice settings(advance)
-h, --help      show this option exit.
-V, --voice-setup       Setup the voice features
NOTE:
Use '#info' in the prompt to see more option
```
you can use commands in prompt by using `#`
in the AI-PROMPT, it will automatically shows the commands. if not, you can use `#help` to see Availabe Options:
### example 1
```shell
$~ >ai
Use [#info] to see more options
AI-PROMPT> #
             #audio
             #about
             #multi
             #sin
             #help
             #info
             #chip

```
### Example 2
```shell
$~ > ai
Use [#info] to see more options
AI-PROMPT> #help
Available commands:
• [#multi]: Switch to Multiline mode(ALT + ⏎ (ENTER) to enter)
• [#sin]: Switch to Single line mode
• [#info]: Show the info
• [clr]: clear the conversation
• [undo]: Restore the conversation
• [q,exit,quit]: quit or exit program
• [#about]: See the about
• [#chip]: See the ip address(Currently unavailable)
```
## Usage
1. Run the script.
2. Engage in easygoing conversations.
3. Explore voice settings for a personalized experience.

## Contributing

Feel free to contribute! Check out the [Contribution Guidelines](CONTRIBUTING.md) for details.

## License

AI-PROMPT is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries, email hasanfq818@gmail.com.

## Disclaimer

AI-PROMPT is designed for fun, learning, and casual use. Use caution for critical applications.
