# Cron parser
Parses a cron string and expands each field to show the times at which it will run

### Running 
To run:
`python cron.py "cron string"`

e.g `python cron.py "*/15 0 1,15 * 1-5 /usr/bin/find"`

Alternatively:
- Run `chmod +x cron.py` to make the script executable
- Then run using `./cron.py "*/15 0 1,15 * 1-5 /usr/bin/find"`
