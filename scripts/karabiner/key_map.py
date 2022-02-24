"""A list of all available key names.

The keys below are ordered to stay in sync with:
https://github.com/pqrs-org/Karabiner-Elements/blob/main/src/apps/PreferencesWindow/Resources/simple_modifications.json
(This file was last compared with that file on Feb 23, 2022.)

When both the key and the value are strings, the key is just a shorhand for
that value, so either the key string or the value string can be used.

The commented out key names are for keys that don't have a shorthand
alternative. For exmaple, 'caps_lock' doesn't have a shorthand, so it can be
used as-is by just using the string 'caps_lock'.

All string values in the key map are for key codes.
For example, this line:
  'ctrl': 'left_control',
... is equivalent to this line:
  'ctrl': {'key_code': 'left_control'},

Some keys have "(from only)" or "(to only)" mentioned after them.
"(from only)" means that the key can be mapped from but not to.
"(to only)" means that the key can be mapped to but not from.
"""

KEY_MAP = {
    # ------------------------------------------------------------------------
    # MODIFIER KEYS:
    # caps_lock
    'ctrl': 'left_control',
    'shift': 'left_shift',
    'alt': 'left_option',
    'cmd': 'left_command',
    'l_ctrl': 'left_control',
    'l_shift': 'left_shift',
    'l_alt': 'left_option',
    'l_cmd': 'left_command',
    'r_ctr': 'right_control',
    'r_shift': 'right_shift',
    'r_alt': 'right_option',
    'r_cmd': 'right_command',
    'apple_fn': {
        'apple_vendor_top_case_key_code': 'keyboard_fn'
    },  # Can also use 'fn' (listed below).
    # ------------------------------------------------------------------------
    # CONTROLS AND SYMBOLS:
    'enter': 'return_or_enter',  # (Note: 'return' is reserved below for a different key)
    'esc': 'escape',
    'delete': 'delete_or_backspace',
    'backspace': 'delete_or_backspace',
    # delete_forward
    # tab
    'space': 'spacebar',
    '-': 'hyphen',
    '=': 'equal_sign',
    '[': 'open_bracket',
    ']': 'close_bracket',
    '\\': 'backslash',
    '£': 'non_us_pound',
    ';': 'semicolon',
    "'": 'quote',
    '`': 'grave_accent_and_tilde',
    ',': 'comma',
    '.': 'period',
    '/': 'slash',
    '§': 'non_us_backslash',
    # ------------------------------------------------------------------------
    # ARROW KEYS:
    'up': 'up_arrow',
    'down': 'down_arrow',
    'left': 'left_arrow',
    'right': 'right_arrow',
    # page_up
    # page_down
    # home
    # end
    # ------------------------------------------------------------------------
    # LETTER KEYS:
    # a
    # b
    # c
    # d
    # e
    # f
    # g
    # h
    # i
    # j
    # k
    # l
    # m
    # n
    # o
    # p
    # q
    # r
    # s
    # t
    # u
    # v
    # w
    # x
    # y
    # z
    # ------------------------------------------------------------------------
    # NUMBER KEYS:
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 0
    # ------------------------------------------------------------------------
    # FUNCTION KEYS:
    # f1
    # f2
    # f3
    # f4
    # f5
    # f6
    # f7
    # f8
    # f9
    # f10
    # f11
    # f12
    # f13
    # f14
    # f15
    # f16
    # f17
    # f18
    # f19
    # f20
    # f21 (from only)
    # f22 (from only)
    # f23 (from only)
    # f24 (from only)
    # ------------------------------------------------------------------------
    # MEDIA CONTROLS:
    'display_brightness_down': {'consumer_key_code': 'display_brightness_decrement'},  # (to only)
    'display_brightness_up': {'consumer_key_code': 'display_brightness_increment'},  # (to only)
    'apple_mission_control': {
        'apple_vendor_keyboard_key_code': 'mission_control'
    },  # (to only) Can also use 'mission_control' (listed below).
    'spotlight': {'apple_vendor_keyboard_key_code': 'spotlight'},  # (to only)
    'dictation': {'consumer_key_code': 'dictation'},  # (to only)
    'apple_launchpad': {
        'apple_vendor_keyboard_key_code': 'launchpad'
    },  # (to only) Can also use 'launchpad' (listed below).
    'apple_dashboard': {
        'apple_vendor_keyboard_key_code': 'dashboard'
    },  # (to only) Can also use 'dashboard' (listed below).
    'illumination_down': {'apple_vendor_top_case_key_code': 'illumination_down'},  # (to only)
    'illumination_up': {'apple_vendor_top_case_key_code': 'illumination_up'},  # (to only)
    'consumer_rewind': {'consumer_key_code': 'rewind'},  # Can also use 'rewind' (listed below).
    'play_or_pause': {'consumer_key_code': 'play_or_pause'},
    'fast_forward': {'consumer_key_code': 'fast_forward'},
    'consoumer_mute': {'consumer_key_code': 'mute'},  # Can also use 'mute' (listed below).
    'consumer_volume_decrement': {
        'consumer_key_code': 'volume_decrement'
    },  # Can also use 'volume_decrement' (listed below).
    'consumer_volume_increment': {
        'consumer_key_code': 'volume_increment'
    },  # Can also use 'volume_increment' (listed below).
    'menu': {'consumer_key_code': 'menu'},  # (from only) Touch ID on Magic Keyboard.
    'al_terminal_lock_or_screensaver': {
        'consumer_key_code': 'al_terminal_lock_or_screensaver'
    },  # Lock key on Magic Keyboard without Touch ID.
    'eject': {'consumer_key_code': 'eject'},
    'brightness_down': {'apple_vendor_keyboard_key_code': 'brightness_down'},  # (to only)
    'brightness_up': {'apple_vendor_keyboard_key_code': 'brightness_up'},  # (to only)
    'brightness_down_2': {'apple_vendor_top_case_key_code': 'brightness_down'},  # (to only)
    'brightness_up_2': {'apple_vendor_top_case_key_code': 'brightness_up'},  # (to only)
    'scan_previous_track': {'consumer_key_code': 'scan_previous_track'},
    'scan_next_track': {'consumer_key_code': 'scan_next_track'},
    # ------------------------------------------------------------------------
    # KEYPAD KEYS:
    # keypad_num_lock
    # keypad_slash
    # keypad_asterisk
    # keypad_hyphen
    # keypad_plus
    # keypad_enter
    # keypad_
    # keypad_2
    # keypad_3
    # keypad_4
    # keypad_5
    # keypad_6
    # keypad_7
    # keypad_8
    # keypad_9
    # keypad_0
    # keypad_period
    # keypad_equal_sign
    # keypad_comma
    # ------------------------------------------------------------------------
    # VIRTUAL KEYS:
    'none': 'vk_none',  # (to only). To disable a key, map it to this key.
    # ------------------------------------------------------------------------
    # KEYS IN PC KEYBOARDS:
    # print_screen
    # scroll_lock
    # pause
    # insert
    # application
    # help
    # power
    # execute (from only)
    # menu (from only)
    # select (from only)
    # stop (from only)
    # again (from only)
    # undo (from only)
    # cut (from only)
    # copy (from only)
    # paste (from only)
    # find (from only)
    # ------------------------------------------------------------------------
    # INTERNATIONAL KEYS:
    # international1
    # international2 (from only)
    # international3
    # international4 (from only)
    # international5 (from only)
    # international6 (from only)
    # international7 (from only)
    # international8 (from only)
    # international9 (from only)
    # lang1
    # lang2
    # lang3 (from only)
    # lang4 (from only)
    # lang5 (from only)
    # lang6 (from only)
    # lang7 (from only)
    # lang8 (from only)
    # lang9 (from only)
    # ------------------------------------------------------------------------
    # JAPANESE:
    # japanese_eisuu (英数キー)
    # japanese_kana (かなキー)
    # japanese_pc_nfer (PCキーボードの無変換キー, from only)
    # japanese_pc_xfer (PCキーボードの変換キー, from only)
    # japanese_pc_katakana (PCキーボードのかなキー, from only)
    # ------------------------------------------------------------------------
    # MOUSE BUTTONS:
    'button1': {'pointing_button': 'button1'},  # (to only)
    'button2': {'pointing_button': 'button2'},
    'button3': {'pointing_button': 'button3'},
    'button4': {'pointing_button': 'button4'},
    'button5': {'pointing_button': 'button5'},
    'button6': {'pointing_button': 'button6'},
    'button7': {'pointing_button': 'button7'},
    'button8': {'pointing_button': 'button8'},
    'button9': {'pointing_button': 'button9'},
    'button10': {'pointing_button': 'button10'},
    'button11': {'pointing_button': 'button11'},
    'button12': {'pointing_button': 'button12'},
    'button13': {'pointing_button': 'button13'},
    'button14': {'pointing_button': 'button14'},
    'button15': {'pointing_button': 'button15'},
    'button16': {'pointing_button': 'button16'},
    'button17': {'pointing_button': 'button17'},
    'button18': {'pointing_button': 'button18'},
    'button19': {'pointing_button': 'button19'},
    'button20': {'pointing_button': 'button20'},
    'button21': {'pointing_button': 'button21'},
    'button22': {'pointing_button': 'button22'},
    'button23': {'pointing_button': 'button23'},
    'button24': {'pointing_button': 'button24'},
    'button25': {'pointing_button': 'button25'},
    'button26': {'pointing_button': 'button26'},
    'button27': {'pointing_button': 'button27'},
    'button28': {'pointing_button': 'button28'},
    'button29': {'pointing_button': 'button29'},
    'button30': {'pointing_button': 'button30'},
    'button31': {'pointing_button': 'button31'},
    'button32': {'pointing_button': 'button32'},
    # ------------------------------------------------------------------------
    # MOUSE KEYS:
    'mouse_up': {'mouse_key': {'y': -1536}},  # (to only)
    'mouse_up_fast': {'mouse_key': {'y': -3072}},  # (to only)
    'mouse_up_slow': {'mouse_key': {'y': -768}},  # (to only)
    'mouse_down': {'mouse_key': {'y': 1536}},  # (to only)
    'mouse_down_fast': {'mouse_key': {'y': 3072}},  # (to only)
    'mouse_down_slow': {'mouse_key': {'y': 768}},  # (to only)
    'mouse_left': {'mouse_key': {'x': -1536}},  # (to only)
    'mouse_left_fast': {'mouse_key': {'x': -3072}},  # (to only)
    'mouse_left_slow': {'mouse_key': {'x': -768}},  # (to only)
    'mouse_right': {'mouse_key': {'x': 1536}},  # (to only)
    'mouse_right_fast': {'mouse_key': {'x': 3072}},  # (to only)
    'mouse_right_slow': {'mouse_key': {'x': 768}},  # (to only)
    'scroll_up': {'mouse_key': {'vertical_wheel': -32}},  # (to only)
    'scroll_up_fast': {'mouse_key': {'vertical_wheel': -64}},  # (to only)
    'scroll_up_slow': {'mouse_key': {'vertical_wheel': -16}},  # (to only)
    'scroll_down': {'mouse_key': {'vertical_wheel': 32}},  # (to only)
    'scroll_down_fast': {'mouse_key': {'vertical_wheel': 64}},  # (to only)
    'scroll_down_slow': {'mouse_key': {'vertical_wheel': 16}},  # (to only)
    'scroll_left': {'mouse_key': {'horizontal_wheel': 32}},  # (to only)
    'scroll_left_fast': {'mouse_key': {'horizontal_wheel': 64}},  # (to only)
    'scroll_left_slow': {'mouse_key': {'horizontal_wheel': 16}},  # (to only)
    'scroll_right': {'mouse_key': {'horizontal_wheel': -32}},  # (to only)
    'scroll_right_fast': {'mouse_key': {'horizontal_wheel': -64}},  # (to only)
    'scroll_right_slow': {'mouse_key': {'horizontal_wheel': -16}},  # (to only)
    'speed_multiplier_double': {'mouse_key': {'speed_multiplier': 2.0}},  # (to only)
    'speed_multiplier_half': {'mouse_key': {'speed_multiplier': 0.5}},  # (to only)
    # ------------------------------------------------------------------------
    # STICKY MODIFIER KEYS:
    'sticky_left_control': [
        {'sticky_modifier': {'left_control': 'toggle'}},
        {'key_code': 'left_control'},
    ],  # (to only)
    'sticky_left_shift': [
        {'sticky_modifier': {'left_shift': 'toggle'}},
        {'key_code': 'left_shift'},
    ],  # (to only)
    'sticky_left_option': [
        {'sticky_modifier': {'left_option': 'toggle'}},
        {'key_code': 'left_option'},
    ],  # (to only)
    'sticky_left_command': [
        {'sticky_modifier': {'left_command': 'toggle'}},
        {'key_code': 'left_command'},
    ],  # (to only)
    'sticky_right_control': [
        {'sticky_modifier': {'right_control': 'toggle'}},
        {'key_code': 'right_control'},
    ],  # (to only)
    'sticky_right_shift': [
        {'sticky_modifier': {'right_shift': 'toggle'}},
        {'key_code': 'right_shift'},
    ],  # (to only)
    'sticky_right_option': [
        {'sticky_modifier': {'right_option': 'toggle'}},
        {'key_code': 'right_option'},
    ],
    'sticky_right_command': [
        {'sticky_modifier': {'right_command': 'toggle'}},
        {'key_code': 'right_command'},
    ],  # (to only)
    'sticky_fn': [
        {'sticky_modifier': {'fn': 'toggle'}},
        {'key_code': 'fn'},
    ],  # (to only)
    'sticky_left_control_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'left_control': 'toggle'}
    },  # (to only)
    'sticky_left_shift_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'left_shift': 'toggle'}
    },  # (to only)
    'sticky_left_option_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'left_option': 'toggle'}
    },  # (to only)
    'sticky_left_command_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'left_command': 'toggle'}
    },  # (to only)
    'sticky_right_control_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'right_control': 'toggle'}
    },  # (to only)
    'sticky_right_shift_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'right_shift': 'toggle'}
    },  # (to only)
    'sticky_right_option_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'right_option': 'toggle'}
    },  # (to only)
    'sticky_right_command_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'right_command': 'toggle'}
    },  # (to only)
    'sticky_fn_pressing_and_holding_down_is_disabled': {
        'sticky_modifier': {'fn': 'toggle'}
    },  # (to only)
    # ------------------------------------------------------------------------
    # SOFTWARE FUNCTION:
    'cgevent_double_click_left_button': {
        'software_function': {'cg_event_double_click': {'button': 0}}
    },  # (to only)
    'cgevent_double_click_right_button': {
        'software_function': {'cg_event_double_click': {'button': 1}}
    },  # (to only)
    'cgevent_double_click_center_button': {
        'software_function': {'cg_event_double_click': {'button': 2}}
    },  # (to only)
    'set_mouse_cursor_position_to_x0_y0_of_the_first_screen': {
        'software_function': {'set_mouse_cursor_position': {'x': 0, 'y': 0, 'screen': 0}}
    },  # (to only)
    'set_mouse_cursor_position_to_the_center_of_the_first_screen': {
        'software_function': {'set_mouse_cursor_position': {'x': '50%', 'y': '50%', 'screen': 0}}
    },  # (to only)
    'set_mouse_cursor_position_to_x0_y0_of_the_second_screen': {
        'software_function': {'set_mouse_cursor_position': {'x': 0, 'y': 0, 'screen': 1}}
    },  # (to only)
    'set_mouse_cursor_position_to_the_center_of_the_second_screen': {
        'software_function': {'set_mouse_cursor_position': {'x': '50%', 'y': '50%', 'screen': 1}}
    },  # (to only)
    'sleep': {'software_function': {'iokit_power_management_sleep_system': {}}},  # (to only)
    # ------------------------------------------------------------------------
    # APPLICATION LAUNCH KEYS:
    'al_word_processor': {'consumer_key_code': 'al_word_processor'},
    'al_text_editor': {'consumer_key_code': 'al_text_editor'},
    'al_spreadsheet': {'consumer_key_code': 'al_spreadsheet'},
    'al_graphics_editor': {'consumer_key_code': 'al_graphics_editor'},  # (from only)
    'al_presentation_app': {'consumer_key_code': 'al_presentation_app'},
    'al_database_app': {'consumer_key_code': 'al_database_app'},  # (from only)
    'al_email_reader': {'consumer_key_code': 'al_email_reader'},
    'al_newsreader': {'consumer_key_code': 'al_newsreader'},  # (from only)
    'al_voicemail': {'consumer_key_code': 'al_voicemail'},  # (from only)
    'al_contacts_or_address_book': {
        'consumer_key_code': 'al_contacts_or_address_book'
    },  # (from only)
    'al_calendar_or_schedule': {'consumer_key_code': 'al_Calendar_Or_Schedule'},  # (from only)
    'al_task_or_project_manager': {
        'consumer_key_code': 'al_task_or_project_manager'
    },  # (from only)
    'al_log_or_journal_or_timecard': {
        'consumer_key_code': 'al_log_or_journal_or_timecard'
    },  # (from only)
    'al_checkbook_or_finance': {'consumer_key_code': 'al_checkbook_or_finance'},  # (from only)
    'al_calculator': {'consumer_key_code': 'al_calculator'},
    'al_a_or_v_capture_or_playback': {
        'consumer_key_code': 'al_a_or_v_capture_or_playback'
    },  # (from only)
    'al_local_machine_browser': {'consumer_key_code': 'al_local_machine_browser'},
    'al_lan_or_wan_browser': {'consumer_key_code': 'al_lan_or_wan_browser'},  # (from only)
    'al_internet_browser': {'consumer_key_code': 'al_internet_browser'},
    'al_remote_networking_or_isp_connect': {
        'consumer_key_code': 'al_remote_networking_or_isp_connect'
    },  # (from only)
    'al_network_conference': {'consumer_key_code': 'al_network_conference'},  # (from only)
    'al_network_chat': {'consumer_key_code': 'al_network_chat'},  # (from only)
    'al_telephony_or_dialer': {'consumer_key_code': 'al_telephony_or_dialer'},  # (from only)
    'al_logon': {'consumer_key_code': 'al_logon'},  # (from only)
    'al_logoff': {'consumer_key_code': 'al_logoff'},  # (from only)
    'al_logon_or_logoff': {'consumer_key_code': 'al_logon_or_logoff'},  # (from only)
    'al_control_panel': {'consumer_key_code': 'al_control_panel'},  # (from only)
    'al_command_line_processor_or_run': {
        'consumer_key_code': 'al_command_line_processor_or_run'
    },  # (from only)
    'al_process_or_task_manager': {
        'consumer_key_code': 'al_process_or_task_manager'
    },  # (from only)
    'al_select_task_or_application': {
        'consumer_key_code': 'al_select_task_or_application'
    },  # (from only)
    'al_next_task_or_application': {
        'consumer_key_code': 'al_next_task_or_application'
    },  # (from only)
    'al_previous_task_or_application': {
        'consumer_key_code': 'al_previous_task_or_application'
    },  # (from only)
    'al_preemptive_halt_task_or_application': {
        'consumer_key_code': 'al_preemptive_halt_task_or_application'
    },  # (from only)
    'al_integrated_help_center': {'consumer_key_code': 'al_integrated_help_center'},  # (from only)
    'al_documents': {'consumer_key_code': 'al_documents'},  # (from only)
    'al_thesaurus': {'consumer_key_code': 'al_thesaurus'},  # (from only)
    'al_dictionary': {'consumer_key_code': 'al_dictionary'},
    'al_desktop': {'consumer_key_code': 'al_desktop'},  # (from only)
    'al_spell_check': {'consumer_key_code': 'al_spell_check'},  # (from only)
    'al_grammer_check': {'consumer_key_code': 'al_grammer_check'},  # (from only)
    'al_wireless_status': {'consumer_key_code': 'al_wireless_status'},  # (from only)
    'al_keyboard_layout': {'consumer_key_code': 'al_keyboard_layout'},  # (from only)
    'al_virus_protection': {'consumer_key_code': 'al_virus_protection'},  # (from only)
    'al_encryption': {'consumer_key_code': 'al_encryption'},  # (from only)
    'al_screen_saver': {'consumer_key_code': 'al_screen_saver'},  # (from only)
    'al_alarms': {'consumer_key_code': 'al_alarms'},  # (from only)
    'al_clock': {'consumer_key_code': 'al_clock'},  # (from only)
    'al_file_browser': {'consumer_key_code': 'al_file_browser'},  # (from only)
    'al_power_status': {'consumer_key_code': 'al_power_status'},  # (from only)
    'al_image_browser': {'consumer_key_code': 'al_image_browser'},  # (from only)
    'al_audio_browser': {'consumer_key_code': 'al_audio_browser'},  # (from only)
    'al_movie_browser': {'consumer_key_code': 'al_movie_browser'},  # (from only)
    'al_digital_rights_manager': {'consumer_key_code': 'al_digital_rights_manager'},  # (from only)
    'al_digital_wallet': {'consumer_key_code': 'al_digital_wallet'},  # (from only)
    'al_instant_messaging': {'consumer_key_code': 'al_instant_messaging'},  # (from only)
    'al_oem_feature_browser': {'consumer_key_code': 'al_oem_feature_browser'},  # (from only)
    'al_oem_help': {'consumer_key_code': 'al_oem_help'},  # (from only)
    'al_online_community': {'consumer_key_code': 'al_online_community'},  # (from only)
    'al_entertainment_content_browser': {
        'consumer_key_code': 'al_entertainment_content_browser'
    },  # (from only)
    'al_online_shopping_browswer': {
        'consumer_key_code': 'al_online_shopping_browswer'
    },  # (from only)
    'al_smart_card_information_or_help': {
        'consumer_key_code': 'al_smart_card_information_or_help'
    },  # (from only)
    'al_market_monitor_or_finance_browser': {
        'consumer_key_code': 'al_market_monitor_or_finance_browser'
    },  # (from only)
    'al_customized_corporate_news_browser': {
        'consumer_key_code': 'al_customized_corporate_news_browser'
    },  # (from only)
    'al_online_activity_browswer': {
        'consumer_key_code': 'al_online_activity_browswer'
    },  # (from only)
    'al_research_or_search_browswer': {
        'consumer_key_code': 'al_research_or_search_browswer'
    },  # (from only)
    'al_audio_player': {'consumer_key_code': 'al_audio_player'},  # (from only)
    'al_message_status': {'consumer_key_code': 'al_message_status'},  # (from only)
    'al_contact_sync': {'consumer_key_code': 'al_contact_sync'},  # (from only)
    'al_navigation': {'consumer_key_code': 'al_navigation'},  # (from only)
    'al_contextaware_desktop_assistant': {
        'consumer_key_code': 'al_contextaware_desktop_assistant'
    },  # (from only)
    # ------------------------------------------------------------------------
    # GENERIC GUI APPLICATION CONTROL KEYS:
    'ac_home': {'consumer_key_code': 'ac_home'},
    'ac_back': {'consumer_key_code': 'ac_back'},
    'ac_forward': {'consumer_key_code': 'ac_forward'},
    'ac_refresh': {'consumer_key_code': 'ac_refresh'},
    'ac_bookmarks': {'consumer_key_code': 'ac_bookmarks'},
    # ------------------------------------------------------------------------
    # OTHERS:
    # keypad_equal_sign_as400 (to only)
    # locking_caps_lock (to only)
    # locking_num_lock (to only)
    # locking_scroll_lock (to only)
    # alternate_erase (to only)
    # sys_req_or_attention (to only)
    # cancel (to only)
    # clear (to only)
    # prior (to only)
    # return (to only, a rarely used return key (HID usage code: 0x9e))
    # separator (to only)
    # out (to only)
    # oper (to only)
    # clear_or_again (to only)
    # cr_sel_or_props (to only)
    # ex_sel (to only)
    # left_alt (alias for 'left_option')
    # left_gui (alias for 'left_command')
    # right_alt (alias for 'right_option')
    # right_gui (alias for 'right_command')
    # vk_consumer_brightness_down (to only, alias for 'display_brightness_decrement')
    # vk_consumer_brightness_up (to only, alias for 'display_brightness_increment')
    # vk_mission_control (to only, alias for 'mission_control')
    # vk_launchpad (to only, alias for 'launchpad')
    # vk_dashboard (to only, alias for 'dashboard')
    # vk_consumer_illumination_down (to only, alias for 'illumination_decrement')
    # vk_consumer_illumination_up (to only, alias for 'illumination_increment')
    # vk_consumer_previous (to only, alias for 'rewind')
    # vk_consumer_play (to only, alias for 'play')
    # vk_consumer_next (to only, alias for 'fast_forward')
    # volume_down (alias for 'volume_decrement')
    # volume_up (alias for 'volume_increment')
    # display_brightness_decrement (to only)
    # display_brightness_increment (to only)
    # rewind (to only)
    # play_or_pause (to only)
    # fastforward (to only)
    'consumer_fastforward': {'consumer_key_code': 'fastforward'},
    # mute
    # volume_decrement
    # volume_increment
    # apple_display_brightness_decrement (to only)
    # apple_display_brightness_increment (to only)
    # dashboard (to only)
    'function': {'apple_vendor_keyboard_key_code': 'function'},  # (to only)
    # launchpad (to only)
    # mission_control (to only)
    'expose_desktop': {'apple_vendor_keyboard_key_code': 'expose_desktop'},  # (to only)
    'language': {'apple_vendor_keyboard_key_code': 'language'},  # (to only)
    # fn
    # apple_top_case_display_brightness_decrement (to only)
    # apple_top_case_display_brightness_increment (to only)
    'video_mirror': {'apple_vendor_top_case_key_code': 'video_mirror'},  # (to only)
    'illumination_toggle': {'apple_vendor_top_case_key_code': 'illumination_toggle'},  # (to only)
    # illumination_decrement (to only)
    # illumination_increment (to only)
    # ------------------------------------------------------------------------
}


def get_key(key):
    if key in KEY_MAP:
        if isinstance(KEY_MAP[key], str):
            return {'key_code': KEY_MAP[key]}

        return KEY_MAP[key]

    if isinstance(key, str):
        return {'key_code': key}

    return key
