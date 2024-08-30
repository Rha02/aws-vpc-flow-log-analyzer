# aws-vpc-flow-log-analyzer

## Installation requirements
- Python 3.x - (codebase built with 3.11)

## How to use
Place the flow logs file and the tag lookup csv table inside the `/data` folder in the root directory.

In root directory, use the following command to run the `main.py` program. Replace `<flow_logs.txt>` and `<tag_table.csv>` with the actual filepaths to the files inside the `/data` directory.
```sh
py main.py <flow_logs.txt> <tag_table.csv>
```

Example for running the app with the files already in `/data ` directory:
```sh
py main.py flow_logs.txt tag_table.csv
```

The output will be written to an `output.txt` file in the root directory.

## Assumptions made
1. The AWS VPC flow log records are of a valid (default) format and are of version 2.

2. The first line in the tag table csv is the header containing column names.

3. The primary internet protocols supported are `TCP`, `UDP`, and `ICMP`. If a protocol number in the flow log record doesn't match any of these 3 protocols, then the app will try to use python's built-in socket module to identify the internet protocol. However, there is no guarantee all other protocols are supported.