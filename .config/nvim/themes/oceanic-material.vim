hi Comment cterm=italic
let g:oceanic_material_hide_endofbuffer=1
let g:oceanic_material_terminal_italics=1
let g:oceanic_material_termcolors=256
let g:oceanic_material_transparent_background = 1

set background=dark
colorscheme oceanic_material
syntax on

let g:airline_theme = 'selenized'
" checks if your terminal has 24-bit color support
if (has("termguicolors"))
    set termguicolors
    hi LineNr ctermbg=NONE guibg=NONE
endif
