<div align="center">
  
  # RaspAp stats on Waveshare E-Paper
  _Display some simple stats on a Waveshare E-Paper display._
  
  <br />

  [![Follow on Twitter](https://img.shields.io/badge/follow-%40AssistantNMS-1d9bf0?logo=twitter&style=for-the-badge)][assistantnmsTwitter]
  [![Discord](https://img.shields.io/discord/625007826913198080?style=for-the-badge)][discord]
  ![Profile views](https://komarev.com/ghpvc/?username=Khaoz-Topsy&color=green&style=for-the-badge)
  
  <br /> 
</div>

> This is based on the work from the Waveshare team's [repository][waveshareRepo]

## Prerequisites

- Make sure that `python3-pil` is installed
  - `sudo apt-get install python3-pil`
- Install everything defined in the [setup.py](./setup.py)
  - `pip install . --break-system-packages`
- Enable I2C
  - `sudo raspi-config`
  - Select Interfacing Options
  - I2C
  - Enable
  - Reboot is optional _I think_
- Setup the correct Waveshare screen for what you have
  - In my case I have the 2.13 inch screen v4, I copied the file from the Waveshare team's [repository][waveshareRepo]
  - Place the file in `lib/waveshare_epd`
- Setup environment variables
  - Copy [.env.template](./.env.template) into a file called `.env`
  - Edit the variables in the new `.env` file
- Correct permission on the [run.sh](./run.sh) file
  - `chmod +x ./run.sh

## Run

Run the whole setup with the run.sh. This should call the RaspApi endpoint running on your device and render some basic text to the Waveshare e-Paper screen.

## Updating the screen

I went with the "cheaty" option and setup a cron job

- `sudo crontab -e`
- Add `0,5,10,15,20,25,30,35,40,45,50,55  * * * * /home/<YOUR_DIRECTORY_>/run.sh`


[waveshareRepo]: https://github.com/waveshareteam/e-Paper

[raspapWeb]: https://raspap.com
[assistantnmsTwitter]: https://twitter.com/AssistantNMS?ref=KurtGithub
[discord]: https://assistantapps.com/discord?ref=KurtGithub
