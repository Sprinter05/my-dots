-------------------------------
-- LAZY PLUGIN MANAGER
-------------------------------
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
-------------------------------
-- VIM OPTIONS
-------------------------------
vim.opt.rtp:prepend(lazypath)
vim.opt.termguicolors = true
vim.cmd[[set splitright]]
vim.cmd[[set noshowmode]]
vim.cmd[[set number]]
vim.cmd[[set cmdheight=0]]
vim.cmd[[set clipboard=unnamedplus]]
vim.cmd("set foldcolumn=0")
-- vim.cmd("behave mswin")
-- Disable integrated file explorer
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1
-------------------------------
-- KEYBINDS
-------------------------------
local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }
-- Disable scary q: history
map('n', 'q:', "<nop>", opts);
-- Move between splits
map('n', '<S-Left>', "<C-w>h", opts);
map('n', '<S-Down>', "<C-w>j", opts);
map('n', '<S-Up>', "<C-w>k", opts);
map('n', '<S-Right>', "<C-w>l", opts);
-- Resize splits
map('n', '<C-S-Up>', "<C-w>+", opts);
map('n', '<C-S-Down>', "<C-w>-", opts);
map('n', '<C-S-Right>', "<C-w>>", opts);
map('n', '<C-S-Left>', "<C-w><", opts);
map('n', '<C-S>=', "<C-w>=", opts);
-- Create splits
map('n', '<C-S>ç', "<C-w>v", opts);
map('n', '<C-S>-', "<C-w>s", opts);
-- Kill split
map('n', '<C-S>q', "<C-w>q", opts);
-- Buffer and handling
map('n', '<C-n>', '<Cmd>enew<CR>', opts)
map('n', '<C-Tab>', '<Cmd>BufferNext<CR>', opts)
map('n', '<C-S-Tab>', '<Cmd>BufferPrevious<CR>', opts)
map('n', '<C-S>p', '<Cmd>BufferPin<CR>', opts)
map('n', '<C-S>w', '<Cmd>BufferClose<CR>', opts)
map('n', '<C-S>x', '<Cmd>bw!<CR>', opts)
map('n', '<C-Q>', '<Cmd>BufferPick<CR>', opts)
-- Terminal
map('t', '<C-space>', '<C-\\><C-n><C-w>h', opts)
map('n', '<C-S>g', '<Cmd>botright split term://bash<CR>', opts)
-- Nvim Plugins
map('n', '<C-S>T', '<Cmd>RnvimrToggle<CR>', opts)
map('n', '<C-S>t', '<Cmd>NvimTreeToggle<CR>', opts)
map('n', '<C-S>e', '<Cmd>TroubleToggle<CR>', opts)
map('n', '<C-S>f', '<Cmd>Telescope agrolens query=functions<CR>', opts)
map('n', '<C-S>c', '<Cmd>CccPick<CR>', opts)
map('n', '<C-S>d', '<Cmd>Dashboard<CR>', opts)
-- Cutlass
map('n', 'm', 'd', opts)
map('n', 'mm', 'dd', opts)
-------------------------------
-- Plugins
-------------------------------
require("lazy").setup({
  -- Icons, Colors and Themes
  { "nvim-tree/nvim-web-devicons", name = "nvim-web-devicons"},
  { "lewis6991/gitsigns.nvim", name = "gitsigns"},
  { "RRethy/nvim-base16", name = "nvim-base16" },
  { "catppuccin/nvim", name = "catppuccin" },
  { "nvim-lualine/lualine.nvim", name = "lualine" },
  --- LSP
  {'williamboman/mason.nvim'},
  {'williamboman/mason-lspconfig.nvim'},
  {'VonHeikemen/lsp-zero.nvim', branch = 'v3.x'},
  {'neovim/nvim-lspconfig'},
  {'hrsh7th/cmp-nvim-lsp'},
  {'hrsh7th/nvim-cmp'},
  {'L3MON4D3/LuaSnip'},
  -- Errors and Syntax
  { "folke/trouble.nvim", name="trouble" },
  { "nvim-treesitter/nvim-treesitter", name="treesitter"},
  { "lukas-reineke/indent-blankline.nvim", name="indent-blankline", main = "ibl", opts = {} },
  { 'm-demare/hlargs.nvim', name="hlargs" },
  { "HiPhish/rainbow-delimiters.nvim", name="rainbow-delimiters" },
  { "m4xshen/autoclose.nvim", name="autoclose" },
  -- File manager
  { "nvim-tree/nvim-tree.lua", name="nvime-tree" },
  { 'kevinhwang91/rnvimr', name="rnvimr" },
  -- Find things
  { 'nvim-lua/plenary.nvim', name="plenary" },
  { 'nvim-telescope/telescope.nvim', tag = '0.1.5', name='telescope' },
  { "desdic/agrolens.nvim", name="agrolens" },
  { 'nvimdev/hlsearch.nvim', event = 'BufRead' },
  -- Clipboard
  {
    "tversteeg/registers.nvim",
    name = "registers",
    keys = {
      { "\"",    mode = { "n", "v" } },
      { "<C-R>", mode = "i" }
    },
    cmd = "Registers",
  },
  -- Color Picker
  { "uga-rosa/ccc.nvim", name = "create-color-code"},
  -- Comments
  { 'numToStr/Comment.nvim', name="nvim-commnet", lazy=false },
  -- Winbar
  { "SmiteshP/nvim-navic" },
  { "utilyre/barbecue.nvim", name="barbecue" },
  -- Tablines
  { 'romgrk/barbar.nvim', name= "barbar" },
  -- Startup and notifications
  { 'nvimdev/dashboard-nvim', name="dashboard-nvim", event = 'VimEnter' },
  { 'rcarriga/nvim-notify', name="nvim-notify" },
  -- Folds
  { 'kevinhwang91/promise-async' },
  { 'kevinhwang91/nvim-ufo', name="nvim-ufo" },
  -- Yank
  { "gbprod/cutlass.nvim", name="cutlass" },
  -- Git
  { "sindrets/diffview.nvim" },
  { "ibhagwan/fzf-lua" },
  { "NeogitOrg/neogit", name="neogit" },
  -- Workspaces
  { "natecraddock/workspaces.nvim", name="workspaces-nvim" },
  -- Session
  { "olimorris/persisted.nvim", name="persisted", config=true},
  -- Others
  { 'andweeb/presence.nvim', name="discord-presence" },
  { 'nvim-lua/popup.nvim' },
  { 'sudormrfbin/cheatsheet.nvim', name="cheatsheet" },
})
-------------------------------
-- CONFIGS
-------------------------------
-- Colorscheme, icons and theme
vim.cmd('colorscheme base16-catppuccin-macchiato')
require('nvim-web-devicons').setup()
require('gitsigns').setup()
require("catppuccin").setup({
    flavour = "macchiato",
    transparent_background = true,
    dim_inactive = {
      enabled = false, -- dims the background color of inactive window
      shade = "dark",
      percentage = 0.15, -- percentage of the shade to apply to the inactive window
    },
    no_bold = true,
    no_itaic = true,
    no_underline = true,
    styles = {
        comments = { "italic" },
        conditionals = {},
        loops = {},
        functions = { "italic" },
        keywords = { "italic" },
        strings = {},
        variables = { "bold" },
        numbers = {},
        booleans = {},
        properties = {},
        types = {},
        operators = {},
    },
    integrations = {
      cmp = true,
      gitsigns = true,
      nvimtree = true,
      treesitter = true,
    },
    color_overrides = {},
    custom_highlights = {},
})
vim.cmd.colorscheme "catppuccin-mocha"
require('lualine').setup({
    tabline = {},
    winbar = {},
    options = { theme = 'base16' },
})
-- LSP
local lsp_zero = require('lsp-zero')
lsp_zero.on_attach(function(client, bufnr)
  -- :help lsp-zero-keybindings
  lsp_zero.default_keymaps({buffer = bufnr})
end)
-- LSP Manager
require('mason').setup({})
require('mason-lspconfig').setup({
  ensure_installed = {},
  handlers = {
    lsp_zero.default_setup,
  },
})
-- Syntax
require("autoclose").setup()
require('hlargs').setup()
require('hlargs').enable()
require("nvim-treesitter.configs").setup {
  highlight = { enable = true, },
}
require("ibl").setup({
  indent = {
    char = '▏',
  },
  scope = {
    enabled = false,
  },
})
require("ibl").overwrite {
  exclude = { filetypes = {'lspinfo', 'packer', 'checkhealth', 'help', 'man', 'gitcommit', 'TelescopePrompt', 'TelescopeResults', 'dashboard', '' } }
}
-- File explorer
local function my_on_attach(bufnr)
  local api = require "nvim-tree.api"
  local function opts(desc)
    return { desc = "nvim-tree: " .. desc, buffer = bufnr, noremap = true, silent = true, nowait = true }
  end
  api.config.mappings.default_on_attach(bufnr)
  vim.keymap.set('n', '<C-t>', api.tree.change_root_to_node, opts('Up'))
