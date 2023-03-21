# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zshrc.pre.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.pre.zsh"

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# ----------------------------------------------------------------------------#
#                                                                             #
#   MY CUSTOM SETTINGS                                                        #
#                                                                             #
# ----------------------------------------------------------------------------#

# Key bindings for `Cmd + Left` -> `beginning-of-line` and `Cmd + Right` -> `end-of-line`.
bindkey '\e\e[D' beginning-of-line
bindkey '\e\e[C' end-of-line

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/elliotwaite/mambaforge/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/elliotwaite/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/Users/elliotwaite/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/Users/elliotwaite/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/Users/elliotwaite/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/Users/elliotwaite/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<

# For user bin.
export PATH=$PATH:$HOME/bin

# For Rust.
. "$HOME/.cargo/env"

# For Volta.
export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"

# For Nim.
export PATH=$PATH:$HOME/.nimble/bin

# For React Native.
export REACT_EDITOR=pycharm

# For Flutter.
export PATH=$PATH:$HOME/sdks/flutter/bin

# For Expo Android emulator (https://docs.expo.dev/workflow/android-studio-emulator/).
export ANDROID_SDK=$HOME/Library/Android/sdk
export PATH=$PATH:$HOME/Library/Android/sdk/emulator
export PATH=$PATH:$HOME/Library/Android/sdk/platform-tools
export PATH=$PATH:$HOME/Library/Android/sdk/tools

# For Google Cloud SDK. The first line updates PATH for the Google Cloud SDK. The second line enables shell command completion for gcloud.
if [ -f '/Users/elliotwaite/sdks/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/elliotwaite/sdks/google-cloud-sdk/path.zsh.inc'; fi
if [ -f '/Users/elliotwaite/sdks/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/elliotwaite/sdks/google-cloud-sdk/completion.zsh.inc'; fi

# For tauri-mobile. Specifies the Android SDK installation directory.
export ANDROID_HOME=$HOME/Library/Android/sdk
export NDK_HOME=$HOME/Library/Android/sdk/ndk/25.2.9519653

# For Timestream app (requires: npm i -g sync-directory).
alias watcher='syncdir /Users/elliotwaite/code/repos/timestream-next/src /Users/elliotwaite/code/repos/timestream-expo/src -w -do'

# ----------------------------------------------------------------------------#
#                                                                             #
#                                                                             #
#                                                                             #
# ----------------------------------------------------------------------------#

# Fig post block. Keep at the bottom of this file.
[[ -f "$HOME/.fig/shell/zshrc.post.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.post.zsh"
