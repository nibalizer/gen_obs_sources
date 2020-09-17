gen_obs_sources
===============


Simple script to generate obs browser soruces. Useful if you're making many of them.

Note: this outputs *incomplete* raw json. You must manually copy and paste the output of this script into your OBS json configuration file (into the `scenes: [` block )and reload OBS.

### Quickstart

```
virtualen --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Edit `input.yaml` to be what you want

```
python gen.py
```

Capture output and put it into your scene collection `.json` file.


### Example

```
$ python gen.py
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "libobs.mute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "libobs.unmute": []
            },
            "id": "browser_source",
            "mixers": 255,
            "monitoring_type": 0,
            "muted": false,
            "name": "Spencer",
            "prev_ver": 419430408,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "height": 1080,
                "url": "https://obs.ninja/?view=ABCDEF&bitrate=20000&stereo&scene=1&room=someroom&label=spencer ",
                "width": 1920
            },
            "sync": 0,
            "versioned_id": "browser_source",
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "libobs.mute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "libobs.unmute": []
            },
            "id": "browser_source",
            "mixers": 255,
            "monitoring_type": 0,
            "muted": false,
            "name": "Mike",
            "prev_ver": 419430408,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "height": 1080,
                "url": "https://obs.ninja/?view=GHJIKL&bitrate=20000&stereo&scene=1&room=someroom&label=Mike ",
                "width": 1920
            },
            "sync": 0,
            "versioned_id": "browser_source",
            "volume": 1.0
        },
```
