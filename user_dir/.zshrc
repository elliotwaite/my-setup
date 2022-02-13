ZSH_DIR=$HOME/code/zsh

# Download zsh-syntax-highlighting into your ZSH_DIR:
#   https://github.com/zsh-users/zsh-syntax-highlighting
source $ZSH_DIR/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Download zsh-autosuggestions into your ZSH_DIR:
#   https://github.com/zsh-users/zsh-autosuggestions
source $ZSH_DIR/zsh-autosuggestions/zsh-autosuggestions.zsh

# Download zsh-completions into your ZSH_DIR:
#   https://github.com/zsh-users/zsh-completions
#
# Also, download completions for nim and nimble by downloading their
# completion files into "ZSH_DIR/zsh-completions/src". You can do this by using
# the curl commands below, but note: if you use a different "ZSH_DIR", update
# the "~/code/zsh" part of the commands before running them.
#   curl https://raw.githubusercontent.com/nim-lang/Nim/devel/tools/nim.zsh-completion -o ~/code/zsh/zsh-completions/src/_nim
#   curl https://raw.githubusercontent.com/nim-lang/nimble/master/nimble.zsh-completion -o ~/code/zsh/zsh-completions/src/_nimble
#
# Also, to fix the "insecure directories" error message, I had to run:
#   compaudit | xargs chmod g-w
# as suggested here:
#   https://github.com/zsh-users/zsh-completions/issues/680#issuecomment-612960481
fpath=($ZSH_DIR/zsh-completions/src $fpath)
autoload -U compinit && compinit

# Download enhancd into your ZSH_DIR:
#   https://github.com/b4b4r07/enhancd
#
# Also, follow instructions to install fzy and ccat with homebrew:
#   https://github.com/b4b4r07/enhancd#bash
source $ZSH_DIR/enhancd/init.sh

# Download powerlevel10k into the ZSH_DIR:
#   https://github.com/romkatv/powerlevel10k
#
# Configure p10k by runing `p10k configure` or edit ~/.p10k.zsh.
source ~/code/zsh/powerlevel10k/powerlevel10k.zsh-theme
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

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
# <<< conda initialize <<<

# For user bin.
export PATH=$PATH:$HOME/bin

# For Nim.
export PATH=$PATH:$HOME/.nimble/bin

# For Flutter.
export PATH=$PATH:$HOME/sdks/flutter/bin

# For Expo Android emulator (https://docs.expo.dev/workflow/android-studio-emulator/).
export ANDROID_SDK=$HOME/Library/Android/sdk
export PATH=$PATH:$HOME/Library/Android/sdk/platform-tools
export PATH=$PATH:$HOME/Library/Android/sdk/tools

# Alias for blackd.
alias black="bash -c \"nohup sh -c 'blackd --bind-port 45484' &> /tmp/black.out\""

# For NVM.
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
