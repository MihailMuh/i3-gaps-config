# Установка i3-gaps

sudo pacman -S xorg-server xorg-xinit i3-gaps i3status dmenu

# Установка paru (для гугла и не только)
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

# Установка терминала, файлового менеджера, менеджера обоев, графического менеджера (соответсвенно)
sudo pacman -S alacritty pcmanfm nitrogen picom

В этом репо, в конфиге nitrogen, установлена пака для обоев по пути ~/Pictures/wallpapers и картинка для рабочего стола - space.jpg (см. папку wallpapers в этом репо)
Для своей настройки вводи в терминал nitrogen для gui редактора

# Установка Гугла
paru -S google-chrome
