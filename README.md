# MapReducer files for tshark
This repository contains Python scripts for running a MapReduce task on a tshark output file to enumerate the number of unique source IP addresses.

It was written for the CT6045 module at the University of Gloucestershire.

### `tshark.py`
`tshark.py` contains a script which can capture `stdout` from tshark and write it to a file specified in the global variables at the top of the script. You can configure this further by modifying the output file or the number of packets you would like tshark to detect.

### `mapper.py`
`mapper.py` contains a script which processes `stdin` (which should be the output file generated by `tshark.py`) and prints key-value pairs of `source_ip_address, count` to `stdout`, tab-delimited.

### `reducer.py`
`reducer.py` contains a script which 'reduces' the data passed to it from `stdin`. It should count every unique source IP address it finds in the original output and write its result to a given output in HDFS.

## Running this code
Then, you should ensure you have tshark installed. If you don't, you can install it by running:
```bash
sudo apt-get update
sudo apt-get install tshark
```

Start by cloning this repository to `hduser`'s `~` directory. You should be running these commands as `hduser`. You can become `hduser` by running:
```bash
su - hduser
```

And entering their password.

You *must* ensure that you allow permissions for non-sudoers to run tshark during the install process. You also need to ensure that `hduser` is added to the `wireshark` user group. Make sure you are logged in as someone who has sudo permissions, then you can do this by running:
```bash
sudo usermod -a -G wireshark hduser
```

Now, log back in as `hduser` (if you had to log out to add them to the user group) and set your working directory to this repository's project folder and execute `tshark.py`. It will write its output to a file you specify in the global variables in the script. By default it is `~/tshark-output.txt`.

You should then write the `tshark-output.txt` file to HDFS. You can do this by running:
```bash
/usr/local/bin/hadoop/hdfs dfs -mkdir -p /user/hduser/tshark
/usr/local/bin/hadoop/hdfs dfs -copyFromLocal ~/tshark-output.txt /user/hduser/tshark/tshark-output.txt
```

You need to ensure that `hadoop-straming-3.1.2.jar` is present in your `/usr/local/hadoop/bin/` directory. It is available on Moodle.

Now set your working directory to your Hadoop install (`/usr/local/hadoop/`) and run the following command:
```bash
bin/hadoop jar bin/hadoop-streaming-3.1.2.jar -file /home/hduser/tshark-mapreducer/mapper.py -mapper /home/hduser/tshark-mapreducer/mapper.py -file /home/hduser/tshark-mapreducer/reducer.py -reducer /home/hduser/tshark-mapreducer/reducer.py -input /user/hduser/tshark/tshark-output.txt -output /user/hduser/tshark-output
```

This command assumes you:
* Have started your Hadoop cluster
* Cloned this repository to `~` and did not edit the folder name.
* Have saved your tshark output file in HDFS as `/user/hduser/tshark/tshark-output.txt`
* Have `hadoop-streaming-3.1.2.jar` present in `/usr/local/hadoop/bin/`

If not, you may need to edit some of the command according to how you have set up your files.

Otherwise, everything should have been processed correctly and you should have encountered no errors. You can check the output of the MapReduce process by running:
```bash
/usr/local/hadoop/bin/hdfs dfs -cat /user/hduser/tshark-output/part-00000
```

## Credit
The majority of the code in `reducer.py` was written by Dr. Thomas Win. Some parts of the code have been adapted to allow the script to run in Python 3.6.
