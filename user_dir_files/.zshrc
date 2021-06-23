ZSH_DIR=$HOME/code/zsh

# Download zsh-syntax-highlighting into the ZSH_DIR:
#   https://github.com/zsh-users/zsh-syntax-highlighting
source $ZSH_DIR/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Download zsh-autosuggestions into the ZSH_DIR:
#   https://github.com/zsh-users/zsh-autosuggestions
source $ZSH_DIR/zsh-autosuggestions/zsh-autosuggestions.zsh

# Download zsh-completions into the ZSH_DIR:
#   https://github.com/zsh-users/zsh-completions
#
# Also, download completions for nim and nimble by downloading there
# completion files into "ZSH_DIR/zsh-completions/src". You can do this by using
# the curl commands below, but note: if you use a different "ZSH_DIR", change
# the "~/code/zsh" part of each commands specified output path.
#   curl https://raw.githubusercontent.com/nim-lang/Nim/devel/tools/nim.zsh-completion -o ~/code/zsh/zsh-completions/src/_nim
#   curl https://raw.githubusercontent.com/nim-lang/nimble/master/nimble.zsh-completion -o ~/code/zsh/zsh-completions/src/_nimble
fpath=($ZSH_DIR/zsh-completions/src $fpath)

# Download powerlevel10k into the ZSH_DIR:
#   https://github.com/romkatv/powerlevel10k
#
# Configure p10k by runing `p10k configure` or edit ~/.p10k.zsh.
source ~/code/zsh/powerlevel10k/powerlevel10k.zsh-theme
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/elliotwaite/miniforge3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/elliotwaite/miniforge3/etc/profile.d/conda.sh" ]; then
        . "/Users/elliotwaite/miniforge3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/elliotwaite/miniforge3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# For user bin.
export PATH=$PATH:$HOME/bin

# For Nim.
export PATH=$PATH:$HOME/.nimble/bin

# Alias for blackd.
alias blackd="bash -c \"nohup sh -c 'blackd --bind-port 45484' &> /tmp/black.out\""
