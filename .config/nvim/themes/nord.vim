hi Comment cterm=italic
let g:nord_disable_background= v:true
let g:nord_contrast = v:true
let g:nord_borders = v:false
let g:nord_italic = v:false

set background=dark
colorscheme nord
syntax on

let g:airline_theme = 'base16_nord'

" checks if your terminal has 24-bit color support
if (has("termguicolors"))
    set termguicolors
    hi LineNr ctermbg=NONE guibg=NONE
endif
