# Short-Link Bot

#### This repository contains a bot that takes long URLs and converts them into short links. 
#### It's a simple and efficient way to make your URLs more manageable and shareable.

## Features
+ Converts long URLs into short links
+ Easy to use 
+ Customizable and extensible

## Installation  
1. Clone the repository:\
`git clone https://github.com/it-tr1p/Short-links.git`
2. Create venv & install the dependencies:\
`poetry shell & poetry install`
3. Change the name of `.env.dist` to `.env` and set all environment variables as you need\
4. Change project name and other information in `pyproject.toml`

## Migrations
Generate alembic revision for migration with given name \
`make generate NAME=<name>` \
Apply migrations to the target database \
`make migrate`

## Roadmap
+ Add custom name for shorted links
+ Save your URLs
+ Create Web-service
