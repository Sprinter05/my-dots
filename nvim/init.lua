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

-- Open new panes to the right
vim.cmd[[set splitright]]

-- Hides the mode prompt
-- vim.cmd[[set noshowmode]]

-- Enables line numbering
vim.cmd[[set number]]

-- Enables relative numbering
vim.cmd[[set relativenumber]]

-- Max amount of lines that the prompt can show
vim.cmd[[set cmdheight=1]]

-- Highlight current line
vim.cmd[[set cursorline]]

-- Enable system wide clipboard
vim.cmd[[set clipboard=unnamedplus]]

-- DIsable showing column fold lines
vim.cmd("set foldcolumn=0")

-- Use Windows keybindinggs
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

-- Nvim Plugins
map('n', '<C-S>T', '<Cmd>RnvimrToggle<CR>', opts)
map('n', '<C-S>p', '<Cmd>Telescope find_files<CR>', opts)
map('n', '<C-S>t', '<Cmd>NvimTreeToggle<CR>', opts)
map('n', '<C-S>d', '<Cmd>Dashboard<CR>', opts)

-- Cutlass
-- map('n', 'm', 'd', opts)
-- map('n', 'mm', 'dd', opts)

-------------------------------
-- Plugins
-------------------------------
require("lazy").setup({
  -- Icons, Colors and Themes
  { "nvim-tree/nvim-web-devicons", name = "nvim-web-devicons"}, -- Icons
  { "lewis6991/gitsigns.nvim", name = "gitsigns"}, -- Git Icons
  { "RRethy/nvim-base16", name = "nvim-base16" }, -- Base16 Color Schemes
  { "catppuccin/nvim", name = "catppuccin" }, -- Catppuccin Color Scheme

  -- Bars
  { "nvim-lualine/lualine.nvim", name = "lualine" }, -- Status Line
  { 'romgrk/barbar.nvim', name= "barbar" }, -- Show tabs
  
  -- Syntax
  { "lukas-reineke/indent-blankline.nvim", name="indent-blankline", main = "ibl" }, -- Show indentation lines
  { 'm-demare/hlargs.nvim', name="hlargs" }, -- Highlight arguments
  { "HiPhish/rainbow-delimiters.nvim", name="rainbow-delimiters" }, -- Colored brackets
  { "nvim-treesitter/nvim-treesitter", name="treesitter"}, -- Dependency of rainbow-delimiters
  { "m4xshen/autoclose.nvim", name="autoclose" }, -- Close brackets automatically
  { 'nvimdev/hlsearch.nvim', event = 'BufRead' }, -- Remove highlighting when exiting find prompt
  
  -- File manager
  { "nvim-tree/nvim-tree.lua", name="nvim-tree" }, -- Tree file explorer
  { 'kevinhwang91/rnvimr', name="rnvimr" }, -- Ranger on a window
  { 'nvim-lua/popup.nvim' }, -- Dependency for showing popups
  
  -- Find things
  { 'nvim-telescope/telescope.nvim', tag = '0.1.5', name='telescope' }, -- Fuzzy finder for files
  { "desdic/agrolens.nvim", name="agrolens" }, -- Predefined queries for telescope
  
  -- History
  { 'mbbill/undotree', name="undotree" }, -- Show undo history
  
  -- Comments
  { 'numToStr/Comment.nvim', name="nvim-comment" }, -- Add comments more easily
  
  -- Notifications
  { 'rcarriga/nvim-notify', name="nvim-notify" }, -- Show notifications

  -- Dashboard
  { 'nvimdev/dashboard-nvim', name="dashboard-nvim", event = 'VimEnter' }, -- Show dashboard

  -- Yank
  -- { "gbprod/cutlass.nvim", name="cutlass" }, -- Enables using both registers and clipboard

  -- Git
  { "sindrets/diffview.nvim" }, -- Show diffs and history
  {'akinsho/git-conflict.nvim', config = true}, -- Show merge conflicts

  -- Workspaces
  { "natecraddock/workspaces.nvim", name="workspaces-nvim" }, -- Workspaces for coding

  -- Session
  { "olimorris/persisted.nvim", name="persisted", config=true}, -- Saves last used session

  -- Integrations
  { 'andweeb/presence.nvim', name="discord-presence" }, -- Discord Rich Presence
})

-------------------------------
-- CONFIGS
-------------------------------

-- Setup plugins to use nofications
require("notify").setup({
  background_colour = "#000000",
})
vim.notify = require("notify")

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

-- Setup status line
require('lualine').setup({
    tabline = {},
    winbar = {},
    options = { theme = 'base16' },
})

-- Syntax
require("autoclose").setup()
require('hlargs').setup()
require('hlargs').enable()
require("nvim-treesitter.configs").setup {
  highlight = { enable = true, },
}

-- Indentation lines
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
require('hlsearch').setup()

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
      { desc = ' New', group = 'Label', action = 'enew', key = 'n' },
      { desc = '󰂺 Workspaces', group = 'Number', action = 'Telescope workspaces', key = 'w' },
      { desc = '󰉉 Last Session', group = 'String', action = 'SessionLoadLast', key = 's' },
    },
  },
}

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
-- require("cutlass").setup({
--   cut_key = 'f',
-- })
