" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')
    
    " LaTeX docs
    Plug 'lervag/vimtex'

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " Theme
    Plug 'joshdick/onedark.vim'
    Plug 'glepnir/oceanic-material'
    Plug 'shaunsingh/nord.nvim'
    Plug 'Mofiqul/dracula.nvim'

    " Status line  
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
   
    " Coc Intelisense. 
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Cool Icons
    Plug 'ryanoasis/vim-devicons'

    Plug 'mhinz/vim-signify'
    Plug 'tpope/vim-fugitive'
    Plug 'tpope/vim-rhubarb'
    Plug 'junegunn/gv.vim'


call plug#end()
