The settings below have been exported to "./pycharm_settings.zip" in case you
want to import them.

# PyCharm

The setting below are for `PyCharm > Preferences…`, and "*also set these globally" means to also set them in `File > New Projects Setup > Preferences for New Projects…`.

## Appearance & Behavior

- Appearance
    - Theme: Cyberpunk Theme
    - Antialiasing
        - IDE: Greyscale
        - Editor: Greyscale
- Atom Material Icons Settings
    - Top level settigns:
        - [x]  Enable File Icons
        - [x]  Enable Folder Icons
        - [ ]  Monochrome Icons
        - [ ]  Enable UI Icons
        - [x]  Enable PSI Icons
        - [ ]  Hide File Icons
        - [ ]  Hide Folder Icons
        - [ ]  Hollow Folders
        - [ ]  Bigger Icons
        - Arrows Style: >
        - [x]  Custom Accent Color: #CACACA
        - [ ]  Custom themed Color
    - Associations:
        - See: https://github.com/elliotwaite/custom-atom-material-icons

## Keymap

(Note: These are only the non-default ones I added.)

- Editor Actions
    - Complete Current Statement: ⌘⏎, ⇧⏎
    - Delete to End of Previous Line: Keyboard Maestro Macro
    - Move Caret to Next Word: ⌘P
    - Move Caret to Next Word in Different “CamelHumps” Mode: ⌥**→**
    - Move Caret to Next Word with Selection in Different “CamelHumps” Mode: ⌥⇧**→**
    - Move Caret to Next Word with Selection: ⇧⌘P
    - Move Caret to Previous Word: ⌘Y
    - Move Caret to Previous Word in Different “CamelHumps” Mode: ⌥←
    - Move Caret to Previous Word with Selection in Different “CamelHumps” Mode: ⌥⇧←
    - Move Caret to Previous Word with Selection: ⇧⌘Y
    - Scroll to Bottom: ⌥Wheel down
    - Scroll to Top: ⌥Wheel up
    - Extend Selection: ⌘. and ⇧⌘.
    - Toggle Case: ⌘U
    - Shrink Selection: ⌘M and ⇧⌘M
- Main menu
    - File
        - Open…: ⌘O
    - Edit
        - Copy Paths: ⌥C
        - Find
            - Find Next / Move to Next Occurrence: ⌥G
            - Find Previous / Move to Previous Occurrence: ⌥⇧G
            - Add Selection for Next Occurrence: ⌘G
            - Unselect Occurrence: ⇧⌘G
            - Find in Files...: ⌥F
            - Replace in Files...: ⌃F
        - Copy as Image: ⇧⌘C (Code Screenshots plugin)
        - Wrap Line to Column: ⇧⌘F (Wrap to Column plugin)
    - View
        - Quick Definition: ⇧⌘B
        - Parameter Info: ⌘T
        - Active Editor
            - Soft-Wrap: ⌥W
    - Navigate
        - Navigate in File
            - Go to Declaration or Usages: ⌥⌘B
            - Go to Implementation(s): ⌘B
    - Code
        - Comment with Line Comment: ⌘3
        - Show Reformat File Dialog: ⌥⇧F
        - Optimize Imports: ⌘I
        - Move Line Down: ⇧⌘↓
        - Move Line Up: ⇧⌘↑
    - Refactor
        - Rename...: ⇧⌘N
    - Run
        - Run: ⌥R
        - Debug: ⌥⇧R
        - Edit Configurations…: ⌥⇧⌘R
        - Stop: ⌘E
    - Window
        - Editor Tabs
            - Close All Tabs: ⌥⌘W
- Tool Windows
    - Terminal: ⌘1
- Plugins
    - Terminal
        - Select All: ⌘A (leave as also used for: Main Menu > Edit > Select All)
- Other
    - Scroll
        - Scroll Page Up: ⌘Wheel up
        - Scroll Page Down: ⌘Wheel down
    - Tabs
        - Reopen Closed Tab: ⇧⌘T
    - Debug context configuration: ⇧⌘R
    - Excluded: ⌥⌘E
    - New Scratch Buffer: ⌥5
    - Not Excluded: ⌥⇧⌘E
    - Run context configuration: ⌘R
    - Show Context Actions: ⌘5
    - Show Quick Fixes: ⌘5
- Refactor
    - Move…: ⌘M

## Editor

- General
    - Auto Import
        - TypeScript / JavaScript (PyCharm Professional only)
            - [x]  Add TypeScript import automatically
                - [x]  Unambiguous imports on the fly
        - Python
            - [x]  Show auto-import tooltip
    - Breadcrumbs
        - [ ]  Show breadcrumbs
    - Code Completion
        - Parameter Info
            - [ ]  Show parameter info popup in [1000] ms
    - Code Folding
        - [ ]  Show code folding outline
        - Fold by default:
            - [ ]  (Uncheck all)
    - Console
        - [x]  Override console cycle buffer size (1024 KB): 10240
    - Editor Tabs
        - Closing Policy
            - Tab limit: 100
    - Smart Keys
        - Reformat on paste: [None]
        - Python (PyCharm Professional only)
            - [x]  Smart indent pasted lines
