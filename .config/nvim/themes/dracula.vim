hi Comment cterm=italic
colorscheme dracula
let g:airline_theme = 'base16_dracula'
let g:dracula_transparent_bg = v:true
let g:dracula_hide_endofbuffer=1
let g:dracula_terminal_italics=1
let g:dracula_termcolors=256


set background=dark
syntax on
if (has("termguicolors"))
    set termguicolors
    hi LineNr ctermbg=NONE guibg=NONE
endif
