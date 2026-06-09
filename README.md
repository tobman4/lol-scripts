# League of Legends Scripts

A collection of Python scripts for automating tasks and gathering data from the League of Legends client using the LCU (League Client Update) API.

## Prerequisites

- Python 3.x
- League of Legends Client

## Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv .env
   ```
2. **Activate the environment:**
   - **Windows:** `.\.env\Scripts\activate`
   - **Linux/macOS:** `source .env/bin/activate`
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Common Arguments

Most scripts utilize a shared utility module (`util.py`) and support these arguments:

- `-l`, `--lockfile`: Path to the League of Legends `lockfile`. Defaults to `C:\Riot Games\League of Legends\lockfile` (Windows path).
- `--log-level`: Set the logging level (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`). Default is `INFO`.

## Available Scripts

### Lobby & Queue Management

- **`smart-queue.py`**: Automates queuing. Restarts the queue if it exceeds a maximum time and can automatically accept matches.
  - Usage: `python smart-queue.py [-m MAX_QUEUE] [-b BREAK_TIME] [--no-accept]`
- **`social_distancing.py`**: Moves you between subteams in a lobby to avoid being next to other players.
  - Usage: `python social_distancing.py [-i INTERVAL]`
- **`trap.py`**: Invites a specific summoner to your lobby and then immediately leaves.
  - Usage: `python trap.py -t TARGET_NAME`
- **`tft-funny.py`**: Quickly changes the lobby type to TFT and leaves.
  - Usage: `python tft-funny.py [-s]` (use `-s` to try starting the queue before leaving).

### Champion Select

- **`auto-ban.py`**: Automatically bans a specified champion when you enter Champion Select.
  - Usage: `python auto-ban.py -c CHAMPION_NAME`
- **`hot-roll.py`**: In ARAM, rerolls a champion and then immediately attempts to swap back to the previous one (to help teammates or "thin" the pool).
  - Usage: `python hot-roll.py`

### Data & Debugging

- **`dump-inventory.py`**: Exports your player inventory (champions, skins, etc.).
  - Usage: `python dump-inventory.py [--format {console,json,csv}]`
- **`eog.py`**: Displays End-of-Game (EOG) statistics in a formatted table after a match.
  - Usage: `python eog.py`
- **`dbg-dump.py`**: Dumps raw LCU API data for various endpoints to a directory for debugging purposes.
- **`find_queueIDs.py`**: Brute-forces or scans a range of IDs to identify valid LCU queue IDs.

## Project Structure

- **`lol/`**: Contains modules for interacting with different LCU API domains (Lobby, Champ Select, Inventory, etc.).
- **`riot/`**: Modules for Riot-specific account APIs.
- **`ddragon/`**: Utility for fetching champion data and versions from Riot's Data Dragon.
- **`util.py`**: Shared logic for argument parsing, environment setup, and common helpers.
