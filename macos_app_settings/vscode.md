Setup:

- To use a dark version of the app icon:
    1. Download the dark version of the icon [here](https://github.com/mohouyizme/vscode-big-sur-icons).
    2. In Finder, right click the VS Code app icon > Get Info.
    3. Drag the download icon onto the app icon in the top left of the Get Info window.
- To use Source Code Pro as the terminal font, we need to use a patched version of the font (SauceCodePro Nerd Font) so that the font icons will display correctly:
    1. Download `SourceCodePro.zip` from [here](https://github.com/ryanoasis/nerd-fonts/releases) (in the assets seciton, click the link to “Show all 55 assets”).
    2. Install all versions of the font that don’t end with  “… Mono.ttf” or “… Windows Compatible.ttf”.
    3. Set the VS Code setting for “Terminal > Integrated: Font Family” to: `SauceCodePro Nerd Font`

# Extensions

`code --list-extensions`

```
alefragnani.project-manager
bierner.markdown-preview-github-styles
buenon.scratchpads
ChakrounAnas.turbo-console-log
christian-kohler.npm-intellisense
christian-kohler.path-intellisense
ctf0.macros
dbaeumer.vscode-eslint
eamodio.gitlens
esbenp.prettier-vscode
formulahendry.auto-rename-tag
formulahendry.code-runner
GitHub.copilot
hwencc.html-tag-wrapper
inu1255.easy-snippet
iocave.customize-ui
iocave.monkey-patch
jkjustjoshing.vscode-text-pastry
lacroixdavid1.vscode-format-context-menu
meganrogge.template-string-converter
mgmcdermott.vscode-language-babel
mhutchie.git-graph
ms-python.isort
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode.live-server
msjsdiag.vscode-react-native
naumovs.color-highlight
nhoizey.gremlins
patbenatar.advanced-new-file
PKief.material-icon-theme
pranaygp.vscode-css-peek
qezhu.gitlink
RapidAPI.vscode-rapidapi-client
richie5um2.vscode-sort-json
ritwickdey.LiveServer
ryuta46.multi-command
sleistner.vscode-fileutils
slevesque.vscode-multiclip
stkb.rewrap
streetsidesoftware.code-spell-checker
stringham.copy-with-imports
svipas.control-snippets
tamasfe.even-better-toml
Tyriar.sort-lines
VisualStudioExptTeam.intellicode-api-usage-examples
VisualStudioExptTeam.vscodeintellicode
wayou.vscode-todo-highlight
withfig.fig
xyz.local-history
yzhang.markdown-all-in-one
zhuangtongfa.material-theme
znck.grammarly
```

# Settings

`Code > User > settings.json`

```
{
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  },
  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "breadcrumbs.enabled": false,
  "cSpell.userWords": [
    "downleveling",
    "preact",
    "runtimes"
  ],
  "code-runner.clearPreviousOutput": true,
  "code-runner.enableAppInsights": false,
  "code-runner.saveFileBeforeRun": true,
  "code-runner.showExecutionMessage": false,
  "customizeUI.fontSizeMap": {
    "13px": "14px"
  },
  "debug.console.fontSize": 15,
  "editor.accessibilitySupport": "off",
  "editor.codeActionsOnSave": {
    "source.fixAll": true,
    "source.organizeImports": true
  },
  "editor.find.autoFindInSelection": "multiline",
  "editor.folding": false,
  "editor.fontFamily": "Source Code Pro",
  "editor.fontSize": 15,
  "editor.formatOnPaste": true,
  "editor.formatOnSave": true,
  "editor.formatOnType": true,
  "editor.guides.indentation": false,
  "editor.inlineSuggest.enabled": true,
  "editor.lineNumbers": "off",
  "editor.linkedEditing": true,
  "editor.matchBrackets": "never",
  "editor.minimap.autohide": true,
  "editor.mouseWheelScrollSensitivity": 0.5,
  "editor.renderLineHighlight": "none",
  "files.autoSave": "onFocusChange",
  "files.exclude": {
    "**/.expo": true,
    "**/.history": true,
    "**/.idea": true,
    "**/.next": true,
    "**/.vscode": true,
    "**/node_modules": true
  },
  "gitlens.currentLine.enabled": false,
  "gitlens.statusBar.enabled": false,
  "isort.args": [
    "--profile",
    "black"
  ],
  "markdown.preview.fontSize": 15,
  "material-icon-theme.activeIconPack": "react",
  "material-icon-theme.folders.theme": "none",
  "prettier.semi": false,
  "prettier.singleQuote": true,
  "prettier.trailingComma": "all",
  "projectManager.git.baseFolders": [
    "~/code/repos"
  ],
  "projectManager.git.maxDepthRecursion": 1,
  "projectManager.showParentFolderInfoOnDuplicates": true,
  "projectManager.sortList": "Recent",
  "python.analysis.autoImportCompletions": true,
  "python.formatting.blackPath": "/Users/elliotwaite/mambaforge/bin/blue",
  "python.formatting.provider": "black",
  "rewrap.autoWrap.enabled": true,
  "rewrap.wrappingColumn": 79,
  "scm.countBadge": "off",
  "scm.inputFontSize": 15,
  "search.exclude": {
    "**/yarn.lock": true
  },
  "telemetry.telemetryLevel": "off",
  "template-string-converter.autoRemoveTemplateString": true,
  "template-string-converter.convertOutermostQuotes": true,
  "terminal.integrated.cursorStyle": "line",
  "terminal.integrated.env.osx": {
    "FIG_NEW_SESSION": "1"
  },
  "terminal.integrated.fontFamily": "SauceCodePro Nerd Font",
  "terminal.integrated.fontSize": 15,
  "terminal.integrated.inheritEnv": false,
  "terminal.integrated.mouseWheelScrollSensitivity": 0.5,
  "turboConsoleLog.delimiterInsideMessage": "⏤",
  "turboConsoleLog.includeFileNameAndLineNum": false,
  "turboConsoleLog.logMessagePrefix": "🚨",
  "turboConsoleLog.quote": "'",
  "window.title": " ",
  "workbench.editor.enablePreview": false,
  "workbench.list.mouseWheelScrollSensitivity": 0.5,
  "workbench.startupEditor": "none",
  "workbench.statusBar.visible": false,
  "workbench.tree.indent": 16
}
```

# Keybindings

`Code > User > keybindings.json`

```
// Place your key bindings in this file to override the defaultsauto[]
[
    {
        "command": "editor.action.duplicateSelection",
        "key": "cmd+d"
    },
    {
        "command": "editor.action.addSelectionToNextFindMatch",
        "key": "cmd+g"
    },
    {
        "command": "cursorWordLeft",
        "key": "cmd+y",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordPartLeft",
        "key": "alt+left",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordEndRight",
        "key": "cmd+p",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordPartRight",
        "key": "alt+right",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordEndRight",
        "key": "cmd+\\",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordEndRightSelect",
        "key": "shift+cmd+p",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordEndRightSelect",
        "key": "shift+cmd+\\",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordLeftSelect",
        "key": "shift+cmd+y",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordPartLeftSelect",
        "key": "shift+alt+left",
        "when": "textInputFocus"
    },
    {
        "command": "cursorWordPartRightSelect",
        "key": "shift+alt+right",
        "when": "textInputFocus"
    },
    {
        "command": "editor.action.smartSelect.shrink",
        "key": "shift+cmd+m",
        "when": "editorTextFocus"
    },
    {
        "command": "editor.action.smartSelect.expand",
        "key": "shift+cmd+.",
        "when": "editorTextFocus"
    },
    {
        "command": "editor.action.transformToUppercase",
        "key": "cmd+u"
    },
    {
        "command": "editor.action.transformToLowercase",
        "key": "shift+cmd+u"
    },
    {
        "command": "editor.action.transformToSnakecase",
        "key": "ctrl+u"
    },
    {
        "command": "editor.action.transformToTitlecase",
        "key": "ctrl+cmd+u"
    },
    {
        "command": "editor.action.transformToKebabcase",
        "key": "ctrl+shift+u"
    },
    {
        "command": "editor.action.previousMatchFindAction",
        "key": "shift+alt+g",
        "when": "editorFocus"
    },
    {
        "command": "cursorUndo",
        "key": "shift+cmd+g",
        "when": "textInputFocus"
    },
    {
        "command": "editor.action.moveLinesUpAction",
        "key": "shift+cmd+up",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "command": "editor.action.moveLinesDownAction",
        "key": "shift+cmd+down",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "command": "workbench.action.findInFiles",
        "key": "alt+f"
    },
    {
        "command": "workbench.action.replaceInFiles",
        "key": "ctrl+f"
    },
    {
        "command": "rewrap.rewrapComment",
        "key": "shift+cmd+f",
        "when": "editorTextFocus"
    },
    {
        "command": "extension.advancedNewFile",
        "key": "cmd+n"
    },
    {
        "command": "workbench.action.showCommands",
        "key": "shift+cmd"
    },
    {
        "command": "workbench.action.showCommands",
        "key": "cmd+/"
    },
    {
        "command": "workbench.action.terminal.toggleTerminal",
        "key": "cmd+1",
        "when": "terminal.active"
    },
    {
        "command": "workbench.action.openGlobalKeybindings",
        "key": "shift+cmd+,"
    },
    {
        "command": "workbench.action.quickOpen",
        "key": "cmd+o"
    },
    {
        "command": "editor.action.revealDefinition",
        "key": "cmd+b",
        "when": "editorHasDefinitionProvider && editorTextFocus && !isInEmbeddedEditor"
    },
    {
        "command": "editor.action.inlineSuggest.trigger",
        "key": "alt+'",
        "when": "config.github.copilot.inlineSuggest.enable && editorTextFocus && !editorHasSelection && !inlineSuggestionsVisible"
    },
    {
        "command": "editor.action.inlineSuggest.commit",
        "key": "cmd+right",
        "when": "config.github.copilot.inlineSuggest.enable && editorTextFocus && !editorHasSelection && inlineSuggestionVisible"
    },
    {
        "command": "editor.action.goToReferences",
        "key": "shift+cmd+b",
        "when": "editorHasReferenceProvider && editorTextFocus && !inReferenceSearchEditor && !isInEmbeddedEditor"
    },
    {
        "command": "editor.action.commentLine",
        "key": "cmd+3",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "command": "editor.action.organizeImports",
        "key": "cmd+i",
        "when": "editorTextFocus && !editorReadonly && supportedCodeAction =~ /(\\s|^)source\\.organizeImports\\b/"
    },
    {
        "command": "editor.action.rename",
        "key": "shift+cmd+n",
        "when": "editorHasRenameProvider && editorTextFocus && !editorReadonly"
    },
    {
        "command": "code-runner.run",
        "key": "cmd+r"
    },
    {
        "command": "workbench.action.debug.start",
        "key": "alt+r",
        "when": "debuggersAvailable && debugState == 'inactive'"
    },
    {
        "command": "code-runner.stop",
        "key": "cmd+e"
    },
    {
        "command": "workbench.action.debug.stop",
        "key": "cmd+e",
        "when": "inDebugMode && !focusedSessionIsAttach"
    },
    {
        "command": "scratchpads.newScratchpad",
        "key": "alt+5"
    },
    {
        "command": "problems.action.showQuickFixes",
        "key": "cmd+5",
        "when": "problemFocus"
    },
    {
        "command": "workbench.action.terminal.quickFix",
        "key": "cmd+5",
        "when": "terminalFocus && terminalProcessSupported"
    },
    {
        "command": "editor.action.quickFix",
        "key": "cmd+5",
        "when": "editorHasCodeActionsProvider && editorTextFocus && !editorReadonly"
    },
    {
        "command": "editor.action.deleteLines",
        "key": "cmd+backspace",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "command": "notebook.formatCell",
        "key": "shift+cmd+f",
        "when": "editorHasDocumentFormattingProvider && editorTextFocus && inCompositeEditor && notebookEditable && !editorReadonly && activeEditor == 'workbench.editor.notebook'"
    },
    {
        "command": "notebook.format",
        "key": "shift+cmd+f",
        "when": "notebookEditable && !editorTextFocus && activeEditor == 'workbench.editor.notebook'"
    },
    {
        "command": "extension.wrapTag",
        "key": "cmd+2",
        "when": "editorTextFocus"
    },
    {
        "command": "workbench.action.toggleStatusbarVisibility",
        "key": "alt+s"
    },
    {
        "command": "toggleSuggestionDetails",
        "key": "cmd+space",
        "when": "suggestWidgetVisible && textInputFocus"
    },
    {
        "command": "editor.action.triggerSuggest",
        "key": "cmd+space",
        "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly"
    },
    {
        "args": {
            "sequence": [
                "workbench.view.explorer",
                "workbench.action.focusActiveEditorGroup"
            ]
        },
        "command": "extension.multiCommand.execute",
        "key": "escape",
        "when": "focusedView == 'workbench.view.search' || focusedView == 'workbench.scm' || focusedView == 'workbench.debug.welcome'"
    },
    {
        "command": "workbench.action.navigateBack",
        "key": "cmd+[",
        "when": "canNavigateBack"
    },
    {
        "command": "workbench.action.navigateForward",
        "key": "cmd+]",
        "when": "canNavigateForward"
    },
    {
        "command": "turboConsoleLog.displayLogMessage",
        "key": "cmd+l"
    },
    {
        "command": "turboConsoleLog.deleteAllLogMessages",
        "key": "shift+cmd+l"
    },
    {
        "command": "turboConsoleLog.commentAllLogMessages",
        "key": "ctrl+l"
    },
    {
        "command": "turboConsoleLog.uncommentAllLogMessages",
        "key": "ctrl+shift+l"
    },
    {
        "command": "workbench.view.scm",
        "key": "cmd+k",
        "when": "workbench.scm.active"
    },
    {
        "command": "workbench.view.debug",
        "key": "shift+cmd+r",
        "when": "viewContainer.workbench.view.debug.enabled"
    },
    {
        "command": "workbench.action.toggleActivityBarVisibility",
        "key": "alt+a"
    },
    {
        "command": "projectManager.listProjectsNewWindow",
        "key": "cmd+p"
    },
    {
        "command": "editor.action.triggerParameterHints",
        "key": "cmd+i",
        "when": "editorHasSignatureHelpProvider && editorTextFocus"
    },
    {
        "command": "explorer.newFile",
        "key": "cmd+t"
    },
    {
        "command": "github.copilot.generate",
        "key": "shift+cmd+space",
        "when": "editorTextFocus && github.copilot.activated"
    },
    {
        "command": "editor.action.selectAllMatches",
        "key": "cmd+enter",
        "when": "editorFocus && findWidgetVisible"
    },
    {
        "command": "editor.action.moveSelectionToNextFindMatch",
        "key": "alt+cmd+g",
        "when": "editorFocus"
    },
    {
        "command": "editor.action.selectHighlights",
        "key": "alt+g",
        "when": "editorFocus"
    },
    {
        "command": "toggleSearchEditorCaseSensitive",
        "key": "shift+cmd+a",
        "when": "inSearchEditor && searchInputBoxFocus"
    },
    {
        "command": "workbench.action.terminal.toggleFindCaseSensitive",
        "key": "shift+cmd+a",
        "when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
    },
    {
        "command": "toggleFindCaseSensitive",
        "key": "shift+cmd+a",
        "when": "editorFocus"
    },
    {
        "command": "editor.action.toggleWordWrap",
        "key": "alt+w"
    },
    {
        "command": "editor.action.showHover",
        "key": "shift+cmd+i",
        "when": "editorTextFocus"
    },
    {
        "command": "editor.debug.action.showDebugHover",
        "key": "shift+cmd+i",
        "when": "editorTextFocus && inDebugMode"
    },
    {
        "command": "workbench.action.showTreeHover",
        "key": "shift+cmd+i",
        "when": "customTreeView && listFocus && !inputFocus"
    },
    {
        "command": "editor.action.peekDefinition",
        "key": "ctrl+b",
        "when": "editorHasDefinitionProvider && editorTextFocus && !inReferenceSearchEditor && !isInEmbeddedEditor"
    },
    {
        "command": "editor.action.revealDefinitionAside",
        "key": "alt+b",
        "when": "editorHasDefinitionProvider && editorTextFocus && !isInEmbeddedEditor"
    },
    {
        "command": "editor.action.inPlaceReplace.up",
        "key": "ctrl+i",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "command": "-editor.action.inPlaceReplace.up",
        "key": "shift+cmd+,",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "command": "editor.action.inPlaceReplace.down",
        "key": "ctrl+k",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "command": "workbench.action.openSnippets",
        "key": "ctrl+,"
    },
    {
        "command": "editor.action.insertCursorBelow",
        "key": "alt+down",
        "when": "editorTextFocus"
    },
    {
        "command": "editor.action.insertCursorAbove",
        "key": "alt+up",
        "when": "editorTextFocus"
    },
    {
        "command": "workbench.action.quickOpenPreviousRecentlyUsedEditorInGroup",
        "key": "alt+tab",
        "when": "!activeEditorGroupEmpty"
    },
    {
        "command": "workbench.action.quickOpenSelectNext",
        "key": "alt+tab",
        "when": "inQuickOpen"
    },
    {
        "command": "workbench.action.quickOpenSelectPrevious",
        "key": "shift+alt+tab",
        "when": "inQuickOpen"
    }
]
```

TypeScript Snippets

```
{
  "c -> console.log()": {
    "prefix": "c",
    "description": "",
    "body": [
      "console.log($0)"
    ]
  },
  "cs -> const styles = StyleSheet.create({": {
    "prefix": "cs",
    "description": "",
    "body": [
      "const styles = StyleSheet.create({",
      "  $1: {",
      "    $0,",
      "  },",
      "})",
      ""
    ]
  },
  "cst -> const themedStyles = ThemedStyleSheet.create((theme) => ({": {
    "prefix": "cst",
    "description": "",
    "body": [
      "const themedStyles = ThemedStyleSheet.create((theme) => ({",
      "  $1: {",
      "    $0,",
      "  },",
      "}))",
      ""
    ]
  },
  "ex -> export function $1() {": {
    "prefix": "ex",
    "description": "",
    "body": [
      "export function $1() {",
      "  $0",
      "}",
      ""
    ]
  },
  "st -> const styles = ThemedStyleSheet.useStyles(themedStyles)": {
    "prefix": "st",
    "description": "",
    "body": [
      "const styles = ThemedStyleSheet.useStyles(themedStyles)",
    ]
  },
  "sty -> style={styles.$0}": {
    "prefix": "sty",
    "description": "",
    "body": [
      "style={styles.$0}"
    ]
  },
  "th -> const theme = useTheme()": {
    "prefix": "th",
    "description": "",
    "body": [
      "const theme = useTheme()",
    ]
  },
  "ts -> const themedStyles = ThemedStyleSheet.create((theme) => ({": {
    "prefix": "ts",
    "description": "",
    "body": [
      "const themedStyles = ThemedStyleSheet.create((theme) => ({"
    ]
  }
}
```
