### FlibustaDailySync - A script to synchronize daily archives from Flibusta
#### Description
A script to synchronize daily archives from website Flibusta
#### Dependencies
  - lxml - pip install lxml --user (mandatory)
  - tqdm - pip install tqdm --user (mandatory)
  - urllib - pip install urllib --user (mandatory)
  - requests - pip install requests --user (mandatory)
  - argsparse - pip install argparse --user (mandatory)
#### Usage
    usage: flibusta_daily.py [-h] [-u URL] [-p PATH]

    A script to synchronize daily archives from website Flibusta

    optional arguments:
    -h, --help            show this help message and exit
    -u URL, --url URL     URL address, default: https://flibusta.is/
    -p PATH, --path PATH  The directory in which we will synchronize, default:
                            /tmp/
