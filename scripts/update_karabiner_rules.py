import json
from pathlib import Path

KARABINER_CONFIG_PATH = Path.home() / '.config/karabiner/karabiner.json'

# Maps shorthand names to the actual names used in Karabiner.
# See: https://github.com/JoshuaManuel/Karabiner-Elements-Key-List
KEY_MAP = {
    'l_cmd': 'left_command',
    'l_alt': 'left_alt',
    'l_ctrl': 'left_control',
    'l_shift': 'left_shift',
    'r_cmd': 'right_command',
    'r_alt': 'right_alt',
    'r_ctr': 'right_control',
    'r_shift': 'right_shift',
    'up': 'up_arrow',
    'down': 'down_arrow',
    'left': 'left_arrow',
    'right': 'right_arrow',
    "'": 'quote',
}

# These rules will override any existing rules in the Karabiner config file.
RULES = {
    'Right Hand Cmd Key Mappings': [
        # u
        ('l_cmd', 'u', 'l_alt', 'left'),
        # i
        ('l_cmd r_shift', 'i', 'r_shift', 'up'),
        ('l_cmd l_shift', 'i', 'l_alt l_shift', 'up'),
        ('l_cmd', 'i', '', 'up'),
        ('l_alt', 'i', 'l_cmd', 'up'),
        # o
        ('l_cmd', 'o', 'l_alt', 'right'),
        # h
        ('l_cmd', 'h', 'l_cmd', 'left'),
        # j
        ('l_cmd', 'j', '', 'left'),
        # k
        ('l_cmd r_shift', 'k', 'r_shift', 'down'),
        ('l_cmd l_shift', 'k', 'l_cmd l_shift', 'down'),
        ('l_cmd', 'k', '', 'down'),
        ('l_alt', 'k', 'l_cmd', 'down'),
        # l
        ('l_cmd', 'l', '', 'right'),
        # '
        ('l_cmd', "'", 'l_cmd', 'right'),
    ],
}


def get_key(key):
    return KEY_MAP[key] if key in KEY_MAP else key


def get_rule(description, manipulators):
    return {
        'description': description,
        'manipulators': [
            {
                'from': {
                    'key_code': get_key(from_key_code),
                    'modifiers': {
                        'mandatory': [get_key(modifier) for modifier in from_modifiers.split()],
                        'optional': ['any'],
                    },
                },
                'to': [
                    {
                        'key_code': get_key(to_key_code),
                        'modifiers': [get_key(modifier) for modifier in to_modifiers.split()],
                    }
                ],
                'type': 'basic',
            }
            for (
                from_modifiers,
                from_key_code,
                to_modifiers,
                to_key_code,
            ) in manipulators
        ],
    }


def update_karabiner_rules():
    with open(KARABINER_CONFIG_PATH, "r") as f:
        karabiner_config = json.load(f)

    karabiner_config['profiles'][0]['complex_modifications']['rules'] = [
        get_rule(description, manipulators) for (description, manipulators) in RULES.items()
    ]

    with open(KARABINER_CONFIG_PATH, 'w') as f:
        json.dump(karabiner_config, f, indent=4)


if __name__ == "__main__":
    update_karabiner_rules()
