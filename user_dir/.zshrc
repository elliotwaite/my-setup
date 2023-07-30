# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zshrc.pre.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.pre.zsh"

# ----------------------------------------------------------------------------#
#                                                                             #
#   POWERLEVEL10K SETTINGS                                                    #
#                                                                             #
# ----------------------------------------------------------------------------#

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
#   AUTO GENERATED BY CONDA                                                   #
#                                                                             #
# ----------------------------------------------------------------------------#

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

# ----------------------------------------------------------------------------#
#                                                                             #
#   AUTO GENERATED BY RUST                                                    #
#                                                                             #
# ----------------------------------------------------------------------------#

. "$HOME/.cargo/env"

# ----------------------------------------------------------------------------#
#                                                                             #
#   AUTO GENERATED BY PNPM                                                    #
#                                                                             #
# ----------------------------------------------------------------------------#

# pnpm
export PNPM_HOME="/Users/elliotwaite/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# ----------------------------------------------------------------------------#
#                                                                             #
#   MY CUSTOM SETTINGS                                                        #
#                                                                             #
# ----------------------------------------------------------------------------#

# Custom key bindings:
bindkey '\e\e[D' beginning-of-line # Cmd + Left -> beginning-of-line.
bindkey '\e\e[C' end-of-line # Cmd + Right -> end-of-line.

# Adds ~/bin to PATH:
export PATH=$PATH:$HOME/bin

# Alias for PNPM:
alias p=pnpm

# For Deno:
export DENO_INSTALL="/Users/elliotwaite/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# For Tauri mobile:
export JAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"
export ANDROID_HOME="$HOME/Library/Android/sdk"
export NDK_HOME="$ANDROID_HOME/ndk/25.0.8775105"

# For React Native:
export REACT_EDITOR=pycharm

# For Expo Android emulator (https://docs.expo.dev/workflow/android-studio-emulator/):
export ANDROID_SDK=$HOME/Library/Android/sdk
export PATH=$PATH:$HOME/Library/Android/sdk/emulator
export PATH=$PATH:$HOME/Library/Android/sdk/platform-tools
export PATH=$PATH:$HOME/Library/Android/sdk/tools

# For Google Cloud SDK:
if [ -f '/Users/elliotwaite/sdks/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/elliotwaite/sdks/google-cloud-sdk/path.zsh.inc'; fi # Updates PATH for the Google Cloud SDK.
if [ -f '/Users/elliotwaite/sdks/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/elliotwaite/sdks/google-cloud-sdk/completion.zsh.inc'; fi # Enables shell command completions for gcloud.

# For Nim:
export PATH=$PATH:$HOME/.nimble/bin

# For Frum (Ruby version manager):
eval "$(frum init)"

# ----------------------------------------------------------------------------#
#                                                                             #
#                                                                             #
#                                                                             #
# ----------------------------------------------------------------------------#

# Fig post block. Keep at the bottom of this file.
[[ -f "$HOME/.fig/shell/zshrc.post.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.post.zsh"