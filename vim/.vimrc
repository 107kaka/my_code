set nocompatible
filetype off

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required!
Bundle 'gmarik/vundle'

" set plugin
"-----------------------------------------------------------------
" vim enhancements
Bundle 'bufexplorer.zip'
Bundle 'Kien/ctrlp.vim'
Bundle 'scrooloose/nerdtree'
Bundle 'SirVer/ultisnips'
"Bundle 'bling/vim-airline'

" Git plugins
Bundle 'airblade/vim-gitgutter'
Bundle 'tpope/vim-fugitive'

" General Programming
Bundle 'scrooloose/syntastic'
"Bundle 'Valloric/YouCompleteMe'
Bundle 'majutsushi/tagbar'
Bundle 'altercation/vim-colors-solarized'

" C Programming 
Bundle 'c.vim'
Bundle 'Raimondi/delimitMate'
Bundle 'vim-scripts/a.vim'

filetype plugin indent on 		"requried for vundle

" basic settings
set helplang=cn
set encoding=utf-8
syntax enable
syntax on
set backspace=indent,eol,start
set history=500

set laststatus=2
set statusline=%F:\%l

let g:tagbar_width = 22
let g:tagbar_left = 0
map <F8> :Tagbar<cr>

if has('gui_running')
	set background=light
else
	set background=dark
endif
set background=dark
set t_Co=16
let g:solarized_termcolors=16
colorscheme solarized

let g:NERDTreeWinSize=22
map <F12> :NERDTree<CR>

"let g:ycm_key_list_select_completion=['<C-TAB>','<Down>']
"let g:ycm_key_list_previous_conpletion=['<C-S-TAB>','<Up>']
