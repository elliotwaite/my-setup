"""A script for updating the Karabiner config file.

The below modifications will overwrite any existing modifications in the
config file at: ~/.config/karabiner/karabiner.json

Karabiner handles input events in the following order:
  1. Catch events from hardware.
  2. Apply Simple Modifications.
  3. Apply Complex Modifications.
  4. Apply Function Keys Modifications.
  5. Post events to applications via a virtual keyboard.

All three types of modifications (simple, complex, and function keys) can
be specified below.

For the full list of available key names that can be mapped from/to, see:
  ./key_map.py
"""
import json
from pathlib import Path

from apple_scripts import apple_script_shell_command, OPEN_NEW_BRAVE_TAB_APPLE_SCRIPT
from conditions import (
    IF_DEVICE_IS_APPLE_INTERNAL_KEYBOARD,
    IF_DEVICE_IS_EVOLUENT_VERTICAL_MOUSE_C,
    IF_FRONT_APPLICATION_IS_BRAVE_OR_CHROME,
)
from key_map import get_key

KARABINER_CONFIG_PATH = Path.home() / '.config/karabiner/karabiner.json'

# Simple modification are mappings from one key to another. This should be a
# list of (from_key, to_key) tuples. See "./key_map.py" for key names.
SIMPLE_MODIFICATIONS = [
    ('f3', 'f17'),
    ('f4', 'f18'),
    ('f5', 'f19'),
]

# This is the list of complex modification rules. For more info on complex
# modifications, see: https://karabiner-elements.pqrs.org/docs/json/
#
# The values in the `manipulators` list can be tuples of this type:
# (
#   from_key (a string of one or more key names),
#   from_modifiers_mandatory (optional, a string of zero or more modifier key names),
#   from_modifiers_optional (optional, a string of zero or more modifier key names, or 'any'),
#   to_key (optional, a string of zero or more key names),
#   to_modifiers (optional, a string of zero or more modifier key names),
#   conditions (optional, a `manipulator.conditions` list),
#   to_config (optional, a dict. If specified it will be merged with the last `to` dict),
# )
#
# If `from_key` specifies multiple keys, those keys will have to be pressed
# simultaneously to trigger the mapping. See:
# https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/simultaneous/
#
# If `to_key` specifies multiple keys, those keys will be pressed in order.
# For example, this will map `left_command + h` to typing out "hello":
# ('h', 'l_cmd', 'any', 'h e l l o')
#
# `conditions` can be used to only trigger the mapping if certain conditions
# are met, such as only when a certain application is being used, or only when
# a certain keyboard or mouse is being used. For the full list of options see:
# https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/
#
# `to_config` can be used to specify extra settings that will be applied to the
# key being mapped to (or to the last key being mapped to if multiple `to_key`
# keys are specified). For example, this will map `left_command + h` to typing
# out "hello", but unlike the above example, this version will prevent the "o"
# from being typed repeatedly if `left_command + h` is held:
# ('h', 'l_cmd', 'any', 'h e l l o', None, None, {'repeat': False})
#
# For more info about how `to_config` could be used, see:
# https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/
#
# For more complex manipulators, you can specify them directly without using
# the tuple format described above. The tuple format is just for convenience.

