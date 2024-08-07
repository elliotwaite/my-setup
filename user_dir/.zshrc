#-------------------------------------------------------------------------------
# POWERLEVEL10K
#
# We install powerlevel10k into our `~/lib` dir, instead of using the default
# parent directory of `~` that is used in their docs.
#
# To install powerlevel10k, run:
# $ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/lib/powerlevel10k
# See: https://github.com/romkatv/powerlevel10k#manual
#
# To update the powerlevel10k, run:
# $ git -C ~/lib/powerlevel10k pull
# See: https://github.com/romkatv/powerlevel10k#how-do-i-update-powerlevel10k
#
# To configure powerlevel10k, edit `~/.p10k.zsh`, or run:
# $ p10k configure
# See: https://github.com/romkatv/powerlevel10k#configuration
source ~/lib/powerlevel10k/powerlevel10k.zsh-theme
source ~/.p10k.zsh

#-------------------------------------------------------------------------------
# AUTO GENERATED BY PNPM

# pnpm
export PNPM_HOME="/Users/elliotwaite/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

#-------------------------------------------------------------------------------
# MY CUSTOM SETTINGS

# Custom key bindings:
bindkey ';9D' backward-word # Cmd + Left -> Go to beginning of line. (iTerm)
bindkey ';9C' forward-word # Cmd + Right -> Go to end of line. (iTerm)
bindkey ';4D' backward-kill-word # Alt + Shift + Left -> Delete the word to the left. (VS Code)
bindkey ';4C' kill-word # Alt + Shift + Right -> Delete the word to the right. (VS Code)
bindkey ';2D' backward-delete-char # Shift + Left -> Delete the character to the left. (VS Code)
bindkey ';2C' delete-char # Shift + Right -> Delete the character to the right. (VS Code)
bindkey ';5D' backward-kill-line # Cmd + Shift + Left -> Delete to start of line. (VS Code, custom escape sequence: "\u001b[1;5D")
bindkey ';5C' kill-line # Cmd + Shift + Right -> Delete to end of line. (VS Code, custom escape sequence "\u001b[1;5C")

# For my home dir executables:
export PATH="$PATH:$HOME/bin"

# For Cursor:
export PATH="$PATH:/Applications/Cursor.app/Contents/Resources/app/bin"

# For Pixi (requires running `pixi completion --shell zsh > ~/.zfunc/_pixi`):
export PATH="$PATH:/Users/elliotwaite/.pixi/bin"

# To install the Pixi completions, run:
# $ pixi completion --shell zsh > ~/.zfunc/_pixi
# Note: This with how we install the Ruff completions, but differs from the
# installation instructions in the Pixi docs here:
# https://prefix.dev/docs/pixi/overview#autocompletion
# We use this method instead so that we don't have to generate the completions
# each time we intialize a terminal.
#
# To install the Ruff completions, run:
# $ ruff generate-shell-completion zsh > ~/.zfunc/_ruff
# See: https://docs.astral.sh/ruff/configuration/#shell-autocompletion
#
# Then these lines enable the completions (this step is from the Ruff docs):
fpath+=~/.zfunc
autoload -Uz compinit && compinit

# For Bun:
export BUN_INSTALL="$HOME/.bun"
export PATH="$PATH:$BUN_INSTALL/bin"
[ -s "/Users/elliotwaite/.bun/_bun" ] && source "/Users/elliotwaite/.bun/_bun" # Adds completions.

# For Docker:
export PATH="$PATH:$HOME/.docker/bin"

# For Postgres libpq CLI tools (to install, run: brew install libpq):
export PATH="$PATH:/usr/local/opt/libpq/bin"

# Aliases for Pixi:
# alias p="pixi"
alias pixup="pixi self-update"

# Aliases for Bun:
alias b="bun"
alias bup="bun upgrade"
# alias d="bun run --bun dev"
# alias dip="bun run --bun dev-ip"
# alias build="bun run --bun build"
# alias start="bun run --bun start"
# alias t="bun run --bun test"
# alias add="bun add -E"

# Aliases for PNPM:
alias p="pnpm"
# alias i="pnpm i"
# alias up="pnpm update --latest"
alias pup="curl -fsSL https://get.pnpm.io/install.sh | sh -"
# alias d="pnpm dev"
# alias dip="pnpm dev-ip"
# alias build="pnpm build"
# alias s="pnpm start"
# alias t="pnpm test"
# alias add="pnpm add -E"

#-------------------------------------------------------------------------------
# MY CUSTOM SETTINGS THAT CURRENTLY AREN'T BEING USED
#
# These settings have been commented out because they currently aren't being
# used, but they can be uncommented and moved into the section above if I ever
# want to start using them again.

# # For VS Code:
# export PATH="$PATH:/Applications/Visual Studio Code - Insiders.app/Contents/Resources/app/bin"

# # For Rust:
# . "$HOME/.cargo/env"

# # For Deno:
# export DENO_INSTALL="/Users/elliotwaite/.deno"
# export PATH="$PATH:$DENO_INSTALL/bin"

# # For Nim:
# export PATH="$PATH:$HOME/.nimble/bin"

# # For EdgeDB:
# export PATH="$PATH:$HOME/Library/Application Support/edgedb/bin"

# # For Tauri mobile:
# export JAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"
# export ANDROID_HOME="$HOME/Library/Android/sdk"
# export NDK_HOME="$ANDROID_HOME/ndk/25.0.8775105"

# # For React Native:
# export REACT_EDITOR="pycharm"

# # For Expo Android emulator (see: https://docs.expo.dev/workflow/android-studio-emulator/):
# export ANDROID_SDK="$HOME/Library/Android/sdk"
# export PATH="$PATH:$HOME/Library/Android/sdk/emulator"
# export PATH="$PATH:$HOME/Library/Android/sdk/platform-tools"
# export PATH="$PATH:$HOME/Library/Android/sdk/tools"

# # For Google Cloud SDK:
# if [ -f "/Users/elliotwaite/sdks/google-cloud-sdk/path.zsh.inc" ]; then . "/Users/elliotwaite/sdks/google-cloud-sdk/path.zsh.inc"; fi # Updates PATH.
# if [ -f "/Users/elliotwaite/sdks/google-cloud-sdk/completion.zsh.inc" ]; then . "/Users/elliotwaite/sdks/google-cloud-sdk/completion.zsh.inc"; fi # Adds completions.

# # For Frum (Ruby version manager):
# eval "$(frum init)"
