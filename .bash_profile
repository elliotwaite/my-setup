# Change the prompt string to be the current working directory followed by the dollar sign and a space.
export PS1="\W\$ "

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/elliotwaite/google-cloud-sdk/path.bash.inc' ]; then source '/Users/elliotwaite/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/elliotwaite/google-cloud-sdk/completion.bash.inc' ]; then source '/Users/elliotwaite/google-cloud-sdk/completion.bash.inc'; fi

# Added by Miniconda3 installer.
export PATH="/Users/elliotwaite/miniconda3/bin:$PATH"

# Added by NVM installer.
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# An alias for TensorBoard.
Alias tb="tensorboard --logdir=runs --host=0.0.0.0"