COMPLEX_MODIFICATIONS = [
    {
        'description': 'Left Cmd/Alt + Right Hand Keys -> Navigation',
        'manipulators': [
            # u
            ('u', 'l_cmd', 'any', 'left', 'alt'),
            # i
            ('i', 'l_cmd r_shift', 'any', 'up', 'shift'),
            ('i', 'l_cmd l_shift', 'any', 'up', 'alt shift'),
            ('i', 'l_cmd', 'any', 'up', ''),
            ('i', 'l_alt', 'any', 'up', 'cmd'),
            # o
            ('o', 'l_cmd', 'any', 'right', 'alt'),
            # h
            ('h', 'l_cmd', 'any', 'left', 'cmd'),
            # j
            ('j', 'l_cmd', 'any', 'left', ''),
            # k
            ('k', 'l_cmd r_shift', 'any', 'down', 'shift'),
            ('k', 'l_cmd l_shift', 'any', 'down', 'cmd shift'),
            ('k', 'l_cmd', 'any', 'down', ''),
            ('k', 'l_alt', 'any', 'down', 'cmd'),
            # l
            ('l', 'l_cmd', 'any', 'right', ''),
            # '
            ("'", 'l_cmd', 'any', 'right', 'cmd'),
        ],
    },
    {
        'description': 'Touch Bar Keyboard: Backtick -> Esc, Cmd + Backtick -> Backtick',
        'manipulators': [
            ('`', 'cmd', 'any', '`', '', IF_DEVICE_IS_APPLE_INTERNAL_KEYBOARD),
            ('`', '', 'any', 'esc', '', IF_DEVICE_IS_APPLE_INTERNAL_KEYBOARD),
        ],
    },
    {
        'description': 'Evoluent Mouse Button Swaps (2 <-> 3, 4 <-> 5)',
        'manipulators': [
            # Swap buttons 2 and 3 (middle and right click).
            ('button2', '', '', 'button3', '', IF_DEVICE_IS_EVOLUENT_VERTICAL_MOUSE_C),
            ('button3', '', 'any', 'button2', '', IF_DEVICE_IS_EVOLUENT_VERTICAL_MOUSE_C),
            # Swap buttons 4 and 5 (forward and back navigation).
            ('button4', '', 'any', 'button5', '', IF_DEVICE_IS_EVOLUENT_VERTICAL_MOUSE_C),
            ('button5', '', 'any', 'button4', '', IF_DEVICE_IS_EVOLUENT_VERTICAL_MOUSE_C),
        ],
    },
    {
        'description': 'Browser Hotkeys',
        'manipulators': [
            # Open a new Brave tab.
            ('esc', 'l_cmd', 'any', apple_script_shell_command(OPEN_NEW_BRAVE_TAB_APPLE_SCRIPT)),
            # Cmd + 1 -> Show JavaScript console (View > Developer > JavaScript Console).
            ('1', 'l_cmd', 'any', 'j', 'cmd alt', IF_FRONT_APPLICATION_IS_BRAVE_OR_CHROME),
            # Cmd + i -> Show developer tools (View > Developer > Developer Tools).
            ('i', 'r_cmd', 'any', 'i', 'cmd alt', IF_FRONT_APPLICATION_IS_BRAVE_OR_CHROME),
            # Alt + f -> Toggle full sreen mode (View > Enter Full Screen).
            ('f', 'l_alt', 'any', 'f', 'cmd ctrl', IF_FRONT_APPLICATION_IS_BRAVE_OR_CHROME),
        ],
    },
]

# Function keys modifications can be used to remap f1 - f12 to any other keys.
# This should be a list of ('f[number]', to_key) tuples.
FUNCTION_KEYS_MODIFICATIONS = [
    ('f1', 'f1'),
    ('f2', 'f2'),
    ('f3', 'f3'),
    ('f4', 'f4'),
    ('f5', 'f5'),
    ('f6', 'f6'),
    ('f7', 'f7'),
    ('f8', 'f8'),
    ('f9', 'f9'),
    ('f10', 'f10'),
    ('f11', 'f11'),
    ('f12', 'f12'),
]


def convert_modification_tuple(modification_tuple):
    from_key_code, to_key_code = modification_tuple
    return {
        'from': get_key(from_key_code),
        'to': [get_key(to_key_code)],
    }


