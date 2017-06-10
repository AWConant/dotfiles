PS1='\h[\W]λ '
PS1="$PS1"'$([ -n "$TMUX" ] && tmux setenv TMUXPWD_$(tmux display -p "#D" | tr -d %) "$PWD")'
PS2='more> '

export HISTSIZE=500
export HISTFILESIZE=500
export BROWSER=firefox
export WORKON_HOME=/scratch/aconant1/Envs
export LESS=eFRX
export DISPLAY=localhost:0.0

# ---------------------------------------------------------------
function template {
    cp ~/template.py $1.py
    touch in/$1.in
}
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
alias grep='grep --color=always'
# ---------------------------------------------------------------
if [ -f /etc/bash_completion ]; then
  . /etc/bash_completion
fi