end
require("nvim-tree").setup {
  sort = {
    sorter = "case_sensitive",
  },
  view = {
    width = 30,
  },
  renderer = {
    group_empty = true,
  },
  filters = {
    dotfiles = true,
  },
  on_attach = my_on_attach,
}
-- Find and Search
require "telescope".load_extension("agrolens")
require("telescope").extensions = {
  agrolens = {
     debug = false,
     same_type = true,
     include_hidden_buffers = false,
     disable_indentation = false,
     aliases = {}
  }
}
require("registers").setup({})
require('hlsearch').setup()
-- Winbar
require("barbecue").setup({
  attach_navic = true,
  create_autocmd = true,
  include_buftypes = { "" },
  exclude_filetypes = { "netrw", "toggleterm" },
  modifiers = {
    dirname = ":~:.",
    basename = "",
  },
  show_dirname = true,
  show_basename = true,
  show_modified = false,
  show_navic = true,
  theme = "auto",
  context_follow_icon_color = false,
  symbols = {
    modified = "●",
    ellipsis = "…",
    separator = "",
  },
  kinds = {
    File = "",
    Module = "",
    Namespace = "",
    Package = "",
    Class = "",
    Method = "",
    Property = "",
    Field = "",
    Constructor = "",
    Enum = "",
    Interface = "",
    Function = "",
    Variable = "",
    Constant = "",
    String = "",
    Number = "",
    Boolean = "",
    Array = "",
    Object = "",
    Key = "",
    Null = "",
    EnumMember = "",
    Struct = "",
    Event = "",
    Operator = "",
    TypeParameter = "",
  },
})
require("barbecue.ui").toggle(true)
require("barbecue.ui").update(winnr)
require("barbecue.ui").navigate(index, winnr)
-- Tabline
vim.g.barbar_auto_setup = false
require'barbar'.setup {
  animation = true,
  auto_hide = false,
  tabpages = true,
  clickable = true,
  focus_on_close = 'left',
  icons = {
    buffer_index = false,
    buffer_number = false,
    button = '',
    diagnostics = {
      [vim.diagnostic.severity.ERROR] = {enabled = true, icon = ' '},
      [vim.diagnostic.severity.WARN] = {enabled = true, icon=' '},
      [vim.diagnostic.severity.INFO] = {enabled = false},
      [vim.diagnostic.severity.HINT] = {enabled = true},
    },
    filetype = {
      custom_colors = false,
      enabled = true,
    },
    separator = {left = '▎', right = ''},
    separator_at_end = true,
    modified = {button = '●'},
    pinned = {button = '', filename = true},
    preset = 'default',
    alternate = {filetype = {enabled = false}},
    current = {buffer_index = true},
    inactive = {button = '×'},
    visible = {modified = {buffer_number = false}},
  },
  insert_at_end = false,
  insert_at_start = false,
  maximum_padding = 1,
  minimum_padding = 1,
  maximum_length = 30,
  minimum_length = 0,
  semantic_letters = true,
  letters = 'asdfjkl;ghnmxcvbziowerutyqpASDFJKLGHNMXCVBZIOWERUTYQP',
  no_name_title = nil,
}
-- Folds
vim.o.foldcolumn = '1'
vim.o.foldlevel = 99
vim.o.foldlevelstart = 99
vim.o.foldenable = true
require('ufo').setup({})
-- Startup
require('dashboard').setup {
  theme = 'hyper',
  config = {
    header = {
      "                                                     ",
      "  ███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗ ",
      "  ████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║ ",
      "  ██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║ ",
      "  ██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║ ",
      "  ██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║ ",
      "  ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝ ",
      "                                                     ",
    },
    shortcut = {
      { desc = '󰊳 Update', group = '@property', action = 'Lazy update', key = 'u' },
      { desc = '󰂺 Workspaces', group = 'Label', action = 'Telescope workspaces', key = 'w' },
      { desc = '󰉉 Last Session', group = 'String', action = 'SessionLoadLast', key = 's' },
    },
  },
}
-- Git
require('neogit').setup({})
-- Comment
require('Comment').setup()
-- Workspaces
require("workspaces").setup()
require "telescope".load_extension("workspaces")
require("workspaces").setup({
  hooks = {
      open = "Telescope find_files",
  }
})
-- Session
require("persisted").setup({
  save_dir = vim.fn.expand(vim.fn.stdpath("data") .. "/sessions/"),
  silent = true,
  use_git_branch = true,
  autosave = true,
  autoload = false,
})
-- Cutlass
require("cutlass").setup({
  cut_key = 'f',
})