def convert_manipulator_tuple(manipulator):
    if len(manipulator) == 4:
        manipulator = (*manipulator, None)  # Default `to_modifiers`.

    if len(manipulator) == 5:
        manipulator = (*manipulator, None)  # Default `conditions`.

    if len(manipulator) == 6:
        manipulator = (*manipulator, None)  # Default `to_config`.

    (
        from_keys,
        from_modifiers_mandatory,
        from_modifiers_optional,
        to_obj,
        to_modifiers,
        conditions,
        to_config,
    ) = manipulator

    assert from_keys and isinstance(from_keys, str), (
        f'`from_keys` was set to "{from_keys}". '
        '`from_keys` must be a string of one or more key names '
        '(see "key_map.py" for key names).',
    )
    assert not from_modifiers_mandatory or isinstance(from_modifiers_mandatory, str), (
        f'`from_modifiers_mandatory` was set to "{from_modifiers_mandatory}". '
        '`from_modifiers_mandatory` must be a string of zero or more modifier key names '
        '(see "key_map.py" for modifier key names).',
    )
    assert not from_modifiers_optional or isinstance(from_modifiers_optional, str), (
        f'`from_modifiers_optional` was set to "{from_modifiers_optional}". '
        '`from_modifiers_optional` must be "any", a string of zero or more modifier keynames '
        '(see "key_map.py" for modifier key names), or None.',
    )
    assert not to_obj or (
        isinstance(to_obj, str)
        or isinstance(to_obj, dict)
        or isinstance(to_obj, list)
        and isinstance(to_obj[0], dict)
    ), (
        f'`to_obj` was set to "{to_obj}". '
        '`to_obj` must be a string of zero or more key names '
        '(see "key_map.py" for key names), '
        'or a `manipulator.to[0]` dict, or a `manipulator.to` list of dicts, or None.'
    )
    assert not to_modifiers or isinstance(to_modifiers, str), (
        f'`to_modifiers` was set to "{to_modifiers}". '
        '`to_modifiers` must be a string of zero or more modifier key names '
        '(see "key_map.py" for modifier key names), or None.',
    )
    assert not conditions or isinstance(conditions, list) and isinstance(conditions[0], dict), (
        f'`conditions` was set to "{conditions}". '
        '`conditions` must be a list of `manipulator.conditions '
        '(see: https://karabiner-elements.pqrs.org/docs/json/'
        'complex-modifications-manipulator-definition/conditions/), or None.',
    )
    assert not to_config or isinstance(to_config, dict), (
        f'`to_config` was set to "{to_config}". '
        '`to_config` must be a string of zero or more modifier key names '
        '(see "key_map.py" for modifier key names), or None',
    )

    from_keys = [get_key(key) for key in from_keys.split()]

    if from_modifiers_mandatory:
        from_modifiers_mandatory = [
            get_key(key)['key_code'] for key in from_modifiers_mandatory.split()
        ]

    if from_modifiers_optional:
        from_modifiers_optional = [
            get_key(key)['key_code'] for key in from_modifiers_optional.split()
        ]

    if isinstance(to_obj, str):
        to_obj = [get_key(key) for key in to_obj.split()]

    if to_modifiers:
        to_modifiers = [get_key(key)['key_code'] for key in to_modifiers.split()]

    result = {
        'type': 'basic',
    }

    if conditions:
        result['conditions'] = conditions

    if len(from_keys) > 1:
        result['from'] = {'simultaneous': from_keys}
    else:
        result['from'] = from_keys[0]

    if from_modifiers_mandatory or from_modifiers_optional:
        result['from']['modifiers'] = {}
        if from_modifiers_mandatory:
            result['from']['modifiers']['mandatory'] = from_modifiers_mandatory
        if from_modifiers_optional:
            result['from']['modifiers']['optional'] = from_modifiers_optional

    if isinstance(to_obj, list):
        if to_obj:
            result['to'] = to_obj
        else:
            result['to'] = [{}]
    elif isinstance(to_obj, dict):
        result['to'] = [to_obj]

    if to_modifiers:
        result['to'][0]['modifiers'] = to_modifiers

    if to_config:
        result['to'][-1].update(to_config)

    return result


def convert_complex_modification_rule(rule):
    result = rule.copy()
    result['manipulators'] = [
        convert_manipulator_tuple(manipulator) if isinstance(manipulator, tuple) else manipulator
        for manipulator in rule['manipulators']
    ]
    return result


def update_karabiner_config():
    with open(KARABINER_CONFIG_PATH, 'r') as f:
        karabiner_config = json.load(f)

    karabiner_config['profiles'][0]['simple_modifications'] = [
        convert_modification_tuple(modification) for modification in SIMPLE_MODIFICATIONS
    ]

    karabiner_config['profiles'][0]['complex_modifications']['rules'] = [
        convert_complex_modification_rule(rule) for rule in COMPLEX_MODIFICATIONS
    ]

    karabiner_config['profiles'][0]['fn_function_keys'] = [
        convert_modification_tuple(modification) for modification in FUNCTION_KEYS_MODIFICATIONS
    ]

    with open(KARABINER_CONFIG_PATH, 'w') as f:
        json.dump(karabiner_config, f, indent=4)


if __name__ == "__main__":
    update_karabiner_config()
