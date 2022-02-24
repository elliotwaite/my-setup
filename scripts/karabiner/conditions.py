IF_IS_APPLE_INTERNAL_KEYBOARD = [
    {
        'type': 'device_if',
        'identifiers': [
            {
                'vendor_id': 1452,
                'product_id': 636,
                'is_keyboard': True,
            }
        ],
    },
]

IF_IS_EVOLUENT_VERTICAL_MOUSE_C = [
    {
        'type': 'device_if',
        'identifiers': [
            {
                'vendor_id': 6780,
                'product_id': 405,
            }
        ],
    }
]

IF_IS_BROWSER = [
    {
        'type': 'frontmost_application_if',
        'bundle_identifiers': [
            r'^com\.brave\.Browser$',
            r'^com\.google\.Chrome$',
        ],
    }
]
