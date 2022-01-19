# Smart Watch IoT Interactive Server

This is an application that acquires your heart rate with a smartwatch, and recommends and plays back the appropriate BPM according to your heart rate.

The colored servers in the figure below are constructed.
The URLs of each repository are as follows.

- AWS server (https://github.com/ITK13201/smart-watch-iot-server)
- Raspberry Pi IoT Server (https://github.com/ITK13201/smart-watch-iot-client)
- **(This repository) Raspberry Pi Discord Server** (https://github.com/ITK13201/smart-watch-iot-interactive-server)

![system_chart](./docs/img/system_chart.png)

## Install

```shell
pip install pipenv
pipenv install --dev
```

## Usage

### Run

```shell
pipenv run start
```

### Enter the virtual environment

```shell
pipenv shell
```

### Tracking and Format "*.py" file

```shell
pipenv run watch
```

### Format changed "*.py" file

```shell
pipenv run format
```