- Font
    - Font: Source Code Pro
    - Size: 15
- Color Scheme
    - Console Font
        - [x]  Use console font instead of the default
        - Font: SauceCodePro Nerd Font
            - To get this font, download SourceCodePro.zip from [here](https://github.com/ryanoasis/nerd-fonts/releases) (in the assets seciton, click the link to “Show all 55 assets”), then install all versions of the font that don’t end with “… Mono.ttf” or “… Windows Compatible.ttf”.
- Code Style (*also set these globally, maybe “Scheme” is the only one needed?)
    - Scheme: Elliot Waite Style (IDE) (which is based on: Default (IDE))
    - General
        - Hard wrap at: 1000
        - Visual guides: 80, 100 (or 73, 90)
    - Formatter
        - Do not format: *.py
    - Dart (Android Studio only)
        - Line length: 100
    - Python
        - Imports
            - Optimize Imports
                - [x]  Sort import statements
                    - [x]  Sort imported names in "from" imports
                    - [ ]  Sort plain and 'from' imports separately within a group
                    - [x]  Sort case-insensitively
                - Structure of “from” imports
                    - [x]  Always split imports
    - CSS / Less / Sass / SCSS / Stylus / HTML / JSON / XML / Other File Types (some are PyCharm Professional only)
        - Tabs and Indents
            - Tab size: 2
            - Indent: 2
            - Continuation indent: 4
    - HTML
        - Other
            - Generated quote marks: None
    - JavaScript and TypeScript (PyCharm Professional only, If Prettier settings change, follow the Prettier per project instructions below then *set these globally to do mimic what Pretterier does. First, apply these to JavaScript, then for TypeScript: Set from… Javascript (I think? make sure all are copied)).
        - Set from…
            - JavaScript Standard Style
        - Spaces
            - Before parentheses
                - [ ]  Function declaration parentheses
                - [ ]  In function expression
            - Other
                - [ ]  Before '*' in generator
        - Imports (need to be set in both JavaScript and Typescript)
            - [JavaScript] Use paths relative to the project, resource or sources roots [TypeScript] Use paths relative to tsconfig.json
            - Do not import exactly from:
                
                ```
                rxjs/Rx
                node_modules/**
                **/node_modules/**
                @angular/material
                @angular/material/typings/**
                jotai/ts*/**
                valtio/ts*/**
                @react-navigation/native/**
                react-native-reanimated/lib/**
                react-native-gesture-handler/lib/typescript/handlers/gestures/reanimatedWrapper/**
                @preact/signals-core/**
                @shopify/react-native-skia/src/**
                ```
                
                - Note: The original values were:
                    
                    ```
                    rxjs/Rx
                    node_modules/**
                    */node_modules/**
                    @angular/material
                    @angular/material/typings/**
                    ```
                    
            - [x]  Sort imports by members (already default?)
            - [x]  Sort imports by modules
- Inspections
    - Profile: use these same settings for both Default and Project Default
    - General
        - Duplicated code fragment [  ]
    - HTML
        - Empty tag [  ]
        - Unknown attribute [  ]
        - Unknown tag [  ]
    - JavaScript and TypeScript
        - Async code and promises
            - Result of method call returning a promise is ignored [  ]
    - Python
        - PEP 8 coding style violation
            - Ignore errors ([link to the list of error codes](https://pep8.readthedocs.io/en/latest/intro.html#error-codes))
                - E203 (whitespace before ‘:’)
                - E402 (module level import not at top of file)
                - E741 (do not use variables named ‘l’, ‘O’, or ‘I’)
                - W292 (no newline at end of file)
- Live Templates
    - Note: For all templates, set the description to be the template text, set “Expand with” to “Default (Tab)”, set “Reformat according to style”, and set the language the template is applicable to (e.g., Python or JavaScript/TypeScript).
    - user
        - **
            
            ```
            print('*' * 80)
            ```
            
        - .gitignore
            
            ```
            /.git/
            ```
            
        - ba
            
            ```
            batch(() => {
              $END$
            })
            ```
            
        - c
            
            ```
            console.log($END$)
            ```
            
        - cl
            
            ```
            class $VAR$:
                def __init__(self):
                    $END$
            ```
            
        - cs
            
            ```
            import { StyleSheet } from 'react-native'
            const styles = StyleSheet.create({
              $VAR$: {
                $END$
              },
            })
            ```
            
        - cst
            
            ```
            const themedStyles = ThemedStyleSheet.create((theme) => ({
              $VAR$: {
                $END$
              },
            }))
            ```
            
        - cur
            
            ```
            CUR_DIR = os.path.dirname(os.path.realpath(__file__))
            ```
            
        - ex
            
            ```
            export function $END$() {
              $END$
            }
            ```
            
        - in
            
            ```
            def __init__(self):
                $END$
            ```
            
        - jax
            
            ```
            import jax
            ```
            
        - jnp
            
            ```
            import jax.numpy as jnp
            ```
            
        - main
            
            ```
            def main():
                $END$
            
            if __name__ == '__main__':
                main()
            ```
            
        - np
            
            ```
            import numpy as np
            ```
            
        - pd
            
            ```
            import pandas as pd
            ```
            
        - pr
            
            ```
            print(f'{$CLIPBOARD$ = }')
            ```
            
        - py
            
            ```
            import plotly.offline as py
            import plotly.graph_objs as go
            ```
            
        - st
            
            ```
            const styles = ThemedStyleSheet.useStyles(themedStyles)
            ```
            
        - sty
            
            ```
            style={styles.$END$}
            ```
            
        - sup
            
            ```
            super().__init__()
            ```
            
        - th
            
            ```
            const theme = useTheme()
            ```
            
        - to
            
            ```
            import torch
            import torch.nn as nn
            import torch.nn.functional as 
            ```
            
        - ts
            
            ```
            const themedStyles = ThemedStyleSheet.create((theme) => ({
            ```
            
        - walk
            
            ```
            for dir_path, dir_names, filenames in os.walk($VAR$):
                for filename in filenames:
                    path = os.path.join(dir_path, filename)
                    $END$
            ```
            
        - {.
            
            ```
            {...($VAR$ && { $VAR$: $VAR$ })
            ```
            
- Inlay Hints
    - [ ]  Show hints for:
- Emmet
    - CSS (PyCharm Professional only)
        - [ ]  Enable CSS Emmet

## Plugins

- Atom Material Icons
- Code Screenshots
- Cyberpunk Theme
- Debug Theme
- GitHub Copilot
- Next.js
- Node.js
- Prettier
- Run Configurations for TypeScript
- Statistic
- String Manipulation
- Wrap to Column
- Zero Width Characters locator 2

## Version Control (*also set these globally)

Confirmation:

- When files are created: Add silently Apply to files created outside PyCharm
- When files are deleted: Remove silently

## Language & Frameworks (*also set these globally)

- JavaScript
    - Code Quality
        - ESLint
            - [x]  Run eslint –fix on save
    - Prettier
        - Prettier package: ~/.nvm/versions/node/v16.13.2/lib/node_modules/prettier
            - This requires running: npm i -g prettier
            - The version number (v16.13.2) may vary.
        - [x]  On ‘Reformat Code’ action
        - [x]  On save
        - Also per project:
            - Run: yarn add -D prettier
            - And add this to the package.json:
                - "prettier": {
                - "semi": false,
                - "singleQuote": true,
                - "trailingComma": "all"
                - }
            - While viewing the package.json file, click the “Yes” at the top right for “Use code style based on Prettier for this project?” And if you accidentally click “No”, you can press ⇧⌘A and select “Apply Prettier Code Style Rules” from the Find Action list.
- GitHub Copilot
    - Show IDE completions side-by-side
    - Color for completions: 9F9F9F
- Node.js
    - [x]  Coding assistance for Node.js (?maybe don’t need anymore)
- Rust
    - Rustfmt (*also set these globally)
        - [x]  Use rustfmt instead of the built-in formatter
        - [x]  Run rustfmt on Save

## Tools

- Actions on Save
    - [x]  Reformat code
    - [x]  (tentatively no on this one) Optimize imports
- Python Scientific (PyCharm Professional only)
    - [ ]  Show plots in tool window
- Terminal (*also set these globally)
    - Application Settings (*also set these globally)
        - Shell path: `/bin/zsh`
        - Cursor shape: Vertical
- Wrap to Column
    - Right margin override: 79
    - Plaintext filetypes: `.md,.markdown,.adoc,.asciidoc,.txt`
    - [ ]  Use minimum raggedness algorithm
- Advanced Settings
    - Find/Replace
        - Maximum number of results to show in Find in Files/Show Usages preview: 10000

Additional non-preferences settings:

- Menu bar
    - View
        - Appearance
            - [ ]  Tool Buttons (? PyCharm Professional only)
            - [ ]  Navigation Bar
- Cmd+Shift+A
    - Registry…
        - dart.server.aditional.arguments > --enable-completion-model (Android Studio only, to opt-in to the machine-learning backed code completion preview)
        - undo.documentUndoLimit > 1000
        - undo.globalUndoLimit > 100
        - dart.server.aditional.arguments > --enable-completion-model
