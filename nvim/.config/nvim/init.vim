call plug#begin('~/.local/share/nvim/plugged')

Plug 'scrooloose/nerdtree'
Plug 'valloric/youcompleteme'
Plug 'kien/ctrlp.vim'
Plug 'scrooloose/nerdcommenter'

" Looking
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Themes
" Plug 'ianks/gruvbox'
" Plug 'sonph/onehalf'
" Plug 'arcticicestudio/nord-vim'
Plug 'dracula/vim', { 'as': 'dracula' }

call plug#end()
   
" Fundamental settings
set encoding=utf-8
filetype on
filetype plugin on
filetype plugin indent on
syntax on

" Some useful settings
set smartindent
set expandtab         "tab to spaces
set tabstop=2         "the width of a tab
set shiftwidth=2      "the width for indent
set foldenable
set foldmethod=indent "folding by indent
set foldlevel=99
set ignorecase        "ignore the case when search texts
set smartcase         "if searching text contains uppercase case will not be ignored
set mouse=a           "turns on mouse support
" Lookings
set number
set cursorline
set nowrap           "no line wrapping
colorscheme dracula  "use the theme onehalfdark
set background=dark "use the light version of gruvbox
let $NVIM_TUI_ENABLE_TRUE_COLOR=1

" Key bindings
map <C-n> :NERDTreeToggle<CR>

" Nerd tree settings
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" CtrlP Settings
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'
let g:ctrlp_working_path_mode = 'ra'

" Airline
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_idx_mode = 1
let g:airline_powerline_fonts = 1
if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif
