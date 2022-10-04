<div align="center">

# Установка Arch Linux
https://gist.github.com/fjpalacios/441f2f6d27f25ee238b9bfcb068865db

<br>

# Скриншот
![screenshot](./assets/screenshot.png)

# Установка для Arch Linux
</div>

## Установка Xserver
```
sudo pacman -S xorg-server xorg-apps xorg-xinit
```

## Установка i3-gaps
```
sudo pacman -S i3-gaps polybar rofi
```

### Установка терминала, файлового менеджера, менеджера обоев, менеджера анимаций, менеджера скриншотов (соответсвенно)
```
sudo pacman -S alacritty nautilus nitrogen picom gnome-screenshot
```
В этом репо, в конфиге nitrogen, установлена пака для обоев по пути ~/Pictures/wallpapers и картинка для рабочего стола - space.jpg (см. папку wallpapers в этом репо).

Для своей настройки вводи в терминал ```nitrogen``` для gui редактора

## Установка paru (для гугла и не только)
```
sudo pacman -S --needed base-devel git
```
```
git clone https://aur.archlinux.org/paru.git
```
```
cd paru
```
```
makepkg -si
```

## Установка полезного ПО
```
paru -S google-chrome sublime-text-3
```

Символическая ссылка, чтобы открывать sublime через консоль, например subl /etc/hosts
```
sudo ln -s /opt/sublime_text_3/sublime_text /usr/local/bin/subl
```

## Копирование конфигов
```
git clone https://github.com/MihailMuh/i3-gaps-config.git
```
```
cd i3-gaps-config
```
```
cp -r ./config/* ~/.config
```
