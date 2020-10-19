# Change the prompt string to be the current working directory followed by the dollar sign and a space.
export PS1="\W$ "

# Added by NVM installer.
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/elliotwaite/sdks/google-cloud-sdk/path.bash.inc' ]; then . '/Users/elliotwaite/sdks/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/elliotwaite/sdks/google-cloud-sdk/completion.bash.inc' ]; then . '/Users/elliotwaite/sdks/google-cloud-sdk/completion.bash.inc'; fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/elliotwaite/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/elliotwaite/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/elliotwaite/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/elliotwaite/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# For Nim.
export PATH=$PATH:/Users/elliotwaite/.nimble/bin

# Alias for Blackd.
alias b="bash -c \"nohup sh -c 'blackd --bind-port 45484' &> /tmp/black.out\""

# For Flutter.
export PATH="$PATH:/Users/elliotwaite/sdks/flutter/bin"