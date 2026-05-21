# lol-scripts

## Setup

1. Create python environment `python -m venv .`
2. Activate python environment `./.env/activate`
3. Install dependencies `pip install -r requirements.txt`

## Use
1. Run `./.env/Scripts/activate`
2. Run a script `python {script_name}.py`. Get help by using `python {script_name}.py --help`

## Scripts

### smart-queue.py

This script automates the process of queueing for a game. It continuously monitors the queue state and restarts the queue if it exceeds a specified maximum time. Additionally, it can automatically accept a match when found unless specified otherwise.

#### Features

- **Automatic Queue Management**: Starts and restarts the queue if it exceeds the maximum queue time.
- **Match Acceptance**: Automatically accepts the match when found unless the `--no-accept` flag is used.
- **Configurable Parameters**: Allows customization maximum queue time, and break time between queue restarts.

#### Usage

##### Command Line Arguments

- `-l` or `--lockfile`: Path to the League of Legends lockfile. Default is `C:\\Riot Games\\League of Legends\\lockfile`.
- `-m` or `--max_queue`: Maximum time (in seconds) to wait in the queue before restarting. Default is 30 seconds.
- `-b` or `--break_time`: Break time (in seconds) between queue restarts. Default is 5 seconds.
- `--no-accept`: If specified, the script will not automatically accept the match when found.

#### Example Command

```sh
python smart-queue.py -l "path/to/lockfile" -m 60 -b 10 --no-accept
```

### hot-roll.py

This script automates actions during the champion select phase in aram. It reroll then immediately swap back.

#### Usage

##### Command Line Arguments

- `-l` or `--lockfile`: Path to the League of Legends lockfile. Default is `C:\\Riot Games\\League of Legends\\lockfile`.

#### Example Command

```sh
python champ-select.py -l "path/to/lockfile"
```