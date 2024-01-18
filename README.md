# HashBot for Discord

HashBot is a custom Discord bot designed to interact with the Pwnagotchi network auditing tool, enhancing the functionality of the DiscoHash plugin. It allows users to request and receive network hash information directly through Discord commands.

## Acknowledgments

- This bot is an extension of the work done by [@flamebarke](https://github.com/flamebarke), particularly building upon the Main DiscoHash plugin in their repository.
- The `hashbot.py` code is derived from @flamebarke's repository and aims to augment the DiscoHash plugin's capabilities.

## Features

- **Hash Retrieval**: Users can request hashes for a specified number of access points through Discord.
- **Command Interaction**: Easy-to-use Discord commands to interact with Pwnagotchi.
- **Seamless Integration**: Works alongside the Pwnagotchi's DiscoHash plugin.

<details>
<summary><b>Installation</b></summary>
<p>

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hashbot.git

2. **Navigate to the Repository Directory**:
   ```bash
   cd hashbot

3. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt

</p>
</details>

<details>
<summary><b>Setting Up Discord Bot</b></summary>
<p>

____________________

# HashBot for Discord

HashBot is a custom Discord bot designed to interact with the Pwnagotchi network auditing tool, enhancing the functionality of the DiscoHash plugin. It allows users to request and receive network hash information directly through Discord commands.

## Acknowledgments

- This bot is an extension of the work done by @flamebarke, particularly building upon the Main DiscoHash plugin in their repository.
- The `hashbot.py` code is derived from @flamebarke's repository and aims to augment the DiscoHash plugin's capabilities.

  
## Features

- **Hash Retrieval**: Users can request hashes for a specified number of access points.
- **Command Interaction**: Interact with the bot using simple Discord commands.
- **Seamless Integration**: Designed to work with Pwnagotchi's custom plugin system.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine or server for development and testing purposes.

### Prerequisites

- Python 3.6 or later
- `discord.py` library
- `python-dotenv` library for environment variable management

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hashbot.git

### Navigate to the Repository Directory:

cd hashbot

### Install Required Libraries:

pip install -r requirements.txt

## Setting Up Discord Bot

### Create a Discord Bot:
- Visit the Discord Developer Portal.
- Click "New Application", give it a name, and create your app.
- Go to the "Bot" tab and click "Add Bot".


### Set Up .env File:
Create a .env file in the root directory.
Add your Discord Bot Token, Guild ID, and Channel ID:

DISCORD_TOKEN=your_discord_bot_token
DISCORD_GUILD=your_discord_guild_id
GUILD_CHANNEL=your_discord_channel_id


## Usage
To run the bot, use the following command in the root directory of hashbot.py and the .env file:

python3 hashbot.py


Bot Commands
/dump [NUMBER]: Retrieves the specified number of hashes from Pwnagotchi and sends them in a text file.

# Acknowledgments
Special thanks to the Pwnagotchi project. I never would've figured this out if I didn't have you 😘
Most special thanks to @v0yager for creating DiscoHash and this Hat tip to anyone whose code was used.


### Notes:

- **Customization**: Customize the URL in the `git clone` command with your actual GitHub repository URL.
- **Additional Documentation**: If you have contributing guidelines or a license file, link them in the `README.md`. If not, you might want to create these files.
- **Functionality Details**: Add or modify any specific instructions or features related to your version of HashBot.
- **Markdown Formatting**: This is formatted in Markdown, which is standard for `README.md` files on GitHub. You can further enhance it with additional Markdown formatting as needed.

This `README.md` provides a basic structure that you can expand upon based on the specifics of your project and its deployment.
