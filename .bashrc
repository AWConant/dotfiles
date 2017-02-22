PS1='\h[\W]λ '
PS2='more> '

export HISTSIZE=500
export HISTFILESIZE=500
export BROWSER=firefox
export PYTHONSTARTUP=${HOME}/.pythonrc
export WORKON_HOME=/scratch/aconant1/Envs
export LESS=eFRX

# ---------------------------------------------------------------
alias back='cd $OLDPWD'
alias ls='ls -CF'
alias ll='ls -l'
alias la='ls -a'
alias lal='ls -al'
alias lnew='ls -alt | head -16'
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias r='resize'
alias h='history'
alias c='/usr/bin/clear'
alias df='df -k'
alias du='du -k'
alias land='enscript -2rhGj'
alias l1='enscript -1rhGj'
alias xlock='/usr/local/bin/xlock -remote -mode dclock -mono -nice 10'
alias blindness='~/blindness/blindness.py'
alias tm='tmux'
alias xop='xdg-open'
alias cd21='cd ~/gcs21-s17'
alias grep='grep --color=always'
alias up3='cd ../../..'
# ---------------------------------------------------------------
if [ -f /etc/bash_completion ]; then
  . /etc/bash_completion
fi
