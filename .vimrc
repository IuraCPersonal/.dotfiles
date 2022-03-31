                                             
"  _   ___      ___   _ 
" | | | \ \ /\ / / | | |
" | |_| |\ V  V /| |_| |
"  \__,_| \_/\_/  \__,_|
"                           
" Config by s1mpi                           

"=================================================
" => Plugins
"=================================================

set nocompatible              " be iMproved, required
filetype off                  " required

call plug#begin('~/.vim/plugged')

"{{ Color Schemes }}
    Plug 'joshdick/onedark.vim'
    Plug 'arcticicestudio/nord-vim'
    Plug 'ghifarit53/tokyonight-vim'
"{{ Syntax Highlighting and Colors }}
    Plug 'itchyny/lightline.vim'
    Plug 'ap/vim-css-color'
    Plug 'pangloss/vim-javascript'
    Plug 'sheerun/vim-polyglot'
    Plug 'vim-python/python-syntax'
"{{ File Management }}
    Plug 'vifm/vifm.vim'                               " Vifm
    Plug 'preservim/nerdtree'                          " Nerdtree
    Plug 'tiagofumo/vim-nerdtree-syntax-highlight'     " Highlighting Nerdtree
    Plug 'ryanoasis/vim-devicons'                      " Icons for Nerdtree
"{{ Others }}
    Plug 'vimsence/vimsence'
    Plug 'tpope/vim-surround' 
"{{ Git }}
    Plug 'airblade/vim-gitgutter'

call plug#end()

filetype plugin indent on    " required

"=================================================
" => General Settings
"=================================================

syntax on

set nu
set number
set nocompatible
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set ignorecase
set mouse=a
set nowrap
set smartcase
set noswapfile
set nobackup
set background=dark
set termguicolors
set incsearch
set scrolloff=5
set backspace=indent,eol,start

"=================================================
" => Nerd Tree
"=================================================

nnoremap <C-t> :NERDTreeToggle<CR>
" let g:NERDTreeDirArrowExpandable = ''
" let g:NERDTreeDirArrowCollapsible = ''
let NERDTreeShowLineNumbers=1
let NERDTreeShowHidden=1
let NERDTreeMinimalUI = 1
let g:NERDTreeWinSize=38


"=================================================
" => Discord Rich Presence
"=================================================


"=================================================
" => Lightline Config
"=================================================

set laststatus=2

let g:lightline = {'colorscheme' : 'tokyonight'}
let g:airline_theme = "tokyonight"

"=================================================
" => Mouse Scrolling
"=================================================

set mouse=nicr

"=================================================
" => Open terminal inside Vim
"=================================================

"map <Leader>tt :vnew term://bash<CR>


"=================================================
" => Vim-Markdown
"=================================================


"=================================================
" => Display Option
"=================================================

set showmode
set showcmd
set cmdheight=1

"=================================================
" Colorscheme
"=================================================
"colorscheme nord
"colorscheme onedark
"colorscheme github
  
set termguicolors

let g:tokyonight_style = 'night' " available: night, storm
let g:tokyonight_enable_italic = 1
let g:tokyonight_transparent_background = 1

colorscheme tokyonight

hi Normal guibg=NONE ctermbg=NONE

"=================================================
" Personal Key Binds
"=================================================

:imap jj <Esc>

map <S-s> :!pdflatex % && zathura %:r.pdf<CR>
map <C-s> :!clear && python %<CR>

let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

