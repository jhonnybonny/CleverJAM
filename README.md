# CleverJAM
SDR jammer with hopping

### Automatic cleverjamming

To automate jammer , write list of frequencies that save a JSON file . This JSON file looks as follows:

```sh
$ cat jam.json  
{
    "Name1": {
        "Bandwidth": "10MHz", 
        "Freq": 924e5
    },
    "Name2": {
        "Bandwidth": "20MHz", 
        "Freq": 10e5
    }    
}
```

```sh
$ python3 clever.py --file jam.json -d jump_time
```

Then leverage the gain for transmission and you should observe that a lot of noise is overflowing the targeted cells with gaussian noise.

![Jamming session](https://raw.githubusercontent.com/jhonnybonny/just-pic-/main/sceererreen.jpg)

Please note that the delay between each targeted cell can be set with a provided arguments '-d' (see arguments helper). 
$ python smartjam_rpcclient.py -f cells_<generated timestamp>.json
Then leverage the gain for transmission and you should observe that a lot of noise is overflowing the targeted cells with gaussian noise.

Jamming session

Please note that the delay between each targeted cell can be set with a provided arguments '-d' (see arguments helper).
