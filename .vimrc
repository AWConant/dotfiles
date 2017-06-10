"""""""""""""""""""""""""""""""""""""""""""""""""
"set nocompatible
"filetype off
"
"set rtp+=~/.vim/bundle/Vundle.vim
"call vundle#begin()
"
"Plugin 'VundleVim/Vundle.vim'
"
"Plugin 'scrooloose/nerdcommenter'
""Plugin 'scrooloose/syntastic'
"
"call vundle#end()
"filetype plugin indent on

"""""""""""""""""""""""""""""""""""""""""""""""""

"set statusline+=%#warningmsg#
"set statusline+=%{SyntasticStatuslineFlag()}
"set statusline+=%*
"
"let g:syntastic_always_populate_loc_list = 1
"let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 1
"let g:syntastic_check_on_wq = 0

"""""""""""""""""""""""""""""""""""""""""""""""""

" so I can paste with the mouse (hit F2 to toggle)
set pastetoggle=<F2>

" no autowrap of lines
set wrapmargin=0

" have man lines of command-line (etc) history:
set history=1000

" have command-line completion <Tab> (for filenames, help topics, option names)
" first list the available options and complete the longest common part, then
" have further <Tab>s cycle through the possibilities:
set wildmode=list:longest,full

" display the current mode and partially-typed commands in the status line:
set showmode
set showcmd

set shiftwidth=4
set shiftround
set expandtab
set autoindent

" enable filetype detection:
filetype on
filetype indent on
filetype plugin on

" in human-language files, automatically format everything at 72 chars:
autocmd FileType mail,human set formatoptions+=t textwidth=72

" for C-like programming, have automatic indentation:
autocmd FileType c,cpp,slang set cindent

autocmd BufNewFile,BufRead *.glsl set syntax=cpp

" for actual C (not C++) programming where comments have explicit end
" characters, if starting a new line in the middle of a comment automatically
" insert the comment leader characters:
autocmd FileType c set formatoptions+=ro

" for python
autocmd FileType python set expandtab shiftwidth=4 softtabstop=4

" for OCaml
autocmd FileType ocaml setlocal expandtab shiftwidth=2 

" in makefiles, don't expand tabs to spaces, since actual tab characters are
" needed, and have indentation at 8 chars to be sure that all indents are tabs
" (despite the mappings later):
autocmd FileType make set noexpandtab shiftwidth=8

" make searches case-insensitive, unless they contain upper-case letters:
set ignorecase
set smartcase

" Renames tmux tabs to names of last edited files in vim
autocmd BufEnter * call system("tmux rename-window " . expand("%:t"))
autocmd VimLeave * call system("tmux rename-window bash")
autocmd BufEnter * let &titlestring = ' ' . expand("%:t")
set title

" Enables line numbers
set number

" Hard mode lite (disables arrow keys)
noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>

" For fatfingering capital letters on saves
command WQ wq
command Wq wq
command W w
command Q q

" map jk to esc
imap jk <Esc>

" column at 80 chars
set colorcolumn=80
highlight ColorColumn ctermbg=235 guibg=#2c2d27

" copy paste between windows
set clipboard=unnamedplus

" preferred colorscheme
colorscheme evening
