IF_DEVICE_IS_APPLE_INTERNAL_KEYBOARD = [
    {
        "type": "device_if",
        "identifiers": [
            {
                "vendor_id": 1452,
                "product_id": 636,
                "is_keyboard": True,
            }
        ],
    },
]

IF_DEVICE_IS_EVOLUENT_VERTICAL_MOUSE_C = [
    {
        "type": "device_if",
        "identifiers": [
            {
                "vendor_id": 6780,
                "product_id": 405,
            }
        ],
    }
]

IF_FRONT_APPLICATION_IS_BRAVE_OR_CHROME = [
    {
        "type": "frontmost_application_if",
        "bundle_identifiers": [
            r"^com\.brave\.Browser$",
            r"^com\.google\.Chrome$",
        ],
    }
]

IF_FRONT_APPLICATION_IS_BRAVE_CHROME_FIREFOX_SAFARI_OR_EDGE = [
    {
        "type": "frontmost_application_if",
        "bundle_identifiers": [
            r"^com\.brave\.Browser$",
            r"^com\.google\.Chrome$",
            r"^org\.mozilla\.firefox$",
            r"^com\.apple\.Safari$",
            r"^com\.microsoft\.edgemac$",
        ],
    }
]

IF_FRONT_APPLICATION_IS_PYCHARM = [
    {
        "type": "frontmost_application_if",
        "bundle_identifiers": [
            r"^com\.jetbrains\.pycharm$",
            r"^com\.jetbrains\.pycharm-EAP$",
        ],
    }
]
